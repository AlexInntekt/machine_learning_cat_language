import os
import base64 

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt


# def convert_image_to_str(image_path):
#     with open(image_path, "rb") as imageFile:
#         st = base64.b64encode(imageFile.read())
#         return(st)

# def train():
#     path = "/home/alex/Desktop/FILS/NNGA/proj/data/audio_data/growling/1.wav"
#     st = convert_image_to_str(path)
#     print(st)


def train():
    #https://www.tensorflow.org/tutorials/images/classification

    batch_size = 128
    epochs = 15
    IMG_HEIGHT = 150
    IMG_WIDTH = 150

    train_dir = "/home/alex/Desktop/FILS/NNGA/proj/data/spectral_data"
    validation_dir = "/home/alex/Desktop/FILS/NNGA/proj/data/spectral_data"

    train_growling_dir = os.path.join(train_dir, 'growling')  
    train_hissing_dir = os.path.join(train_dir, 'hissing')  
    train_chattering_dir = os.path.join(train_dir, 'chattering')
    train_trilling_dir = os.path.join(train_dir, 'trilling')
    train_purring_dir = os.path.join(train_dir, 'purring')

    validation_growling_dir = os.path.join(validation_dir, 'growling')
    validation_hissing_dir = os.path.join(validation_dir, 'hissing')
    validation_chattering_dir = os.path.join(validation_dir, 'chattering')
    validation_trilling_dir = os.path.join(validation_dir, 'trilling')
    validation_purring_dir = os.path.join(validation_dir, 'purring')

    num_growling_tr = len(os.listdir(train_growling_dir))
    num_hissing_tr = len(os.listdir(train_hissing_dir))
    num_chattering_tr = len(os.listdir(train_chattering_dir))
    num_trilling_tr = len(os.listdir(train_trilling_dir))
    num_purring_tr = len(os.listdir(train_purring_dir))

    num_growling_val = len(os.listdir(validation_growling_dir))
    num_hissing_val = len(os.listdir(validation_hissing_dir))
    num_chattering_val = len(os.listdir(validation_chattering_dir))
    num_trilling_val = len(os.listdir(validation_trilling_dir))
    num_purring_val = len(os.listdir(validation_purring_dir))

    total_train = num_growling_tr + num_hissing_tr + num_chattering_tr + num_trilling_tr + num_purring_tr
    total_val = num_growling_val + num_hissing_val + num_chattering_val + num_trilling_val + num_purring_val

    train_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our training data
    validation_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our validation data



    train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                           directory=train_dir,
                                                           shuffle=True,
                                                           target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                           class_mode='binary')

    val_data_gen = validation_image_generator.flow_from_directory(batch_size=batch_size,
                                                              directory=validation_dir,
                                                              target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                              class_mode='binary')

    model = Sequential([
        Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
        MaxPooling2D(),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

    model.summary()

    history = model.fit_generator(
        train_data_gen,
        steps_per_epoch=total_train // batch_size,
        epochs=epochs,
        validation_data=val_data_gen,
        validation_steps=total_val // batch_size
    )