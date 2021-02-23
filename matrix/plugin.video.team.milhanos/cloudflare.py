# -*- coding: utf-8 -*-
import os
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
 
AddonID = xbmcaddon.Addon().getAddonInfo('id')
addon = xbmcaddon.Addon(id=AddonID) 
addon_version = addon.getAddonInfo('version')
debug = addon.getSetting('debug')

def addon_log(string):	
        if debug == 'true':
            xbmc.log("[addon Lists-%s]: %s" %(addon_version, string))

def platform():
	if xbmc.getCondVisibility('system.platform.android'):             return 'android'
	elif xbmc.getCondVisibility('system.platform.linux'):             return 'linux'
	elif xbmc.getCondVisibility('system.platform.linux.Raspberrypi'): return 'linux'
	elif xbmc.getCondVisibility('system.platform.windows'):           return 'windows'
	elif xbmc.getCondVisibility('system.platform.osx'):               return 'osx'
	elif xbmc.getCondVisibility('system.platform.atv2'):              return 'atv2'
	elif xbmc.getCondVisibility('system.platform.ios'):               return 'ios'
	elif xbmc.getCondVisibility('system.platform.darwin'):            return 'ios'	