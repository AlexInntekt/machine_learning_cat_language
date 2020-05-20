import os

import config
from bujor_library import plotInFrequencyAndSave,readWav

def create_spectograms():
    for class_name_path in config.AUDIO_DATA_CLASSES_DIR:
        print(class_name_path)

        for filename in os.listdir(class_name_path):
            if filename.endswith(".mp3"): 
                file_path = os.path.join(class_name_path, filename)
                plot_and_save(file_path)
            else:
                continue

def plot_and_save(file_path):
    fs, x = readWav(file_path)
    plotInFrequencyAndSave(x, fs, "rezult.jpg")

    pass