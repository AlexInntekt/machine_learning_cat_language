import os

import pylab
import wave

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
                save_path = save_path.replace(".wav","")

                print("Converting ")
                print(input_file_path)
                print("..to..")
                print(save_path)
                print("\n\n")

                graph_spectrogram(input_file_path, save_path)
                # plot_and_save(input_file_path, save_path)
                
            else:
                continue

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

def graph_spectrogram(input_file_path, output_file_path):
    sound_info, frame_rate = get_wav_info(input_file_path)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % input_file_path)
    # pylab.title('spectrogram')
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig(output_file_path)

def plot_and_save(input_file_path, output_file_path):
    fs, x = readWav(input_file_path)
    
    plotInFrequencyAndSave(x, fs, output_file_path)

    pass