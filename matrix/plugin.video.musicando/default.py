# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.musicando'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID_1 = "PLA_I2ay5YcUX0ACG51hPhUNbVvQh7DBYa"
YOUTUBE_CHANNEL_ID_2 = "PLKBWSlRFdti8b7j0xmnC7V_KLDiJtq3mM"
YOUTUBE_CHANNEL_ID_3 = "PL006FCEA9617FC5D3"
YOUTUBE_CHANNEL_ID_4 = "PLuAVLeOijDklytHKpYFUFIHwoxl1dId30"
YOUTUBE_CHANNEL_ID_5 = "PLFB8AF09186DB9D01"
YOUTUBE_CHANNEL_ID_6 = "PL6Gafkv5Pl9g28WbnvjLOjlfM8_2o3Byi"
YOUTUBE_CHANNEL_ID_7 = "PL_34_m4eTlaP5cyIG-2hUcqF2bZxHgZlZ"
YOUTUBE_CHANNEL_ID_8 = "PLpTLBDsxuOwsRuSayev2e3VV9MtYJ14vM"
YOUTUBE_CHANNEL_ID_9 = "PLKXrIAvyq_VvjfymsO9ytMufAIvKb9JM4"
YOUTUBE_CHANNEL_ID_10 = "PLQ_PIlf6OzqL3BE0rB6clb9IzLLkkSKUF"
YOUTUBE_CHANNEL_ID_11 = "PLirAqAtl_h2pRAtj2DgTa3uWIZ3-0LKTA"
YOUTUBE_CHANNEL_ID_12 = "PLOuAaPDGy5br7qCO28VX5AzTq4_hmGKDX"
YOUTUBE_CHANNEL_ID_13 = "PLEPQby6_o7m1-wWJunTFbIqAGWOsGF60C" 
YOUTUBE_CHANNEL_ID_14 = "PLEPQby6_o7m1-RL9nCkMHaylGNZukSKyE" 
YOUTUBE_CHANNEL_ID_15 = "PLgFPSBWI2ATsSylWergrX76P05BvPqvj5"
YOUTUBE_CHANNEL_ID_16 = "PL5n4nHJVIy2aLKxhS62pDDeQqj87GBQwG"
YOUTUBE_CHANNEL_ID_17 = "PLS3wtfWNsaB4CAx4mmVXLhIn9mj97_JR6" 
YOUTUBE_CHANNEL_ID_18 = "PLte1uSnf9cie52PLOUCp_stMvdrzDbTcq"
YOUTUBE_CHANNEL_ID_19 = "PLCafHNeL3wfM2PpF72rB7sl-FM45gp1M2"
YOUTUBE_CHANNEL_ID_20 = "PL5Ak9XUVqZ_dotR9a8Tax3FddEmNKCx9M" 
YOUTUBE_CHANNEL_ID_21 = "PLn0y3ceFPGc4HQlWUJ55-VAAGJePuANFs"
YOUTUBE_CHANNEL_ID_22 = "PLZS5lG1BRo7sYjbwJP2PAAepaSavffeZq"
YOUTUBE_CHANNEL_ID_23 = "PL6491007F60E13DD6" 
YOUTUBE_CHANNEL_ID_24 = "PLmdwo0nDs2HkRLalTAewacI9E-OjaQLjq"
YOUTUBE_CHANNEL_ID_25 = "PLcfQmtiAG0X-fmM85dPlql5wfYbmFumzQ"
YOUTUBE_CHANNEL_ID_26 = "PLA_I2ay5YcUVJbVT8tb-cZQ6pGJHWlnHH"
YOUTUBE_CHANNEL_ID_27 = "PL539EAB0AAC7115D6" 
YOUTUBE_CHANNEL_ID_28 = "PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ"
YOUTUBE_CHANNEL_ID_29 = "PLFPg_IUxqnZNnACUGsfn50DySIOVSkiKI"
YOUTUBE_CHANNEL_ID_30 = "PL8F6B0753B2CCA128"
YOUTUBE_CHANNEL_ID_31 = "PLDcnymzs18LWrKzHmzrGH1JzLBqrHi3xQ"
YOUTUBE_CHANNEL_ID_32 = "PLH6pfBXQXHEC2uDmDy5oi3tHW6X8kZ2Jo"
YOUTUBE_CHANNEL_ID_33 = "PL47oRh0-pTouthHPv6AbALWPvPJHlKiF7" 
YOUTUBE_CHANNEL_ID_34 = "PLYAYp5OI4lRLf_oZapf5T5RUZeUcF9eRO"
YOUTUBE_CHANNEL_ID_35 = "PL5ep_pPaQcTe05W_o7KIuS374Q8s7jMDo"
YOUTUBE_CHANNEL_ID_36 = "PL5AA7A6E1055205F2"
YOUTUBE_CHANNEL_ID_37 = "PLvLX2y1VZ-tFJCfRG7hi_OjIAyCriNUT2"
YOUTUBE_CHANNEL_ID_38 = "PLTN0khS5IJuj7PuKEzQgxXtIvwioWTHpg" 
YOUTUBE_CHANNEL_ID_39 = "PLr8RdoI29cXIlkmTAQDgOuwBhDh3yJDBQ"
YOUTUBE_CHANNEL_ID_40 = "PLFRSDckdQc1th9sUu8hpV1pIbjjBgRmDw"
YOUTUBE_CHANNEL_ID_41 = "PL64E6BD94546734D8"
YOUTUBE_CHANNEL_ID_42 = "PL6o_1dl6P3DGZe0Ju52dcnHvNkM7Rj--W"
YOUTUBE_CHANNEL_ID_43 = "PL0zQrw6ZA60Z6JT4lFH-lAq5AfDnO2-aE" 
YOUTUBE_CHANNEL_ID_44 = "PLXupg6NyTvTxw5-_rzIsBgqJ2tysQFYt5"
YOUTUBE_CHANNEL_ID_45 = "PLQog_FHUHAFUDDQPOTeAWSHwzFV1Zz5PZ"
YOUTUBE_CHANNEL_ID_46 = "PL0qf-h7_tcFlVRoYS6f0tjvk0NWdR3aD_"
YOUTUBE_CHANNEL_ID_47 = "PLLQvN69uicxy8S5diyNJMKMzRIxzrLBYo"
YOUTUBE_CHANNEL_ID_48 = "PLWNXn_iQ2yrKzFcUarHPdC4c_LPm-kjQy" 
YOUTUBE_CHANNEL_ID_49 = "PLLMA7Sh3JsOQQFAtj1no-_keicrqjEZDm"
YOUTUBE_CHANNEL_ID_50 = "PL9NMEBQcQqlzwlwLWRz5DMowimCk88FJk"
YOUTUBE_CHANNEL_ID_51 = "PLfY-m4YMsF-OM1zG80pMguej_Ufm8t0VC"
YOUTUBE_CHANNEL_ID_52 = "PLVXq77mXV53-Np39jM456si2PeTrEm9Mj"
YOUTUBE_CHANNEL_ID_53 = "PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG" 
YOUTUBE_CHANNEL_ID_54 = "PLD7SPvDoEddZUrho5ynsBfaI7nqhaNN5c"
YOUTUBE_CHANNEL_ID_55 = "PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J"
YOUTUBE_CHANNEL_ID_56 = "PLirAqAtl_h2pRAtj2DgTa3uWIZ3-0LKTA"
YOUTUBE_CHANNEL_ID_57 = "PLtv6DWBXhImIiGKX13ZzZPkndP6W_nFBu"
YOUTUBE_CHANNEL_ID_58 = "PLDcnymzs18LWrKzHmzrGH1JzLBqrHi3xQ" 
YOUTUBE_CHANNEL_ID_59 = "PLXogPMnvZ7sQqWN1pDfYVeGsrkWYRa6Ex"
YOUTUBE_CHANNEL_ID_60 = "PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10"
YOUTUBE_CHANNEL_ID_61 = "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"
YOUTUBE_CHANNEL_ID_62 = "PL-PXKb5jSjwZT2QzeJCIlYSqs0cZvy808"
YOUTUBE_CHANNEL_ID_63 = "PLkop8kow5TsGKdGT_UGuQV8mfmzp5k0NJ" 
YOUTUBE_CHANNEL_ID_64 = "PLCqukCFvcNBKN4okn9OFCQZvkFdbki2vH"
YOUTUBE_CHANNEL_ID_65 = "PLdJjSWn0fv_epSyOXQKcre9ZfY8sJxrJS"

