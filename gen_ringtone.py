import os
import shutil
from musicpy import daw as mpd
import sf2_loader.read_sf2.fluidsynth
import fluidsynth

from ringtones_config import *

# workaround
sf2_loader.read_sf2.fluidsynth.raw_audio_string = fluidsynth.raw_audio_string

if __name__ == '__main__':
    daw = mpd.daw(1)
    daw.load(0, SOUNDFONT_PATH)

    if not os.path.exists("output"):
        os.mkdir("output")

    for name, chord in RINGTONES.items():
        print(name)
        daw.export(mp.track(chord, instrument=SOUNDFONT_INSTRUMENT, bpm=BPM), filename=f"temp.wav",
                   track_extra_lengths=(3,))

        with pedalboard.io.AudioFile("temp.wav", "r") as input_audio:
            with pedalboard.io.AudioFile(f"output/{name}.mp3", "w", 44100, 2, quality=128) as output_audio:
                chunk = input_audio.read(input_audio.frames)
                output_audio.write(PEDALBOARD_EFFECT.process(chunk, 44100, reset=False))

    os.remove("./temp.wav")

    for name, dup_names in DUPLICATE_RINGTONES.items():
        for dup_name in dup_names:
            shutil.copyfile(f"output/{name}.mp3", f"output/{dup_name}.mp3")
