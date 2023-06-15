import os

import numpy
from PIL import Image
import cv2 as cv

def img_resize(img, widen, height, interpolation=cv.INTER_LINEAR):
    img = cv.resize(img, (widen, height), interpolation=interpolation)

    return img

def resize_images_PIL(input_dir, output_dir, size):
    # 确保输出文件夹存在
    os.makedirs(output_dir, exist_ok=True)
    widen = size[0]
    height = size[1]
    # 遍历目标目录下的所有文件
    for filename in os.listdir(input_dir):
        # 检查文件是否为图片文件
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # 构建输入和输出文件的完整路径
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # 打开图片文件
            image = Image.open(input_path)
            # 判断图片的横竖
            print(filename)
            size_img = image.size

            if size_img[0] > size_img[1]:   # 它是一张横着的图片
                # 调整图片尺寸
                resized_image = image.resize((widen, height))
            else:   # 竖着
                resized_image = image.resize((height, widen))

            # 保存修改后的图片到输出文件夹
            resized_image.save(output_path)

            # 关闭图片文件
            image.close()

def resize_images_cv(input_dir:str, output_dir: str, size: tuple) -> numpy.numarray:
    # 确保输出文件存在
    os.makedirs(output_dir, exist_ok=True)
    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        # 读取图片
        img = cv.imread(img_path)
        # 判断图片的横竖
        # print(img.shape[0], img.shape[1])  # [0]: height [1]: widen
        if img.shape[0] > img.shape[1]: # 竖着的图片
            img = img_resize(img, size[1], size[0])
        else:   # 横着的图片
            img = img_resize(img, size[0], size[1])
        # 保存图片 获取输出路径
        output_path = os.path.join(output_dir, img_name)
        cv.imwrite(output_path, img)

# 指定目标目录、输出目录和目标尺寸
# input_directory = ''
# output_directory = ''
# target_size = (640, 480)

# 调用函数进行图片尺寸修改
resize_images_PIL('img_transform/img_input', 'img_transform/img_output_PIL', (640, 480))

# resize_images_cv('img_transform/img_input', 'img_transform/img_output', (640, 480))
