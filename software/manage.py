import config
import create_spectograms
import process
from bujor_library import plotInFrequencyAndSave, readWav




def start():

    if(config.GENERATE_SPECTROGRAMES):
        create_spectograms.create_spectograms()

    if(config.PROCCESS_TRAINING):
        process.train()


start()


