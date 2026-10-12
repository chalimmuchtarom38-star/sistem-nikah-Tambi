import streamlit as st
import datetime
import os
import io
import openpyxl

# Set Konfigurasi Halaman agar responsif dan nyaman di HP
st.set_page_config(
    page_title="Formulir Nikah Desa",
    page_icon="💍",
    layout="centered"
)

# CSS Tambahan khusus agar tampilan di HP lebih rapi dan tombol mudah diklik
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 3em;
    }
    .stDownloadButton>button {
        width: 100%;
        background-color: #2e7d32;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        height: 3.5em;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💍 Pendaftaran Nikah Desa")
st.markdown("Isilah data calon pengantin dengan cermat langsung dari HP Anda.")

# ----------------------------------------------------
# FUNGSI MEMBACA NOMOR REGISTER TERAKHIR DARI EXCEL
# ----------------------------------------------------
excel_filename = "N_AOFA ARDIAN AZIZ RT 02_01.xlsx"

def get_default_register():
    if os.path.exists(excel_filename):
        try:
            wb = openpyxl.load_workbook(excel_filename, data_only=True)
            ws = wb["ISIAN DATA"]
            val = ws["C7"].value
            if isinstance(val, int):
                return val
        except:
            pass
    return 19

if 'no_register_val' not in st.session_state:
    st.session_state.no_register_val = get_default_register()

# ----------------------------------------------------
# TAB NAVIGATION (RAMAH HP)
# ----------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📋 1. Surat",
    "👨 2. Catin L",
    "👩 3. Catin P",
    "🕌 4. Wali",
    "📄 5. RDS",
    "📥 6. Unduh"
])

# ----------------------------------------------------
# TAB 1: PENGATURAN SURAT & LOKASI
# ----------------------------------------------------
with tab1:
    st.subheader("1. Info Surat & Lokasi")
    nama_desa = st.text_input("Nama Desa", value="TAMBI")
    status_kades = st.selectbox("Status Jabatan Kades", ["Definitif", "Pj", "Plt"])
    nama_kades = st.text_input("Nama Kepala Desa", value="J U R I")
    petugas_pengantar = st.text_input("Petugas Pengantar", value="Chalim Muchtarom, S.Pd.I")
    
    reg_col1, reg_col2 = st.columns([3, 1])
    with reg_col1:
        no_register = st.number_input("NO. Register Surat", min_value=1, value=st.session_state.no_register_val, step=1)
    with reg_col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕"):
            st.session_state.no_register_val += 1
            st.rerun()
            
    tgl_surat = st.date_input("Tanggal Surat", value=datetime.date(2026, 10, 8))
    tgl_pelaksanaan = st.date_input("Tgl Pelaksanaan Akad", value=datetime.date(2026, 11, 19))
    
    selisih_hari = (tgl_pelaksanaan - tgl_surat).days
    if selisih_hari < 10:
        st.warning(f"⚠️ Selisih {selisih_hari} hari (< 10 hari kerja). Perlu Dispensasi Camat!")
    else:
        st.success(f"✅ Selisih {selisih_hari} hari. Sesuai batas waktu.")

    waktu_akad = st.text_input("Waktu Akad Nikah", value="JAM : 08:30")
    alasan_waktu = st.text_input("Catatan / Alasan Waktu", value="KETERBATASAN WAKTU CUTI DARI PEMBERI KERJA")
    
    lokasi_pilihan = st.radio("Lokasi Akad", ["LUAR KANTOR", "KANTOR"])
    if lokasi_pilihan == "KANTOR":
        tempat_akad = "BALAI NIKAH KUA WATUKUMPUL"
        st.info(f"Tempat: {tempat_akad}")
    else:
        tempat_akad = st.text_area("Tempat Akad (Luar Kantor)", value="Dsn Simadu RT 003 RW 008 Desa Badak Kecamatan Belik Kabupaten Pemalang")

