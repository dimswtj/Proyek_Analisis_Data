import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import calendar

sns.set(style='dark')

day_df = pd.read_csv('day.csv')

st.title('Proyek Analisis Data: [Bike Sharing Dataset]')

st.markdown(
    """
    - **Nama:** PUTU GEDE DIMAS WITJAKSANA
    - **Email:** dimaswitjaksana12@gmail.com
    - **ID Dicoding:** dimas_witjaksana
    """
)

with st.sidebar:
    
    st.title('Profile')
    
    st.markdown(
    """
    - **Nama:** PUTU GEDE DIMAS WITJAKSANA
    - **Email:** dimaswitjaksana12@gmail.com
    - **ID Dicoding:** dimas_witjaksana
    """
    )

st.title (" Visualization & Explanatory Analysis")

st.write("Data Head:")
st.write(day_df.head())

st.title("Histogram Data Day")

# Tampilkan histogram menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
day_df.hist(ax=ax)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title (" Heatmap")

# Memilih kolom yang akan digunakan untuk heatmap
heatmap_data = day_df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']]

# Menghitung matriks korelasi
correlation_matrix = heatmap_data.corr()

# Tampilkan heatmap menggunakan Seaborn
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Correlation Matrix')

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title ("Pertanyaan 1")

# Menghitung jumlah penggunaan sepeda tiap bulan
monthly_usage = day_df.groupby("mnth")["cnt"].sum().reset_index()

monthly_usage["mnth"] = monthly_usage["mnth"].apply(lambda x: calendar.month_name[x])

# Tampilkan visualisasi menggunakan Streamlit
st.subheader("Apakah ada bulan-bulan tertentu yang memiliki tingkat penggunaan sepeda yang lebih tinggi daripada yang lain? dan berapa jumlah sepeda yang digunakan tiap bulannya?")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="mnth", y="cnt", data=monthly_usage, palette="viridis", ax=ax)
plt.title("Apakah ada bulan-bulan tertentu yang memiliki tingkat penggunaan sepeda yang lebih tinggi daripada yang lain? dan berapa jumlah sepeda yang digunakan tiap bulannya?")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penggunaan Sepeda")
plt.xticks(rotation=45)
plt.tight_layout()

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

st.title ("Pertanyaan 2")

# Menghitung jumlah penggunaan sepeda berdasarkan musim
seasonal_usage = day_df.groupby("season")["cnt"].sum().reset_index()

season_names = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

# Mengubah angka musim menjadi nama musim
seasonal_usage["season"] = seasonal_usage["season"].map(season_names)

# Tampilkan visualisasi menggunakan Streamlit
st.subheader("Bagaimana pengaruh musim terhadap jumlah penggunaan sepeda dan penggunaan sepeda paling banyak pada musim apa?")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(seasonal_usage["season"], seasonal_usage["cnt"], color='skyblue')
plt.title("Jumlah Penggunaan Sepeda Berdasarkan Musim")
plt.xlabel("Musim")
plt.ylabel("Jumlah Penggunaan Sepeda")
plt.xticks(rotation=0)
plt.tight_layout()

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Menghitung jumlah kemunculan musim pada setiap bulan


# Dictionary untuk mapping angka bulan ke nama bulan
month_names = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember"
}

# Dictionary untuk mapping angka musim ke nama musim
season_names = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

# Mapping bulan menjadi nama bulan dan musim
day_df["mnth"] = day_df["mnth"].map(month_names)
day_df["season"] = day_df["season"].map(season_names)

season_counts = day_df.groupby("mnth")["season"].value_counts().unstack().fillna(0)

# Mengubah angka bulan menjadi nama bulan
season_counts = season_counts.reindex(list(month_names.values()))

# Tampilkan visualisasi menggunakan Streamlit
st.title("Jumlah Kemunculan Musim pada Masing-Masing Bulan")
fig, ax = plt.subplots(figsize=(12, 6))
season_counts.plot(kind='bar', stacked=True, ax=ax)
plt.title("Jumlah Kemunculan Musim pada Masing-Masing Bulan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Kemunculan Musim")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Musim", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Menghitung jumlah kemunculan musim pada file CSV
season_counts_csv = day_df["season"].value_counts()

# Tampilkan visualisasi menggunakan Streamlit
st.title("Jumlah Kemunculan Musim pada File CSV")
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(season_counts_csv.index, season_counts_csv.values, color='skyblue')
plt.title("Jumlah Kemunculan Musim pada File CSV")
plt.xlabel("Musim")
plt.ylabel("Jumlah Kemunculan")
plt.xticks(rotation=0)
plt.tight_layout()

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Menghitung jumlah penggunaan sepeda berdasarkan musim
seasonal_usage = day_df.groupby("season")["cnt"].sum().reset_index()

# Tampilkan visualisasi jumlah penggunaan sepeda berdasarkan musim
st.title("Jumlah Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(seasonal_usage["season"], seasonal_usage["cnt"], color='skyblue')
plt.title("Jumlah Penggunaan Sepeda Berdasarkan Musim")
plt.xlabel("Musim")
plt.ylabel("Jumlah Penggunaan Sepeda")
plt.xticks(rotation=45)
plt.tight_layout()

# Tampilkan plot menggunakan Streamlit
st.pyplot(fig)

# # Dictionary untuk mapping angka musim ke nama musim
# season_names = {
#     1: "Spring",
#     2: "Summer",
#     3: "Fall",
#     4: "Winter"
# }

# # Mengubah angka musim menjadi nama musim
# day_df["season"] = day_df["season"].map(season_names)

# # Menghitung jumlah masing-masing nama musim
# season_counts = day_df["season"].value_counts()

# # Tampilkan visualisasi menggunakan Streamlit
# st.title("Jumlah Kemunculan Musim pada File CSV")
# fig, ax = plt.subplots(figsize=(8, 5))
# ax.bar(season_counts.index, season_counts.values, color='skyblue')
# plt.title("Jumlah Kemunculan Musim pada File CSV")
# plt.xlabel("Musim")
# plt.ylabel("Jumlah Kemunculan")
# plt.xticks(rotation=0)
# plt.tight_layout()

# # Tampilkan plot menggunakan Streamlit
# st.pyplot(fig)

# # Menghitung jumlah penggunaan sepeda berdasarkan musim
# seasonal_usage = day_df.groupby("season")["cnt"].sum().reset_index()

# # Tampilkan visualisasi menggunakan Streamlit
# st.title("Jumlah Penggunaan Sepeda Berdasarkan Musim")
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.bar(seasonal_usage["season"], seasonal_usage["cnt"], color='skyblue')
# plt.title("Jumlah Penggunaan Sepeda Berdasarkan Musim")
# plt.xlabel("Musim")
# plt.ylabel("Jumlah Penggunaan Sepeda")
# plt.xticks(rotation=45)
# plt.tight_layout()

# # Tampilkan plot menggunakan Streamlit
# st.pyplot(fig)

st.title("Conclution pertanyaan 1")
st.subheader("Dari analisis data yang telah dilakukan, dapat disimpulkan bahwa terdapa bulan-bulan tertentu yang memiliki tingkat penggunaan sepeda lebih tinggi daripada bulan-bulan yang lain yaitu bulan mei - bulan oktober dan yang tertinggi adalah pada bulan agustus.")
st.title("Conclution pertanyaan 2")
st.subheader(" Dari Analisis yang telah dilakukan mengenai penggunaan sepeda berdasarkan musim, dapat disimpulkan jika musim memiliki pengaruh yang signifikan terhadap penggunaan sepeda. dapat dilihat jika penggunaan sepeda paling banyak adalah pada musim fall atau gugur.")
