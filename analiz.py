import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CSV'yi oku
df = pd.read_csv("spotify-tracks-dataset.csv")

print("Veri boyutu:", df.shape)

# 2. Gereksiz sutunu kaldir
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# 3. Eksik/tekrarlayan verileri temizle
df = df.dropna(subset=["track_name", "artists"])
df = df.drop_duplicates(subset=["track_id"])

# 4. SQLite veritabanina aktar
conn = sqlite3.connect("spotify.db")
df.to_sql("tracks", conn, if_exists="replace", index=False)

sns.set_style("whitegrid")

# ---------------------------------------------------------
# GRAFIK 1: Ortalama populariteye gore en iyi 10 tur
# (sarki sayisi degil, gercek populerlik puanina bakiyoruz)
# ---------------------------------------------------------
query1 = """
    SELECT track_genre, ROUND(AVG(popularity), 1) AS ort_populerlik
    FROM tracks
    GROUP BY track_genre
    ORDER BY ort_populerlik DESC
    LIMIT 10
"""
result1 = pd.read_sql_query(query1, conn)
print("\nEn populer 10 tur (ortalama populerlik puanina gore):")
print(result1)

plt.figure(figsize=(10, 6))
sns.barplot(data=result1, x="ort_populerlik", y="track_genre", palette="viridis")
plt.title("Ortalama Populerlik Puanina Gore En Iyi 10 Tur")
plt.xlabel("Ortalama Populerlik Puani (0-100)")
plt.ylabel("Tur")
plt.tight_layout()
plt.savefig("top_genres_by_popularity.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# GRAFIK 2: En cok sarkisi olan 10 sanatci
# ---------------------------------------------------------
query2 = """
    SELECT artists, COUNT(*) AS sarki_sayisi
    FROM tracks
    GROUP BY artists
    ORDER BY sarki_sayisi DESC
    LIMIT 10
"""
result2 = pd.read_sql_query(query2, conn)
print("\nEn cok sarkisi olan 10 sanatci:")
print(result2)

plt.figure(figsize=(10, 6))
sns.barplot(data=result2, x="sarki_sayisi", y="artists", palette="magma")
plt.title("En Cok Sarkisi Olan 10 Sanatci")
plt.xlabel("Sarki Sayisi")
plt.ylabel("Sanatci")
plt.tight_layout()
plt.savefig("top_artists.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# GRAFIK 3: Dans edilebilirlik vs enerji (renk = populerlik)
# ---------------------------------------------------------
sample = df.sample(2000, random_state=42)

plt.figure(figsize=(9, 7))
scatter = plt.scatter(
    sample["danceability"],
    sample["energy"],
    c=sample["popularity"],
    cmap="viridis",
    alpha=0.5,
    s=20
)
plt.colorbar(scatter, label="Populerlik")
plt.title("Dans Edilebilirlik vs Enerji (Renk: Populerlik)")
plt.xlabel("Dans Edilebilirlik")
plt.ylabel("Enerji")
plt.tight_layout()
plt.savefig("danceability_vs_energy.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# GRAFIK 4: En yuksek ortalama enerjiye sahip 10 tur
# ---------------------------------------------------------
query4 = """
    SELECT track_genre, ROUND(AVG(energy), 3) AS ort_enerji
    FROM tracks
    GROUP BY track_genre
    ORDER BY ort_enerji DESC
    LIMIT 10
"""
result4 = pd.read_sql_query(query4, conn)
print("\nEn yuksek ortalama enerjiye sahip 10 tur:")
print(result4)

plt.figure(figsize=(10, 6))
sns.barplot(data=result4, x="ort_enerji", y="track_genre", palette="rocket")
plt.title("En Yuksek Ortalama Enerjiye Sahip 10 Tur")
plt.xlabel("Ortalama Enerji")
plt.ylabel("Tur")
plt.tight_layout()
plt.savefig("top_genres_by_energy.png", dpi=150)
plt.close()

conn.close()
print("\nTamamlandi! 4 grafik olusturuldu:")
print("- top_genres_by_popularity.png")
print("- top_artists.png")
print("- danceability_vs_energy.png")
print("- top_genres_by_energy.png")