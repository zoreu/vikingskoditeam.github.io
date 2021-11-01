# -*- coding: utf-8 -*-
import sys
import six
import os
try:
    from urllib.parse import urlparse, parse_qs, quote, unquote, quote_plus, unquote_plus, urlencode #python 3
except ImportError:    
    from urlparse import urlparse, parse_qs #python 2
    from urllib import quote, unquote, quote_plus, unquote_plus, urlencode
from kodi_six import xbmc, xbmcvfs, xbmcgui, xbmcplugin, xbmcaddon

plugin = sys.argv[0]
handle = int(sys.argv[1])
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
stream = 'https://5d2c98775bafe.streamlock.net:443/8090/8090/playlist.m3u8'
info = 'Canal Ricos, Perus, São Paulo\n\nWhatsapp: (11) 98870-0735'

if six.PY3:
    profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
    home = xbmcvfs.translatePath(addon.getAddonInfo('path'))
else:
    profile = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
    home = xbmc.translatePath(addon.getAddonInfo('path')).decode('utf-8')

fanart_default = os.path.join(home, 'fanart.png')
    
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
    li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    if fanart:
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', fanart_default)
    xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=li, isFolder=folder)
    

def play(name,url,iconimage,description,playable):
    if url and 'plugin' in url:
        xbmc.executebuiltin('RunPlugin(%s)'%url)        
    elif url and not 'plugin' in url:
        if six.PY3:
            li=xbmcgui.ListItem(name, path=url)
            if iconimage:
                li.setArt({"icon": "DefaultVideo.png", "thumb": iconimage})
        else:
            li = xbmcgui.ListItem(name, path=url, iconImage=iconimage, thumbnailImage=iconimage)
        li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
        if not playable == 'false':
            xbmcplugin.setResolvedUrl(handle, True, li)
        else:
            xbmc.Player().play(item=url, listitem=li)


def menu():
    item({'name':'[B]Canal Ricos[/B]','action': 'play', 'url': stream, 'description': info, 'mediatype': 'video', 'iconimage': icon},folder=False)
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
    play(name,url,iconimage,description,playable)    