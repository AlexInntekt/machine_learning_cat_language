import os

import config
from bujor_library import plotInFrequencyAndSave,readWav

def create_spectograms():
    for class_name_path_tuple in config.AUDIO_DATA_CLASSES_DIR:
        # print(class_name_path_tuple)

        class_name = class_name_path_tuple[0]
        path = class_name_path_tuple[1]

        for filename in os.listdir(class_name_path_tuple[1]):
            filename = os.path.join(path,filename)
            print(filename)
            if filename.endswith(".mp3"): 
                file_path = os.path.join(class_name_path_tuple[1], filename)

                save_path = os.path.join(config.BASE_DIR,"data")
                save_path = os.path.join(save_path,"spectral_data")
                save_path = os.path.join(save_path, class_name)
            
                print(save_path)
                # plot_and_save(input_file_path, output_file_path)
            else:
                continue

def plot_and_save(input_file_path, output_file_path):
    fs, x = readWav(input_file_path)
    
    plotInFrequencyAndSave(x, fs, output_file_path)

    pass