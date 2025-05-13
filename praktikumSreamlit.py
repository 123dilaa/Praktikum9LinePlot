import streamlit as st
import matplotlib.pyplot as plt


import streamlit as st

# nama anggota kelompok
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        color: #d13661;
        font-size: 36px;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        margin-bottom: 30px;
    }

    .box {
        background-color: #ffe0f0;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(214, 51, 132, 0.2);
        width: 70%;
        margin: 0 auto;
    }

    .anggota {
        font-size: 20px;
        font-weight: 500;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul
st.markdown('<div class="title">💖 Daftar Nama Anggota Kelompok 💖</div>', unsafe_allow_html=True)

# Daftar nama dalam box
st.markdown(
    """
    <div class="box">
        <div class="anggota">1. Wulan Ramadewi</div>
        <div class="anggota">2. Siti Fadilla Siregar</div>
        <div class="anggota">3. Zahra Prahamari</div>
    </div>
    """,
    unsafe_allow_html=True
)


# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 15, 7, 25, 30, 28, 40, 45, 50, 48, 60, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 25, 30, 25, 35, 40]

# Streamlit layout
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", 
                            ("Line Plot", 
                            "Kustomisasi Line Plot", 
                            "Garis Berbeda untuk Menunjukkan Trend", 
                            "Subplot"))

def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales)
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig)

def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='red', linestyle='-.', marker='x')
    ax.set_title('Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def trend_lines_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A Trend', linestyle='--', color='blue')
    ax.plot(months, product_B_sales, label='Product B Trend', linestyle='-', color='red')
    ax.set_title('Tren Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot for Product A
    axs[0].plot(months, product_A_sales, label='Product A', color='blue', marker='o')
    axs[0].set_title('Penjualan Produk A Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # Plot for Product B
    axs[1].plot(months, product_B_sales, label='Product B', color='red', marker='x')
    axs[1].set_title('Penjualan Produk B Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

if option == "Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_lines_plot()
elif option == "Subplot":
    subplots()


