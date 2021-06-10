# -*- coding: utf-8 -*-

import sys
import requests
import re
import os
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import sqlite3
import base64
try:
    import urllib.parse as urllib
except ImportError:
    import urllib
try:
    import json
except:
    import simplejson as json
   


nome_contador = "OneX-1.0.0.Matrix"
link_contador = "https://whos.amung.us/pingjs/?k=6gjsucgcje"
db_host = 'https://raw.githubusercontent.com/zoreu/base_onex/main/base.txt'

addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
addon_version = addon.getAddonInfo('version')
try:
    profile = xbmcvfs.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
except:
    profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
try:
    home = xbmcvfs.translatePath(addon.getAddonInfo('path').decode('utf-8'))
except:
    home = xbmcvfs.translatePath(addon.getAddonInfo('path'))
icon_menu = home+'/resources/media/icon_menu.png'
fanart_default = home+'/fanart.jpg'
favorites = os.path.join(profile, 'favorites.dat')
temp = profile
if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else:
    FAV = []



def notify(message,name=False,iconimage=False,timeShown=5000):
    if name and iconimage:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (name, message, timeShown, iconimage))
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addonname, message, timeShown, icon))


def database_update(url):
    try:
        os.mkdir(temp)
    except:
        pass
    try:
        import ntpath
        r = requests.get(url, allow_redirects=True, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"})
        r.encoding = 'utf-8'
        data = r.text
        link = re.compile('url="(.*?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)[0]
        filename = ntpath.basename(link)
        # r=root, d=directories, f = files
        myfile = []
        for r, d, f in os.walk(temp):
            for file in f:
                if file.endswith(".db"):
                    myfile.append(os.path.join(r, file))
        if not filename in str(myfile):
            for r, d, f in os.walk(temp):
                for file in f:
                    if file.endswith(".db"):
                        try:
                            os.remove(os.path.join(r, file))
                        except:
                            pass
            r2 = requests.get(link, allow_redirects=True, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"})
            open(temp+'/'+filename, 'wb').write(r2.content)            
    except:
        pass
    
       
def conection_sqlite(sql):
    try:
        db_list = []
        for r, d, f in os.walk(temp):
            for file in f:
                if file.endswith(".db"):
                    db_list.append(os.path.join(r, file))        
        db = db_list[0]
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close
        return rows
    except:
        rows = ''
        return rows        
        

def principal():
    addDir('[B]Pesquisar[/B]','',6,'','','','Pesquise por Filmes, Series, Animes ou Novelas','','')
    addDir('[B]Minha lista[/B]','',15,'','','','Segure a tecla ok para exibir adicionar a minha lista','','')
    addDir('[B]Limpar minha lista[/B]','',16,'','','','Entre aqui para limpar minha lista','','')
    addDir('[B]Filmes[/B]','',1,'','','','','','')
    addDir('[B]Series[/B]','',3,'','','','','','')
    addDir('[B]Animes[/B]','',7,'','','','','','')
    addDir('[B]Novelas[/B]','',10,'','','','','','')
    addDir('[B]Rádios[/B]','',17,'','','','','','')
    addDir('[B]Verificar e atualizar conteúdos[/B]','',18,'','','','','','')
    SetView('WideList')
    #xbmcplugin.endOfDirectory(addon_handle,cacheToDisc=False)
    xbmcplugin.endOfDirectory(addon_handle)
    
 
    
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

def find():
    vq = get_search_string(heading="Digite algo para pesquisar")        
    if ( not vq ): return False, 0
    title = urllib.quote_plus(vq)
    pesquisar(title)


def pesquisar(name):
    pesquisar_filmes(name)
    pesquisar_series(name)
    pesquisar_animes(name)
    pesquisar_novelas(name)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle) 


def pesquisar_filmes(name):
    sql = "SELECT * FROM filmes WHERE search like '%"+name+"%' ORDER BY name"
    rows = conection_sqlite(sql)
    if rows !=[]:
        for grupo,cover,search,name,link,subtitle,thumbnail,fanart,info in rows:
            nome_negrito = '[B]'+name+'[/B]'
            addDir(nome_negrito.encode('utf-8', 'ignore'),link.encode('utf-8'),20,str(subtitle),str(thumbnail),str(fanart),str(info).encode('utf-8', 'ignore'),'','',favorite=True)
    

def pesquisar_series(name):
    sql = "SELECT * FROM series WHERE search like '%"+name+"%' ORDER BY category"
    rows = conection_sqlite(sql)
    if rows !=[]:
        categorias = []
        for cat,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(cat) not in categorias and not str(cat) == 'None':
                categorias.append(str(cat))
                nome_negrito = '[B]'+str(cat)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',4,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),'',favorite=True)
    

def pesquisar_animes(name):
    sql = "SELECT * FROM animes WHERE search like '%"+name+"%' ORDER BY category"
    rows = conection_sqlite(sql)
    if rows !=[]:
        categorias = []
        for cat,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(cat) not in categorias and not str(cat) == 'None':
                categorias.append(str(cat))
                nome_negrito = '[B]'+str(cat)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',8,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),'',favorite=True)


def pesquisar_novelas(name):
    sql = "SELECT * FROM novelas WHERE search like '%"+name+"%' ORDER BY category"
    rows = conection_sqlite(sql)
    if rows !=[]:
        categorias = []
        for cat,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(cat) not in categorias and not str(cat) == 'None':
                categorias.append(str(cat))
                nome_negrito = '[B]'+str(cat)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',11,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),'',favorite=True)


def categorias_filmes():
    sql = 'SELECT * FROM filmes ORDER BY category'
    rows = conection_sqlite(sql)
    if rows !=[]:
        categorias = []
        for cat,cover,search,name,link,subtitle,thumbnail,fanart,info in rows:            
            if str(cat) not in categorias and not str(cat) == 'None':
                categorias.append(str(cat))
                nome_negrito = '[B]'+str(cat)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',2,'',str(cover),'','',str(cat).encode('utf-8', 'ignore'),'')
    SetView('WideList')
    xbmcplugin.endOfDirectory(addon_handle)
    

def exibir_filmes(cat):
    sql = 'SELECT * FROM filmes ORDER BY name'
    rows = conection_sqlite(sql)
    if rows !=[]:
        for grupo,cover,search,name,link,subtitle,thumbnail,fanart,info in rows:
            if str(grupo) == cat:
                nome_negrito = '[B]'+name+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),link.encode('utf-8'),20,str(subtitle),str(thumbnail),str(fanart),str(info).encode('utf-8', 'ignore'),str(cat).encode('utf-8'),'',True,False,favorite=True)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)
    
