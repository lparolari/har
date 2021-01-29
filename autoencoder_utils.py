import matplotlib.pyplot as plt
import numpy as np
import random


def plot_acc(x):
    plt.plot(x[0])
    plt.plot(x[1])
    plt.plot(x[2])


def plot_gyro(x):
    plt.plot(x[3])
    plt.plot(x[4])
    plt.plot(x[5])


def plot_sensors(x):
    plt.subplot(1, 2, 1)
    plot_acc(x)
    plt.subplot(1, 2, 2)
    plot_gyro(x)


def show_samples(X: np.ndarray, y: np.ndarray, n=10, is_random=False):
    def i_or_random(i): return i if not is_random else random.randint(
        0, X.shape[0])
    indicies = list(map(i_or_random, range(n)))

    for i in indicies:
        x = X[i]

        print(f"X[{i}]: {y[i]}")
        plot_sensors(x)
        plt.show()


def get_name(i):
    """
    Return the name of i-th component of a sensor sample
    """
    assert i >= 0 and i <= 5, f"Component {i} is not supported, must be between 0 and 5"
    names = ["x_acc", "y_acc", "z_acc", "x_gyro", "y_gyro", "z_gyro"]

    return names[i]


def plot_reconstruction_error(sample, reconstruction):
    """
    Plot reconstruction error by diff for sensors
    """
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.title(get_name(i))

        plt.plot(sample[i], 'b')
        plt.plot(reconstruction[i], 'r')
        plt.fill_between(
            np.arange(125), reconstruction[i], sample[i], color='lightcoral')

    plt.legend(labels=["sample", "reconstruction", "error"])


def plot_reconstructed_signal(sample, code, reconstruction):
    """
    Show reconstucted acc/gyro signal splitted and visualize the code
    """
    plt.subplot(1, 5, 1)
    plt.title("acc original")
    plot_acc(sample)

    plt.subplot(1, 5, 2)
    plt.title("gyro original")
    plot_gyro(sample)

    plt.subplot(1, 5, 3)
    plt.title("code")
    plt.imshow(code)

    plt.subplot(1, 5, 4)
    plt.title("acc reconstructed")
    plot_acc(reconstruction)

    plt.subplot(1, 5, 5)
    plt.title("gyro reconstructed")
    plot_gyro(reconstruction)


def show_loss(history):
    h = history.history
    plt.plot(h["loss"], label="loss")
    plt.plot(h["val_loss"], label="val_loss")
    plt.legend()
    plt.show()


def show_mse(autoencoder, X_test):
    print("MSE =", autoencoder.evaluate(X_test, X_test, verbose=0))


def show_reconstructed_signals(X, encoder, decoder, n=10):
    for i in range(n):
        sample = X[i]
        code = encoder.predict(sample[np.newaxis, :])[0]
        reconstruction = decoder.predict(code[np.newaxis, :])[0]

        # Resize and reshape code for plot
        code_size_approx = int(np.ceil(np.sqrt(len(code))))
        code = code.copy()
        code.resize(np.power(code_size_approx, 2))

        plt.figure(figsize=(12, 3))
        plot_reconstructed_signal(sample=sample, code=code.reshape(
            (code_size_approx, code_size_approx)), reconstruction=reconstruction)
        plt.show()


def show_reconstruction_errors(X, encoder, decoder, n=10):
    samples = X[:n]
    codes = encoder.predict(samples)
    reconstructions = decoder.predict(codes)

    for i in range(n):
        sample = samples[i]
        reconstruction = reconstructions[i]

        plt.figure(figsize=(12, 8))
        plot_reconstruction_error(sample, reconstruction)
        plt.show()
