import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
def read_image(image_name):
    """
    Чтение изображения.
    image_name: названия файла
    result: dict {'r':array, 'g':array, 'b':array}
    """
    img = plt.imread(image_name).astype(float)
    result = dict()
    result['r'] = np.ndarray.tolist(img[:,:,0])
    result['g'] = np.ndarray.tolist(img[:,:,1])
    result['b'] = np.ndarray.tolist(img[:,:,2])
    return result

def _merge_rgb(img):
    """
    Преобразование из dict (r,g,b) в один массив.
    img: dict. RGB каналы изображения
    result: array MxNx3
    """
    M, N = len(img['r']), len(img['r'][0])
    result = np.zeros((M,N,3), dtype = 'float')
    result[...,0] = np.array(img['r'])
    result[...,1] = np.array(img['g'])
    result[...,2] = np.array(img['b'])
    return result

def save_image(fname, img):
    """
    Сохранения изображения.
    fname: название файла куда будет сохранено изображение
    img: изображение. dict(rgb)
    """
    rgbArray = _merge_rgb(img)
    result = Image.fromarray(rgbArray.astype(np.uint8))
    result.save(fname, format='bmp')
