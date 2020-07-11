# TensoFlow 2 Tutorials
by [Lindo Khoza](https://www.linkedin.com/in/lindo-khoza-606b7817b/) / [Github](https://github.com/willkhoza)

## TensorFlow 2 - Tutotial 01

Tutorial 1 is about building a simple linear nueral network in Keras. The word Keras will almost be used interchangebly with TensorFlow 2. There is a concrete difference but that is outside the scope of these Tutorials. But for completeness, Keras is just a mask for TensorFlow 2, allowing the standard user to build TensorFlow 2 models in a manner easier than working with pure TensorFlow 2 code. 

The simple linear nueral network is an example of what is called supervised models. These are models in which you have both the covariates and the so called dependent variable. 


Other models include unsupervised models, these are models built on solely having just the covariates, a common strategy in this case is to pursue some sort of clustering in order to generate insight from that. There's also an interesting group of models called reinforcement learning, these are built on bayesian logic, where the model improves through trial and error while navigating some enviroment.

### Generate Multiple Linear Regression Data

#### Background

The structure of a simple linear nueral network can never model non-linear regressions, regardless of how complex you arrange it. This is because all that a nueral network is convolutions of multiple functions. As such, the convolution of linear functions inside other linear functions is still a linear function. 

In order to accomodate more complex dependencies in the data, you will use something called activatyion functions. This will allow your nueral network the mathematical structure it requires to model non-linear regressions. This is discussed in [Tutorial x](linkhere.com).

#### Notes

The intention behind generating linearly regressed data is to be able to study the nueral network in it's simplest form. The use of this structure of nueral network is very limited, and possibly counterintuive as will be seen shortly. Albeit, this is an important step, so much so that I've made a Python script that is dedicated to generating this multiple linear regression dataset.

The [python script](00_simulate_data.py) generates a csv with an arbitrary amount of covariates and observations, the last column being variable we seek to model in our supervised model. The data generated has a linear relationship together with a little bit of noise. Some of the covariates produced a not related to the dependent variables, so the analyst still has the obligition to identify this dependance.


### Do the anlytical due dilligence in R

The R folder does some analytical due dilligence in R. This is simply building the statistical multivate regression model in R.

### Build a simple nueral network in Keras

import pandas as pd
import tensorflow as tf
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