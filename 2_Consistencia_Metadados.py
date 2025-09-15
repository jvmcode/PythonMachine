import pandas as pd
import matplotlib.pyplot as plt
import pickle

with open('df_metadados.pkl', 'rb') as f:
    df = pickle.load(f)

# 🔍 Verificar valores nulos
print("\n❓ Quantidade de valores nulos por coluna:")
print(df.isnull().sum())

# 📐 Verificar distribuição das dimensões (largura x altura)
plt.figure(figsize=(8, 6))
plt.scatter(df['width'], df['height'], alpha=0.5)
plt.xlabel('Width')
plt.ylabel('Height')
plt.title('📊 Distribuição das Dimensões das Imagens')
plt.grid(True)
plt.show()

# 📏 Verificar dimensões fora do padrão (exemplo: imagens muito pequenas ou muito grandes)
# Ajuste os limites conforme necessário
min_width, max_width = 100, 2000
min_height, max_height = 100, 2000

dim_outliers = df[
    (df['width'] < min_width) | (df['width'] > max_width) |
    (df['height'] < min_height) | (df['height'] > max_height)
]

print(f"\n⚠️ Imagens com dimensões fora do intervalo esperado ({min_width}-{max_width}px largura, {min_height}-{max_height}px altura):")
print(dim_outliers[['image_path', 'width', 'height']])
