import streamlit as st
import datetime

st.set_page_config(
    page_title="Sistem Formulir Pendaftaran Nikah Desa",
    page_icon="💍",
    layout="wide"
)

st.title("💍 Aplikasi Pendaftaran Nikah (Formulir Isian Data Desa)")
st.markdown("Isilah data calon pasangan pengantin dengan **cermat & teliti**.")

# TAB NAVIGATION
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 1. Pengaturan Surat & Lokasi",
    "👨 2. Catin Laki-Laki & Ortu",
    "👩 3. Catin Perempuan & Ortu",
    "🕌 4. Data Wali Nikah",
    "📄 5. Ringkasan & Cetak Data (RDS)"
])

# TAB 1: PENGATURAN SURAT & LOKASI
with tab1:
    st.subheader("Informasi Desa & Registrasi Surat")
    col1, col2 = st.columns(2)
    
    with col1:
        nama_desa = st.text_input("Nama Desa", value="TAMBI")
        status_kades = st.selectbox("Status Jabatan Kades", ["Definitif", "Pj", "Plt"])
        nama_kades = st.text_input("Nama Kepala Desa", value="J U R I")
        petugas_pengantar = st.text_input("Petugas Pengantar", value="Chalim Muchtarom, S.Pd.I")
        no_register = st.number_input("NO. Register Surat", min_value=1, value=19, step=1)
        
    with col2:
        tgl_surat = st.date_input("Tanggal Surat", value=datetime.date(2026, 10, 8))
        tgl_pelaksanaan = st.date_input("Tanggal Pelaksanaan Akad Nikah", value=datetime.date(2026, 11, 19))
        
        selisih_hari = (tgl_pelaksanaan - tgl_surat).days
        if selisih_hari < 10:
            st.warning(f"⚠️ Selisih tanggal {selisih_hari} hari (Kurang dari 10 hari kerja). **Perlu Dispensasi Camat!**")
        else:
            st.success(f"✅ Selisih tanggal {selisih_hari} hari. Pengajuan sesuai batas waktu.")

        waktu_akad = st.text_input("Waktu Akad Nikah", value="JAM : 08:30")
        alasan_waktu = st.text_input("Catatan / Alasan Waktu", value="KETERBATASAN WAKTU CUTI DARI PEMBERI KERJA")
        
        lokasi_pilihan = st.radio("Lokasi Akad", ["LUAR KANTOR", "KANTOR"])
        if lokasi_pilihan == "KANTOR":
            tempat_akad = "BALAI NIKAH KUA WATUKUMPUL"
            st.info(f"Tempat Akad: {tempat_akad}")
        else:
            tempat_akad = st.text_area("Tempat Akad Nikah (Luar Kantor)", value="Dsn Simadu RT 003 RW 008 Desa Badak Kecamatan Belik Kabupaten Pemalang")

