from mitmproxy import ctx
import mitmproxy
import re

server_uri_regex = r"\/_v2\/.*\/h\/.*\/"


def uri_formater(uri):
    '''
    '/_v2/9a701df34ba7e4ae16c25b01dd7fefae2a1925c413179feb8b897fc61aff/h/e4/ecfbbf0012.html'

    to

    '/_v2/9a701df34ba7e4ae16c25b01dd7fefae2a1925c413179feb8b897fc61aff/h/e4/'
    '''
    stripped = uri.split('/')[:-1]
    return '/'.join(stripped) + '/'


def request(flow):

    flow.request.path
    if re.search(server_uri_regex, flow.request.path):
        a = open('log.txt','w')

        a.write(flow.request.host+'\n')
        a.write(uri_formater(flow.request.path)+'\n')

        a.close()
        try:
            ctx.master.shutdown()
        except:
            pass
