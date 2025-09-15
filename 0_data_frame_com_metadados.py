import cv2
import os
import pandas as pd
import imagehash
from PIL import Image

root_dir = './sports-classification/train'

# Classes que queremos analisar. As 10 classes com maior numero de imagens.
selected_classes = [
    'football', 'formula 1 racing', 'nascar racing', 'baseball',
    'hockey', 'basketball', 'olympic wrestling', 'rugby',
    'canoe slalom', 'roller derby'
]

count_corrupted = 0
corrupted = []
dataframe_list = []

for folder in os.listdir(root_dir):
    if folder not in selected_classes:
        continue

    child_dir = os.path.join(root_dir, folder)
    for image in os.listdir(child_dir):
        img_dir = os.path.join(child_dir, image)
        try:
            _, image_format = image.split('.')
        except ValueError:
            image_format = None

        image_format = image_format.lower() if image_format else None
        img = cv2.imread(img_dir)

        if img is not None:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_hash = imagehash.phash(img_pil)
            width, height, channels = img.shape
            img_corrupted = False
        else:
            count_corrupted += 1
            corrupted.append(img_dir)
            img_corrupted = True
            img_hash, image_format, width, height, channels = None, None, None, None, None

        dataframe_list.append([
            img_dir, img_corrupted, img_hash, image_format,
            width, height, channels, folder
        ])

print(f'Total de Imagens Corrompidas: {count_corrupted}')
print(f'Imagens corrompidas: {corrupted}')

df = pd.DataFrame(columns=[
    'image_path', 'corrupted', 'image_hash', 'image_format',
    'width', 'height', 'channels', 'label'
], data=dataframe_list)
