import os

import config
from bujor_library import plotInFrequencyAndSave,readWav

def create_spectograms():
    for class_name_path_tuple in config.AUDIO_DATA_CLASSES_DIR:
        # print(class_name_path_tuple)

        class_name = class_name_path_tuple[0]
        path = class_name_path_tuple[1]

        for filename in os.listdir(class_name_path_tuple[1]):
            input_file_path = os.path.join(path,filename)
            # print(filename)
            if input_file_path.endswith(".wav"): 
                # file_path = os.path.join(class_name_path_tuple[1], filename)
                # print(file_path)
                save_path = os.path.join(config.BASE_DIR,"data")
                save_path = os.path.join(save_path,"spectral_data")
                # print(class_name)
                save_path = os.path.join(save_path, class_name)
                
                save_path = os.path.join(save_path, filename)
                save_path = save_path+".jpg"
            
                print(input_file_path)
                print(save_path)
                # plot_and_save(input_file_path, output_file_path)
                print("\n\n")
            else:
                continue

def plot_and_save(input_file_path, output_file_path):
    fs, x = readWav(input_file_path)
    
    plotInFrequencyAndSave(x, fs, output_file_path)

    pass