#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:32:54 2018

@author: tarik
"""

# Building a CNN (Convolutional Neural Network) for the purpose of
# image recognition

# This entire model's output is at 93% with additional optimization not considered

# Importing the required libraries
from keras.models import Sequential
from keras.layers import Convolution2D # Built-in Keras libraries for faster testing
from keras.layers import MaxPooling2D # MaxPooling allows for bitwise conversion
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator # For processing images

# Initializing the CNN
classifier = Sequential()

# Adding the convolution

classifier.add(Convolution2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

# Adding Max Pooling

classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Adding another Conv Layer to increase the accuracy of the outcome
classifier.add(Convolution2D(32, (3, 3), activation='relu')) # Don't need input_shape
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening the image to a 2D plane for analysis

classifier.add(Flatten())

# Adding a fully connected Dense layer

classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=1, activation='sigmoid'))

# Compiling the CNN

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Fitting the CNN to the images

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/single_prediction',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/single_prediction',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=25,
        validation_data=test_set,
        validation_steps=2000)