def categorias_series():
    sql = 'SELECT * FROM series ORDER BY category'
    rows = conection_sqlite(sql)
    if rows !=[]:
        categorias = []
        for cat,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(cat) not in categorias and not str(cat) == 'None':
                categorias.append(str(cat))
                nome_negrito = '[B]'+str(cat)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',4,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),'',favorite=True)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)
    
   
def categorias_animes():
    sql = 'SELECT * FROM animes ORDER BY category'
    rows = conection_sqlite(sql)
    if rows !=[]:
        categorias = []
        for cat,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(cat) not in categorias and not str(cat) == 'None':
                categorias.append(str(cat))
                nome_negrito = '[B]'+str(cat)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',8,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),'',favorite=True)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)

def categorias_novelas():
    sql = 'SELECT * FROM novelas ORDER BY category'
    rows = conection_sqlite(sql)
    if rows !=[]:
        categorias = []
        for cat,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(cat) not in categorias and not str(cat) == 'None':
                categorias.append(str(cat))
                nome_negrito = '[B]'+str(cat)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',11,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),'',favorite=True)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)     
    
def exibir_temporadas(cat):
    sql = 'SELECT * FROM series ORDER BY category'
    rows = conection_sqlite(sql)
    if rows !=[]:
        temporadas = []
        for grupo,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(grupo) == cat and str(season) not in temporadas and not str(season) == 'None':
                temporadas.append(str(season))
                nome_negrito = '[B]'+str(season)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',5,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),str(season).encode('utf-8', 'ignore'))
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)
    
def exibir_temporadas_animes(cat):
    sql = 'SELECT * FROM animes ORDER BY category'
    rows = conection_sqlite(sql)
    if rows !=[]:
        temporadas = []
        for grupo,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(grupo) == cat and str(season) not in temporadas and not str(season) == 'None':
                temporadas.append(str(season))
                nome_negrito = '[B]'+str(season)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',9,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),str(season).encode('utf-8', 'ignore'))
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)

def exibir_temporadas_novelas(cat):
    sql = 'SELECT * FROM novelas ORDER BY category'
    rows = conection_sqlite(sql)
    if rows !=[]:
        temporadas = []
        for grupo,cover,search,season,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(grupo) == cat and str(season) not in temporadas and not str(season) == 'None':
                temporadas.append(str(season))
                nome_negrito = '[B]'+str(season)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),'',12,'',str(cover),'',str(main_info).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),str(season).encode('utf-8', 'ignore'))
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)    

