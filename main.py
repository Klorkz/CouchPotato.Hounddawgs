from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import simplifyString, tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback
import cookielib
import urllib2
import time
import re

log = CPLog(__name__)



class Hounddawgs(TorrentProvider, MovieProvider):

  urls = {
    'test': 'https://hounddawgs.org/',
    'login': 'https://hounddawgs.org/login.php',
    'detail': 'https://hounddawgs.org/torrents.php?id=%s',
    'download': 'https://hounddawgs.org/torrents.php?action=download&id=%s&authkey=%s&torrent_pass=%s',
    'search': 'https://hounddawgs.org/torrents.php?searchstr=%s%s'
  }

  cat_ids = [
    ([89, 82, 59, 57, 92], ['720p', '1080p']),
    ([90, 60, 58], ['dvdr']),
    ([73, 74, 77, 94, 91, 81, 93], ['cam', 'ts', 'dvdrip', 'tc', 'r5', 'scr', 'brrip']),
  ]

  http_time_between_calls = 2  # Seconds
  cat_backup_id = None
  
  def _searchOnTitle(self, title, movie, quality, results):
  
    if not '<title>News :: HoundDawgs</title>' in self.urlopen(self.urls['login'], data=self.getLoginParams()):
      log.info('problems logging into Hounddawgs')
      return []

    #correct category search
    categories= ""
    for x in self.getCatId(quality):
      categories+='&filter_cat[' + str(x) + ']'

    searchurl = self.urls['search'] % (tryUrlencode('%s %s' % (title.replace(':', ''), movie['info']['year'])), categories)
    
    data = self.getHTMLData(searchurl).decode('latin-1')
      
    if data:
      
      html = BeautifulSoup(data)
         
      try:
        resultsTable = html.find('table', attrs = {'id' : 'torrent_table'})
        if not resultsTable:
          log.info('no torrent table found from Hounddawgs')
          return
            
        # Collecting entries
        entries_sticky = resultsTable.find_all('tr' , attrs = {'class' : 'torrent sticky'})
        entries_std = resultsTable.find_all('tr' , attrs = {'class' : 'torrent'})
        entries = entries_std + entries_sticky
        
        authkey = (entries[0].findAll('td')[1].find_all('a')[0])['href'].split('authkey=', 1)[1].rsplit('&torrent_pass', 1)[0]
        torrent_pass = (entries[0].findAll('td')[1].find_all('a')[0])['href'].rsplit('&torrent_pass=', 1)[1]
            
        if not len(entries) > 0:
          log.info('no entries found on Hounddawgs torrent table')
        else:
          log.info('%s entries found from Hounddawgs' % str(len(entries)))
          # Extracting results from entries
          for result in entries:

            torrentId = result.find('a', attrs = {'onmouseout' :'return nd();'})['href'].replace('torrents.php?id=','')
            log.info(torrentId)
            torrentName = (result.find('a', attrs = {'onmouseout' :'return nd();'})).text
            log.info(torrentName)

            try:
              torrentDescription = ((((result.findAll('td')[1]).findAll('span')[3]).findAll('a')[1])['href']).replace('https://anon.click/','')
              torrentDescription = re.sub(r'\D*[^t{2}\d+]', '', torrentDescription)
            except:
              torrentDescription = ''


            results.append({
              'id': torrentId,
              'name': torrentName,
              'url': (self.urls['download'] % (torrentId, authkey, torrent_pass)).encode('utf8'),
              'detail_url': (self.urls['detail'] % torrentId).encode('utf8'),
              'size': self.parseSize((result.findAll('td', attrs = {'class' : 'nobr'})[1]).text),
              'seeders': tryInt((result.findAll('td')[7]).text),
              'leechers': tryInt((result.findAll('td')[8]).text),
              'description': torrentDescription,
          })

      except:
        log.error('Failed to parsing %s: %s', (self.getName(),traceback.format_exc()))
            
  def getLoginParams(self):
    return {
      'username': str(self.conf('username')),
      'password': str(self.conf('password')),
      'login': 'Login',
    }        
      
  def loginSuccess(self, output):
        return True

    