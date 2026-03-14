def run():  
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px

    # judul
    st.title('VOLVE FIELD PRODUCTION ANALYSIS')

    # Header 1
    st.header('A. Probelem Statement')
    st.image('https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41598-025-96112-5/MediaObjects/41598_2025_96112_Fig1_HTML.png')

    ## subheader 1.1
    st.subheader('1. Background') #latar belakang
    st.markdown('''
    Performa sistem sumur merupakan salah satu aspek yang sangat penting dalam keberhasilan mengalirkan fluida (minyak) ke permukaan untuk selanjutnya dilakukan treatment. Seiring berjalannya bisa saja performa sistem sumur dapat menurun yang disebabkan oleh menurun nya tekanan direservoir sehingga perlu untuk dilakukan penyesuaian, selain itu dominasi air yang terproduksi juga menyebabkan kerja sumur lebih berat karena sifat alami air yang lebih berat dari pada minyak, partikel minyak yang menempel pada dinding sumur juga menyebabkan kebutuhan tekanan yang lebih tinggi untuk menaikkan fluida.

    Pada projek kali ini akan menggunakan data volve field yang merupakan data open source. Lapangan ini sudah tidak aktif lagi dan terletak di laut utara norwegia.
    ''')

    ## subheader 1.2 
    st.subheader('2. Dataset') #dataset
    st.markdown(
    '''```
    Dataset ini memiliki 24 kolom, dengan rincian
        1.  DATEPRD                 : Waktu dilakukannya produksi (daily)
        2.  WELL_BORE_CODE	        : Kode unik untuk setiap sumur
        3.  NPD_WELL_BORE_CODE	    : Kode unik tiap sumur dari NPD (Norwegian Petroleum Department)
        4.  NPD_WELL_BORE_NAME	    : Nama tiap sumur dari NPD
        5.  NPD_FIELD_CODE	        : Kode lapangan dari NPD
        6.  NPD_FIELD_NAME	        : Nama lapangan dari NPD
        7.  NPD_FACILITY_CODE	    : Kode Fasilitas yang melakukan projek 
        8.  NPD_FACILITY_NAME	    : Nama Fasilitas yang melakukan projek 
        9.  ON_STREAM_HRS	        : Waktu produksi tiap harinya (hours)   
        10. AVG_DOWNHOLE_PRESSURE	: Rata-rata Tekanan di dasar sumur (psi)
        11. AVG_DOWNHOLE_TEMPERATURE: Rata-rata temperatur di dasar sumur (F)
        12. AVG_DP_TUBING	        : Perbedaan/penurunan tekanan pada tubing (psi)
        13. AVG_ANNULUS_PRESS	    : Rata-rata tekanan pada anulus (runag antara casing dan tubing) (psi)
        14. AVG_CHOKE_SIZE_P	    : Bukan choke / volve (%)
        15. AVG_CHOKE_UOM	        : Ukuran valve (inch)
        16. AVG_WHP_P               : Rata-rata tekanan pada kepala sumur
        17. AVG_WHT_P	            : Rata-Rata temperature pada kepala sumur                 
        18. DP_CHOKE_SIZE	        : Perbedaan tekanan ketika melewati valve (psi)
        19. BORE_OIL_VOL	        : Volume Minyak Terproduksi
        20. BORE_GAS_VOL	        : Volume Gas Terproduksi
        21. BORE_WAT_VOL	        : Volume Air Terproduksi
        22. BORE_WI_VOL	            : Volume Injeksi air
        23. FLOW_KIND	            : Tipe aliran (produksi/injeksi)
        24. WELL_TYPE               : Tipe sumur (produksi/injeksi)
    ```'''
    )

    ## subheader 1.3
    st.subheader('3. Objective')
    st.markdown('- Pada projek ini akan dilakukan modeling guna didapat model yang mampu memprediksi produksi minyak pada sumur ')
    st.markdown('- Menemukan algoritma yang mampu merepresentasikan produksi sumur')
    st.markdown('- Melakukan improving algoritma dengan melakukan tuning hyperparameter')
    st.markdown('- Melakukan Evaluasi dengan memasukan salah satu data dan melihat perbandingan antara prediksi model dan aktual data ')

    # Header 2
    st.header('B. Exploratory Data Analysis')

    ## subheader 2.1
    st.subheader('1. Transformasi') # transform data
    st.markdown('''
    Dari 24 Kolom dari data 'Volve production data' terdapat beberapa kolom yang memilki makna yang sama.
    Sehingga akan dihapus dari dataset untuk efisiensi tabel, adapaun kelompok tabel yang memiliki makna yang sama

        1. Info Sumur ('WELL_BORE_CODE', 'NPD_WELL_BORE_CODE', 'NPD_WELL_BORE_NAME') hanya akan menggunakan kolom 'NPD_WELL_BORE_NAME'
        2. Info Field ('NPD_FIELD_CODE', 'NPD_FIELD_NAME', 'NPD_FACILITY_CODE','NPD_FACILITY_NAME',) hanya akan menggunakan kolom 'NPD_FIELD_NAME'
            sebenarnya field dan facility disini memiliki arti yang berbeda, field berarti lapangan yang di eksplorasi dan facility berarti rig yang melakukan eksplorasi. berhubung yang melakukan eksplorasi hanya 1 rig untuk itu hanya diambil 'NPD_FIELD_NAME' saja
        3. Jenis Sumur ('FLOW_KIND', 'WELL_TYPE') akan digunakan kolom 'WELL_TYPE'. Keduanya sama-sama menjelaskan jenis sumur (produksi/injeksi)
    ''')
    st.markdown('''
    setelah diupdate dataset memiliki 18 kolom dari sebelumnya 24 kolom

            ['DATEPRD', 'NPD_WELL_BORE_NAME', 'NPD_FIELD_NAME', 'ON_STREAM_HRS',
        'AVG_DOWNHOLE_PRESSURE', 'AVG_DOWNHOLE_TEMPERATURE', 'AVG_DP_TUBING',
        'AVG_ANNULUS_PRESS', 'AVG_CHOKE_SIZE_P', 'AVG_CHOKE_UOM', 'AVG_WHP_P',
        'AVG_WHT_P', 'DP_CHOKE_SIZE', 'BORE_OIL_VOL', 'BORE_GAS_VOL',
        'BORE_WAT_VOL', 'BORE_WI_VOL', 'WELL_TYPE']
    ''')

    ## subheader 2.2
    st.subheader('2. Klasifikasi Sumur') #klasifikasi sumur
    st.markdown('''
                a. Sumur Produksi
                - 15/9-F-1-C
                - 15/9-F-11
                - 15/9-F-12
                - 15/9-F-14
                - 15/9-F-15 D

                b. Sumur Injeksi
                - 15/9-F-4
                - 15/9-F-5
                ''')


    ## subheader 2.3
    st.subheader('3. Total Produksi')
    st.image('/Images/Fluid_Prod.png')

    ## subsubheader 2.4
    st.subheader('4. Hubungan Produksi Setiap Fluida')

    ### subheader 2.4.1
    st.markdown('I. Akumulasi Produksi')
    st.image('/Images/Akum.png')

    ### subsubheader 2.4.2
    st.markdown('II. Rate Production')
    st.image('/Images/Rate.png')

    ## Subsubheader 2.5
    st.subheader('5. Hubungan Produksi Fluida')
    st.markdown('''
                - Minyak merupakan yang paling diinginkan dalam eksplorasi sumur minyak sehingga dalam analisis pada sub-bab ini akan mencari korelasi antara produksi minyak vs air dan minyak vs gas
    - Hubungan minyak vs air dikenal dengan istilah watercut yang artinya seberapa besar air menginvasi biasanya dinyatakan dalam %. Pada umumnya water cut akan semakin tinggi seiring berjalanya waktu dan mengindikasikan lapangan sudah cukup tua
    - Hubungan minyak vs gas disebut dengan GOR (gas oil ratio), ini menggambarkan bagaimana komponen minyak apakah termasuk minyak berat atau ringan, dan berdasarkan GOR juga bisa menambah informasi untuk menentukan jenis drive mechanism sehingga dengan mengetahui GOR pada suatu lapangan perusahaan dapat mempersiapkan startegi baik dari sisi teknis produksi maupun bisnis
    - ketiga kolom yang akan dicek korelasinya. Berhubung ditribusi ketiga kolom bersifat skew moderate sehingga metode korelasi akan digunakan metode pearson karena kedua kolom juga numeric
    - Sumur yang dilakukan Uji hanyalah sumur produksi saja, karna sumur injeksi tidak memiliki produksi''')

    ### subsubheader 2.5.1
    st.markdown('I. Oil vs Water')

    #### sub-sub-sub-subheader 2.5.1.1
    st.markdown('i. sumur 15/9-F-1 C')
    st.image('/Images/oil_wat1.png')
    st.markdown('''
                Berdasarkan uji korelasi didapat
    - spearman = 0.62 
    - p-value  = 1.45 e-82

    disimpulkan hubungan produksi minyak dan air untuk sumur15/9-F-1 C cukup kuat kearah positif, sehingga semakin tinggi produksi minyak semakin tinggi pula produksi air
    - namun berdasarkan visualisasi, ditahun kedua eksplorasi air cenderung mendominasi dibanding produksi minyak
                ''')

    #### sub-sub-sub-subheader 2.5.1.2
    st.markdown('ii. sumur 15/9-F-11')
    st.image('/Images/oil_wat2.png')
    st.markdown('''
                Berdasarkan uji korelasi didapat
    - spearman -0.51 
    - p-value 0.08

    disimpulkan hubungan produksi minyak dan air untuk sumur15/9-F-11 cukup kuat kearah negatif, sehingga semakin tinggi produksi minyak semakin rendah produksi air begitu juga sebaliknya
    - Uji korelasi spearman didukung visualisasi bahwa produksi air rendah ketika produksi minyak tinggi dan ketika produksi minyak mulai menurun produksi air justru semakin naik
                ''')

    #### sub-sub-sub-subheader 2.5.1.3
    st.markdown('iii. sumur 15/9-F-12')
    st.image('/Images/oil_wat3.png')
    st.markdown('''Berdasarkan uji korelasi didapat
    - spearman -0.22 
    - p-value 1.1e-37

    disimpulkan hubungan produksi minyak dan air untuk sumur15/9-F-12 cenderung lemah ke arah negatif, sehingga ketika produksi minyak tinggi produksi maka produksi air akan rendah, begitu pula sebaliknya 
    - Kesimpulan ini didukung oleh plot dimana produksi air dan minyak saling bertolak belakang''')

    #### sub-sub-sub-subheader 2.5.1.4
    st.markdown('iv. sumur 15/9-F-14')
    st.image('/Images/oil_wat4.png')
    st.markdown('''
    Berdasarkan uji korelasi didapat
    - spearman 0.05 
    - p-value 0.0042

    disimpulkan bahwa hubungan produksi minyak dan air untuk sumur 15/9-F-14 cenderung sangat lemah ke arah positif
    - Namun jika dilihat dari visualisai, uji korelasi tidak menggambarkan produksi air dan minyak.
    - Produksi minyak dan air cenderung lebih memiliki hubungan terhadap waktu
                ''')

    #### sub-sub-sub-subheader 2.5.1.5
    st.markdown('v. sumur 15/9-F-15 D')
    st.image('/Images/oil_wat5.png')
    st.markdown('''
    Berdasarkan uji korelasi didapat
    - spearman 0.05 
    - p-value 0.0042

    disimpulkan bahwa hubungan produksi minyak dan air untuk sumur 15/9-F-14 cenderung sangat lemah ke arah positif
    - Namun jika dilihat dari visualisai, uji korelasi tidak menggambarkan produksi air dan minyak.
    - Produksi minyak dan air cenderung lebih memiliki hubungan terhadap waktu
                ''')


    ### subsubheader 2.5.2
    st.markdown('II. Oil vs Gas')
    st.image('/Images/oil_gas.png')
    st.markdown('''
    berdasarkan plot dan uji korelasi (spearman) semua sumur memiliki keterikatan yang sangat kuat, sehingga dapat diasumsikan jika
    - volve field merupakan lapangan minyak yang terasosiai minyak, artinya minyak pada field ini memiki kandungan gas yang tinggi
    - kandungan gas yang tinggi ini menjadi salah satu tenaga penggerak minyak untuk membawa minyak ke lubang sumur karena pada dasarnya gas akan mengalir ke tekanan yang lebih rendah 
    - perusahaan dapat menentukan strategi teknis untuk oprasi maupun bisnis untuk penjualan, karena gas tidak bisa disimpan dalam waktu yang lama
                ''')

    ## subheader 2.6
    st.subheader('6. Korelasi Tekanan')

    ### sub-subheader 2.6.1
    st.markdown('I. Bagaimana Tekanan Reservoir')
    st.markdown('''
                - Pada data ini memang tidak terdapat tekanan reservoir tapi pada umumnya untuk sumur produksi tekanan reservoir lebih besar dari pada tekanan dasar sumur (downhole pressure). Secara alami seiring berjalan nya waktu tekanan reservoir akan terus menurun , penentuan tekanan reservoir masih baik atau tidak dapat kita lihat perbandingan produksi minyak vs BHP, data yang didapat BHP cenderung konstan namun minyak terus menurun ini menindikasikan tekanan reservoir terus mengalami penurunan
    - Sumur 15/9-F-4 tidak di analisis karena merupakan sumur injeksi
                ''')

    #### sub-sub-sub-subheader 2.5.1.1
    st.markdown('i. sumur 15/9-F-1 C')
    st.image('/Images/oil_bhp1.png')
    st.markdown('''
                - terdapat pola berulang dimana jika produksi (line hijau)=0 maka setelah nya BHP (line biru) pasti naik, hal ini dilakukan untuk menjaga tekanan reservoir agar tidak langsung drop 
    - ketika sumur dibuka lagi pressure akan langsung turun secara extreme dan ini terus berulang sehingga di asumsikan tekanan pada reservoir yang mendorong fluida ke sumur 15/9-F-1 C sudah tidak kuat 
    - dari pola yang terbentuk sumur ini sepertinya masih pada tahap primary recovery sehingga bisa dilakukan pendekatan atau analisis lebih jauh untuk mendapatkan kepastian dan jika benar apakah sumur ini masih layak di lanjutkan ke tahap primary dan tertiary recovery
                ''')

    #### sub-sub-sub-subheader 2.5.1.2
    st.markdown('ii. sumur 15/9-F-11')
    st.image('/Images/oil_bhp2.png')
    st.markdown('''
                - untuk mempertahankan tekanan hal yang sama juga dilakukan terhadap sumur 15/9-F-11 yaitu dengan mengehtikan produksi sehingga tekanan akan terakumulasi menyebabkan produksi yang baik saat sumur di buka kembali
    - reservoir di sumur 15/9-F-11 memiliki tekanan yang baik sehingga produksi minyak lebih stabil 
    - pada oktober 2015 produksi melonjak drastis, ini merupakan indikasi dilakukan nya treatment pada sumur atau bisa saja sumur ini mendapat impact dari injeksi air karena kita ketahui terdapat 2 sumur injeksi pada field ini namun untuk kepastiannya akan dilakukan analisis pada sumur injeksi pada sub bab berikutnya
    - dapat kita lihat jika sumur ini terus mengalami penurunan tekanan reservoir setelah mencapai 'peak' produksi nya, ini dilihat dari produksi minyak yang terus mengalami penurunan walaupun BHP dijaga konstan bahkan cenderung naik''')

    #### sub-sub-sub-subheader 2.5.1.3
    st.markdown('iii. sumur 15/9-F-12')
    st.image('/Images/oil_bhp3.png')
    st.markdown('''- sekilas dapat dilihat pada tahun 2012 BHP=0 namun produksi oil masih tinggi 2000 MSTB+, kemungkinan terbesar adalah tidak adanya data record BHP atau data tidak dipublish
    - walau tidak ada BHP kita dapat asumsikan bahwa tekanan reservoir sudah sangat melemah terlebih sumur sudah berproduksi cukup lama (3 tahun lebih) sehingga pada tahun 2010 sampai 2011 terjadi penurunan produksi yang ekstrem
    - pada tahun 2015 dapat dilihat terjadi lonjakan produksi yang pasti dilakukan sesuatu terhadap sumur ini
    - berdasarkan history sumur lain dan data yang kita punya kemungkinan bisa terjadi karena sumur di shut terlebih dahulu atau mendapat impact dari injeksiair dari sumur injeksi karena sumur 15/9-F-11 juga mengalami pelonjakan produksi di tahun yang sama ''')

    #### sub-sub-sub-subheader 2.5.1.4
    st.markdown('iv. sumur 15/9-F-14')
    st.image('/Images/oil_bhp4.png')
    st.markdown('''- jika dilihat sekilas sumur 15/9-F-14 cenderung memiliki karakteristik yang sama dengan sumur 15/9-F-1 C yaitu penurunan produksi yang signifikan walaupun BHP cukup stabil. Jika kita lebih teliti lagi sumur 16/9-F-4 memiliki periode produksi yang lebih panjang (9 tahun) dibanding sumur 15/9-F-1 C (3 tahun) 
    - secara quantity juga 15/9-F-14 memiliki produksi yang lebih tinggi, jika kita gunakan interval waktu yg lebih lengkap mungkin penurunan akan lebih landai
    - secara visual tekanan sudah benar-benar tidak bisa mendorong minyak pada pertangahan tahun 2014
    - dari pola yang terlihat memang secara trend produksi terus mengalami penurunan namun terdapat beberapa momen produksi minyak mengalami kenaikan, pada periode tersebut diharapkan dilakukan analisa lebih lanjut untuk mendapatkan informasi mengenai treatmen apa saja yang sudah dilakukan untuk mningkatkan produksi sumur ini sehingga dapat dilakukan analisa untuk dilakukan developing pada sumur ini
    - dapat kita lihat jika sumur ini terus mengalami penurunan tekanan reservoir setelah 2 tahun aktif, ini dilihat dari produksi minyak yang terus mengalami penurunan walaupun BHP dijaga konstan bahkan cenderung naik''')

    #####sub-sub-sub-subheader 2.5.1.5
    st.markdown('v. sumur 15/9-F-15 D')
    st.image('/Images/oil_bhp5.png')
    st.markdown('- untuk produksi sumur 15/9-F-15 D cenderung kecil dari awal jika dibandingkan dengan sumur yang lain. untuk mengetahui mengapa demikian perlu dicek properties dari reservoir disekitar sumur ini karena perbedaaan yang sangat signifikan dari sumur lainnya')



    ### sub-subheader 2.6.2
    st.markdown('II. Bagaimana Hambatan pada Sumur')
    st.markdown('''
                - Uji korelasi dilakukan guna melihat bagaimana pengaruh pressure drop terhadap produksi minyak dan air
    - pressure drop adalah = perubahan tekanan pada setiap kedalaman sehingga semakin dalam sebuah sumur semakin besar pressure atau tekanan yang dibutuhkan untuk menaikan minyak
                ''')

    #### sub-sub-sub-subheader 2.6.1.1
    st.markdown('i. sumur 15/9-F-1 C')
    st.image('/Images/pd1.png')
    st.markdown('''
    - uji korelasi hubungan pressure drop dengan produksi minyak menghasilkan nilai korelasi cenderung lemah kearah kiri (-0.233) sehingga diasumsikan pada sistem sumur ini semakin besar hambatan semakin sulit minyak untuk mengalir untuk mencari spesifik hambatannya
    - sedangkan untuk air cenderung bernilai positif sehingga air tidak mengalami kesulitan untuk mengalir
    - sedangkan dari scatter plot cenderung produksi menurun ketika pressure drop meningkat sehingga fix terdapat hambatan pada sumur ini
    ''')

    #### sub-sub-sub-subheader 2.6.1.2
    st.markdown('ii. sumur 15/9-F-11')
    st.image('/Images/pd2.png')
    st.markdown('''
    - sedangkan dari scatter plot cenderung produksi menurun ketika pressure drop meningkat sehingga fix terdapat hambatan pada sumur ini
    ''')


    #### sub-sub-sub-subheader 2.6.1.3
    st.markdown('iii. sumur 15/9-F-12')
    st.image('/Images/pd3.png')
    st.markdown('- pada data ini perlu di analisis lebih lanjut karena terhadap minyak pressure drop justru memiliki korelasi kuat positif')

    #### sub-sub-sub-subheader 2.6.1.4
    st.markdown('iv. sumur 15/9-F-14')
    st.image('/Images/pd4.png')
    st.markdown('''
    - uji korelasi hubungan pressure drop dengan produksi minyak menghasilkan nilai kuat lemah kearah kiri (-0.528) 
    - persebaran data cenderung menggambarkan penurunan produksi ketika pressure drop mengalami penurunan, hal ini sesuai dengan uji korealasi
    ''')

    #### sub-sub-sub-subheader 2.6.1.5
    st.markdown('v. sumur 15/9-F-15 D')
    st.image('/Images/pd5.png')
    st.markdown('''- uji korelasi hubungan pressure drop dengan produksi minyak menghasilkan nilai korelasi kuat kearah kiri (-0.563) sehingga diasumsikan pada sistem sumur ini terdapat hambatan sehingga perlu analisis tambahan untuk mencari spesifik hambatannya
    - sedangkan untuk air cenderung bernilai positif sehingga air tidak mengalami kesulitan untuk mengalir''')

    ## subheader 2.7
    st.subheader('7. Decline Curve Analysis')
    st.image('/Images/dca.png')
    st.markdown('''
                Sumur dengan peak besar & drop cepat → Hyperbolic
    - 15/9-F-12
    - 15/9-F-14

    Sumur dengan produksi lebih stabil & turunnya halus → Exponential
    - 15/9-F-1 C
    - 15/9-F-15 D
    - 15/9-F-5

    Sumur dengan drop drastis setelah peak pendek → Harmonic/near-Hyperbolic
    - 15/9-F-11
                ''')

    ## subheader 2.8 
    st.subheader('8. Dampak Injeksi')
    st.markdown('''
                - Injeksi air (water flooding) merupakan salaah satu metode yang dilakukan untuk menjaga tekanan reservoir dan diharapkan tekanan reservoir mampu untuk mendorong minyak ke lobang sumur, namun demkian waterflooding tetap memiliki resiko yaitu jika tidak dilakukan dengan seksama maka berpotensi terjadinya water breakthrough, yaitu air lebih cepat dan banyak terproduksi bersama minyak sehingga akan menimbulkan kerugian baik dari sisi teknis maupun ekonomis
    - Injeksi air aka dilakukan seteleha beberapa waktu sumur produksi di produksikan
                ''')

    ### sub-subheader 2.8.1
    st.markdown('I. Sumur Injeksi 15/9-F-4')
    st.image('/Images/wi1.png')
    st.markdown('''
                Sumur Injeksi 15/9-F-4 sepertinya lebih berdampak atau memang diperuntukan untuk sumur 15/9-F-12 dan sumur 15/9-F-14 untuk itu akan dilakukan plot ulang untuk kedua sumur dengan vs injeksi air dari sumur 15/9-F-4
                ''')

    #### sub-subheader 2.8.1.1
    st.markdown('15/9-F-4 vs 15/9-F-12')
    st.image('/Images/wi1_1.png')
    st.markdown('''
                - secara teknis ketik air (line biru) diinjeksikan poduksi minyak mengalami pelonjakan yangg signifikan
    - namun jika dilihat dari sisi bisnis sbenarnya ini belum perlu dilakukan karna produksi minyak masih cenderung tinggi karna jika injeksi air dilakukan terlalu dini maka dikhawartikan akan terjadi water breaktrhough yaitu air terproduksi lebih cepat
                ''')

    #### sub-subheader 2.8.1.2
    st.markdown('15/9-F-4 vs 15/9-F-14')
    st.image('/Images/wi1_2.png')
    st.markdown('''
                - Produksi minyak sempat mengalami shut sebelum dilakukan injeksi air, sehingga dapat diasumsikan sementara bahwa injeksi ini dilakukan memang untuk meningkatkan produksi dari sumur 15/9-F-14
    - lonjakan yang terjadi pada produksi minyak di sumur 15/9-F-12 bisa saja disebabkan oleh injeksi air yang dilakukan pada sumur 15/9-F-4, sehingga diasumsikan kedua sumur berdekatan atau memiliki hubungan reservoir
                ''')

    ### sub-subheader 2.8.2
    st.markdown('II. Sumur Injeksi 15/9-F-5')
    st.image('/Images/wi2.png')
    st.markdown('''
                Sumur Injeksi 15/9-F-5 sepertinya lebih berdampak atau memang diperuntukan untuk sumur 15/9-F-12 dan sumur 15/9-F-14 untuk itu akan dilakukan plot ulang untuk kedua sumur dengan vs injeksi air dari sumur 15/9-F-4
                ''')

    ### sub-subheader 2.8.2.1
    st.markdown('15/9-F-5 vs 15/9-F-12')
    st.image('/Images/wi2_1.png')
    st.markdown('''
                - injeksi sumur 15/9/-F-5 dilakukan beberapa bulan setelah sumur 15/9-F-12 beberapa bulan setelah diproduksikan
    - bersamaan dengan dioprasikan nya sumur injeksi 15/9-F-5 sumur produksi 15/9-F-12 mengalami penurunan produksi
    - setelah sumur injeksi 15/9-F-5 berproduksi dapat dilihat bahwa sumur produksi 15/9-F-12 mengalami kenaikan produksi minyak, sehingga dapat di asumsikan bahwa sumur injeksi 15/9-F-5 memnag di-scenariokan untuk sumur produksi 15/9-F-12
    ''')

    #### sub-subheader 2.8.2.2
    st.markdown('15/9-F-5 vs 15/9-F-14')
    st.image('/Images/wi2_2.png')
    st.markdown('''
    - injeksi air yang dilakukann oleh sumur injeksi 15/9-F-5 cenderung tidak berdampak pada sumur produksi minyak sumur 15/9-F-14 karna produksi minyak tetap menurun meskipun terdapat fluktuatif
                ''')
    

if __name__=='__main__':
    run()