def exibir_episodios(cat,season):
    sql = 'SELECT * FROM series ORDER BY episode'
    rows = conection_sqlite(sql)
    if rows !=[]:
        for grupo,cover,search,temp,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(grupo) == cat and str(temp) == season and not str(temp) == 'None':
                nome_negrito = '[B]'+str(episode)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),link.encode('utf-8'),20,str(subtitle),str(thumbnail),str(fanart),str(episode_info).encode('utf-8', 'ignore'),'','',True,False)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)

def exibir_episodios_animes(cat,season):
    sql = 'SELECT * FROM animes ORDER BY episode'
    rows = conection_sqlite(sql)
    if rows !=[]:
        for grupo,cover,search,temp,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(grupo) == cat and str(temp) == season and not str(temp) == 'None':
                nome_negrito = '[B]'+str(episode)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),link.encode('utf-8'),20,str(subtitle),str(thumbnail),str(fanart),str(episode_info).encode('utf-8', 'ignore'),'','',True,False)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)

def exibir_episodios_novelas(cat,season):
    sql = 'SELECT * FROM novelas ORDER BY episode'
    rows = conection_sqlite(sql)
    if rows !=[]:
        for grupo,cover,search,temp,main_info,episode,link,subtitle,thumbnail,fanart,episode_info in rows:
            if str(grupo) == cat and str(temp) == season and not str(temp) == 'None':
                nome_negrito = '[B]'+str(episode)+'[/B]'
                addDir(nome_negrito.encode('utf-8', 'ignore'),link.encode('utf-8'),20,str(subtitle),str(thumbnail),str(fanart),str(episode_info).encode('utf-8', 'ignore'),'','',True,False)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle)     
    
def radios():
    sql = 'SELECT * FROM radios ORDER BY name'
    rows = conection_sqlite(sql)
    if rows !=[]:
        for name,url,thumbnail,fanart,description in rows:
            addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),20,'',str(thumbnail),str(fanart),str(description).encode('utf-8', 'ignore'),'radios','',play=True,folder=False,favorite=True)
    xbmcplugin.setContent(addon_handle, 'movies')
    SetView('InfoWall')
    xbmcplugin.endOfDirectory(addon_handle) 


def base64decode(string):
    decoded = base64.b64decode(string).decode('utf-8')
    return decoded 

def play_video(name,url,iconimage,description,subtitle,play):
    #notify('Resolvendo url...',name,iconimage)
    #url_resolved = str(resolve(url))
    url_resolved = str(resolve(url))
    if url_resolved !='' or url_resolved !='None':
        legenda = xbmcaddon.Addon().getSetting("legenda")
        if legenda == 'true':
            file_srt = srt_browser()
        else:
            file_srt = ''
        if 'netcine' in url_resolved:
            url_final = url_resolved+'|Referer=https://p.netcine.biz/'
        else:
            url_final = url_resolved 
        if 'plugin://' in url_resolved:
            xbmc.executebuiltin('RunPlugin(' + url_resolved + ')')
        else:
            li = xbmcgui.ListItem(name, path=url_final)
            li.setArt({"icon": iconimage, "thumb": iconimage})
            li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
            if subtitle !='' and subtitle !=None and subtitle !='None':
                try:
                    subtitle = base64decode(subtitle)
                except:
                    pass
                li.setSubtitles([subtitle])
            if play == 'True':
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, li)
            else:        
                xbmc.Player().play(item=url_final, listitem=li)
    else:
        #xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Não foi possivel reproduzir o video')
        notify('Falha ao resolver url!',name,iconimage)

  

def open_url(url,referer=False):
    if referer:    
        headers = {
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",    
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "iframe",
        "Referer": referer,     
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
        }
    else:
        headers = {
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",    
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "iframe",    
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
        }
    try:
        r = requests.get(url, allow_redirects=True, headers=headers, verify=False)
        r.encoding = 'utf-8'
        data = r.text
        return data
    except:
        data = ''
        return data 

