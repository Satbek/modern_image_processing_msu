import unittest
import sys
sys.path.append('../src')
import matplotlib.pyplot as plt
import numpy as np
import shutil, glob, os
from util.data.bmp import read_image, save_image, _merge_rgb

class TestImageRead(unittest.TestCase):
    """
    Тесты функций для считывания изображений 
    """
    def setUp(self):
        for image in glob.iglob('images/*.bmp'):
            shutil.copy(image,'.')

    def test_read_image(self):
        for image in glob.iglob('*.bmp'):
            im1 = np.ndarray.tolist(plt.imread(image).astype(float))
            im2 = np.ndarray.tolist(_merge_rgb(read_image(image)))
            self.assertEqual(im1, im2, image)

    def test_save_image(self):
        for im_name in glob.iglob('*.bmp'):
            #Считываем и сохраняем под новым именем
            new_im_name = 'new_' + im_name
            img = read_image(im_name)
            save_image(fname = new_im_name, img = img)
            #Грузим и сверяем
            self.assertEqual(np.ndarray.tolist(plt.imread(im_name)),np.ndarray.tolist(plt.imread(new_im_name)))

    def tearDown(self):
        for image in glob.iglob('*.bmp'):
            os.remove(image)


if __name__ == '__main__':
    unittest.main()
