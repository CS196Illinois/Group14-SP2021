import tensorflow as tf
import numpy as np
import pathlib
#import matplotlib.pyplot

batch_size = 2
img_height = 1024
img_width = 1024

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'E:\CNN dataset',
    validation_split=0.2,
    subset='training',
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)
print(train_ds.class_names)
val_ds = train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'E:\CNN dataset',
    validation_split=0.2,
    subset='validation',
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

num_classes = 2
model = tf.keras.models.Sequential([
    tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 5
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)
model.save('E:\CNN saved models')