# ----------------------------------------------------
# TAB 2: CATIN LAKI-LAKI & ORTU
# ----------------------------------------------------
with tab2:
    st.subheader("2. Catin Laki-Laki & Ortu")
    catin_p_nama = st.text_input("Nama Lengkap (Laki-Laki)", value="AOFA ARDIAN FADILLAH AZIZ")
    catin_p_nik = st.text_input("NIK (Laki-Laki)", value="3327041308020004")
    catin_p_pendidikan = st.selectbox("Pendidikan (Laki-Laki)", ["SD/MI", "SLTP/MTS", "SLTA/MA", "D3", "S1", "S2/S3"], index=2)
    catin_p_tmpt_lahir = st.text_input("Tempat Lahir (Laki-Laki)", value="PEMALANG")
    catin_p_tgl_lahir = st.date_input("Tgl Lahir (Laki-Laki)", value=datetime.date(2002, 8, 13))
    
    catin_p_pekerjaan = st.selectbox("Pekerjaan (Laki-Laki)", ["WIRASWASTA", "PETANI", "PNS", "KARYAWAN SWASTA", "BURUH", "Lainnya"])
    if catin_p_pekerjaan == "Lainnya":
        catin_p_pekerjaan_val = st.text_input("Pekerjaan Lainnya", value="")
    else:
        catin_p_pekerjaan_val = catin_p_pekerjaan
        
    catin_p_warganegara = st.text_input("Kewarganegaraan (Laki-Laki)", value="INDONESIA")
    catin_p_status = st.selectbox("Status Pernikahan", ["JEJAKA (BELUM KAWIN)", "DUDA MATI", "DUDA CERAI"])
    catin_p_alamat1 = st.text_input("Alamat Baris 1", value="DK. Tambi RT 002 RW 001 Tambi")
    catin_p_alamat2 = st.text_input("Alamat Baris 2", value="Kec. Watukumpul Kab. Pemalang")

    st.markdown("---")
    st.markdown("#### Orang Tua Catin Laki-Laki")
    p_ayah_status = st.selectbox("Status Ayah", ["Hidup", "Meninggal", "Miruda", "Sepi Ayah"], index=0, key="pa_status")
    p_ayah_nama = st.text_input("Nama Ayah", value="TOHIRIN")
    p_ayah_bin = st.text_input("Bin Ayah", value="MUHAYAT")
    p_ayah_nik = st.text_input("NIK Ayah", value="3327040107730222")
    p_ayah_tmpt_lahir = st.text_input("Tempat Lahir Ayah", value="PEMALANG")
    p_ayah_tgl_lahir = st.date_input("Tgl Lahir Ayah", value=datetime.date(1973, 7, 1))
    p_ayah_pekerjaan = st.text_input("Pekerjaan Ayah", value="WIRASWASTA")
    p_ayah_alamat1 = st.text_input("Alamat Ayah 1", value="DK. Tambi RT 002 RW 001 Tambi")
    p_ayah_alamat2 = st.text_input("Alamat Ayah 2", value="Kec. Watukumpul Kab. Pemalang")

    p_ibu_status = st.selectbox("Status Ibu", ["Hidup", "Meninggal"], index=0, key="pi_status")
    p_ibu_nama = st.text_input("Nama Ibu", value="KARIPAH")
    p_ibu_binti = st.text_input("Binti Ibu", value="SUMARTO")
    p_ibu_nik = st.text_input("NIK Ibu", value="3327044107740064")
    p_ibu_tmpt_lahir = st.text_input("Tempat Lahir Ibu", value="PEMALANG")
    p_ibu_tgl_lahir = st.date_input("Tgl Lahir Ibu", value=datetime.date(1974, 7, 1))
    p_ibu_pekerjaan = st.text_input("Pekerjaan Ibu", value="MENGURUS RUMAH TANGGA")
    p_ibu_alamat1 = st.text_input("Alamat Ibu 1", value="DK. Tambi RT 002 RW 001 Tambi")
    p_ibu_alamat2 = st.text_input("Alamat Ibu 2", value="Kec. Watukumpul Kab. Pemalang")

