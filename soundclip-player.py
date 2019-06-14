import os
import simpleaudio
from time import sleep

clips = os.listdir()

print(clips)

#for event in button.read_loop():
#  if should_ring(last_event_timestamp, event):
#    last_event_timestamp = event.timestamp()
#    wave_obj = simpleaudio.WaveObject.from_wave_file("voy_door_chime.wav")
#    play_obj = wave_obj.play()
#    play_obj.wait_done()
