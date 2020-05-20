import config
import create_spectograms

from bujor_library import plotInFrequencyAndSave, readWav



def plot_and_save(file_path):
    fs, x = readWav(file_path)
    plotInFrequencyAndSave(x, fs, "rezult.jpg")

    pass

def start():

    # create_spectograms.create_spectograms()
    plot_and_save("/home/alex/Desktop/FILS/NNGA/proj/data/audio_data/growling/41.wav")

start()


