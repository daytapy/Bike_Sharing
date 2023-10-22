import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

bike_df = pd.read_csv('bike_data.csv')

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("bikerental2.png")
    st.text('Nama : M Syahrul Majid')
    st.text('Email : majidsyahrul30@gmail.com')

st.header('Bike Sharing Dashboard :sparkles:')

st.subheader("Perbedaan Pola Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan")

col1, col2 = st.columns(2)
 
with col1:
    time1 = '193 Bikes'
    st.metric("Average Weekday", value=time1)
 
with col2:
    time2 = '181 Bikes'
    st.metric("Average Weekend", value=time2)

# Kelompokkan data berdasarkan hari kerja dan akhir pekan
weekday_data = bike_df[bike_df['workingday'] == 1]  # Hari kerja (Senin hingga Jumat)
weekend_data = bike_df[bike_df['workingday'] == 0]  # Akhir pekan (Sabtu dan Minggu)

# Hitung rata-rata peminjaman sepeda per jam pada hari kerja dan akhir pekan
weekday_avg = weekday_data.groupby('hour')['count'].mean()
weekend_avg = weekend_data.groupby('hour')['count'].mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(weekday_avg, label='Hari Kerja', marker='o', color='g')
ax.plot(weekend_avg, label='Akhir Pekan', marker='o', color='r')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata-rata Jumlah Peminjaman')
ax.set_xticks(range(24))
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.subheader("Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda")

data_cuaca = bike_df.groupby(by='weather')['count'].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(data_cuaca['weather'], data_cuaca['count'], color=["#8FBC8F", "#D3D3D3", "#D3D3D3", "#D3D3D3"])
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Jumlah Peminjaman', fontsize=11)
st.pyplot(fig)


st.subheader("Pengaruh Kondisi Musim terhadap Peminjaman Sepeda")

data_musim = bike_df.groupby(by='season')['count'].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(data_musim['season'], data_cuaca['count'], color=["#8FBC8F", "#D3D3D3", "#D3D3D3", "#D3D3D3"])
ax.set_xlabel('Kondisi Musim')
ax.set_ylabel('Rata-rata Jumlah Peminjaman', fontsize=11)
st.pyplot(fig)

st.caption('Copyright (c) Daytapy 2023')
