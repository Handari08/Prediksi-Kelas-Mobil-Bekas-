# Prediksi Kelas Mobil Bekas

Project ini merupakan implementasi machine learning untuk mengelompokkan dan memprediksi kategori mobil bekas menggunakan metode clustering dan klasifikasi.

---

## 📌 Deskripsi Project

Project ini menggunakan:
- K-Means Clustering untuk mengelompokkan mobil berdasarkan karakteristik
- Random Forest untuk memprediksi kategori mobil
- Flask sebagai backend untuk implementasi web

Sistem memungkinkan pengguna untuk memasukkan data kendaraan dan mendapatkan prediksi kategori mobil secara real-time.

---

## ⚙️ Teknologi yang Digunakan

- Python
- Pandas & NumPy
- Scikit-learn
- Flask
- HTML & CSS

---

## 📊 Fitur Sistem

- Input data kendaraan
- Prediksi kategori mobil
- Dashboard hasil prediksi
- Visualisasi data clustering

---

## 📁 Struktur Folder
Cars-Clustered-Prediction/
│
├── app/
│   ├── init.py
│   ├── model_loader.py
│   ├── routes.py
│   └── utils.py
│
├── data/
│   └── used_car_clustered.csv
│
├── model/
│   ├── rf_model.pkl
│   └── scaler.pkl
│
├── static/
│   ├── script.css
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── index.html
│   └── result.html
│
├── config.py
├── requirements.txt
└── run.py

---

## 🚀 Cara Menjalankan Project

1. Clone repository:
   git clone https://github.com/username/repo-name.git
2. Masuk ke folder project:
   cd Cars-Clustered-Prediction
3. Install dependencies:
   pip install -r requirements.txt
4. Jalankan aplikasi:
   python run.py
5. Buka browser:
   http://localhost:5000 (atau bisa disesuaikan)

---

## 📈 Metode Machine Learning

- Clustering: K-Means
- Classification: Random Forest

---

## 📎 Catatan

Project ini dibuat untuk keperluan UAS mata kuliah Machine Learning / Data Science.

