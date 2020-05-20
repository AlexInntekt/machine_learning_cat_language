
import os

SHOW_CONFIG_VALUES = False
GENERATE_SPECTROGRAMES = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DATA_DIR = os.path.join(BASE_DIR, "data/audio_data")
AUDIO_DATA_CLASSES_DIR = []
CLASSES_NAMES = ['growling','purring','chattering','hissing','trilling']



for class_name in CLASSES_NAMES:
    class_path = os.path.join(AUDIO_DATA_DIR, class_name)
    classes_tuple = (class_name,class_path)
    AUDIO_DATA_CLASSES_DIR.append(classes_tuple)

if SHOW_CONFIG_VALUES:
    print("Base directory: {}".format(BASE_DIR))
    print("AUDIO_DATA_CLASSES_DIR: {}".format(AUDIO_DATA_CLASSES_DIR))