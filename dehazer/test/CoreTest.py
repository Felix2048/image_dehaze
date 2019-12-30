from dehazer.core import DarkChannel
import numpy as np
import unittest

from PIL import Image
import matplotlib.pyplot as plt


class CoreTest(unittest.TestCase):

    def test_dark_channel(self):
        origin = Image.open('../../image/forest1.jpg')
        image = np.asarray(origin)
        plt.figure('origin')
        plt.imshow(origin)
        plt.show()
        darkChannel = DarkChannel.getDarkChannel(image)
        plt.figure('darkChannel')
        plt.imshow(darkChannel, cmap='gray')
        plt.show()
        self.assertTrue(darkChannel is not None)

    def test_none_dark_channel(self):
        with self.assertRaises(AttributeError):
            DarkChannel.getDarkChannel()