import pickle
import pandas as pd
import matplotlib.pyplot as plt

# 🔄 Carregar o DataFrame salvo anteriormente
with open('df_metadados.pkl', 'rb') as f:
    df = pickle.load(f)

# 📊 Contagem de imagens por classe
class_counts = df['label'].value_counts()
print("\n📦 Número de imagens por classe:")
print(class_counts)

# 📉 Verificar desequilíbrio entre classes
min_count = class_counts.min()
max_count = class_counts.max()
print(f"\n⚖️ Classe com menos imagens: {class_counts.idxmin()} ({min_count})")
print(f"⚖️ Classe com mais imagens: {class_counts.idxmax()} ({max_count})")

# 📊 Gráfico de barras
ax = class_counts.plot(kind='bar', title='Distribuição das Classes', figsize=(10, 6), color='skyblue')
plt.xticks(rotation=40)
plt.ylabel('Quantidade de Imagens')

# Adicionando os valores exatos em cima de cada barra
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()),
                ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
