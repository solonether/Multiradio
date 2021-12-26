#/bin/python

import PySimpleGUI as sg
import vlc

url = 'https://ssl1.mediastreaming.it:9094'

vlc = vlc.Instance('--input-repeat=-1', '--fullscreen')

player = vlc.media_player_new()
media = vlc.media_new(url)

player.set_media(media)
player.play()

input('Enter per uscire')