# TAB 2: CATIN LAKI-LAKI & ORTU
with tab2:
    st.subheader("Data Calon Pengantin Laki-Laki")
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        catin_p_nama = st.text_input("1. Nama Lengkap (Laki-Laki)", value="AOFA ARDIAN FADILLAH AZIZ")
        catin_p_nik = st.text_input("2. NIK (Laki-Laki)", value="3327041308020004")
        catin_p_pendidikan = st.selectbox("Pendidikan (Laki-Laki)", ["SD/MI", "SLTP/MTS", "SLTA/MA", "D3", "S1", "S2/S3"], index=2)
        catin_p_tmpt_lahir = st.text_input("3. Tempat Lahir (Laki-Laki)", value="PEMALANG")
        catin_p_tgl_lahir = st.date_input("Tanggal Lahir (Laki-Laki)", value=datetime.date(2002, 8, 13))
        
    with col_p2:
        catin_p_pekerjaan = st.selectbox("4. Pekerjaan (Laki-Laki)", ["WIRASWASTA", "PETANI", "PNS", "KARYAWAN SWASTA", "BURUH", "Lainnya"])
        if catin_p_pekerjaan == "Lainnya":
            catin_p_pekerjaan = st.text_input("Pekerjaan Lainnya (Laki-Laki)", value="")
            
        catin_p_warganegara = st.text_input("5. Kewarganegaraan (Laki-Laki)", value="INDONESIA")
        catin_p_status = st.selectbox("6. Status Pernikahan", ["JEJAKA (BELUM KAWIN)", "DUDA MATI", "DUDA CERAI"])
        catin_p_alamat1 = st.text_input("7. Alamat Baris 1 (Laki-Laki)", value="DK. Tambi RT 002 RW 001 Tambi")
        catin_p_alamat2 = st.text_input("Alamat Baris 2 (Laki-Laki)", value="Kec. Watukumpul Kab. Pemalang")

    st.markdown("---")
    st.subheader("Data Orang Tua Catin Laki-Laki")
    status_ortu_p = st.radio("Status Orang Tua Catin Laki-Laki", ["BERSAMA (Hidup)", "Ayah Meninggal", "Ibu Meninggal", "Kedua Orang Tua Meninggal"], key="status_ortu_p")
    
    col_pa1, col_pa2 = st.columns(2)
    with col_pa1:
        st.markdown("**-- Data Ayah Kandung --**")
        p_ayah_nama = st.text_input("Nama Ayah (Laki-Laki)", value="TOHIRIN")
        p_ayah_bin = st.text_input("Bin (Ayah Laki-Laki)", value="MUHAYAT")
        p_ayah_nik = st.text_input("NIK Ayah (Laki-Laki)", value="3327040107730222")
        p_ayah_tmpt_lahir = st.text_input("Tempat Lahir Ayah", value="PEMALANG")
        p_ayah_tgl_lahir = st.date_input("Tgl Lahir Ayah", value=datetime.date(1973, 7, 1))
        p_ayah_pekerjaan = st.text_input("Pekerjaan Ayah", value="WIRASWASTA")
        p_ayah_alamat = st.text_input("Alamat Ayah", value="DK. Tambi RT 002 RW 001 Tambi Kec. Watukumpul Kab. Pemalang")

    with col_pa2:
        st.markdown("**-- Data Ibu Kandung --**")
        p_ibu_nama = st.text_input("Nama Ibu (Laki-Laki)", value="KARIPAH")
        p_ibu_binti = st.text_input("Binti (Ibu Laki-Laki)", value="SUMARTO")
        p_ibu_nik = st.text_input("NIK Ibu (Laki-Laki)", value="3327044107740064")
        p_ibu_tmpt_lahir = st.text_input("Tempat Lahir Ibu", value="PEMALANG")
        p_ibu_tgl_lahir = st.date_input("Tgl Lahir Ibu", value=datetime.date(1974, 7, 1))
        p_ibu_pekerjaan = st.text_input("Pekerjaan Ibu", value="MENGURUS RUMAH TANGGA")
        p_ibu_alamat = st.text_input("Alamat Ibu", value="DK. Tambi RT 002 RW 001 Tambi Kec. Watukumpul Kab. Pemalang")