#streamtape.com        
def streamtape(url):
    correct_url = url.replace('streamtape.com/v/', 'streamtape.com/e/')
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    r = requests.get(url, allow_redirects=True, headers=headers, verify=False)
    r.encoding = 'utf-8'
    data = r.text
    link_part1_re = re.compile('videolink.+?style="display:none;">(.*?)&token=').findall(data)
    link_part2_re = re.compile("<script>.+?token=(.*?)'.+?</script>").findall(data)
    if link_part1_re !=[] and link_part2_re !=[]:
        #link = 'https:'+link_re[0]+'&stream=1'
        #link = 'https:'+link_part1_re[0]+'&token='+link_part2_re[0]
        link = 'https:'+link_part1_re[0]+'&token='+link_part2_re[0]+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    else:
        link = ''
    return link


#https://filmes.click/ - pegar link com index2.php ou play2.php
def filmes_click(url):
    parsed_uri = urllib.urlparse(url)
    base = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    data = open_url(url)
    link1 = re.compile('source src="(.*?)"').findall(data)
    link2 = re.compile('media.MediaInfo.+?"(.+?)".+?,', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
    if link1 !=[]:
        resolved = base+link1[0]
    elif link2 !=[]:
        resolved = base+link2[0]
    else:
        resolved = ''
    return resolved    

#https://megafilmeshdd.co/
def megafilmeshdd_co(url):
    data = open_url(url)
    link = re.compile('file":"(.*?)",').findall(data)
    if link !=[]:
        resolved = link[0].replace('\/', '/')
    else:
        resolved = ''
    return resolved
    
#https://superfilmes.tv/ - pegar legenda no link  
def superfilmes_tv(url):
    data = open_url(url)
    link = re.compile("mp4Id.+?=.+?'(.*?)'").findall(data)
    if link !=[]:
        resolved = link[0]+'|Referer=https://superfilmes.tv/'
        resolved = resolved.replace(' ', '')
    else:
        resolved = ''
    return resolved    

#vidyard.com - https://filmesgratiscinefilmeshd.com.br/
def vidyard_com(url):
    if not '.json' in url:
        parsed_uri = urllib.urlparse(url)
        base = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        link = re.escape(url)
        id = re.compile(r'.com/(.*?)\\').findall(link)
        id2 = re.compile(r'.com/(.*)').findall(link)
        if id !=[]:
            api = base+'player/'+id[0]+'.json'
        elif id2 !=[]:
            api = base+'player/'+id2[0]+'.json'
        data = open_url(api)
        _720p = re.compile('"profile":"720p","url":"(.*?)","mimeType"').findall(data)
        _480p = re.compile('"profile":"480p","url":"(.*?)","mimeType"').findall(data)
        _360p = re.compile('"profile":"360p","url":"(.*?)","mimeType"').findall(data)
        if _720p !=[]:
            resolved = _720p[0]+'|Referer='+base
        elif _480p !=[]:
            resolved = _480p[0]+'|Referer='+base
        elif _360p !=[]:
            resolved = _360p[0]+'|Referer='+base
        else:
            resolved = ''
    elif '.json' in url:
        data = open_url(url)
        _720p = re.compile('"profile":"720p","url":"(.*?)","mimeType"').findall(data)
        _480p = re.compile('"profile":"480p","url":"(.*?)","mimeType"').findall(data)
        _360p = re.compile('"profile":"360p","url":"(.*?)","mimeType"').findall(data)
        if _720p !=[]:
            resolved = _720p[0]+'|Referer='+base
        elif _480p !=[]:
            resolved = _480p[0]+'|Referer='+base
        elif _360p !=[]:
            resolved = _360p[0]+'|Referer='+base
        else:
            resolved = ''
    else:
        resolved = ''
    return resolved

##https://www.mmfilmeshd.tv/
def mmfilmes_tv(url):
    if 'player.moduda.fun' in url and 'embed' in url:
        data = open_url(url,'https://www.mmfilmeshd.tv/')
        iframe = re.compile("addiframe.+?'(.*?)'").findall(data)
        if iframe !=[]:
            data2 = open_url(iframe[0],'https://player.moduda.fun/')
            source = re.compile("file':'(.*?)',").findall(data2)
            resolved = source[0]
        else:
            resolved = ''
    else:
        resolved = ''
    return resolved


#https://fshd.link/ - https://www.askflix.net/
def fsh_link(url):
    if 'fshd.link' in url and 'embed' in url:
        data = open_url(url,'https://www.receitasdahora.online/')
        source = re.compile('"file":"(.*?)",').findall(data)
        if source !=[]:
            resolved = source[0].replace('\/', '/')
        else:
            resolved = ''
    else:
        resolved = ''
    return resolved
    
def youtube(url):
    url_data = urllib.urlparse(url)
    query = urllib.parse_qs(url_data.query)
    video = query["v"][0]
    plugin = 'plugin://plugin.video.youtube/play/?video_id={}'.format(video)
    return plugin
    

def resolve(url):
    #obs: fembeed é feurl
    try:
        from lib import resolveurl
    except:
        pass
    try:
        url = base64decode(url)
    except:
        pass
    #resolved1 = resolveurl.resolve(url)
    #xbmcgui.Dialog().ok('[COLOR white][B]AVISO[/B][/COLOR]', str(resolved1))
    try:
        if 'streamtape' in url:
            resolved = streamtape(url)
        elif 'filmes.click' in url and 'index2.php' in url or 'filmes.click' in url and 'play2.php' in url:
            resolved = filmes_click(url)
        elif 'filmes.click' in url and '.mp4' in url:
            resolved = url
        elif 'megafilmeshdd.co' in url:
            resolved = megafilmeshdd_co(url)
        elif 'superfilmes.tv' in url and 'share' in url:
            resolved = superfilmes_tv(url)
        #https://fornodelenha.net/
        elif 'apiblogger.xyz' in url:
            #https://apiblogger.xyz/blogger/video-play.mp4/?contentId=a15479cd9ff388a4
            resolved = url+'|Referer=https://play.midiaflixhd.com/'
        elif 'vidyard.com' in url:
            resolved = vidyard_com(url)
        elif 'player.moduda.fun' in url and 'embed' in url:
            resolved = mmfilmes_tv(url)
        elif 'fshd.link' in url and 'embed' in url:
            resolved = fsh_link(url)
        elif 'youtube.com' in url and 'watch' in url:
            resolved = youtube(url)
        elif not 'feurl' in url and not 'fembed' in url and '.mp4' in url or '.m3u8' in url or '.mp3' in url:
            resolved = url
        else:
            if 'feurl.com' and 'api' in url:
                url = url.replace('api/source','v')
            resolved = resolveurl.resolve(url)
            if not 'http' in str(resolved):
                notify('Falha ao resolver, tente novamente...')
            #xbmcgui.Dialog().ok('Sucesso', resolved)
    except:
        resolved = url
    return resolved
       

def limpar_lista():
    try:
        Path = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
    except:
        Path = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('profile'))
    arquivo = os.path.join(Path, "favorites.dat")
    exists = os.path.isfile(arquivo)
    if exists:
        if xbmcgui.Dialog().yesno(addonname, 'Deseja limpar minha lista?'):
            try:
                os.remove(arquivo)
            except:
                pass
            xbmcgui.Dialog().ok('Sucesso', '[B][COLOR white]Minha lista limpa com sucesso![/COLOR][/B]')


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
                subtitle = i[3]
                iconimage = i[4]
                fanArt = i[5]
                description = i[6]
                cat = i[7]
                season = i[8]
                play = i[9]
                if play == 'True':
                    play = True
                    folder = False
                else:
                    play = False
                    folder = True
                
                addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),mode,str(subtitle),str(iconimage),str(fanArt),str(description).encode('utf-8', 'ignore'),str(cat).encode('utf-8', 'ignore'),str(season).encode('utf-8', 'ignore'),play=play,folder=folder,favorite=True)
            xbmcplugin.setContent(addon_handle, 'movies')
            SetView('InfoWall')
            xbmcplugin.endOfDirectory(addon_handle)
        else:
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Nenhuma Série ou Filme Adicionado na Minha lista')
                
    except:
        xbmcplugin.setContent(addon_handle, 'movies')
        SetView('InfoWall')
        xbmcplugin.endOfDirectory(addon_handle)

