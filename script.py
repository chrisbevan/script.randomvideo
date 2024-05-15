import sys
import xbmc
import xbmcgui
import xbmcaddon
import os
import random

# log: /Users/chrisbevan/Library/Logs
# tail -f kodi.log | grep "debug <general>: script.randomvideo:"

ADDON = xbmcaddon.Addon()
ADDONID = ADDON.getAddonInfo('id')
CWD = ADDON.getAddonInfo('path')

def log(txt):
    message = '%s: %s' % (ADDONID, txt)
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

class main():
    params = dict(arg.split('=') for arg in sys.argv[1].split('&'))
    videodir = params.get("dir","")
    
    log(videodir)
    all_files = os.listdir(videodir)
    video_files = [f for f in all_files if f.endswith((".mp4", ".mkv", ".avi", ".mov"))]
    random.shuffle(video_files)
        
    # Create an empty playlist
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

    # Add each video to the playlist
    for video in video_files:
        video_path = os.path.join(videodir, video)
        playlist.add(video_path)
    
    xbmc.Player().play(item = playlist,windowed=True)
        

if __name__ == '__main__':
    main()
