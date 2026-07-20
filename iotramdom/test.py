import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', 
           input_shape=(28, 28, 1)),
           MaxPooling2D((2, 2)),
           Flatten(),
           Dense(64, activation='relu'),
           Dense(10, activation='softmax')
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

model.save('edge_ai_model.h5')

loaded_model = tf.keras.models.load_model('edge_ai_model.h5')

sample_image = x_test[0]
sample_image_reshaped = sample_image.reshape(1, 28, 28, 1)

prediction = loaded_model.predict(sample_image_reshaped)
predicted_class = np.argmax(prediction)

plt.imshow(sample_image.reshape(28,28), cmap='gray')
plt.title(f"predicted Class: {predicted_class}")
plt.show()
