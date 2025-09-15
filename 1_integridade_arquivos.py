import cv2
import os
import pandas as pd
import imagehash
import matplotlib.pyplot as plt
from PIL import Image

# Diretório raiz
root_dir = './sports-classification/train'

# Classes selecionadas
selected_classes = [
    'football', 'formula 1 racing', 'nascar racing', 'baseball',
    'hockey', 'basketball', 'olympic wrestling', 'rugby',
    'canoe slalom', 'roller derby'
]

# Inicialização
count_corrupted = 0
corrupted = []
dataframe_list = []

# Coleta de metadados
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

# Criar DataFrame
df = pd.DataFrame(columns=[
    'image_path', 'corrupted', 'image_hash', 'image_format',
    'width', 'height', 'channels', 'label'
], data=dataframe_list)

# 🔍 Verificação de formatos
print("\n📦 Quantidade de imagens por formato:")
print(df['image_format'].value_counts())

# 📊 Gráfico de formatos
ax = df['image_format'].value_counts().plot(kind='bar', title='Número de imagens por formato', figsize=(8, 6))
plt.xticks(rotation=40)
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=10)
plt.show()

# 📈 Estatísticas das dimensões
print("\n📐 Estatísticas das dimensões das imagens:")
print(df.describe().loc[['mean', 'std', 'min', 'max']])

# 🧨 Imagens corrompidas
print(f"\n❌ Total de imagens corrompidas: {count_corrupted}")
print("Lista de imagens corrompidas:")
for path in corrupted:
    print("-", path)
    
import pickle

with open('df_metadados.pkl', 'wb') as f:
    pickle.dump(df, f)

