# -*- coding: utf-8 -*-
"""Predictive Analysis_David.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xmGsy50nOdHzGs4hyZAAsAhEKszQerDW

# PREDICTIVE ANALYSIS
- David Kristian Silalahi
- MC-43

# Proyek Machine Learning: Prediksi Risiko Diabetes

Proyek ini bertujuan membangun model prediktif untuk menentukan apakah seorang pasien berisiko terkena diabetes berdasarkan data klinis. Dataset yang digunakan adalah dataset Pima Indians Diabetes.
"""

# Import library
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

"""## 1. Memuat Dataset
Dataset dimuat dari file `diabetes.csv`. Dataset ini memiliki 768 baris dan 9 kolom, dengan label target 'Outcome'.

"""

# Load data
df = pd.read_csv("diabetes.csv")
df.head()

"""## 2. Pembersihan Data
Beberapa kolom seperti `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, dan `BMI` memiliki nilai nol yang tidak logis. Kita akan menggantinya dengan nilai median.

"""

# Kolom yang akan diperbaiki
columns_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[columns_to_fix] = df[columns_to_fix].replace(0, np.nan)

# Imputasi dengan median
df.fillna(df.median(), inplace=True)

"""## 3. Pemisahan Fitur dan Label
Kita pisahkan fitur (`X`) dan label (`y`), lalu normalisasi fitur menggunakan StandardScaler

"""

# Feature & target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Normalisasi
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

"""## 4. Membagi Data
Data dibagi menjadi data latih dan data uji dengan rasio 80:20.

"""

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

"""## 5. Pelatihan Model
Kita melatih dua model: Logistic Regression dan Random Forest.

"""

log_reg = LogisticRegression(random_state=42)
rf = RandomForestClassifier(random_state=42)

log_reg.fit(X_train, y_train)
rf.fit(X_train, y_train)

"""## 6. Evaluasi Model
Evaluasi dilakukan menggunakan classification report dan akurasi.

"""

y_pred_log = log_reg.predict(X_test)
y_pred_rf = rf.predict(X_test)

print("Logistic Regression Report:")
print(classification_report(y_test, y_pred_log))
print("Accuracy:", accuracy_score(y_test, y_pred_log))

print("\nRandom Forest Report:")
print(classification_report(y_test, y_pred_rf))
print("Accuracy:", accuracy_score(y_test, y_pred_rf))

"""## Visualisasi Korelasi dan Distribusi Data
Kita akan lihat korelasi antar fitur serta distribusi label untuk mengetahui ketidakseimbangan kelas.

"""

import matplotlib.pyplot as plt
import seaborn as sns

# Korelasi fitur
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.title("Heatmap Korelasi Fitur")
plt.show()

# Distribusi target
sns.countplot(x='Outcome', data=df)
plt.title("Distribusi Label (Outcome)")
plt.show()

"""## Feature Importance dari Random Forest
Kita lihat fitur mana yang paling berpengaruh terhadap prediksi berdasarkan Random Forest.

"""

# Feature importance dari Random Forest
feature_names = X.columns
importances = rf.feature_importances_

plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=feature_names)
plt.title("Feature Importance dari Random Forest")
plt.show()

"""## Hyperparameter Tuning dengan GridSearchCV
Kita lakukan pencarian parameter terbaik untuk Random Forest menggunakan GridSearchCV.

"""

from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_rf = grid_search.best_estimator_
y_pred_best = best_rf.predict(X_test)

print("Random Forest setelah Hyperparameter Tuning:")
print(classification_report(y_test, y_pred_best))
print("Accuracy:", accuracy_score(y_test, y_pred_best))

