# Judul Project
Well performance analysis and production forecasting
## Repository Outline
`Bagian ini menjelaskan secara singkat konten/isi dari file yang dipush ke repository`

Contoh:
```
1. Deployment - Folder berisi file-file untuk deployment dengan hugging face
2. Images - Folder berisi gambar yang digunakan di hugging face
3. Model - Folder yang berisi file model yang diguanakan untuk forecasting
4. forecsating.ipynb - file yang digunakan untuk menyiapkan model dan memodelkan untuk inference
5. infference.ipynb - file yang digunakan untuk melakukan forecasting atau prediksi
6. Volve production data.xlsx - file yang berisi dataset
dst.
```

## Problem Background
`
Penurunan produksi minyak akan menurun secara alami seiring berjalannya waktu disebabkan oleh menurunnya tekanan di reservoir sehingga berkurang pula tenaga untuk mendorong minyak mengalir. Selain disebabkan oleh tekanan reservoir, penurunan produksi juga bisa disebabkan oleh sistem sumur itu sendiri, bisa saja terdapat endapan yang menempel pada dinding tubing sehingga menyebabkan berkurangnya performa sistem sumur untuk mengalirkan minyak dari dasar sumur ke permukaan. Pada projek kali ini akan dilakukan perhitungan korelasi untuk mencari apakah terdapat masalah pada sistem sumur, diharapkan didapat kesimpulan apakah terdapat korelasi sistem sumur terhadap jumlah minyak yang berhasil dialirkan. Selain dari nilai korelasi, untuk melakukan validasi pada projek ini akan dibuatkan model inference untuk memprediksi produksi jika dilakukan adjusment terhadap parameter di sistem sumur
`

## Project Output
`
Membuat model inference untuk memprediksi minyak sebagai media validasi hubungan sistem sumur terhadap produksi
link hugging face : https://huggingface.co/spaces/tomatijo/Task_ML2
`

## Data
`
KOLOM IDENTIFIKASI 

1. Identifikasi Sumur
   - WELL_BORE_CODE: Kode unik untuk identifikasi setiap sumur
   - NPD_WELL_BORE_CODE: Kode resmi dari Norwegian Petroleum Directorate (NPD)
   - NPD_WELL_BORE_NAME: Nama resmi sumur menurut NPD
   - NPD_FIELD_CODE: Kode lapangan migas tempat sumur berada
   - NPD_FIELD_NAME: Nama lapangan migas
   - NPD_FACILITY_CODE: Kode fasilitas produksi (platform/rig)
   - NPD_FACILITY_NAME: Nama fasilitas produksi

2. Informasi Waktu & Klasifikasi
   - DATEPRD: Tanggal produksi 
   - FLOW_KIND: Jenis aliran 
   - WELL_TYPE: Tipe sumur 


3. Parameter Waktu Operasi
   - ON_STREAM_HRS: Jam operasi sumur dalam periode tersebut (biasanya 24 jam untuk daily data)

4. Parameter Tekanan
   - AVG_DOWNHOLE_PRESSURE: Tekanan rata-rata di dasar sumur (downhole pressure)
   - AVG_ANNULUS_PRESS: Tekanan annulus (ruang antara casing dan tubing)
   - AVG_DP_TUBING: Pressure drop di tubing (penurunan tekanan sepanjang tubing)

5. Parameter Temperatur & Lainnya
   - AVG_DOWNHOLE_TEMPERATURE: Temperatur rata-rata di dasar sumur
   - AVG_MHP_P: Manifold Head Pressure (tekanan di manifold)
   - AVG_MHT_P: Manifold Head Temperature (temperatur di manifold)
   
6. Parameter Choke (KATUP PENGATUR ALIRAN)
   - AVG_CHOKE_SIZE_P: Ukuran bukaan choke (persentase atau besaran)
   - AVG_CHOKE_UOM: Unit of Measure untuk choke (%, inch, mm)
   - DP_CHOKE_SIZE: Differential pressure across choke

7. Volume Produksi (VOLUME OUTPUT)
   - BORE_OTL_VOL: Volume minyak yang diproduksi (Oil volume)
   - BORE_GAS_VOL: Volume gas yang diproduksi (Gas volume)
   - BORE_WAT_VOL: Volume air yang diproduksi (Water volume)
   - BORE_WI_VOL: Volume air yang diinjeksikan (Water injection volume)
`

## Method
`
Metode yang digunakan pada projek ini adalah model supervised learning dengan model regresi
`

## Stacks
bahasa pemrogmanan
- Python

Library
- import pandas as pd
- matplotlib
- spearmanr
- StandardScaler
- ColumnTransformer
- pickle
- ross_validate
- KNeighborsRegressor
- SVR
- DecisionTreeRegressor
- RandomForestRegressor,
- GradientBoostingRegressor
- RandomizedSearchCV
- joblib
- train_test_split
- Pipeline

## Reference
`
https://www.kaggle.com/datasets/imranulhaquenoor/volve-well-production
`