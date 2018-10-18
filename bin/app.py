import sys
sys.path.append("../src")
import util.data.bmp as bmp
from transform import mirror, rotate, normalize
from filter import sobel, median, gauss, gradient

def proccess_image(image, func, *args, **kwargs):
    """
    Применение функции к изображению, считанному через read_image
    image: dict {'r':array, 'g':array, 'b':array}
    func: функция для обработки изображени, первым аргументом у нее должен быть двумерный массив
    *args, **kwargs: аргументы функции func
    result: dict {'r':array, 'g':array, 'b':array}
    """
    result = dict()
    for chanel in image:
        result[chanel] = func(image[chanel], *args, **kwargs)
    return result

def rotate_command(array, direction, degree):
    if direction == 'cw':
        degree = int(degree)
    else:
        degree = -int(degree)
    return rotate.rotate(array, degree)

def mirror_command(*args, **kwargs):
    return mirror.mirror(*args, **kwargs)

def sobel_command(*args, **kwargs):
    res = sobel.sobel(*args, **kwargs)
    res = normalize.shift(res, 128)
    res = normalize.suppress_ejection(res)
    return res

def median_command(array, rad):
    rad = int(rad)
    return median.median(array, rad)

def gauss_command(array, mode, sigma):
    sigma = float(sigma)
    return gauss.gauss(array, mode, sigma)

def gradient_command(array, mode, sigma):
    sigma = float(sigma)
    res = gradient.gradient(array, mode, sigma)
    res = normalize.suppress_ejection(res)
    return res

def main(): 
    command = sys.argv[1] + "_command"
    params = sys.argv[2:-2]
    input_image = sys.argv[-2]
    output_image = sys.argv[-1]
    img = bmp.read_image(input_image)
    result = proccess_image(img, eval(command), *params)
    bmp.save_image(output_image, result)

if __name__ == "__main__":
    main()
