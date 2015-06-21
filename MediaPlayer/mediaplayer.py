import pyglet
import os

metadata = os.stat("song.mp3")
song = open("song.mp3", "rb")
stream = pyglet.media.StreamingSource()
stream.get_audio_data(song)
# stream.duration = metadata.st_atime

player = pyglet.media.Player()
player.queue(stream)
player.play()

pyglet.app.run()