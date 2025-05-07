# 🧠 Machine Learning Project: Prediksi Risiko Diabetes

## 1. 🌍 Domain Proyek
Diabetes merupakan penyakit metabolik kronis yang umum dan dapat menyebabkan komplikasi serius seperti gagal ginjal, penyakit jantung, hingga kebutaan. Deteksi dini menjadi kunci untuk mencegah komplikasi tersebut.

📈 Menurut WHO, jumlah penderita diabetes meningkat drastis setiap tahun. Proyek ini bertujuan membangun model machine learning untuk memprediksi risiko diabetes berdasarkan data medis sederhana.

**Referensi:**
- [World Health Organization (WHO), 2023 – Diabetes](https://www.who.int/news-room/fact-sheets/detail/diabetes)
- [Pima Indians Diabetes Dataset - Kaggle/UCI](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## 2. 💼 Business Understanding

### 🧩 Problem Statement
Bagaimana cara memprediksi risiko diabetes hanya dari data pemeriksaan awal (usia, glukosa, tekanan darah, dll)?

### 🎯 Goals
Membangun model klasifikasi yang akurat dan mudah diinterpretasi untuk skrining risiko diabetes.

### 🧪 Solution Statement
- Gunakan dua algoritma: **Logistic Regression** & **Random Forest**.
- Bandingkan performa kedua model.
- Terapkan **hyperparameter tuning** untuk Random Forest.
- Evaluasi dengan metrik: **accuracy, precision, recall, f1-score**.

---

## 3. 📊 Data Understanding

Dataset: **Pima Indians Diabetes Dataset**  
Ukuran: 768 baris × 9 kolom

| Fitur | Deskripsi |
|---|---|
| Pregnancies | Jumlah kehamilan |
| Glucose | Kadar glukosa darah |
| BloodPressure | Tekanan darah diastolik |
| SkinThickness | Ketebalan kulit |
| Insulin | Kadar insulin serum |
| BMI | Indeks massa tubuh |
| DiabetesPedigreeFunction | Riwayat genetik diabetes |
| Age | Usia |
| Outcome | Label (0 = tidak diabetes, 1 = diabetes) |

Distribusi kelas:
- Tidak diabetes: ~500 entri  
- Diabetes: ~200 entri  

🔍 **Eksplorasi Data:**
- Korelasi fitur divisualisasikan dengan heatmap.
- Glukosa dan BMI korelasinya tinggi terhadap outcome.
- Distribusi label divisualisasikan dengan countplot.

---

## 4. 🧹 Data Preparation

Langkah-langkah:
- Nilai 0 di kolom medis diganti dengan `NaN` (karena tidak valid secara klinis).
- Missing values diimputasi menggunakan **median**.
- Data dinormalisasi menggunakan **StandardScaler**.

Output: data yang bersih, siap dilatih model.

---

## 5. 🧠 Modeling

### 🔸 Logistic Regression
- Sederhana dan interpretatif.
- Menggunakan parameter default.

### 🔸 Random Forest
- Kuat untuk data non-linear & outlier.
- Default + tuning dengan `GridSearchCV`.

#### 🔧 Hyperparameter Tuning:
- `n_estimators`: [50, 100]  
- `max_depth`: [None, 5, 10]  
- `min_samples_split`: [2, 5]  

### 🔍 Feature Importance:
Fitur paling berpengaruh: **Glucose**, **BMI**, dan **Age**.

#### 📌 Ringkasan:
| Model | Kelebihan | Kekurangan |
|---|---|---|
| Logistic Regression | Cepat, interpretatif | Kurang akurat untuk non-linear |
| Random Forest | Akurat, fleksibel | Lambat, kurang interpretatif |

Model terbaik dipilih berdasarkan akurasi & f1-score tertinggi.

---

## 6. 📈 Evaluation

### 📏 Metrik:
- **Accuracy** = (TP + TN) / Total
- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN)
- **F1-score** = 2 * (P * R) / (P + R)

### 🧪 Hasil:
| Model | Accuracy | F1-score |
|---|---|---|
| Logistic Regression | 75.32% | 0.74 |
| Random Forest (default) | 74.03% | 0.73 |
| Random Forest (tuned) ✅ | **76.62%** | **0.76** |

**✅ Model Terbaik:** Random Forest dengan tuning.

---

## 7. ✅ Kesimpulan

Proyek ini berhasil membangun sistem klasifikasi untuk mendeteksi risiko diabetes menggunakan data pemeriksaan awal.  
Model **Random Forest dengan tuning** menunjukkan performa terbaik dan dapat digunakan sebagai alat bantu skrining awal di fasilitas kesehatan karena sifatnya yang **cepat, hemat biaya, dan non-invasif**.

---

### 👨‍💻 Disusun oleh:
**David Kristian Silalahi**