def addFavorite(name,url,mode,subtitle,iconimage,fanart,description,cat,season,play):
    favList = []
    if os.path.exists(favorites)==False:
        addonID = xbmcaddon.Addon().getAddonInfo('id')
        addon_data_path = xbmcvfs.translatePath(os.path.join('special://home/userdata/addon_data', addonID))
        if os.path.exists(addon_data_path)==False:
            os.mkdir(addon_data_path)
        xbmc.sleep(7)
        favList.append((name,url,mode,subtitle,iconimage,fanart,description,cat,season,play))
        a = open(favorites, "w")
        a.write(json.dumps(favList))
        a.close()
        notify('adicionado a Minha lista!',name,iconimage)
        #xbmc.executebuiltin("XBMC.Container.Refresh")
    else:
        a = open(favorites).read()
        data = json.loads(a)
        data.append((name,url,mode,subtitle,iconimage,fanart,description,cat,season,play))
        b = open(favorites, "w")
        b.write(json.dumps(data))
        b.close()
        notify('Adicionado a Minha lista!',name,iconimage)
        #xbmc.executebuiltin("XBMC.Container.Refresh")


def rmFavorite(name):
    data = json.loads(open(favorites).read())
    for index in range(len(data)):
        if data[index][0]==name:
            del data[index]
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    notify('Removido da Minha lista!')
    #xbmc.executebuiltin("Container.Refresh")        
    


