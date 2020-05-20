import os

import config

def create_spectograms():
    for class_name_path in config.AUDIO_DATA_CLASSES_DIR:
        print(class_name_path)

        for filename in os.listdir(class_name_path):
            if filename.endswith(".mp3"): 
                print(os.path.join(class_name_path, filename))
                continue
            else:
                continue