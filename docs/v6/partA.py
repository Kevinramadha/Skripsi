# ===================== A. DATA =====================
def A_sumber(D):
    s = D.slide('Lampiran · Data dan Sumber Data')
    sub(s, 'Data tahunan 2015–2025 tingkat provinsi; tahun dasar 2025, simulasi sampai 2050 dengan langkah waktu 1 tahun')
    rows = [['Kelompok', 'Variabel', 'Indikator', 'Satuan', 'Periode', 'Skala', 'Sumber data'],
            ['Permintaan wisatawan', 'Jumlah Wisatawan', 'Kunjungan wisnus + wisman', 'Kunjungan', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, Statistik Wisnus & Wisman'],
            ['', 'Total Malam Menginap', 'Malam menginap tamu di akomodasi', 'Malam', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, Statistik TPK'],
            ['', 'Proporsi Wisatawan Menginap', 'Wisatawan menginap ÷ total kunjungan', 'Dmnl', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, diolah'],
            ['', 'Rata-rata Lama Menginap Tamu', 'Rata-rata malam menginap tamu', 'Malam', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, Statistik TPK'],
            ['', 'Pengeluaran per Kunjungan', 'Rata-rata belanja per kunjungan', 'Miliar Rp/kunjungan', '2018–2025', 'Tahunan, nasional', 'BPS RI, Statistik Wisman & Wisnus'],
            ['Akomodasi', 'Jumlah Hotel dan Akomodasi', 'Unit hotel bintang + nonbintang', 'Unit', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, Statistik Hotel & Akomodasi Lain'],
            ['', 'Jumlah Kamar', 'Kamar tersedia', 'Kamar', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, Statistik Hotel & Akomodasi Lain'],
            ['', 'Tingkat Penghunian Kamar (TPK)', 'Persentase kamar terisi', 'Persen', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, Statistik TPK'],
            ['', 'Tingkat Penghunian Ganda (TPG)', 'Rata-rata tamu per kamar terisi', 'Orang', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, Statistik TPK'],
            ['ODTW', 'Jumlah ODTW', 'Unit ODTW terdaftar', 'Unit', '2018–2024', 'Tahunan, provinsi', 'BPS, Statistik ODTW'],
            ['Ketenagakerjaan', 'Tenaga Kerja Pariwisata', 'Pekerja KBLI I dan R, S, T, U', 'Jiwa', '2017–2025', 'Tahunan, provinsi', 'BPS, Sakernas'],
            ['Ekonomi', 'PDRB Sektor Pariwisata', 'PDRB ADHK kategori I dan R, S, T, U', 'Miliar Rp', '2015–2025', 'Tahunan, provinsi', 'BPS DIY, PDRB Lapangan Usaha'],
            ['', 'Investasi Sektor Pariwisata', 'Realisasi PMA + PMDN KBLI pariwisata', 'Miliar Rp', '2015–2025', 'Tahunan, provinsi', 'Kementerian Investasi/BKPM'],
            ['Lahan', 'Lahan Terbangun (citra)', 'Luas kelas terbangun (built)', 'Hektar', '2016–2025', 'Tahunan, provinsi', 'Dynamic World, Google Earth Engine'],
            ['', 'Luas Lahan Tersedia', 'Luas wilayah administratif', 'Hektar', 'Tetap', 'Titik tunggal, provinsi', 'Kepmendagri, dikutip BPS DIY'],
            ['ODTW (citra)', 'Intensitas cahaya malam (NTL)', 'Radiansi komposit tahunan', 'nW/cm²/sr', '2015–2025', 'Tahunan, provinsi', 'VIIRS DNB (NOAA), Google Earth Engine']]
    hl = {(r, 4): YEL_L for r in (5, 10, 11, 14)}
    gf = tbl(s, 0.9, 2.1, 18.2, [2.0, 3.0, 3.5, 1.6, 1.25, 1.85, 4.0], rows, size=10, rowh=0.385, hl=hl, center=(4,))
    for r in range(1, len(rows)):
        c = gf.table.cell(r, 0).text_frame.paragraphs[0]
        if c.runs: c.runs[0].font.bold = True; c.runs[0].font.color.rgb = rgb(TEAL)
    note(s, 'Kuning = periode tidak lengkap. ODTW 2015–2017 dan 2025 diestimasi dengan NTL; lahan 2015 diekstrapolasi; tenaga kerja 2015–2016 dan pengeluaran 2015–2017 diekstrapolasi (lihat lampiran ekstrapolasi). Model memuat 61 variabel: 5 stock, 10 flow, 11 auxiliary, 35 parameter.',
         y=8.85, h=0.95)
    src(s, 'Sumber: Buku Subbab 3.4.1 (Tabel 2).')


def A_historis(D):
    yrs = list(range(2015, 2026))
    perm = [[6413735, 6331609, 82126, 5698325, 4056916, 1.400, 0.001024], [6551294, 6436655, 114639, 6097324, 4407538, 1.380, 0.001129],
            [6644412, 6498739, 145673, 10899900, 6854907, 1.590, 0.001245], [7996959, 7858137, 138822, 10293319, 6525894, 1.580, 0.001373],
            [20520104, 20407076, 113028, 13363923, 9006150, 1.480, 0.001246], [19610135, 19591482, 18653, 4753098, 3210480, 1.480, 0.001259],
            [22849394.5, 22834000, 15394.5, 7379577, 4642840, 1.590, 0.002035], [25755726, 25743590, 12136, 9267217, 6364013, 1.460, 0.002010],
            [30542580, 30437069, 105511, 11417702, 7857534, 1.450, 0.002431], [38134536, 38030739, 103797, 11503540, 8154522, 1.410, 0.002720],
            [40695654, 40592837, 102817, 11954114, 8377109, 1.430, 0.002720]]
    s = D.slide('Lampiran · Data Historis 2015–2025 (1/3): Permintaan')
    sub(s, 'Permintaan wisatawan dan pengeluaran; data sebelum penyambungan wisnus')
    rows = [['Tahun', 'Jumlah wisatawan', 'Wisnus', 'Wisman', 'Total malam menginap', 'Wisatawan menginap', 'Lama menginap (malam)', 'Pengeluaran/kunjungan (miliar Rp)']]
    hl = {}
    for i, (y, v) in enumerate(zip(yrs, perm), 1):
        rows.append([str(y), fmt(v[0], 1 if y == 2021 else 0), fmt(v[1], 0), fmt(v[2], 1 if y == 2021 else 0), fmt(v[3], 0), fmt(v[4], 0), fmt(v[5], 3), fmt(v[6], 6)])
        if y <= 2017: hl[(i, 7)] = YEL_L
        if y == 2021: hl[(i, 3)] = YEL_L; hl[(i, 1)] = YEL_L
    tbl(s, 0.9, 2.1, 18.2, [0.9, 2.2, 2.0, 1.4, 2.3, 2.2, 1.9, 2.6], rows, size=11, rowh=0.44, hl=hl, center=tuple(range(8)))
    note(s, 'Kuning = nilai olahan: wisman 2021 diinterpolasi linear (rata-rata 2020 dan 2022), pengeluaran 2015–2017 diekstrapolasi CAGR. Lonjakan 2018→2019 karena perubahan metode pencacahan wisnus (lihat lampiran penyambungan).', y=7.6, h=0.9)
    rows2 = [['Variabel', 'Satuan', 'Sumber'], ['Jumlah wisatawan / wisnus / wisman', 'Kunjungan / perjalanan', 'Publikasi wisatawan nusantara dan mancanegara, BPS'],
             ['Total malam, wisatawan menginap, lama menginap', 'Malam / orang', 'Publikasi Tingkat Penghunian Kamar, BPS DIY'], ['Pengeluaran per kunjungan', 'Miliar Rp/kunjungan', 'BPS RI (wisnus DIY, wisman nasional × kurs tengah BI)']]
    tbl(s, 0.9, 8.6, 18.2, [5, 3, 10.2], rows2, size=9.5, rowh=0.33)
    src(s, 'Sumber: Buku Lampiran 7; [FIX] Master Data final.xlsx.')

    s = D.slide('Lampiran · Data Historis 2015–2025 (2/3): Akomodasi')
    sub(s, 'Jumlah usaha akomodasi, kamar, dan tingkat penghunian')
    ak = [[1165, 89, 1076, 22594, 34.89, 1.970], [1170, 94, 1076, 23613, 37.72, 2.110], [1179, 117, 1062, 26164, 45.08, 1.910], [1617, 143, 1474, 32869, 45.11, 1.930],
          [1817, 163, 1654, 35717, 45.34, 2.020], [1848, 172, 1676, 36482, 28.90, 2.050], [1696, 168, 1528, 34386, 27.48, 2.150], [1818, 192, 1626, 36644, 44.99, 2.080],
          [1820, 193, 1627, 36883, 44.77, 2.100], [2000, 207, 1793, 52233, 42.17, 2.060], [2291, 222, 2069, 49066, 38.07, 2.070]]
    rows = [['Tahun', 'Hotel & akomodasi (unit)', 'Hotel bintang', 'Nonbintang & lainnya', 'Jumlah kamar', 'TPK (%)', 'TPG (orang/kamar)', 'Kamar per unit*']]
    hl = {}
    for i, (y, v) in enumerate(zip(yrs, ak), 1):
        rows.append([str(y), fmt(v[0], 0), fmt(v[1], 0), fmt(v[2], 0), fmt(v[3], 0), fmt(v[4], 2), fmt(v[5], 3), fmt(v[3] / v[0], 2)])
        if y == 2018: hl[(i, 1)] = YEL_L; hl[(i, 3)] = YEL_L
    tbl(s, 0.9, 2.1, 18.2, [0.9, 2.6, 2.0, 2.6, 2.2, 1.8, 2.3, 2.0], rows, size=11, rowh=0.44, hl=hl, center=tuple(range(8)))
    note(s, 'Kuning: lonjakan 2018 (+438 unit) hampir seluruhnya akomodasi nonbintang, diduga karena perluasan cakupan pendataan; tetap dipakai apa adanya. *Kamar per unit = jumlah kamar ÷ jumlah unit (hitungan sendiri); model memakai 21,4168 (nilai 2025).', y=7.6, h=0.9)
    rows2 = [['Variabel', 'Satuan', 'Sumber'], ['Hotel & akomodasi, bintang, nonbintang, kamar', 'Unit / kamar', 'Statistik Hotel dan Akomodasi Lainnya, BPS DIY'], ['TPK, TPG', 'Persen / orang', 'Publikasi Tingkat Penghunian Kamar, BPS DIY']]
    tbl(s, 0.9, 8.6, 18.2, [5, 3, 10.2], rows2, size=9.5, rowh=0.33)
    src(s, 'Sumber: Buku Lampiran 7; [FIX] Master Data final.xlsx.')

    s = D.slide('Lampiran · Data Historis 2015–2025 (3/3): ODTW, TK, Ekonomi, Lahan')
    sub(s, 'Nilai yang dipakai model; sel kuning adalah hasil estimasi atau ekstrapolasi')
    oth = [[165, 254537, 43037.00, 10131.09, 53.09], [158, 263878, 44561.08, 10694.03, 373.84], [171, 273563, 50223.96, 11347.59, 165.39], [177, 354684, 56624.36, 12100.99, 568.33],
           [189, 334784, 63480.04, 13104.38, 741.45], [180, 313840, 58962.04, 10926.83, 489.69], [170, 310755, 59887.53, 12097.19, 848.80], [183, 395284, 57709.08, 13672.58, 463.59],
           [201, 359340, 75624.40, 14809.20, 1175.26], [218, 350946, 73511.57, 15873.81, 712.28], [201, 364994, 55029.54, 16947.62, 1325.95]]
    rows = [['Tahun', 'Jumlah ODTW (unit)', 'Tenaga kerja pariwisata (jiwa)', 'Lahan terbangun (ha)', 'PDRB ADHK pariwisata (miliar Rp)', 'Investasi pariwisata (miliar Rp)']]
    hl = {}
    for i, (y, v) in enumerate(zip(yrs, oth), 1):
        rows.append([str(y), fmt(v[0], 0), fmt(v[1], 0), fmt(v[2], 2), fmt(v[3], 2), fmt(v[4], 2)])
        if y in (2015, 2016, 2017, 2025): hl[(i, 1)] = YEL_L
        if y in (2015, 2016): hl[(i, 2)] = YEL_L
        if y == 2015: hl[(i, 3)] = YEL_L
    tbl(s, 0.9, 2.1, 18.2, [1.0, 2.6, 3.4, 3.0, 3.6, 3.2], rows, size=11, rowh=0.44, hl=hl, center=tuple(range(6)))
    note(s, 'ODTW 2015–2017 & 2025: estimasi NTL. Tenaga kerja 2015–2016: ekstrapolasi CAGR. Lahan 2015: ekstrapolasi tren log-linear (tidak dipakai menurunkan parameter). Buku Lampiran 7 menulis lahan 2015 “9443.037,00”; nilai di Master Data adalah 43.037,00.', y=7.6, h=0.9, title='Kuning')
    rows2 = [['Variabel', 'Satuan', 'Sumber'], ['Jumlah ODTW', 'Unit', 'Statistik ODTW BPS (2018–2024) dan estimasi NTL'], ['Tenaga kerja (KBLI I & R,S,T,U)', 'Jiwa', 'DIY Dalam Angka / Sakernas, BPS'],
             ['Lahan terbangun', 'Hektar', 'Dynamic World (built), GEE'], ['PDRB ADHK pariwisata; investasi', 'Miliar Rp', 'BPS DIY; BKPM (PMA + PMDN)']]
    tbl(s, 0.9, 8.6, 18.2, [5, 3, 10.2], rows2, size=9, rowh=0.28)
    src(s, 'Sumber: Buku Lampiran 7; [FIX] Master Data final.xlsx.', y=10.15)


def A_sambung(D):
    s = D.slide('Lampiran · Penyusunan Data dan Penyambungan Wisnus')
    sub(s, 'Basis data induk menyeragamkan satuan, periode, dan format; empat ketidakteraturan ditangani sebelum pemodelan')
    hdr(s, 0.9, 2.1, 8.6, 'Tata cara penyusunan data')
    steps(s, 0.9, 2.7, 8.6, [
        ('Daftar variabel', 'Variabel model (stock, flow, auxiliary, parameter) disusun beserta satuan dan sumbernya.'),
        ('Pengumpulan 2015–2025', 'Nilai dikumpulkan dari BPS, BKPM, dan citra satelit, lalu dihimpun dalam satu basis data induk.'),
        ('Penyeragaman', 'Satuan, periode, dan format tahun diseragamkan agar parameter bisa ditelusuri ke sumbernya.'),
        ('Pengisian data kosong', 'ODTW dan lahan terbangun diestimasi dengan citra; TK dan pengeluaran diekstrapolasi.'),
        ('Penanganan 4 ketidakteraturan', 'Patahan wisnus 2018/2019, lahan 2015, lonjakan akomodasi 2018, pandemi 2020–2021.')], h=0.92, gap=0.1, size=11)
    hdr(s, 9.9, 2.1, 9.2, 'Rumus faktor penyambung wisnus')
    formula(s, 9.9, 2.7, 9.2, 2.6, [
        ('g_pra = (W₂₀₁₈ ÷ W₂₀₁₅)^(1/3) − 1 = 7,63%', '   CAGR 2015–2018 (metode lama)'),
        ('g_pasca = (W₂₀₂₅ ÷ W₂₀₂₁)^(1/4) − 1 = 15,52%', '   CAGR 2021–2025 (tanpa 2019–2020)'),
        ('ḡ_wajar = (g_pra + g_pasca) ÷ 2 = 11,58%', ''),
        ('Faktor = (W₂₀₁₉ ÷ W₂₀₁₈) ÷ (1 + ḡ_wajar) = 2,566 ÷ 1,1158 = 2,2997', '')], size=12.5)
    rows = [['Tahun', 'Data mentah', 'Seri tersambung (×2,2997)', 'Pertumbuhan tersambung'],
            ['2015', '6.413.735', '14.749.959', '—'], ['2016', '6.551.294', '15.066.309', '+2,14%'], ['2017', '6.644.412', '15.280.457', '+1,42%'],
            ['2018', '7.996.959', '18.390.971', '+20,36%'], ['2019', '20.520.104', '20.520.104 (asli)', '+11,58%']]
    tbl(s, 9.9, 5.5, 9.2, [1.2, 2.4, 3.2, 2.4], rows, size=10.5, rowh=0.38, center=(0, 1, 2, 3))
    note(s, 'Faktor berada pada rentang 2,22–2,38 bila tahun acuan g_wajar diubah; rentang ini diuji ulang pada kalibrasi Tahap 3. Seri sambungan hanya dipakai untuk uji perilaku P5, tidak untuk menurunkan parameter. Pertumbuhan 2016 (+2,14%) dihitung sendiri dari seri sambungan.', y=8.0, h=1.05)
    src(s, 'Sumber: Buku Subbab 3.6.1 dan 4.5.1 (Tabel 45); [FIX] Master Data final.xlsx, sheet “Perhitungan faktor sambung”.')


def A_ekstrapolasi(D):
    s = D.slide('Lampiran · Ekstrapolasi dan Interpolasi (1/2): Ringkasan')
    sub(s, 'Hanya empat variabel yang diisi dengan ekstrapolasi atau interpolasi; dua variabel lain diisi dengan citra satelit')
    rows = [['Variabel', 'Tahun diisi', 'Metode', 'Rumus', 'Hasil', 'Dasar pemilihan'],
            ['Tenaga kerja pariwisata', '2015, 2016', 'Ekstrapolasi mundur CAGR 2017–2025', 'TKₜ = TKₜ₊₁ ÷ (1 + g);  g = (TK₂₀₂₅/TK₂₀₁₇)^(1/8) − 1 = 3,67%', '2016: 263.878\n2015: 254.537', 'NTL (R² selisih 0,070) dan PDRB (R² selisih 0,093) ditolak sebagai penduga'],
            ['Pengeluaran per kunjungan', '2015–2017', 'Ekstrapolasi mundur CAGR 2018–2025', 'Pₜ = Pₜ₊₁ ÷ (1 + g);  g = (P₂₀₂₅/P₂₀₁₈)^(1/7) − 1 = 10,27%', '2015: Rp1.023.749\n2016: Rp1.128.845\n2017: Rp1.244.730', 'Wisnus & wisman kosong 2015–2017; jendela penuh meredam lonjakan 2020–2021'],
            ['Lahan terbangun', '2015', 'Ekstrapolasi mundur tren log-linear 2016–2025', 'ln Lₜ = a + β·t;  β = 0,0348;  L₂₀₁₅ = L₂₀₁₆ ÷ e^β', '43.037,00 ha', 'Dynamic World baru tersedia 2016; nilai tidak dipakai menurunkan parameter'],
            ['Wisman', '2021', 'Interpolasi linear', 'W₂₀₂₁ = (W₂₀₂₀ + W₂₀₂₂) ÷ 2', '15.394,5 kunjungan', 'Nilai 2021 sama persis dengan rata-rata 2020 dan 2022 (lihat catatan)'],
            ['Jumlah ODTW', '2015–2017, 2025', 'Estimasi regresi NTL (citra)', 'ODTW = 121,61 + 34,59 × NTL', '165, 158, 171, 201', 'R² selisih 0,405 ≥ 0,30; RMSE LOOCV 5,99% ≤ 10%']]
    gf = tbl(s, 0.9, 2.1, 18.2, [2.3, 1.5, 2.5, 4.6, 2.4, 4.9], rows, size=10.5, rowh=0.95, hl={(5, c): LIGHT for c in range(6)})
    gf.table.rows[0].height = Inches(0.45)
    note(s, 'CAGR (compound annual growth rate) dipilih karena menjaga laju pertumbuhan tahunan konstan dan tidak menghasilkan nilai negatif. Interpolasi wisman 2021 disimpulkan dari angka di Master Data (15.394,5 = rata-rata 18.653 dan 12.136); tidak dijelaskan di buku, mohon dicek.', y=8.4, h=1.1)
    src(s, 'Sumber: Buku Subbab 3.5–3.6; notebook “Ekstrapolasi Tenaga Kerja Pariwisata”, “Perhitungan Pengeluaran wisatawan”; [FIX] Master Data final.xlsx.')

    s = D.slide('Lampiran · Ekstrapolasi dan Interpolasi (2/2): Hasil')
    sub(s, 'Seri lengkap setelah pengisian: nilai 2015–2016 (TK) dan 2015–2017 (pengeluaran) adalah hasil ekstrapolasi')
    yrs = [str(y) for y in range(2015, 2026)]
    hdr(s, 0.9, 2.1, 8.9, 'Tenaga kerja pariwisata (ribu jiwa)', 'CAGR 3,67%')
    tk = [254.537, 263.878, 273.563, 354.684, 334.784, 313.840, 310.755, 395.284, 359.340, 350.946, 364.994]
    line_chart(s, 0.9, 2.65, 8.9, 3.0, yrs, [('Tenaga kerja', tk)], [TEAL], fmt_='#,##0', legend=False)
    rows = [['Jendela CAGR (dari 2017)', '2017–18', '2017–19', '2017–20', '2017–21', '2017–22', '2017–23', '2017–24', '2017–25'],
            ['CAGR', '+29,65%*', '+10,63%', '+4,68%', '+3,24%', '+7,64%', '+4,65%', '+3,62%', '+3,67%']]
    tbl(s, 0.9, 5.75, 8.9, [2.4] + [0.81] * 8, rows, size=9, rowh=0.36, center=tuple(range(1, 9)), hl={(1, 8): GREEN})
    T(s, 0.9, 6.5, 8.9, 0.6, [[('*dikeluarkan karena diskontinuitas 2017→2018. Dipilih jendela terpanjang 2017–2025 (hijau).', 9.5, False, GREY, True)]])
    hdr(s, 10.2, 2.1, 8.9, 'Pengeluaran per kunjungan (ribu Rp)', 'CAGR 10,27%')
    pe = [1023.749, 1128.845, 1244.730, 1372.512, 1245.981, 1258.716, 2035.275, 2009.980, 2430.839, 2720.479, 2720.209]
    line_chart(s, 10.2, 2.65, 8.9, 3.0, yrs, [('Pengeluaran', pe)], [CYAN], fmt_='#,##0', legend=False)
    formula(s, 10.2, 5.75, 8.9, 1.25, ['Pengeluaran gabungan = (Wisnus × P_wisnus + Wisman × P_wisman) ÷ (Wisnus + Wisman)',
                                       'P_wisman (US$) × kurs tengah BI; P_wisnus khusus DIY (ribu Rp)'], size=11)
    hdr(s, 0.9, 7.25, 18.2, 'Lahan terbangun 2015 dan wisman 2021')
    rows = [['Langkah', 'Lahan terbangun 2015', 'Wisman 2021'],
            ['Data acuan', 'L₂₀₁₆ = 44.561,08 ha; regresi ln L 2016–2025 → β = 0,0348 (e^β − 1 = 3,54%/tahun)', 'W₂₀₂₀ = 18.653; W₂₀₂₂ = 12.136'],
            ['Perhitungan', '44.561,08 ÷ e^0,0348 = 43.037,00 ha', '(18.653 + 12.136) ÷ 2 = 15.394,5'],
            ['Pemakaian', 'Hanya pelengkap seri; tidak dipakai menurunkan parameter', 'Masuk ke jumlah wisatawan 2021 = 22.849.394,5']]
    tbl(s, 0.9, 7.8, 18.2, [2.2, 9.2, 6.8], rows, size=10, rowh=0.38)
    src(s, 'Sumber: notebook ekstrapolasi (repository); [FIX] Master Data final.xlsx (sheet Tahap 0: β₁ = 0,0348). Rumus lahan 2015 = L₂₀₁₆/e^β direkonstruksi dari nilai Master Data.', y=10.15)
