# 🚗 Prediksi Kelas Mobil Bekas

Sistem ini merupakan implementasi **machine learning berbasis pendekatan hybrid**, yang menggabungkan metode **unsupervised learning (K-Means Clustering)** dan **supervised learning (Random Forest Classification)** untuk mengelompokkan dan memprediksi kategori mobil bekas berdasarkan karakteristik kendaraan.

Model yang telah dibangun kemudian diintegrasikan ke dalam aplikasi web menggunakan **Flask** sebagai backend. Sistem ini dilengkapi dengan antarmuka berbasis **HTML, CSS, dan JavaScript**, sehingga memungkinkan pengguna untuk melakukan prediksi secara interaktif dan real-time.

---

## 📌 Deskripsi Project

Project ini mencakup beberapa tahapan utama:

- Preprocessing data untuk membersihkan dan menyiapkan dataset
- Clustering menggunakan K-Means untuk membentuk kategori mobil
- Pelatihan model Random Forest untuk prediksi kategori
- Integrasi model ke dalam aplikasi web menggunakan Flask

Sistem memungkinkan pengguna memasukkan data kendaraan dan mendapatkan hasil prediksi kategori mobil secara otomatis.

---

## ⚙️ Teknologi yang Digunakan

- Python  
- Pandas & NumPy  
- Scikit-learn  
- Flask  
- HTML, CSS, JavaScript  

---

## 📊 Fitur Sistem

- Input data kendaraan  
- Prediksi kategori mobil secara otomatis  
- Dashboard hasil prediksi  
- Visualisasi hasil clustering  

---

## 📁 Struktur Folder

```bash
Cars-Clustered-Prediction/
│
├── app/
│   ├── __init__.py        # Inisialisasi aplikasi Flask
│   ├── model_loader.py    # Load model dan scaler
│   ├── routes.py          # Routing untuk endpoint Flask
│   └── utils.py           # Fungsi bantu untuk preprocessing & prediksi
│
├── data/
│   └── used_car_clustered.csv   # Dataset hasil clustering
│
├── model/
│   ├── rf_model.pkl       # Model Random Forest yang sudah dilatih
│   └── scaler.pkl         # Scaler untuk normalisasi data
│
├── static/
│   ├── script.css         # Script tambahan UI
│   └── style.css          # Styling halaman web
│
├── templates/
│   ├── base.html          # Template utama
│   ├── dashboard.html     # Halaman dashboard
│   ├── index.html         # Halaman input data
│   └── result.html        # Halaman hasil prediksi
│
├── config.py              # Konfigurasi aplikasi
├── requirements.txt       # Daftar dependency
└── run.py                 # Entry point untuk menjalankan aplikasi

 🚀 Cara Menjalankan Project

```bash
1. Clone repository
git clone https://github.com/username/repo-name.git

2. Masuk ke folder project
cd Cars-Clustered-Prediction

3. Install dependencies
pip install -r requirements.txt

4. Jalankan aplikasi Flask
python run.py

5. Buka di browser
http://localhost:5000
```


📈 Metode Machine Learning

Clustering : K-Means
Classification : Random Forest

📎 Catatan
Project ini dibuat sebagai bagian dari tugas UAS dan bertujuan untuk mengimplementasikan konsep machine learning ke dalam sistem berbasis aplikasi web yang interaktif dan aplikatif.