def addDir(title, url, thumbnail,folder=True):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   # addDir(title = "Musicando",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)
    addDir(title="[COLOR lime]LOS 40 CLASSIC - Solo Los Numeros 1[/COLOR] ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",thumbnail="https://m.media-amazon.com/images/I/71g3X4SkbRL._SS500_.jpg",folder=True )
    addDir(title="[COLOR lime]San Valentin 2020 Baladas[/COLOR] ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",thumbnail="https://c.saavncdn.com/233/Baladas-en-San-Valentin-Vol-1-Spanish-2014-500x500.jpg",folder=True )
    addDir(title="[COLOR lime]Las mejores canciones: Eros Ramazzotti [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/61ZJwWFPTOL._SX342_QL70_ML2_.jpg",folder=True )
    addDir(title="[COLOR lime]Las mejores canciones: Romanticas de la Historia [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",thumbnail="https://chameleons.com.ua/tmp/cache/images/de/c11/dec11ae35206df53a032e9b5560b498a.jpg",folder=True )
    addDir(title="[COLOR lime]Las mejores canciones: Para hacer el Amor [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",thumbnail="https://c.saavncdn.com/222/Las-Mejores-Canciones-Rom-nticas-para-Hacer-el-Amor-Grandes-xitos-de-la-M-sica-de-los-A-os-70-s-80-s-y-90-s-English-2014-500x500.jpg",folder=True )
    addDir(title="[COLOR lime]Las mejores canciones: Instrumental [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",thumbnail="https://i.ytimg.com/vi/2AEtFlvecLI/maxresdefault.jpg",folder=True )
    addDir(title="[COLOR lime]El poder del amor [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",thumbnail="http://www.osvaldocarnival.com.ar/wp-content/uploads/2016/02/poderamor700x475.png",folder=True )
    addDir(title="[COLOR lime]NOW Thats What I Call Power Ballads [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/71d1No%2BzZ3L._SL1101_.jpg",folder=True )
    addDir(title="[COLOR lime]Las mejores canciones romanticas para dedicar a una mujer  [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",thumbnail="https://i.pinimg.com/originals/7c/0f/e4/7c0fe41d89afafaaec6d1d0cab194856.jpg",folder=True )
    addDir(title="[COLOR lime]Black music: Romanticas [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",thumbnail="https://thumbs.dreamstime.com/t/beautiful-singer-girl-singing-microphone-13131685.jpg",folder=True )
    addDir(title="[COLOR lime]Mi tiempo de relax[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",thumbnail="https://resources.tidal.com/images/3e3992c1/05a0/48d4/be42/f8f243d1804c/640x640.jpg",folder=True )
    addDir(title="[COLOR lime]Non Stop[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",thumbnail="http://www.24hoursupport.com/wp-content/uploads/music-non-stop-298x300.jpg",folder=True )
    addDir(title="[COLOR lime]Los mejores videos musicales[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",thumbnail="https://st-listas.20minutos.es/images/2012-04/327206/list_640px.jpg",folder=True )
    addDir(title="[COLOR lime]Navidades Pop[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",thumbnail="http://resources.wimpmusic.com/images/22a86af7/3b78/40b9/88c3/6ce3ab7004c0/640x640.jpg",folder=True )
    addDir(title="[COLOR lime]Top halloween songs[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",thumbnail="https://m.media-amazon.com/images/I/71VYIFLseAL._SS500_.jpg",folder=True )
    addDir(title="[COLOR lime]Los mejores videos musicales del 2019[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",thumbnail="https://i.ytimg.com/vi/5LLaDDBYGqc/maxresdefault.jpg",folder=True )
    addDir(title="[COLOR lime]Bandas sonoras de peliculas[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",thumbnail="https://st-listas.20minutos.es/images/2018-09/433515/list_640px.jpg",folder=True )
    addDir(title="[COLOR lime]Canciones Disney ESP[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",thumbnail="https://www.music-bazaar.com/album-images/vol14/684/684664/2537263-big/Disney-Grandes-Exitos-En-Espanol-cover.jpg",folder=True )
    addDir(title="[COLOR lime]Canciones Disney VO[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",thumbnail="https://i.ytimg.com/vi/ZyBGOfaR8HM/maxresdefault.jpg",folder=True )
    addDir(title="[COLOR lime]Lord Of The Dance RIVERDANCE[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",thumbnail="https://i.ebayimg.com/images/g/QScAAOSwYc5aEvd2/s-l300.jpg",folder=True )
    addDir(title="[COLOR lime]Zarzuelas[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",thumbnail="https://documents.uow.edu.au/~vincent/frontpage.jpg",folder=True )
    addDir(title="[COLOR lime]Conciertos de viena[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",thumbnail="https://www.hola.com/imagenes/viajes/20171102101439/como-asistir-concierto-ano-nuevo-viena-austria/0-503-117/como-asistir-al-concierto-ano-nuevo-viena-m.jpg",folder=True )
    addDir(title="[COLOR lime]Videos para proyectar en SPINNING[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",thumbnail="https://as01.epimg.net/deporteyvida/imagenes/2019/09/03/portada/1567536855_286772_1567537023_noticia_normal_recorte1.jpg",folder=True )
    addDir(title="[COLOR lime]Buddha Bar[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/61II2JL4SdL._SX466_.jpg",folder=True )
    addDir(title="[COLOR lime]Baladas[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",thumbnail="https://angelmaillo.files.wordpress.com/2015/06/baladas.jpg",folder=True )
    addDir(title="[COLOR lime]Latino[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",thumbnail="https://www.kope.es/fotos/musica-latina.jpg",folder=True )
    addDir(title="[COLOR lime]RAP (ESP) 2017: lo mejor [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",thumbnail="https://pbs.twimg.com/profile_images/679616237056454656/bwWambhv_400x400.jpg",folder=True )
    addDir(title="[COLOR lime]New Age [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",thumbnail="https://i.servimg.com/u/f42/12/32/40/98/tm/theene10.jpg",folder=True )
    addDir(title="[COLOR lime]House[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",thumbnail="https://conectandotussentidos.files.wordpress.com/2011/07/housemusic.jpg",folder=True )
    addDir(title="[COLOR lime]Electronica[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",thumbnail="https://mp3life.info/wp-content/uploads/2019/09/estudio-m%C3%BAsica-electr%C3%B3nica-portada.jpg",folder=True )
    addDir(title="[COLOR lime]Jazz[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",thumbnail="https://merehistory.weebly.com/uploads/1/5/1/5/15155754/9463352.png",folder=True )
    addDir(title="[COLOR lime]Pop [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",thumbnail="https://compartefestival.files.wordpress.com/2013/10/top-pop-songs-of-all-times.jpg",folder=True )
    addDir(title="[COLOR lime]Hip Hop[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",thumbnail="https://vignette.wikia.nocookie.net/eswikia/images/b/bd/Hip_hop.png",folder=True )
    addDir(title="[COLOR lime]Rock Alternativo[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",thumbnail="http://1.bp.blogspot.com/-jhK2XedhzH8/Um32Rurc18I/AAAAAAAAAAo/nv58oHH-p7o/s1600/33881.max1024.jpg",folder=True )
    addDir(title="[COLOR lime]Reggae[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",thumbnail="https://arteyculturaenrebeldia.files.wordpress.com/2016/02/reggae-pop-gary-grayson.jpg",folder=True )
    addDir(title="[COLOR lime]Trap[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",thumbnail="https://i.ytimg.com/vi/jqvNYewvgoY/maxresdefault.jpg",folder=True )
    addDir(title="[COLOR lime]Cafe Del Mar  [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",thumbnail="https://static.radio.es/images/broadcasts/ee/a1/103017/1/c300.png",folder=True )
    addDir(title="[COLOR lime]Country[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",thumbnail="https://angelaproffitt.com/wp-content/uploads/2019/09/CMFC2.png",folder=True )
    addDir(title="[COLOR lime]Zumba[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",thumbnail="https://www.mujerhoy.com/noticias/201903/19/media/cortadas/strong-zumba-kdFF-U70955342851XDI-560x420@MujerHoy.jpg",folder=True )
    addDir(title="[COLOR lime]Pop Rock[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",thumbnail="https://bobsmusiccafe.com/wp-content/uploads/2018/05/ROCK2.png",folder=True )
    addDir(title="[COLOR lime]R&B[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",thumbnail="https://image-ticketfly.imgix.net/00/02/82/49/76-og.png",folder=True )
    addDir(title="[COLOR lime]Dance[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",thumbnail="https://image.redbull.com/rbcom/052/2018-09-06/d305b993-4ea7-47b8-9507-9a4b1697f881/0012/0/0/648/2000/2248/1150/1/afropop-dance-crazes.jpg",folder=True )
    addDir(title="[COLOR lime]Clasico (ESP)[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",thumbnail="http://static-1.ivoox.com/canales/3/7/7/4/5901460064773_XXL.jpg",folder=True )
    addDir(title="[COLOR lime]Asiatica[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",thumbnail="https://is5-ssl.mzstatic.com/image/thumb/Music/8e/c0/27/mzi.uxejehjp.jpg/600x600bf.png",folder=True )
    addDir(title="[COLOR lime]Mejicana[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",thumbnail="https://i.ytimg.com/vi/RVONUZUIspM/hqdefault.jpg",folder=True )
    addDir(title="[COLOR lime]Soul[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",thumbnail="https://res.cloudinary.com/teepublic/image/private/s--G_6Uz4mO--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1518865655/production/designs/2371810_0.jpg",folder=True )
    addDir(title="[COLOR lime]Conciertos (ESP)[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",thumbnail="https://i.ytimg.com/vi/EVvcxqcvjNA/hqdefault.jpg",folder=True )
    addDir(title="[COLOR lime]Conciertos[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",thumbnail="http://1.bp.blogspot.com/-_Wg9mMsvRW8/UJ9-b8ybfuI/AAAAAAAAArQ/xTX_nVRlpmI/s1600/bonjovilisbon.jpg",folder=True )
    addDir(title="[COLOR lime]Rhythm & blues[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",thumbnail="http://muzik.galeon.com/blues.gif",folder=True )
    addDir(title="[COLOR lime]Cristiana[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",thumbnail="https://i.ytimg.com/vi/yQpY3e4adBE/maxresdefault.jpg",folder=True )
    addDir(title="[COLOR lime]Hard Rock[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",thumbnail="https://previews.123rf.com/images/ss1001/ss10011706/ss1001170600325/80798448-vector-illustration-crossed-guitars-and-lettering-hard-rock-on-grunge-background.jpg",folder=True )
    addDir(title="[COLOR lime]Heavy Metal[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",thumbnail="https://www.ultimate-guitar.com/static/article/news/9/96119_ver1566915350.jpg",folder=True )
    addDir(title="[COLOR lime]Clasico[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",thumbnail="https://m.media-amazon.com/images/I/61b5pkvmCWL._SS500_.jpg",folder=True )
    addDir(title="[COLOR lime]RedMusic[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",thumbnail="https://i1.sndcdn.com/avatars-000259249518-v79xzu-t500x500.jpg",folder=True )
    addDir(title="[COLOR lime]Billboard Top Songs[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",thumbnail="https://www.music-bazaar.com/album-images/vol15/739/739072/2587643-big/Billboard-Top-20-Alternative-Songs-Top-25-Hot-Rock-Songs-07-04-2014-cover.jpg",folder=True )	
    addDir(title="[COLOR lime]Los 40 Principales[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",thumbnail="http://los40ar00.epimg.net/iconos/v1.x/v1.0/promos/promo_og_los40g.png",folder=True )
    addDir(title="[COLOR lime]VEVO Videos de todos los tiempos[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/31CLD-RfumL.png",folder=True )
    addDir(title="[COLOR lime]Techno ( Videos Del Recuerdo )[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",thumbnail="https://image-cdn.neatoshop.com/styleimg/88621/none/black/default/421300-20;1561607784t.jpg",folder=True )
    addDir(title="[COLOR lime]Las Mejores canciones pop [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",thumbnail="https://nicolasramospintado.files.wordpress.com/2007/04/top-internacional.jpg",folder=True )
    addDir(title="[COLOR lime]Los 70 mejores videos de la historia[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",thumbnail="https://img.desmotivaciones.es/201103/musica_69.jpg",folder=True )
    addDir(title="[COLOR lime]POP Music Playlist 2020[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",thumbnail="https://i1.sndcdn.com/artworks-000648030919-9sx0om-t500x500.jpg",folder=True )
    addDir(title="[COLOR lime]POP Music 2017[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",thumbnail="https://i.ytimg.com/vi/YbvKQK5bhvY/maxresdefault.jpg",folder=True )
    addDir(title="[COLOR lime]POP (ESP) 2017[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",thumbnail="https://m.media-amazon.com/images/I/71w5f2NrjkL._SS500_.jpg",folder=True )
    addDir(title="[COLOR lime]Musica (ESP) 80/90/00 [/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",thumbnail="https://i.pinimg.com/originals/d5/ed/94/d5ed949f90f404352b6c97138de2df42.jpg",folder=True )
    addDir(title="[COLOR lime]Musica del Recuerdo 70, 80, 90[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",thumbnail="https://i.ytimg.com/vi/p1GOfr_TGdo/hqdefault.jpg",folder=True )
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
