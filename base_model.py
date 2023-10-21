import os
import tensorflow as tf
import numpy as np

# sess = tf.Session(config=tf.ConfigProto(device_count={'GPU': 0}))
def main():
    ## read config files
    ## get the data
    (X_train_full, y_train_full), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train_full = X_train_full / 255.0
    X_test = X_test / 255.0
    X_valid, X_train = X_train_full[:5000], X_train_full[5000:]
    y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

    # set random seed
    seed = 2021
    tf.random.set_seed(seed)
    np.random.seed(seed)

    # define layers
    LAYERS = [tf.keras.layers.Flatten(input_shape=[28, 28]),
              tf.keras.layers.Dense(300, kernel_initializer="he_normal"),
              tf.keras.layers.LeakyReLU(),
              tf.keras.layers.Dense(100, kernel_initializer="he_normal"),
              tf.keras.layers.LeakyReLU(),
              tf.keras.layers.Dense(10, activation="softmax")]

    model = tf.keras.models.Sequential(LAYERS)

    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer=tf.keras.optimizers.SGD(learning_rate=1e-3),
                  metrics=["accuracy"])

    model.summary()

    # train the model
    history = model.fit(X_train, y_train, epochs=10,
                        validation_data=(X_valid, y_valid), verbose=2)

    model.save("model.h5")

main()