# TAB 3: CATIN PEREMPUAN & ORTU
with tab3:
    st.subheader("Data Calon Pengantin Perempuan")
    col_w1, col_w2 = st.columns(2)
    
    with col_w1:
        catin_w_nama = st.text_input("1. Nama Lengkap (Perempuan)", value="FIKA INTAN ELMASARI")
        catin_w_nik = st.text_input("2. NIK (Perempuan)", value="3327034810050002")
        catin_w_pendidikan = st.selectbox("Pendidikan (Perempuan)", ["SD/MI", "SLTP/MTS", "SLTA/MA", "D3", "S1", "S2/S3"], index=2)
        catin_w_tmpt_lahir = st.text_input("3. Tempat Lahir (Perempuan)", value="PEMALANG")
        catin_w_tgl_lahir = st.date_input("Tanggal Lahir (Perempuan)", value=datetime.date(2005, 10, 8))
        
    with col_w2:
        catin_w_pekerjaan = st.selectbox("4. Pekerjaan (Perempuan)", ["Pelajar/Mahasiswa", "MENGURUS RUMAH TANGGA", "WIRASWASTA", "KARYAWAN SWASTA", "Lainnya"])
        if catin_w_pekerjaan == "Lainnya":
            catin_w_pekerjaan = st.text_input("Pekerjaan Lainnya (Perempuan)", value="")
            
        catin_w_warganegara = st.text_input("5. Kewarganegaraan (Perempuan)", value="INDONESIA")
        catin_w_status = st.selectbox("6. Status Pernikahan (Perempuan)", ["PERAWAN (BELUM KAWIN)", "JANDA MATI", "JANDA CERAI"])
        catin_w_alamat1 = st.text_input("7. Alamat Baris 1 (Perempuan)", value="Dsn Simadu RT 003 RW 008 Desa Badak")
        catin_w_alamat2 = st.text_input("Alamat Baris 2 (Perempuan)", value="Kecamatan Belik Kabupaten Pemalang")

    st.markdown("---")
    st.subheader("Data Orang Tua Catin Perempuan")
    status_ortu_w = st.radio("Status Orang Tua Catin Perempuan", ["BERSAMA (Hidup)", "Ayah Meninggal", "Ibu Meninggal", "Kedua Orang Tua Meninggal"], key="status_ortu_w")
    
    col_wa1, col_wa2 = st.columns(2)
    with col_wa1:
        st.markdown("**-- Data Ayah Kandung --**")
        w_ayah_nama = st.text_input("Nama Ayah (Perempuan)", value="SAMIUN")
        w_ayah_bin = st.text_input("Bin (Ayah Perempuan)", value="WASNURI")
        w_ayah_nik = st.text_input("NIK Ayah (Perempuan)", value="3327031103810011")
        w_ayah_tmpt_lahir = st.text_input("Tempat Lahir Ayah (Perempuan)", value="PEMALANG")
        w_ayah_tgl_lahir = st.date_input("Tgl Lahir Ayah (Perempuan)", value=datetime.date(1981, 3, 11))
        w_ayah_pekerjaan = st.text_input("Pekerjaan Ayah (Perempuan)", value="PETANI")
        w_ayah_alamat = st.text_input("Alamat Ayah (Perempuan)", value="Dsn Simadu RT 003 RW 008 Desa Badak Kecamatan Belik Kabupaten Pemalang")

    with col_wa2:
        st.markdown("**-- Data Ibu Kandung --**")
        w_ibu_nama = st.text_input("Nama Ibu (Perempuan)", value="SRINANI")
        w_ibu_binti = st.text_input("Binti (Ibu Perempuan)", value="SAHRON")
        w_ibu_nik = st.text_input("NIK Ibu (Perempuan)", value="3327034101870012")
        w_ibu_tmpt_lahir = st.text_input("Tempat Lahir Ibu (Perempuan)", value="PEMALANG")
        w_ibu_tgl_lahir = st.date_input("Tgl Lahir Ibu (Perempuan)", value=datetime.date(1987, 1, 1))
        w_ibu_pekerjaan = st.text_input("Pekerjaan Ibu (Perempuan)", value="MENGURUS RUMAH TANGGA")
        w_ibu_alamat = st.text_input("Alamat Ibu (Perempuan)", value="Dsn Simadu RT 003 RW 008 Desa Badak Kecamatan Belik Kabupaten Pemalang")

