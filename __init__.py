from .main import Hounddawgs

def autoload():
	return Hounddawgs()

config = [{
	'name': 'hounddawgs',
	'groups': [
		{
			'tab': 'searcher',
			'list': 'torrent_providers',
			'name': 'Hounddawgs',
			'description': 'See <a href="http://Hounddawgs.org">Hounddawgs</a>',
			'wizard': True,
      'icon': 'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wDIyMhMrKysfrOzs3+/v79/ysrKf9DQ0H/Ozs5/x8fHf729vX+2trZ/srKyf7S0tH+3t7d+0NDQTf///wDU1NQ6UlJS/RsbG/8eHh7/JCQk/ykpKf8rKyv/KSkp/yUlJf8gICD/HBwc/xwcHP8dHR3/IiIi/3h4eP3d3d08wcHBYSsrK/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9FRUX/1tbWY8fHx2EzMzP/AAAA/yIiIv8SEhL/AAAA/zAwMP8hISH/Tk5O/2xsa/9YWFj/FxcX/wAAAP8KCgr/XV1d/9ra2mPQ0NBhPT09/wAAAP8yMjL/Gxsb/wAAAP81NTX/KCgo/4mJif8AAAD/AQEB/zk5Ov8UFBT/KSkp/2NjY//d3d1j2NjYYUZGRv8AAAD/Pz8//2FhYf84ODj/aGho/zU1Nf9qamr/AAAA/wAAAP8uLi7/dHR0/ywsLP9lZWX/29vbY9zc3GFISEj/AAAA/1FRUf9BQUH/GBgY/2JiYv86Ojr/SEhJ/wAAAP8KCgr/ampq/3l5ef8sLCz/UlJS/8bGxmPa2tphRUVF/wAAAP8+Pj7/ICAg/wAAAP83Nzj/JSUl/zg4OP8pKSn/aWlp/7i4uP82Njb/LCws/0tLTP/Kyspj1dXVYT09Pf8AAAD/EBAQ/wkJCf8AAAD/CwsL/wcHCP8WFhb/XFxc/1paWv8vLy//LCws/ysrK/9ZWVn/2dnZY8/Pz1xERET/AAAA/wAAAP8AAAD/AAAA/wAAAP8KCgr/KSkp/ysrK/8rKyv/Kysr/ysrK/8qKir/eXl5/+Pj417w8PAVjY2N12NjY/9mZmb/bGxs/3R0dP98fHz/iIiI/4+Pj/+SkpL/e3t7/2hoaP98fHz/m5ub/9LS0tr19fUV////AP39/QDy8vIP8/PzD/Pz8w/z8/MP9PT0D/T09A/09PQP9PT0D/Pz8w/z8/MP9PT0D/X19Q/9/f0A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A//8AAP//AAD//wAAgAEAAIABAACAAQAAgAEAAIABAACAAQAAgAEAAIABAACAAQAAgAEAAP//AAD//wAA//8AAA==',
			'options': [
				{
					'name': 'enabled',
					'type': 'enabler',
					'default': False,
				},
				{
					'name': 'username',
					'default': '',
				},
				{
					'name': 'password',
					'default': '',
					'type': 'password',
				},
				{
					'name': 'seed_ratio',
					'label': 'Seed ratio',
					'type': 'float',
					'default': 1,
					'description': 'Will not be (re)moved until this seed ratio is met.',
				},
				{
					'name': 'seed_time',
					'label': 'Seed time',
					'type': 'int',
					'default': 48,
					'description': 'Will not be (re)moved until this seed time (in hours) is met.',
				},
				{
					'name': 'extra_score',
					'advanced': True,
					'label': 'Extra Score',
					'type': 'int',
					'default': 20,
					'description': 'Starting score for each release found via this provider.',
				}
			],
		},
	],
}]