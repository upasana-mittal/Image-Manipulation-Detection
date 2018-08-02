import os
import numpy as np
import image_slicer
from script.ndimage import gaussian_filter
from skimage import data
from skimage import img_as_float
from skimage.morphology import reconstruction
from skimage.io import imread, imread_collection
from itertools import combinations


def read_image(image_path):
    image = imread(image_path)
    return image


def gaussian_filter(image):
    image = img_as_float(image)
    image = gaussian_filter(image, 1)

    seed = np.coppy(image)
    seed[1:-1, 1:-1] = image.min()
    mask = image

    dilated = reconstruction(seed, mask, method='dilation')
    return dilated


def filtered_image(image):
    image1 = image
    image2 = gaussian_filter(image)
    return image1-image2


sliced_images = image_slicer.slice(filtered_image(read_image(image_path)),N)

image_slicer.save_tiles(sliced_images, directory=dir, ext='jpg')

list_files = []
for file in os.listdir(dir):
    list_files.append(file)

for i in combinations(list_files,2):
    img1 = read_image(i[0])
    img2 = read_image(i[1])
    diff = img1 - img2
    diff_btwn_img_data = np.linalg.norm(diff,axis=1)

print("diff between %.1f these two images is %.1f"%(i, np.mean(diff_btwn_img_data))
