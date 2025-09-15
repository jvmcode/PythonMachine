import pickle

# 🔄 Carregar o DataFrame salvo anteriormente
with open('df_metadados.pkl', 'rb') as f:
    df = pickle.load(f)

# 🧨 Total de imagens corrompidas
total_corrompidas = df['corrupted'].sum()
print(f"\n❌ Total de imagens corrompidas: {total_corrompidas}")

# ✅ Distribuição entre corrompidas e válidas
print("\n📊 Contagem de imagens corrompidas vs não corrompidas:")
print(df['corrupted'].value_counts())

# 📋 Listar caminhos das imagens corrompidas (se houver)
if total_corrompidas > 0:
    print("\n🔍 Caminhos das imagens corrompidas:")
    for path in df[df['corrupted'] == True]['image_path']:
        print("-", path)
else:
    print("\n🎉 Nenhuma imagem corrompida encontrada!")