# ----------------------------------------------------
# TAB 3: CATIN PEREMPUAN & ORTU
# ----------------------------------------------------
with tab3:
    st.subheader("3. Catin Perempuan & Ortu")
    catin_w_nama = st.text_input("Nama Lengkap (Perempuan)", value="FIKA INTAN ELMASARI")
    catin_w_nik = st.text_input("NIK (Perempuan)", value="3327034810050002")
    catin_w_pendidikan = st.selectbox("Pendidikan (Perempuan)", ["SD/MI", "SLTP/MTS", "SLTA/MA", "D3", "S1", "S2/S3"], index=2)
    catin_w_tmpt_lahir = st.text_input("Tempat Lahir (Perempuan)", value="PEMALANG")
    catin_w_tgl_lahir = st.date_input("Tgl Lahir (Perempuan)", value=datetime.date(2005, 10, 8))
    
    catin_w_pekerjaan = st.selectbox("Pekerjaan (Perempuan)", ["Pelajar/Mahasiswa", "MENGURUS RUMAH TANGGA", "WIRASWASTA", "KARYAWAN SWASTA", "Lainnya"])
    if catin_w_pekerjaan == "Lainnya":
        catin_w_pekerjaan_val = st.text_input("Pekerjaan Lainnya (P)", value="")
    else:
        catin_w_pekerjaan_val = catin_w_pekerjaan
        
    catin_w_warganegara = st.text_input("Kewarganegaraan (Perempuan)", value="INDONESIA")
    catin_w_status = st.selectbox("Status Pernikahan (P)", ["PERAWAN (BELUM KAWIN)", "JANDA MATI", "JANDA CERAI"])
    catin_w_alamat1 = st.text_input("Alamat Baris 1 (P)", value="Dsn Simadu RT 003 RW 008 Desa Badak")
    catin_w_alamat2 = st.text_input("Alamat Baris 2 (P)", value="Kecamatan Belik Kabupaten Pemalang")

    st.markdown("---")
    st.markdown("#### Orang Tua Catin Perempuan")
    w_ayah_status = st.selectbox("Status Ayah (P)", ["Hidup", "Meninggal", "Miruda", "Sepi Ayah"], index=0, key="wa_status")
    w_ayah_nama = st.text_input("Nama Ayah (P)", value="SAMIUN")
    w_ayah_bin = st.text_input("Bin Ayah (P)", value="WASNURI")
    w_ayah_nik = st.text_input("NIK Ayah (P)", value="3327031103810011")
    w_ayah_tmpt_lahir = st.text_input("Tempat Lahir Ayah (P)", value="PEMALANG")
    w_ayah_tgl_lahir = st.date_input("Tgl Lahir Ayah (P)", value=datetime.date(1981, 3, 11))
    w_ayah_pekerjaan = st.text_input("Pekerjaan Ayah (P)", value="PETANI")
    w_ayah_alamat1 = st.text_input("Alamat Ayah 1 (P)", value="Dsn Simadu RT 003 RW 008 Desa Badak")
    w_ayah_alamat2 = st.text_input("Alamat Ayah 2 (P)", value="Kecamatan Belik Kabupaten Pemalang")

    w_ibu_status = st.selectbox("Status Ibu (P)", ["Hidup", "Meninggal"], index=0, key="wi_status")
    w_ibu_nama = st.text_input("Nama Ibu (P)", value="SRINANI")
    w_ibu_binti = st.text_input("Binti Ibu (P)", value="SAHRON")
    w_ibu_nik = st.text_input("NIK Ibu (P)", value="3327034101870012")
    w_ibu_tmpt_lahir = st.text_input("Tempat Lahir Ibu (P)", value="PEMALANG")
    w_ibu_tgl_lahir = st.date_input("Tgl Lahir Ibu (P)", value=datetime.date(1987, 1, 1))
    w_ibu_pekerjaan = st.text_input("Pekerjaan Ibu (P)", value="MENGURUS RUMAH TANGGA")
    w_ibu_alamat1 = st.text_input("Alamat Ibu 1 (P)", value="Dsn Simadu RT 003 RW 008 Desa Badak")
    w_ibu_alamat2 = st.text_input("Alamat Ibu 2 (P)", value="Kecamatan Belik Kabupaten Pemalang")

