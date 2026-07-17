# Spotify Tracks - Veri Analizi Projesi

Bu proje, Kaggle uzerindeki "Spotify Tracks Dataset" veri setini kullanarak Python (pandas) ve SQL (SQLite) ile veri analizi yapar.

## Veri Seti

- Kaynak: [Spotify Tracks Dataset - Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
- ~114.000 satir, 22 sutun
- Icerik: sarki adi, sanatci, tur, dans edilebilirlik, enerji, populerlik gibi ozellikler

## Yapilan Analizler

- Ortalama populerlik puanina gore en iyi 10 muzik turu
- En cok sarkisi olan 10 sanatci
- Dans edilebilirlik ve enerji arasindaki iliski (populerlige gore renklendirilmis)
- En yuksek ortalama enerjiye sahip 10 tur

## Kullanilan Teknolojiler

- **Python**: pandas (veri temizleme), matplotlib & seaborn (gorsellestirme)
- **SQL**: SQLite ile veritabani sorgulari

## Proje Adimlari

1. CSV dosyasi pandas ile okunur
2. Eksik ve tekrar eden veriler temizlenir
3. Temiz veri SQLite veritabanina aktarilir
4. SQL sorgulariyla analiz sorulari cevaplanir
5. Sonuclar grafik olarak kaydedilir

## Nasil Calistirilir

1. Veri setini [Kaggle'dan indir](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) ve proje klasorune `spotify-tracks-dataset.csv` olarak koy.

2. Gerekli kutuphaneleri kur:
pip install pandas matplotlib seaborn

3. Analizi calistir:
python analiz.py

4. Olusan grafikleri klasorde gorebilirsin:
   - `top_genres_by_popularity.png`
   - `top_artists.png`
   - `danceability_vs_energy.png`
   - `top_genres_by_energy.png`

## Notlar

- Veri seti dosyasi (CSV) ve olusturulan veritabani (.db) boyut nedeniyle bu repoya dahil edilmemistir. Projeyi calistirmak icin veri setini yukaridaki linkten kendin indirmen gerekir.    