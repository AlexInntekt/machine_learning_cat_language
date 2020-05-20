import config
import create_spectograms
import process
from bujor_library import plotInFrequencyAndSave, readWav




def start():

    if(config.GENERATE_SPECTROGRAMES):
        create_spectograms.create_spectograms()
        
    process.train()


start()


