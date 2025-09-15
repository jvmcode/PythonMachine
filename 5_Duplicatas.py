import pickle
import pandas as pd
import matplotlib.pyplot as plt

# 🔄 Carregar o DataFrame salvo anteriormente
with open('df_metadados.pkl', 'rb') as f:
    df = pickle.load(f)

# 🔁 Identificar imagens duplicadas com base no hash
df_duplicated = df[df['image_hash'].duplicated(keep=False)]

print(f"\n🔍 Total de imagens duplicadas: {df_duplicated.shape[0]}")

# 📦 Agrupar duplicatas por hash
duplicated_images = {}
for hash_value in df_duplicated['image_hash'].unique():
    paths = df[df['image_hash'] == hash_value]['image_path'].tolist()
    duplicated_images[str(hash_value)] = paths

# 🧾 Exibir duplicatas agrupadas
print("\n🗂️ Imagens duplicadas agrupadas por hash:")
for hash_str, paths in duplicated_images.items():
    print(f"\nHash: {hash_str}")
    for path in paths:
        print(" -", path)

# 📊 Duplicatas por classe
duplicates_by_class = df_duplicated.groupby('label').size()
print("\n📊 Número de duplicatas por classe:")
print(duplicates_by_class)

# 📉 Gráfico de duplicatas por classe
if not duplicates_by_class.empty:
    ax = duplicates_by_class.plot(kind='bar', title='Duplicatas por Classe', figsize=(10, 6), color='salmon')
    plt.xticks(rotation=40)
    plt.ylabel('Quantidade de Duplicatas')

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()
else:
    print("\n🎉 Nenhuma duplicata encontrada nas classes selecionadas. Nada para plotar!")

