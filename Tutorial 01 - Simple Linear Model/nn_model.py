import pandas as pd
import numpy as np
import tensorflow as tf
import os
import matplotlib.pyplot as plt

# read data
data = pd.read_csv("Tutorial 01 - Simple Linear Model/dat1.csv")
y = data.var10
X = data.drop("var10", axis=1)

# build model
out_layer = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([out_layer])

# compile model
model.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=0.1))

# fit model
history = model.fit(X, y, epochs=150, verbose=True)

# plot metric trajectory
plt.plot(history.history["loss"])
plt.show()

# show layer values
print("trained layer:", out_layer.weights)