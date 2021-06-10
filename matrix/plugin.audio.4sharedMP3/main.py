# -*- coding: utf-8 -*-

import sys
import re
import os
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import urllib.parse as urllib
import urllib.request as urllib2
try:
    import json
except:
    import simplejson as json 


addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addonID = addon.getAddonInfo('id')
icon = addon.getAddonInfo('icon')
addon_version = addon.getAddonInfo('version')
profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
home = xbmcvfs.translatePath(addon.getAddonInfo('path'))
fanart_default = os.path.join(home, 'fanart.jpg')
icone_mp3 = os.path.join(home, 'icon_mp3.jpg')
favorites = os.path.join(profile, 'favorites.dat')
if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else:
    FAV = []
    
api = 'https://www.4shared.com/web/rest/v1_2/files'
playlist_eurodance = 'https://raw.githubusercontent.com/zoreu/zoreu.github.io/master/kodi/playlist_eurodance.txt'
melhores_hitz = 'https://raw.githubusercontent.com/zoreu/zoreu.github.io/master/kodi/melhores_hitz.txt'  


def notify(message,name=False,iconimage=False,timeShown=5000):
    if name and iconimage:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (name, message, timeShown, iconimage))
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addonname, message, timeShown, icon))
        
def to_unicode(text, encoding='utf-8', errors='strict'):
    """Force text to unicode"""
    if isinstance(text, bytes):
        return text.decode(encoding, errors=errors)
    return text

def get_search_string(heading='', message=''):
    """Ask the user for a search string"""
    search_string = None
    keyboard = xbmc.Keyboard(message, heading)
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_string = to_unicode(keyboard.getText())
    return search_string        

def addDir(name,url,mode,iconimage,fanart,description,folder=True,favorite=False,download=False):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)+"&folder="+urllib.quote_plus(str(folder))
    li=xbmcgui.ListItem(name)
    if folder:
        li.setArt({"icon": "DefaultFolder.png", "thumb": iconimage})
    else:
        li.setArt({"icon": "DefaultVideo.png", "thumb": iconimage})
    li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    if fanart > '':
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', fanart_default)
    if mode == 2 and folder == False:
        li.setProperty('IsPlayable', 'true')
    if favorite == True or download == True:
        contextMenu = []
        if download == True:
            contextMenu.append(('BAIXAR MÚSICA','RunPlugin(%s?mode=4&name=%s&url=%s)'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url))))
        if favorite == True:
            try:
                name_fav = json.dumps(name.decode('utf-8'))
            except:
                name_fav = name.decode('utf-8')
            if name_fav in FAV:
                contextMenu.append(('REMOVER DA MINHA PLAYLIST','RunPlugin(%s?mode=6&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
            else:                
                contextMenu.append(('ADICIONAR A MINHA PLAYLIST','RunPlugin(%s?mode=5&name=%s&url=%s&fav_mode=%s&iconimage=%s&fanart=%s&description=%s)'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), str(mode), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description))))
        try:
            li.addContextMenuItems(contextMenu)
        except:
            pass
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=li, isFolder=folder)

def resolver(url):
    try:
        data = open_url(url)
        link = re.compile('<input type="hidden" class="jsD1PreviewUrl" value="(.*?)" />').findall(data)
        if link !=[]:
            resolved = link[0]+'|Referer=https://4shared.com/'
        else:
            resolved = ''
    except:
        resolved = ''
    return resolved

def play_mp3(name,url,iconimage,folder):
    #notify('Resolvendo url...',name,iconimage)
    url = resolver(url)
    li = xbmcgui.ListItem(name, path=url)
    li.setArt({"icon": iconimage, "thumb": iconimage})
    li.setInfo(type='video', infoLabels={'Title': name, 'plot': '' })
    li.setProperty('fanart_image', fanart_default)
    if folder=='True':
        xbmc.Player().play(item=url, listitem=li)
    else:
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, li)

def open_url(url):
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'),('Referer', 'https://4shared.com/')]
        response = opener.open(url)
        data = response.read().decode('utf-8')
    except:
        data = ''
    return data

def exibir_lista(pesquisa):
    url = '{}?query={}&category=1&view=web&limit=100'.format(api,pesquisa)
    data = open_url(url)
    lista = re.compile('"fileName":"(.*?)".+?"d1PageUrl":"(.*?)"').findall(data)
    for filename, page in lista:
        addDir(filename.encode('utf-8', 'ignore'),page,2,icone_mp3,'','Segure a tecla OK ou mantenha pressionado para exibir menu extra',folder=True,favorite=True,download=True)
    xbmcplugin.endOfDirectory(addon_handle)
    
def playlist(url):
    data = open_url(url)
    lista = re.compile('name="(.*?)" url="(.*?)"').findall(data)
    for filename, page in lista:
        addDir(filename.encode('utf-8', 'ignore'),page,2,icone_mp3,'','Segure a tecla OK ou mantenha pressionado para exibir menu extra',folder=False,favorite=True,download=True)
    xbmcplugin.endOfDirectory(addon_handle)  
    
def pesquisar():
    vq = get_search_string(heading="Digite algo para pesquisar", message="")        
    if ( not vq ): return False, 0
    title = vq.replace(' ', '+')
    title = urllib.quote_plus(title)
    exibir_lista(title)
    
