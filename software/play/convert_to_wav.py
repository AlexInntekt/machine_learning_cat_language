from os import path
from pydub import AudioSegment

for x in range(1,100):
    try:
        # files                                                                         
        src = "mp3/{}.mp3".format(x)
        dst = "wav/{}.wav".format(x)

        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
    except Exception as e:
        print("Failed at {}".format(x))