import dbus
import sched, time
#s = sched.scheduler(time.time, time.sleep)
currentTrack = ""
currentArtist = ""

session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                     "/org/mpris/MediaPlayer2")
spotify_properties = dbus.Interface(spotify_bus,
                                    "org.freedesktop.DBus.Properties")

def getsong():
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    # The property Metadata behaves like a python dict
    #for key, value in metadata.items():
        #print(key, value)

    # To just print the title
    global currentTrack
    currentTrack = metadata['xesam:title']

    global currentArtist
    currentArtist = ','.join(metadata['xesam:albumArtist'])

    #print(currentTrack)
    #print(currentArtist)

    if currentArtist != '' :
        f = open('/PATH/TO/TXT/nowlisten.txt', 'w')
        output = currentTrack+' - '+currentArtist #format output here
        print(output)
        f.write(output)
        f.close()

    time.sleep(30)

while True:
    getsong()