# ----------------------------------------------------
# TAB 4: DATA WALI NIKAH
# ----------------------------------------------------
with tab4:
    st.subheader("4. Data Wali Nikah")
    status_perwalian = st.radio("Status Perwalian", ["WALI NASAB", "WALI HAKIM"])
    
    if status_perwalian == "WALI NASAB":
        hubungan_wali = st.selectbox("Hubungan Wali Nasab", ["AYAH KANDUNG", "KAKAK KANDUNG", "ADIK KANDUNG", "PAFE (PAMAN AYAH)", "LAINNYA"])
        
        if hubungan_wali == "AYAH KANDUNG":
            st.info("💡 Data Wali otomatis menyamakan data Ayah Catin Perempuan.")
            wali_nama = w_ayah_nama
            wali_bin = w_ayah_bin
            wali_nik = w_ayah_nik
            wali_tmpt_lahir = w_ayah_tmpt_lahir
            wali_tgl_lahir = w_ayah_tgl_lahir
            wali_pekerjaan = w_ayah_pekerjaan
            wali_alamat1 = w_ayah_alamat1
            wali_alamat2 = w_ayah_alamat2
        else:
            wali_nama = st.text_input("Nama Wali Nikah", value="")
            wali_bin = st.text_input("Bin Wali Nikah", value="")
            wali_nik = st.text_input("NIK Wali Nikah", value="")
            wali_tmpt_lahir = st.text_input("Tempat Lahir Wali", value="PEMALANG")
            wali_tgl_lahir = st.date_input("Tgl Lahir Wali", value=datetime.date(1980, 1, 1))
            wali_pekerjaan = st.text_input("Pekerjaan Wali", value="WIRASWASTA")
            wali_alamat1 = st.text_input("Alamat Wali Baris 1", value="")
            wali_alamat2 = st.text_input("Alamat Wali Baris 2", value="")
    else:
        sebab_wali_hakim = st.selectbox("Sebab Menggunakan Wali Hakim", ["SEPI WALI", "WALI ADHAL", "WALI GAIB/TIDAK DIKETAHUI"])
        st.warning(f"Menggunakan Wali Hakim: **{sebab_wali_hakim}**")
        wali_nama = "KEPALA KUA WATUKUMPUL (WALI HAKIM)"
        wali_bin = "-"
        wali_nik = "-"
        wali_tmpt_lahir = "-"
        wali_tgl_lahir = datetime.date.today()
        wali_pekerjaan = "-"
        wali_alamat1 = "-"
        wali_alamat2 = "-"

# ----------------------------------------------------
# TAB 5: RINGKASAN (RDS)
# ----------------------------------------------------
with tab5:
    st.subheader("5. Ringkasan Data (RDS)")
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
• Pekerjaan     : {catin_p_pekerjaan_val}
• Status        : {catin_p_status}
• Alamat        : {catin_p_alamat1} {catin_p_alamat2}
- Ayah Kandung  : {p_ayah_nama} Bin {p_ayah_bin} (NIK: {p_ayah_nik})
- Ibu Kandung   : {p_ibu_nama} Binti {p_ibu_binti} (NIK: {p_ibu_nik})

C. CALON ISTRI
• Nama Lengkap  : {catin_w_nama}
• NIK / Ed.     : {catin_w_nik} / {catin_w_pendidikan}
• Tempat, Tgl L : {catin_w_tmpt_lahir}, {catin_w_tgl_lahir.strftime('%d-%m-%Y')}
• Pekerjaan     : {catin_w_pekerjaan_val}
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
    st.download_button("📥 Download Teks RDS", data=rds_text, file_name=f"RDS_{catin_p_nama}.txt")

