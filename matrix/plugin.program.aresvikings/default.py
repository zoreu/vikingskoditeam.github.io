import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import xbmcplugin
import os
import sys
import re
import urllib.parse as urllib
import urllib.request as urllib2
from resources.libs import database, downloader, extract, clear


addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
home = xbmcvfs.translatePath(addon.getAddonInfo('path'))
icon = addon.getAddonInfo('icon')
addon_handle = int(sys.argv[1])
build_url_menu = 'https://raw.githubusercontent.com/zoreu/zoreu.github.io/master/kodi/builds_matrix.txt'  

def notify(msg):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addonname, msg, 1000, icon))

def addir(name,url,mode,iconimage,fanart,description,skin,setaddon,folder=True):
    li=xbmcgui.ListItem(name)
    if mode !=0:
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)+"&skin="+urllib.quote_plus(str(skin))+"&setaddon="+urllib.quote_plus(str(setaddon))
    else:
        u=sys.argv[1]
    li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    li.setArt({"icon": iconimage, "thumb": iconimage})
    li.setProperty('fanart_image', fanart)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=li, isFolder=folder)
    
def principal():
    addir('[B]Builds[/B]','',1,'','','','','')
    addir('[B]Elementum[/B]','',3,'','','','','')
    xbmcplugin.endOfDirectory(addon_handle)
    
def list_builds():
    data = open_url(build_url_menu)
    list_build = re.compile('name="(.*?)"\nurl="(.*?)"\niconimage="(.*?)"\nfanart="(.*?)"\ndescription="(.*?)"\nskin_id="(.*?)"').findall(data)
    for name, url, iconimage, fanart, description, skin in list_build:       
       addir(name.encode('utf-8', 'ignore'),url,2,str(iconimage),str(fanart),str(description).encode('utf-8', 'ignore'),str(skin),'',folder=False)

def mybuilds():
    addir('[B]-------- Lista de Builds --------[/B]','',0,'','','','','')
    try:
        list_builds()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)
    
def elementum():
    import ntpath
    data = open_url('https://elementumorg.github.io/')
    list_addons = re.compile('<div class="platform-asset"><a href="(.*?)" title="(.*?)".+?</a>').findall(data)
    for link, name in list_addons:
        #print(name.strip())
        if '-' in link and not 'Client' in name:
            filename = ntpath.basename(link)
            addon_id = filename.split('-')[0]
            #name = name.strip()+' - '+addon_id 
            name = addon_id+' - '+name.strip()
            addir(name.encode('utf-8', 'ignore'),link,4,'','','','',addon_id,folder=False)

def elementum_list():
    addir('[B]-------- Plugins do Elementum --------[/B]','',0,'','','','','')
    try:
        elementum()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)
    
    
def setskin(skin_id):
    skin_txt = os.path.join(home, 'skin.txt')
    try:
        os.remove(skin_txt)
    except:
        pass
    try:
        f = open(skin_txt,'w')
        f.write('skin="%s"'%skin_id)
        f.close()
    except:
        pass  

def install_build(name,url,skin):
    if xbmcgui.Dialog().yesno(addonname, 'Deseja Instalar %s?\nA Configuração atual do kodi será modificada'%name):
        kodi = xbmcvfs.translatePath('special://home')
        addons = xbmcvfs.translatePath('special://home/addons')
        packages = xbmcvfs.translatePath('special://home/addons/packages')
        media_kodi = xbmcvfs.translatePath('special://home/media')
        userdata_kodi = xbmcvfs.translatePath('special://home/userdata')
        download_file = resolve(url)
        try:
            if download_file.endswith(".zip"):
                # limpando kodi
                #try:
                #    clear.reset(addons)
                #except:
                #    pass
                #try:
                #    clear.reset(userdata_kodi)
                #except:
                #    pass
                #try:
                #    clear.reset(media_kodi)
                #except:
                #    pass                    
                import ntpath
                try:
                    os.mkdir(packages)
                except:
                    pass
                filename = ntpath.basename(download_file)
                dest=os.path.join(packages, filename)
                try:
                    os.remove(lib)
                except:
                    pass
                try:
                    downloader.download(download_file, name, dest)
                except:
                    print('Wizard Builds: Falha ao baixar, link invalido ou download cancelado')
                    raise Exception
                try:
                    extract.extract_zip(dest,kodi)
                except:
                    print('Wizard Builds: Falha ao extrair arquivos.')
                    raise Exception
                xbmc.sleep(1000)
                try:
                    os.remove(dest)
                except:
                    pass
                skin_folder = os.path.join(addons, skin)
                if os.path.isdir(skin_folder):
                    setskin(skin)                    
                xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','APERTE OK PARA FECHAR O KODI E ABRA NOVAMENTE!')   
                xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Application.Quit","id":1}') 
            else:
                print('Wizard Builds: Arquivo não é zip ou não foi encontrado um link')
                raise Exception
        except:
            notify('Falha ao Instalar Build!')
            
def install_addon(addon_id,url):
    if xbmcgui.Dialog().yesno(addonname, 'Deseja Instalar %s?'%addon_id):
        addons = xbmcvfs.translatePath('special://home/addons')
        packages = xbmcvfs.translatePath('special://home/addons/packages')
        try:
            import ntpath
            try:
                os.mkdir(packages)
            except:
                pass
            filename = ntpath.basename(url)
            dest=os.path.join(packages, filename)            
            try:
                downloader.download(url, addon_id, dest)
            except:
                print('Wizard Builds: Falha ao baixar, link invalido ou download cancelado')
                raise Exception
            try:
                extract.extract_zip(dest,addons)
            except:
                print('Wizard Builds: Falha ao extrair arquivos.')
                raise Exception
            xbmc.sleep(1000)
            database.enable_addon(addon_id)
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','APERTE OK PARA FECHAR O KODI E ABRA NOVAMENTE!')   
            xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Application.Quit","id":1}')
        except:
            notify('Falha ao Instalar Addon!')         


def open_url(url):
    try:
        hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        req = urllib2.Request(url, headers=hdr)
        response = urllib2.urlopen(req)
        data = response.read().decode('utf-8')
        return data
    except:
        data = ''
        return data

def mediafire(url):
    data = open_url(url)
    link = re.compile('aria-label="Download file"\n.+?href="(.*?)"',re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
    return link[0]

def resolve(url):
    if 'mediafire' in url:
        try:
            resolved = mediafire(url)
        except:
            resolved = ''
    else:
        resolved = url
    return resolved    


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
    name=None
    mode=None
    iconimage=None
    fanart=None
    description=None
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
        skin=urllib.unquote_plus(params["skin"])
    except:
        pass
    try:
        setaddon=urllib.unquote_plus(params["setaddon"])
    except:
        pass                
    if mode==None:
        principal()
    elif mode==1:
        mybuilds()
    elif mode==2:
        install_build(name,url,skin)
    elif mode==3:
        elementum_list()
    elif mode==4:
        install_addon(setaddon,url)

if __name__ == "__main__":
	main()
 