def downloadMP3(name,url):
    if '.mp3' in name:
        file = name
    else:
        file = name+'.mp3'
    folder = xbmcgui.Dialog().browseSingle(0, 'Selecione um local para download', 'local', '', False, False)
    if os.path.isdir(folder):
        from resources.lib import downloader
        dest=os.path.join(folder, file)
        mp3_url = resolver(url)
        if '.mp3' in mp3_url:
            if 'Referer' in mp3_url:
                link = mp3_url.split('|Referer')[0]
            else:
                link = mp3_url
            downloader.download(link, file, dest)
            
def getFavorites():
    try:
        try:
            items = json.loads(open(favorites).read())
        except:
            items = ''
        total = len(items)
        if int(total) > 0:
            for i in items:
                name = i[0]
                url = i[1]
                mode = i[2]
                iconimage = i[3]
                fanart = i[4]
                description = i[5]
                addDir(name.encode('utf-8', 'ignore'),url,mode,iconimage,fanart,description,folder=False,favorite=True,download=True)                
            xbmcplugin.endOfDirectory(addon_handle)
        else:
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Nenhuma música adicionada na Minha Playlist')                
    except:
        xbmcplugin.endOfDirectory(addon_handle)

def addFavorite(name,url,mode,iconimage,fanart,description):
    favList = []
    if os.path.exists(favorites)==False:
        #addonID
        addon_data_path = profile
        if os.path.exists(addon_data_path)==False:
            os.mkdir(addon_data_path)
        xbmc.sleep(7)
        favList.append((name,url,mode,iconimage,fanart,description))
        a = open(favorites, "w")
        a.write(json.dumps(favList))
        a.close()
        notify('adicionado a Minha Playlist!',name,iconimage)
    else:
        a = open(favorites).read()
        data = json.loads(a)
        data.append((name,url,mode,iconimage,fanart,description))
        b = open(favorites, "w")
        b.write(json.dumps(data))
        b.close()
        notify('adicionado a Minha Playlist!',name,iconimage)
        
def rmFavorite(name):
    data = json.loads(open(favorites).read())
    for index in range(len(data)):
        if data[index][0]==name:
            del data[index]
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    notify('Removido da Minha Playlist!')

def limpar_lista():
    exists = os.path.isfile(favorites)
    if exists:
        if xbmcgui.Dialog().yesno(addonname, 'Deseja limpar Minha Playlist?'):
            try:
                os.remove(favorites)
            except:
                pass
            xbmcgui.Dialog().ok('Sucesso', '[B][COLOR white]Minha Playlist limpa com sucesso![/COLOR][/B]')
        
def principal():
    addDir('[B]Pesquisar[/B]','',1,'','','')
    addDir('[B]Minha Playlist[/B]','',7,'','','')
    addDir('[B]Limpar Minha Playlist[/B]','',8,'','','')
    addDir('[B]Playlist Eurodance[/B]',playlist_eurodance,3,'','','')
    addDir('[B]Melhores Hitz[/B]',melhores_hitz,3,'','','')
    xbmcplugin.endOfDirectory(addon_handle)

def SetView(name):
    if name == 'Wall':
        try:
            xbmc.executebuiltin('Container.SetViewMode(500)')
        except:
            pass
    if name == 'List':
        try:
            xbmc.executebuiltin('Container.SetViewMode(50)')
        except:
            pass
    if name == 'Poster':
        try:
            xbmc.executebuiltin('Container.SetViewMode(51)')
        except:
            pass
    if name == 'Shift':
        try:
            xbmc.executebuiltin('Container.SetViewMode(53)')
        except:
            pass
    if name == 'InfoWall':
        try:
            xbmc.executebuiltin('Container.SetViewMode(54)')
        except:
            pass
    if name == 'WideList':
        try:
            xbmc.executebuiltin('Container.SetViewMode(55)')
        except:
            pass
    if name == 'Fanart':
        try:
            xbmc.executebuiltin('Container.SetViewMode(502)')
        except:
            pass

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]

    return param

def main():
    params=get_params()
    url=None
    name=None
    mode=None
    iconimage=None
    fanart=None
    description=None
    folder='True'
    fav_mode=None

    try:
        url=urllib.unquote_plus(params["url"])
    except:
        pass
    try:
        name=urllib.unquote_plus(params["name"])
    except:
        pass
    try:
        iconimage=urllib.unquote_plus(params["iconimage"])
    except:
        pass
    try:
        mode=int(params["mode"])
    except:
        pass
    try:
        fanart=urllib.unquote_plus(params["fanart"])
    except:
        pass
    try:
        description=urllib.unquote_plus(params["description"])
    except:
        pass
    try:
        folder=urllib.unquote_plus(params["folder"])
    except:
        pass        
    try:
        page=int(params["page"])
    except:
        pass        
    try:
        fav_mode=int(params["fav_mode"])
    except:
        pass

    if mode==None:
        principal()       
    elif mode==1:
        pesquisar()
    elif mode==2:
        play_mp3(name,url,iconimage,folder)
    elif mode==3:
        playlist(url)
    elif mode==4:
        downloadMP3(name,url)
    elif mode==5:
        try:
            name = name.split('\\ ')[1]
        except:
            pass
        try:
            name = name.split('  - ')[0]
        except:
            pass
        addFavorite(name,url,fav_mode,iconimage,fanart,description)        
    elif mode==6:
        try:
            name = name.split('\\ ')[1]
        except:
            pass
        try:
            name = name.split('  - ')[0]
        except:
            pass
        rmFavorite(name)
    elif mode==7:
        getFavorites()
    elif mode==8:
        limpar_lista()

if __name__ == "__main__":
	main()