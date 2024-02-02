# -*- coding: utf-8 -*-
import sys
import six
import os
import re
try:
    from urllib.parse import urlparse, parse_qs, quote, unquote, quote_plus, unquote_plus, urlencode #python 3
except ImportError:    
    from urlparse import urlparse, parse_qs #python 2
    from urllib import quote, unquote, quote_plus, unquote_plus, urlencode
from kodi_six import xbmc, xbmcvfs, xbmcgui, xbmcplugin, xbmcaddon
try:
    from urllib.parse import urlencode #python 3
except ImportError:     
    from urllib import urlencode #python 2      
# try:
#     from urllib.request import Request, urlopen, URLError  # Python 3
# except ImportError:
#     from urllib2 import Request, urlopen, URLError # Python 2
# try:
#     from StringIO import StringIO ## for Python 2
# except ImportError:            
#     from io import BytesIO as StringIO ## for Python 3
# import gzip 

plugin = sys.argv[0]
handle = int(sys.argv[1])
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
kversion = int(xbmc.getInfoLabel('System.BuildVersion').split(".")[0])
info = 'Canal Ricos, Perus, São Paulo\n\nWhatsapp: (11) 99105-1755'
site = 'https://www.tvcanalricos.com.br/'

if six.PY3:
    profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
    home = xbmcvfs.translatePath(addon.getAddonInfo('path'))
else:
    profile = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
    home = xbmc.translatePath(addon.getAddonInfo('path')).decode('utf-8')

fanart_default = os.path.join(home, 'fanart.png')

# def navegador(url,timeout=12):
#     req = Request(url)
#     req.add_header('sec-ch-ua', '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"')
#     req.add_header('sec-ch-ua-mobile', '?0')
#     req.add_header('sec-ch-ua-platform', '"Windows"')
#     req.add_header('Upgrade-Insecure-Requests', '1')    
#     req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
#     req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
#     req.add_header('Sec-Fetch-Site', 'none')
#     req.add_header('Sec-Fetch-Mode', 'navigate')
#     req.add_header('Sec-Fetch-User', '?1')
#     req.add_header('Sec-Fetch-Dest', 'document')
#     req.add_header('Accept-Encoding', 'gzip')
#     req.add_header('Accept-Language', 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7')
#     # if referer:    
#     #     req.add_header('Referer', referer)
#     try:
#         response = urlopen(req,timeout=timeout)
#         code = response.getcode()
#         encoding = response.info().get('Content-Encoding')
#     except:
#         code = 401
#         encoding = 'none'
#     if code == 200:
#         if encoding == 'gzip':
#             try:
#                 buf = StringIO(response.read())
#                 f = gzip.GzipFile(fileobj=buf)
#                 content = f.read()
#             except:
#                 content = ''
#         else:
#             try:
#                 content = response.read()
#             except:
#                 content = ''
#     else:
#         content = ''          
#     try:
#         content = content.decode('utf-8')
#     except:
#         pass
#     return content

# def resolver(url):
#     html = navegador(url)
#     link = re.compile('http\S+\.m3u8', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(html)
#     if link:
#         stream = link[0] + '|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36&Referer=' + url
#     else:
#         stream = ''
#     return stream

    
def get_url(params):
    url = '%s?%s'%(plugin, urlencode(params))
    return url

def item(params,folder=True):
    url = get_url(params)
    name = params.get("name")
    if name:
        name = name
    else:
        name = 'Unknow'
    iconimage = params.get("iconimage")
    fanart = params.get("fanart")
    description = params.get("description")
    if description:
        description  = description
    else:
        description = ''
    mediatype = params.get("mediatype")
    playable = params.get("playable")

    if six.PY3:
        li=xbmcgui.ListItem(name)
        if iconimage:
            li.setArt({"icon": "DefaultVideo.png", "thumb": iconimage})
    else:
        if not iconimage:
            iconimage = ''
        li = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    if mediatype:
        try:
            li.setInfo('video', { 'mediatype': str(mediatype) })
        except:
            pass
        
    if playable and not playable == 'false':
       li.setProperty('IsPlayable', 'true')
    if kversion > 19:
        info = li.getVideoInfoTag()
        info.setTitle(name)
        info.setPlot(description)
    else:
        li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    if fanart:
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', fanart_default)
    xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=li, isFolder=folder)
    

def play(name,url,iconimage,description,playable):
    #url = resolver(url)
    if url and 'plugin' in url:
        xbmc.executebuiltin('RunPlugin(%s)'%url)        
    elif url and not 'plugin' in url:
        if six.PY3:
            li=xbmcgui.ListItem(name, path=url)
            if iconimage:
                li.setArt({"icon": "DefaultVideo.png", "thumb": iconimage})
        else:
            li = xbmcgui.ListItem(name, path=url, iconImage=iconimage, thumbnailImage=iconimage)
        if kversion > 19:
            info = li.getVideoInfoTag()
            info.setTitle(name)
            info.setPlot(description)
        else:         
            li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
        if not playable == 'false':
            xbmcplugin.setResolvedUrl(handle, True, li)
        else:
            xbmc.Player().play(item=url, listitem=li)


def menu():
    item({'name':'[B]Canal Ricos[/B]','action': 'play', 'url': 'https://a.cdni.live/tvcanalricos/tvcanalricos/playlist.m3u8', 'description': info, 'mediatype': 'video', 'iconimage': icon, 'playable': 'true'},folder=False)
    xbmcplugin.endOfDirectory(handle)


args = parse_qs(sys.argv[2][1:])
action = args.get("action")
name = args.get("name")
url = args.get("url")
iconimage = args.get("iconimage")
fanart = args.get("fanart")
description = args.get("description")
playable = args.get("playable")
if name:
    name = name[0]
else:
    name = 'Unknow'
if url:
    url = url[0]
else:
    url = ''
if iconimage:
    iconimage = iconimage[0]
else:
    iconimage = ''
if fanart:
    fanart = fanart[0]
else:
    fanart = ''
if description:
    description = description[0]
else:
    description = ''
if playable:
    playable = playable[0]
else:
    playable = 'false'
if action == None:
    menu()
elif 'play' in action:   
    name = '[B]Canal Ricos[/B]'
    iconimage = icon
    description = info
    play(name,url,iconimage,description,playable)
