from tensorflow.keras.models import save_model
import tensorflow as tf


class ModelSaveCallback(tf.keras.callbacks.Callback):

    def __init__(self, file_name):
        super(ModelSaveCallback, self).__init__()
        self.file_name = file_name

    def on_epoch_end(self, epoch, logs=None):
        save_model(self.model, self.file_name)