# ----------------------------------------------------
# TAB 6: UNDUH FILE EXCEL
# ----------------------------------------------------
with tab6:
    st.subheader("6. Unduh File Excel Hasil Isian")
    st.markdown("Klik tombol hijau di bawah untuk mengunduh file Excel terisi data baru. Rumus, format, dan isi sheet lain dijamin aman 100%.")
    
    if os.path.exists(excel_filename):
        def generate_filled_excel():
            wb = openpyxl.load_workbook(excel_filename, data_only=False)
            ws = wb["ISIAN DATA"]
            
            # Write Form Data to Sheet 'ISIAN DATA'
            ws["C3"] = nama_desa
            ws["C4"] = status_kades
            ws["C5"] = nama_kades
            ws["C6"] = petugas_pengantar
            ws["C7"] = no_register
            ws["C8"] = datetime.datetime.combine(tgl_surat, datetime.time.min)
            ws["C9"] = datetime.datetime.combine(tgl_pelaksanaan, datetime.time.min)
            ws["C10"] = waktu_akad
            ws["D10"] = alasan_waktu
            ws["E11"] = lokasi_pilihan
            if lokasi_pilihan == "LUAR KANTOR":
                ws["C11"] = tempat_akad
                
            # Catin Laki-Laki
            ws["C14"] = catin_p_nama
            ws["C15"] = catin_p_nik
            ws["D15"] = catin_p_pendidikan
            ws["C16"] = catin_p_tmpt_lahir
            ws["D16"] = datetime.datetime.combine(catin_p_tgl_lahir, datetime.time.min)
            ws["C17"] = catin_p_pekerjaan_val
            ws["C18"] = catin_p_warganegara
            ws["C19"] = catin_p_status
            ws["C20"] = catin_p_alamat1
            ws["C21"] = catin_p_alamat2
            
            # Ayah Laki-Laki
            ws["E23"] = p_ayah_status
            ws["C23"] = p_ayah_nama
            ws["D23"] = p_ayah_bin
            ws["C24"] = p_ayah_nik
            ws["C25"] = p_ayah_tmpt_lahir
            ws["D25"] = datetime.datetime.combine(p_ayah_tgl_lahir, datetime.time.min)
            ws["C28"] = p_ayah_pekerjaan
            ws["C29"] = p_ayah_alamat1
            ws["C30"] = p_ayah_alamat2
            
            # Ibu Laki-Laki
            ws["E32"] = p_ibu_status
            ws["C32"] = p_ibu_nama
            ws["D32"] = p_ibu_binti
            ws["C33"] = p_ibu_nik
            ws["C34"] = p_ibu_tmpt_lahir
            ws["D34"] = datetime.datetime.combine(p_ibu_tgl_lahir, datetime.time.min)
            ws["C37"] = p_ibu_pekerjaan
            ws["C38"] = p_ibu_alamat1
            ws["C39"] = p_ibu_alamat2
            
            # Catin Perempuan
            ws["C42"] = catin_w_nama
            ws["C43"] = catin_w_nik
            ws["D43"] = catin_w_pendidikan
            ws["C44"] = catin_w_tmpt_lahir
            ws["D44"] = datetime.datetime.combine(catin_w_tgl_lahir, datetime.time.min)
            ws["C45"] = catin_w_pekerjaan_val
            ws["C46"] = catin_w_warganegara
            ws["C47"] = catin_w_status
            ws["C48"] = catin_w_alamat1
            ws["C49"] = catin_w_alamat2
            
            # Ayah Perempuan
            ws["E51"] = w_ayah_status
            ws["C51"] = w_ayah_nama
            ws["D51"] = w_ayah_bin
            ws["C52"] = w_ayah_nik
            ws["C53"] = w_ayah_tmpt_lahir
            ws["D53"] = datetime.datetime.combine(w_ayah_tgl_lahir, datetime.time.min)
            ws["C56"] = w_ayah_pekerjaan
            ws["C57"] = w_ayah_alamat1
            ws["C58"] = w_ayah_alamat2
            
            # Ibu Perempuan
            ws["E60"] = w_ibu_status
            ws["C60"] = w_ibu_nama
            ws["D60"] = w_ibu_binti
            ws["C61"] = w_ibu_nik
            ws["C62"] = w_ibu_tmpt_lahir
            ws["D62"] = datetime.datetime.combine(w_ibu_tgl_lahir, datetime.time.min)
            ws["C65"] = w_ibu_pekerjaan
            ws["C66"] = w_ibu_alamat1
            ws["C67"] = w_ibu_alamat2
            
            # Wali Nikah
            ws["C70"] = status_perwalian
            if status_perwalian == "WALI NASAB":
                ws["H73"] = hubungan_wali
                ws["C75"] = wali_nama
                ws["C76"] = wali_bin
                ws["C77"] = wali_nik
                ws["C78"] = wali_tmpt_lahir
                ws["D78"] = datetime.datetime.combine(wali_tgl_lahir, datetime.time.min)
                ws["C81"] = wali_pekerjaan
                ws["C82"] = wali_alamat1
                ws["C83"] = wali_alamat2
            else:
                ws["H73"] = sebab_wali_hakim

            output = io.BytesIO()
            wb.save(output)
            output.seek(0)
            return output.getvalue()

        file_bytes = generate_filled_excel()
        download_filename = f"NIKAH_{catin_p_nama.replace(' ', '_')}_{catin_w_nama.replace(' ', '_')}.xlsx"
        
        st.download_button(
            label="📊 DOWNLOAD FILE EXCEL TERISI",
            data=file_bytes,
            file_name=download_filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.