# TAB 4: DATA WALI NIKAH
with tab4:
    st.subheader("Informasi & Identitas Wali Nikah")
    status_perwalian = st.radio("Status Perwalian", ["WALI NASAB", "WALI HAKIM"])
    
    if status_perwalian == "WALI NASAB":
        hubungan_wali = st.selectbox("Hubungan Wali Nasab", ["AYAH KANDUNG", "KAKAK KANDUNG", "ADIK KANDUNG", "PAFE (PAMAN AYAH)", "LAINNYA"])
        
        if hubungan_wali == "AYAH KANDUNG":
            st.info("💡 Karena Wali Nasab adalah AYAH KANDUNG, data wali otomatis disesuaikan dari data Ayah Catin Perempuan.")
            wali_nama = w_ayah_nama
            wali_bin = w_ayah_bin
            wali_nik = w_ayah_nik
            wali_tmpt_lahir = w_ayah_tmpt_lahir
            wali_tgl_lahir = w_ayah_tgl_lahir
            wali_pekerjaan = w_ayah_pekerjaan
            wali_alamat = w_ayah_alamat
        else:
            col_wali1, col_wali2 = st.columns(2)
            with col_wali1:
                wali_nama = st.text_input("Nama Wali Nikah", value="")
                wali_bin = st.text_input("Bin Wali Nikah", value="")
                wali_nik = st.text_input("NIK Wali Nikah", value="")
                wali_tmpt_lahir = st.text_input("Tempat Lahir Wali", value="PEMALANG")
            with col_wali2:
                wali_tgl_lahir = st.date_input("Tanggal Lahir Wali", value=datetime.date(1980, 1, 1))
                wali_pekerjaan = st.text_input("Pekerjaan Wali", value="WIRASWASTA")
                wali_alamat = st.text_area("Alamat Wali Nikah", value="")
    else:
        sebab_wali_hakim = st.selectbox("Sebab Menggunakan Wali Hakim", ["SEPI WALI", "WALI ADHAL", "WALI GAIB/TIDAK DIKETAHUI"])
        st.warning(f"Menggunakan Wali Hakim dengan alasan: **{sebab_wali_hakim}**")
        wali_nama = "KEPALA KUA WATUKUMPUL (WALI HAKIM)"
        wali_bin = "-"
        wali_nik = "-"
        wali_tmpt_lahir = "-"
        wali_tgl_lahir = datetime.date.today()
        wali_pekerjaan = "-"
        wali_alamat = "-"

# TAB 5: RINGKASAN & CETAK DATA (RDS)
with tab5:
    st.subheader("📄 Rekam Data Sementara (RDS)")
    st.markdown("Format ringkasan data siap disalin untuk operator KUA atau catatan berkas:")
    
    rds_text = f"""==========================================
REKAM DATA SEMENTARA (RDS) PENDAFTARAN NIKAH
DESA {nama_desa} / REGISTER: {no_register}
PETUGAS: {petugas_pengantar}
==========================================
A. PELAKSANAAN
• Hari / Tanggal : {tgl_pelaksanaan.strftime('%A, %d %B %Y')}
• Waktu         : {waktu_akad}
• Tempat Akad   : {tempat_akad}

B. CALON SUAMI
• Nama Lengkap  : {catin_p_nama}
• NIK / Ed.     : {catin_p_nik} / {catin_p_pendidikan}
• Tempat, Tgl L : {catin_p_tmpt_lahir}, {catin_p_tgl_lahir.strftime('%d-%m-%Y')}
• Pekerjaan     : {catin_p_pekerjaan}
• Status        : {catin_p_status}
• Alamat        : {catin_p_alamat1} {catin_p_alamat2}
- Ayah Kandung  : {p_ayah_nama} Bin {p_ayah_bin} (NIK: {p_ayah_nik})
- Ibu Kandung   : {p_ibu_nama} Binti {p_ibu_binti} (NIK: {p_ibu_nik})

C. CALON ISTRI
• Nama Lengkap  : {catin_w_nama}
• NIK / Ed.     : {catin_w_nik} / {catin_w_pendidikan}
• Tempat, Tgl L : {catin_w_tmpt_lahir}, {catin_w_tgl_lahir.strftime('%d-%m-%Y')}
• Pekerjaan     : {catin_w_pekerjaan}
• Status        : {catin_w_status}
• Alamat        : {catin_w_alamat1} {catin_w_alamat2}
- Ayah Kandung  : {w_ayah_nama} Bin {w_ayah_bin} (NIK: {w_ayah_nik})
- Ibu Kandung   : {w_ibu_nama} Binti {w_ibu_binti} (NIK: {w_ibu_nik})

D. WALI NIKAH
• Status Wali   : {status_perwalian}
• Nama Wali     : {wali_nama} Bin {wali_bin}
• NIK Wali      : {wali_nik}
==========================================
"""
    
    st.code(rds_text, language="text")
    st.download_button("📥 Unduh Teks Ringkasan Data (RDS)", data=rds_text, file_name=f"RDS_{catin_p_nama}.txt")