def addDir(name,url,mode,subtitle,iconimage,fanart,description,cat,season,play=False,folder=True,favorite=False):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)+"&subtitle="+urllib.quote_plus(subtitle)+"&description="+urllib.quote_plus(description)+"&cat="+urllib.quote_plus(cat)+"&season="+urllib.quote_plus(season)+"&play="+urllib.quote_plus(str(play))       
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
    if play:
        li.setProperty('IsPlayable', 'true')
    if favorite:
        try:
            name_fav = json.dumps(name.decode('utf-8'))
        except:
            name_fav = name.decode('utf-8')
        try:
            contextMenu = []
            if name_fav in FAV:
                contextMenu.append(('Remover da Minha lista','RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
            else:
                fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&iconimage=%s&fanart=%s&description=%s&cat=%s&season=%s&play=%s&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(subtitle), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description), urllib.quote_plus(cat), urllib.quote_plus(season), urllib.quote_plus(str(play)), str(mode)))
                contextMenu.append(('Adicionar a Minha Lista','RunPlugin(%s)' %fav_params))
            li.addContextMenuItems(contextMenu)
        except:
            pass
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=li, isFolder=folder)


def contador():
    try:
        import urllib.request as urllib2
        opener = urllib2.build_opener()
        opener.addheaders=[('Accept-Language', 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'),('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'), ('Referer', nome_contador)]
        data = opener.open(link_contador).read()
    except:
        pass
    
contador()   


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
    subtitle=None
    cat=None
    season=None
    pesquisa=None
    fav_mode=None
    page=1
    play='False'

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
        subtitle=urllib.unquote_plus(params["subtitle"])
    except:
        pass
    try:
        cat=urllib.unquote_plus(params["cat"])
    except:
        pass
    try:
        season=urllib.unquote_plus(params["season"])
    except:
        pass        
    try:
        pesquisa=urllib.unquote_plus(params["pesquisa"])
    except:
        pass
    try:
        play=urllib.unquote_plus(params["play"])
    except:
        pass        
    try:
        fav_mode=int(params["fav_mode"])
    except:
        pass

    if mode==None:
        database_update(db_host)
        principal()        
    elif mode==1:
        database_update(db_host)
        categorias_filmes()
    elif mode==2:
        database_update(db_host)
        exibir_filmes(cat)
    elif mode==3:
        database_update(db_host)
        categorias_series()
    elif mode==4:
        database_update(db_host)
        exibir_temporadas(cat)
    elif mode==5:
        database_update(db_host)
        exibir_episodios(cat,season)
    elif mode==6:
        database_update(db_host)
        find()
    elif mode==7:
        database_update(db_host)
        categorias_animes()
    elif mode==8:
        database_update(db_host)
        exibir_temporadas_animes(cat)
    elif mode==9:
        database_update(db_host)
        exibir_episodios_animes(cat,season)
    elif mode==10:
        database_update(db_host)
        categorias_novelas()
    elif mode==11:
        database_update(db_host)
        exibir_temporadas_novelas(cat)
    elif mode==12:
        database_update(db_host)
        exibir_episodios_novelas(cat,season)
    elif mode==13:
        try:
            name = name.split('\\ ')[1]
        except:
            pass
        try:
            name = name.split('  - ')[0]
        except:
            pass
        addFavorite(name,url,fav_mode,subtitle,iconimage,fanart,description,cat,season,play)        
    elif mode==14:
        try:
            name = name.split('\\ ')[1]
        except:
            pass
        try:
            name = name.split('  - ')[0]
        except:
            pass
        rmFavorite(name)
    elif mode==15:
        getFavorites()
    elif mode==16:
        limpar_lista()
    elif mode==17:
        database_update(db_host)
        radios()
    elif mode==18:
        database_update(db_host)
        notify('Conteúdos verificados!')
    elif mode==20:
        play_video(name,url,iconimage,description,subtitle,play)

if __name__ == "__main__":
	main()