import os
import simpleaudio
import random
from time import sleep

clips = os.listdir('sound-clips')

while True:
  random_clip = 'sound-clips/' + clips[random.randrange(0,len(clips))]
  wave_obj = simpleaudio.WaveObject.from_wave_file(random_clip)
  play_obj = wave_obj.play()
  play_obj.wait_done()
  sleep(random.randrange(600,1200))

#for event in button.read_loop():
#  if should_ring(last_event_timestamp, event):
#    last_event_timestamp = event.timestamp()
#    wave_obj = simpleaudio.WaveObject.from_wave_file("voy_door_chime.wav")
#    play_obj = wave_obj.play()
#    play_obj.wait_done()
