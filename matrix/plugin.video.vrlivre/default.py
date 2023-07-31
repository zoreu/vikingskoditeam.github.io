# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.vrlivre'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

base = "plugin://plugin.video.youtube/"


def addDir(title, url, thumbnail,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "[COLOR blue]VRlivreTV[/COLOR] [COLOR red]By Sergio[/COLOR]",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)
   addDir(title = "[COLOR red]Curso de Arduino 2018[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXu0KEA49Cv-nxYnYjna0mfy/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/Arduino.png", folder = True)
   addDir(title = "[COLOR blue]Drops GIMP[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXvrR6BVrmpani5-MxOGk2LP/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/gimp.png", folder = True)
   addDir(title = "[COLOR lime]Batocera & Recalbox[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXsLy024SPWs5oQOWCzu_5F8/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/recalbox.png", folder = True)
   addDir(title = "[COLOR white]Portifólios da Informática (2007 à 2016)[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXubMFEyYak9Y3j8tLH1GjgG/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/portifolio.png", folder = True)
   addDir(title = "[COLOR yellow]Palestras e Eventos[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXv_F7BalCn59t07fltG2_lq/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/palestras.png", folder = True)
   addDir(title = "[COLOR blue]Curso de Artes Gráficas com Software Livre - Barbará Tostes[/COLOR]"              , url = base + "playlist/PL058pFiG1gecMSwTlDZdv-Oc57IuLsmuH/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/grafica.png", folder = True)
   addDir(title = "[COLOR lime]Tutoriais do Canal Digola[/COLOR]"              , url = base + "playlist/PLHJQSVdtWwIUPl1agKHb_XYzZb2sEXIFM/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/digola.png", folder = True)
   addDir(title = "[COLOR white]Tutoriais do Canal Vikings[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXvdOf-ViGkdjVCVHb7SURa6/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/vikings.png", folder = True)
   addDir(title = "[COLOR yellow]Desenhos Vetorizados do Canal Bruno Nerd Comics[/COLOR]"              , url = base + "playlist/PLvZLRSZ-A58sm-RBd_EDYox7n8ZKfye3c/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/nerdcomics.png", folder = True)
   addDir(title = "[COLOR blue]Ultraman - Dublado (480p)[/COLOR]"              , url = base + "playlist/PLQKCUFcFQXDSTj4h8EM3ZXkQJLBFHD93u/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/ultraman.jpg", folder = True)
   addDir(title = "[COLOR lime]O Regresso de Ultraman - Dublado (480p/720p)[/COLOR]"              , url = base + "playlist/PLxMLyiIzP7Ih-ih2Gcxw2kgS0xcruyEor/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/ultraman.jpg", folder = True)
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
