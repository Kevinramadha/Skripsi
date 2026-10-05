# ===================== F. KALIBRASI =====================
def F_protokol(D):
    s = D.slide('Lampiran · Protokol Kalibrasi: Ketentuan, Rumus, dan Aturan Keputusan')
    sub(s, 'Semua aturan ditetapkan sebelum pencarian dijalankan (Oliva, 2003; Homer, 2012)')
    K = [('1 · Parameter dibatasi', 'Hanya parameter asumsi/estimasi yang tidak pasti. Data resmi, identitas stok-aliran, dan nilai referensi tidak dikalibrasi.'),
         ('2 · Rentang berdasar', 'Dari triangulasi rujukan atau selang kepercayaan 95% estimasi asalnya.'),
         ('3 · Pasangan dihitung ulang', 'Parameter pasangan dihitung ulang di setiap titik pencarian agar identitas stok-aliran tetap terpenuhi.'),
         ('4 · Fungsi tujuan NRMSE', 'Satu keluarga dengan U1–U3; DC tidak dipakai karena tidak peka terhadap bias.'),
         ('5 · Aturan keputusan', 'Himpunan indiferen 5% dan aturan R1–R4; kepekaan diperiksa pada 2% dan 10%.')]
    for k, (a, b) in enumerate(K):
        y = 2.05 + k * 0.98
        box(s, 0.9, y, 6.4, 0.88, fill=LIGHT, line=LINE, anchor=MSO_ANCHOR.MIDDLE, margin=0.15, paras=[[(a, 12, True, TEAL)], [(b, 10.5, False, DARK)]])
    formula(s, 7.6, 2.05, 5.6, 2.9, ['NRMSE = √[Σ(Sₜ − Aₜ)² ÷ n] ÷ Ā', 'I = {θ : J(θ) ≤ 1,05 × J_min}',
                                      'k = (e^β₁ − 1) ÷ R̄', 'k_L, k_U = (e^(β₁ ∓ t*·se(β₁)) − 1) ÷ R̄',
                                      ('J = fungsi tujuan; I = himpunan indiferen;', ' β₁ = kemiringan regresi ln(lahan) thd tahun')], title='Rumus', size=12)
    rows = [['Aturan', 'Kondisi', 'Keputusan'],
            ['R1', 'Nilai turunan data ∈ I', 'Perbaikan tidak material → pertahankan nilai turunan data'],
            ['R2', 'I menyentuh kedua ujung rentang', 'Tidak teridentifikasi → pertahankan'],
            ['R3', 'Optimum tepat di batas rentang', 'Telusuri dengan leave-one-year-out (LOYO)'],
            ['R4', 'Selain ketiganya', 'Adopsi, bila lolos uji kompatibilitas Tahap 4']]
    tbl(s, 13.5, 2.05, 5.6, [0.8, 2.2, 2.6], rows, size=10, rowh=0.58, center=(0,), bold_first=True)
    hdr(s, 7.6, 5.25, 11.5, 'Pemicu penolakan uji kompatibilitas (Tahap 4)')
    rows2 = [['Kode', 'Pemicu', 'Ambang'],
             ['M1', 'NRMSE variabel target tahap itu pada uji penuh memburuk', '> 1,05 × sebelum kalibrasi'],
             ['M2', 'Rata-rata NRMSE sembilan variabel uji penuh memburuk', '> 1,05 × sebelum kalibrasi'],
             ['S', 'Uji kondisi ekstrem menjadi gagal / aturan fisik dilanggar', 'Ada pelanggaran'],
             ['T', 'Simulasi horizon diperpanjang tidak stabil', 'Ada ketidakstabilan']]
    tbl(s, 7.6, 5.8, 11.5, [0.9, 7.2, 3.4], rows2, size=10.5, rowh=0.45, center=(0, 2), bold_first=True)
    note(s, 'Evaluasi sesudah kalibrasi memakai data yang sama dengan data kalibrasi, sehingga hasilnya adalah kesesuaian pascakalibrasi, bukan validasi independen.', y=7.15, h=1.9)
    s.shapes[-1].left = Inches(0.9); s.shapes[-1].width = Inches(6.4)
    src(s, 'Sumber: Buku Subbab 3.7.4 (Tabel 19–20).')


def F_tahap0(D):
    s = D.slide('Lampiran · Kalibrasi Tahap 0: Koreksi Penurunan LPE dan LPD')
    sub(s, 'Bukan kalibrasi: penurunan parameter diselaraskan dengan cara Euler menghitung indeks Daya Tarik')
    formula(s, 0.9, 2.05, 8.8, 2.3, ['LPE = g₂₀₂₄→₂₀₂₅ ÷ (DT₂₀₂₄ − r);   LPD = r × LPE',
                                      ('Awal (DT dianggap 1):', '  0,06716 ÷ (1 − 0,75) = 0,26864;  LPD = 0,20148'),
                                      ('Koreksi (DT₂₀₂₄ = 0,99223):', '  0,06716 ÷ (0,99223 − 0,75) = 0,27726;  LPD = 0,207945')],
            title='Rumus (g = pertumbuhan wisatawan 2024→2025; r = rasio LPD/LPE = 0,75)', size=12.5)
    card(s, 0.9, 4.55, 8.8, 2.6, 'Bukti model memakai DT tahun awal periode', [
        'Rasio pertumbuhan 2016→2017 pada keluaran uji P5:',
        [('1,062357', 15, True, TEAL), ('   = hitung manual dengan DT₂₀₁₆ (cocok 6 digit)', 11.5, False, DARK)],
        [('1,063306', 15, True, RED), ('   = hitung manual dengan DT₂₀₁₇ (beda di digit ke-4)', 11.5, False, DARK)],
        'Jadi laju tahun t memakai DT tahun t, bukan t+1 (Euler).'], size=11.5)
    note(s, 'Uji kondisi ekstrem dan uji perilaku dijalankan ulang dengan nilai terkoreksi; hasil ekstrem tetap 15 lolos, 2 lolos dengan catatan, 0 gagal.', y=7.4, h=1.0)
    s.shapes[-1].left = Inches(0.9); s.shapes[-1].width = Inches(8.8)
    rows = [['Variabel (2050)', 'Sebelum koreksi', 'Sesudah koreksi', 'Selisih'],
            ['Jumlah Wisatawan', '94.692.357', '96.197.154', '+1,59%'],
            ['Jumlah Hotel', '5.323', '5.404', '+1,53%'],
            ['Jumlah ODTW', '364', '367', '+0,89%'],
            ['Tenaga Kerja', '640.325', '650.355', '+1,57%'],
            ['Lahan Terbangun (ha)', '122.192', '122.208', '+0,01%'],
            ['PDRB Pariwisata (miliar Rp)', '39.434', '40.061', '+1,59%'],
            ['Investasi (miliar Rp)', '1.925', '1.956', '+1,59%'],
            ['Daya Tarik', '0,814', '0,813', '−0,09%'],
            ['TPK', '0,358', '0,358', '+0,10%'],
            ['RDDL', '0,615', '0,615', '−0,08%']]
    hdr(s, 10.0, 2.05, 9.1, 'Dampak koreksi pada simulasi dasar 2050')
    tbl(s, 10.0, 2.6, 9.1, [3.4, 2.0, 2.0, 1.7], rows, size=11, rowh=0.5, center=(1, 2, 3), bold_first=True, hl={(1, 3): YEL_L})
    src(s, 'Sumber: Buku Subbab 4.6.1; hasil_uji_kondisi_ekstrem_v2.xlsx (sheet Simulasi Dasar).')


def F_tahap1(D):
    s = D.slide('Lampiran · Kalibrasi Tahap 1 (1/2): Akomodasi, Hasil Pencarian')
    sub(s, 'TPK Ambang 0,20–0,35 × Laju Demolisi 0,02–0,08 (775 kombinasi); Sensitivitas Konstruksi dihitung ulang tiap titik')
    rows = [['Uji', 'Nilai turunan (Ambang; Demolisi)', 'J turunan', 'Optimum (Ambang; Demolisi)', 'J optimum', 'Perbaikan'],
            ['P1', '0,275; 0,05', '0,10415', '0,350; 0,0600', '0,09203', '11,64%'],
            ['P1b', '0,275; 0,05', '0,11121', '0,330; 0,0600', '0,10577', '4,89%']]
    tbl(s, 0.9, 2.05, 18.2, [1.2, 4.0, 2.4, 4.2, 2.4, 4.0], rows, size=11.5, rowh=0.48, center=(0, 1, 2, 3, 4, 5), bold_first=True, hl={(1, 3): YEL_L, (1, 5): YEL_L})
    pic_box(s, MED + 'image45.png', 0.9, 3.65, 8.95, 4.6)
    T(s, 0.9, 8.27, 8.95, 0.35, [[('Permukaan fungsi tujuan, uji P1 (Buku Gambar 42)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    pic_box(s, MED + 'image47.png', 10.15, 3.65, 8.95, 4.6)
    T(s, 10.15, 8.27, 8.95, 0.35, [[('Permukaan fungsi tujuan, uji P1b (Buku Gambar 44)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    note(s, 'P1 membaik 11,64% (> 5%), tetapi optimum tepat di batas atas TPK Ambang (0,35) → aturan R3: telusuri dengan LOYO. Pada P1b perbaikan hanya 4,89% dan optimumnya berbeda (0,330).', y=8.75, h=0.85)
    src(s, 'Sumber: Buku Subbab 4.6.2 (Tabel 48, Gambar 42 dan 44); fungsi tujuan pada versi periode objektif.')


def F_tahap1b(D):
    s = D.slide('Lampiran · Kalibrasi Tahap 1 (2/2): Diagnostik dan Keputusan')
    sub(s, 'Optimum ternyata ditarik oleh satu tahun (2019) yang berhimpit dengan lonjakan data akomodasi 2018')
    rows = [['Tahun dikeluarkan', 'Ambang optimum', 'Demolisi optimum', 'Perbaikan'],
            ['(tidak ada)', '0,35', '0,0600', '11,64%'], ['2018', '0,33', '0,0550', '13,49%'], ['2019', '0,27', '0,0200', '5,74%'],
            ['2023', '0,35', '0,0425', '14,96%'], ['2024', '0,34', '0,0775', '16,06%'], ['2025', '0,35', '0,0650', '22,15%']]
    hdr(s, 0.9, 2.05, 8.6, 'Leave-one-year-out (LOYO), uji P1')
    tbl(s, 0.9, 2.6, 8.6, [2.6, 2.0, 2.0, 2.0], rows, size=11.5, rowh=0.48, center=(0, 1, 2, 3), hl={(3, c): YEL_L for c in range(4)})
    card(s, 0.9, 6.15, 8.6, 2.95, 'Tiga bukti nilai optimum tidak layak', [
        ('1. Satu tahun menentukan:', 'hanya mengeluarkan 2019 yang memindah optimum ke dalam rentang dan menjatuhkan perbaikan ke 5,74%. Residual: −22,1% (2018), −13,5% (2019), tahun lain < 1%.'),
        ('2. Gagal di versi lain:', 'pada versi dengan COVID, J naik 0,1003 → 0,1445 dan DC 0,2476 → 0,3215.'),
        ('3. Gagal di rancangan lain:', 'P1b memberi optimum berbeda (0,330) dan perbaikan < 5%.')], size=10.5)
    pic_box(s, MED + 'image46.png', 9.8, 2.05, 9.3, 4.8)
    T(s, 9.8, 6.88, 9.3, 0.35, [[('Jumlah hotel uji P1: data, nilai turunan, dan optimum grid; data melonjak pada 2018 (Buku Gambar 43)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    box(s, 9.8, 7.35, 9.3, 1.75, fill=GREEN, line=None, margin=0.2, anchor=MSO_ANCHOR.MIDDLE, paras=[
        [('Keputusan: nilai turunan data dipertahankan', 13, True, DARK)],
        [('TPK Ambang 0,275 · Laju Demolisi Dasar 0,05 · Sensitivitas Konstruksi 2,31385. Lonjakan 2018 (+438 unit, hampir seluruhnya non-bintang) diduga akibat perluasan cakupan pendataan.', 11.5, False, DARK)]])
    src(s, 'Sumber: Buku Subbab 4.6.2 (Tabel 49 dan Gambar 43). Catatan: di buku tabel ini dirujuk sebagai "Tabel 16"; seharusnya Tabel 49.')


def F_tahap2(D):
    s = D.slide('Lampiran · Kalibrasi Tahap 2: Laju Konversi Dasar Lahan')
    sub(s, 'Rentang = selang kepercayaan 95% dari regresi log-linear yang sama: 0,0034118–0,0851069')
    rows = [['Ukuran', 'Nilai turunan data', 'Titik optimum'],
            ['Laju Konversi Dasar', '0,0436052', '0,063866'], ['J (NRMSE)', '0,17264', '0,14716'],
            ['E1', '0,1125', '0,0404'], ['E2', '0,3918', '0,0657'], ['U1 (bias)', '0,4250', '0,0755'],
            ['DC', '0,4813', '0,4325'], ['Perbaikan relatif', '—', '14,76%']]
    hdr(s, 0.9, 2.05, 5.6, 'Hasil uji parsial P4')
    tbl(s, 0.9, 2.6, 5.6, [2.2, 1.7, 1.7], rows, size=11, rowh=0.47, center=(1, 2), bold_first=True, hl={(r, 2): GREEN for r in range(2, 8)})
    pic_box(s, MED + 'image48.png', 6.8, 2.05, 6.0, 3.6)
    T(s, 6.8, 5.68, 6.0, 0.35, [[('Profil fungsi tujuan, uji P4 (Buku Gambar 45)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    rows2 = [['Tahun keluar', 'k optimum', 'J min', 'J turunan'],
             ['(tidak ada)', '0,0639', '0,14716', '0,17264'], ['2016', '0,0639', '0,15185', '0,17814'], ['2017', '0,0630', '0,15257', '0,17881'],
             ['2018', '0,0630', '0,14970', '0,17499'], ['2019', '0,0614', '0,14120', '0,16444'], ['2022', '0,0655', '0,15499', '0,18322'],
             ['2023', '0,0557', '0,14048', '0,15041'], ['2024', '0,0581', '0,15606', '0,16788'], ['2025', '0,0827', '0,09278', '0,17758']]
    hdr(s, 13.1, 2.05, 6.0, 'LOYO, uji P4')
    tbl(s, 13.1, 2.6, 6.0, [1.7, 1.4, 1.4, 1.5], rows2, size=10.5, rowh=0.4, center=(0, 1, 2, 3), hl={(9, c): YEL_L for c in range(4)})
    card(s, 6.8, 6.15, 6.0, 2.95, 'Membaca hasil', [
        'Perbaikan 14,76% > 5% dan optimum di dalam rentang.',
        'Struktur galat membaik nyata: bias U1 runtuh 0,4250 → 0,0755.',
        'Menurut aturan R4 → kandidat adopsi, tetapi wajib lolos uji kompatibilitas (Tahap 4).'], size=11)
    card(s, 13.1, 6.85, 6.0, 2.25, 'Catatan LOYO', [
        'Tahun 2016–2024 hanya menggeser k ke 0,056–0,066.',
        'Mengeluarkan 2025 (tahun dasar) memindah k ke 0,0827: optimum sebagian bertumpu pada satu titik akhir.'], size=10.5, fill=YEL_L, line=YEL)
    src(s, 'Sumber: Buku Subbab 4.6.3 (Tabel 50–51, Gambar 45).')


def F_tahap4(D):
    s = D.slide('Lampiran · Kalibrasi Tahap 4: Uji Kompatibilitas pada Model Penuh')
    sub(s, 'Nilai Tahap 2 (v3: k = 0,0638662) dibandingkan nilai turunan data (v2: k = 0,0436052)')
    rows = [['Uji', 'Variabel', 'NRMSE v2', 'NRMSE v3', 'v3 / v2', 'Memburuk material'],
            ['B', 'Jumlah Wisatawan', '0,2233', '0,2254', '1,0096', 'Tidak'], ['B', 'Jumlah Hotel', '0,2099', '0,2104', '1,0027', 'Tidak'],
            ['B', 'Jumlah ODTW', '0,0625', '0,0626', '1,0007', 'Tidak'], ['B', 'Tenaga Kerja', '0,1897', '0,1897', '1,0000', 'Tidak'],
            ['B', 'Lahan Terbangun', '0,1796', '0,2378', '1,3241', 'Ya'], ['B', 'TPK', '0,2986', '0,2991', '1,0015', 'Tidak'],
            ['B', 'PDRB Pariwisata', '0,2778', '0,2793', '1,0054', 'Tidak'], ['B', 'Investasi Pariwisata', '0,5203', '0,5215', '1,0024', 'Tidak'],
            ['B', 'Total Malam Menginap', '0,3741', '0,3751', '1,0027', 'Tidak'], ['P1', 'Jumlah Hotel', '0,1041', '0,1041', '1,0000', 'Tidak'],
            ['P1', 'TPK', '0,2263', '0,2263', '1,0000', 'Tidak'], ['P4', 'Lahan Terbangun', '0,1726', '0,1472', '0,8524', '— (membaik)'],
            ['P1b', 'Jumlah Hotel', '0,1112', '0,1112', '1,0000', 'Tidak']]
    hl = {(5, c): PINK for c in range(6)}; hl.update({(12, c): GREEN for c in range(6)})
    tbl(s, 0.9, 2.05, 8.9, [0.7, 2.6, 1.3, 1.3, 1.2, 1.8], rows, size=10.5, rowh=0.44, center=(0, 2, 3, 4, 5), hl=hl)
    pic_box(s, MED + 'image49.png', 10.1, 2.05, 4.4, 2.75)
    pic_box(s, MED + 'image50.png', 14.7, 2.05, 4.4, 2.75)
    T(s, 10.1, 4.83, 9.0, 0.35, [[('Kiri: lahan uji penuh, v2 vs v3 (Gambar 46) · Kanan: lahan uji P4, turunan vs optimum (Gambar 47)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    card(s, 10.1, 5.3, 9.0, 2.2, 'Kenapa membaik di P4 tetapi memburuk di uji penuh?', [
        'P4 mulai 2016 dari 44.561 ha (di bawah garis tren), jadi laju lebih besar membantu mengejar data.',
        'Uji penuh mulai 2019 dari 63.480 ha yang sudah tinggi, jadi laju yang sama justru menjauh dari data 2025 (55.030 ha).',
        'Akar masalahnya ketidakstabilan klasifikasi Dynamic World.'], size=10.5)
    box(s, 10.1, 7.6, 9.0, 1.5, fill=PINK, line=None, margin=0.2, anchor=MSO_ANCHOR.MIDDLE, paras=[
        [('Keputusan: kalibrasi Tahap 2 ditolak (pemicu M1)', 13, True, DARK)],
        [('Lahan uji penuh memburuk 32,4% (rasio 1,3241 > 1,05). Laju Konversi Dasar kembali ke 0,0436052.', 11.5, False, DARK)]])
    src(s, 'Sumber: Buku Subbab 4.6.3 (Tabel 52, Gambar 46–47).')


def F_tahap3(D):
    s = D.slide('Lampiran · Kalibrasi Tahap 3 (1/2): Diagnostik Subsistem Wisatawan')
    sub(s, 'LPE dan LPD tidak memenuhi syarat kalibrasi; yang diukur adalah seberapa besar perubahan yang dituntut data')
    rows = [['Varian', 'Definisi', 'LPE*', 'Laju bersih setara', 'Perbaikan'],
            ['D-A', 'Periode normal 2016–2019', '0,440', '11,00%/th', '50,94%'],
            ['D-B', '2016–2019 + 2022–2025', '0,490', '12,25%/th', '78,78%'],
            ['D-C', 'D-A, faktor sambung 2,22 (batas bawah)', '0,410', '10,25%/th', '29,03%'],
            ['D-C', 'D-A, faktor sambung 2,38 (batas atas)', '0,470', '11,75%/th', '62,99%']]
    tbl(s, 0.9, 2.05, 18.2, [1.3, 7.6, 2.4, 3.6, 3.3], rows, size=11.5, rowh=0.46, center=(0, 2, 3, 4), bold_first=True)
    pic_box(s, MED + 'image51.png', 0.9, 4.55, 8.95, 4.2)
    T(s, 0.9, 8.77, 8.95, 0.35, [[('Profil fungsi tujuan terhadap LPE, varian D-A dan D-B (Buku Gambar 48)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    pic_box(s, MED + 'image52.png', 10.15, 4.55, 8.95, 4.2)
    T(s, 10.15, 8.77, 8.95, 0.35, [[('Punggung keteridentifikasian LPE dan rasio LPD/LPE (Buku Gambar 49)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    note(s, 'Data menuntut LPE 0,410–0,490 (nilai model 0,27726). Namun titik-titik yang sama baiknya membentuk punggung memanjang: LPE 0,26–0,80 berpasangan dengan rasio 0,60–0,86. Data hanya bisa mengenali selisih bersih kedua laju, bukan masing-masing → tidak teridentifikasi (R2).', y=9.15, h=0.85)
    src(s, 'Sumber: Buku Subbab 4.6.4 (Tabel 53, Gambar 48–49).')


def F_tahap3b(D):
    s = D.slide('Lampiran · Kalibrasi Tahap 3 (2/2): Dua Rezim Pertumbuhan')
    sub(s, 'Kesenjangan tren berasal dari pemulihan pascapandemi 2022–2024 yang berada di luar batas model')
    yrs = [str(y) for y in range(2017, 2026)]
    dat = [1.42, 20.36, 11.58, -4.43, 16.52, 12.72, 18.59, 24.86, 6.72]
    sim = [6.44, 6.53, 6.47, 6.51, 6.47, 6.26, 6.55, 6.39, 6.72]
    hdr(s, 0.9, 2.05, 8.9, 'Pertumbuhan tahunan data dan simulasi (%)')
    bar_chart(s, 0.9, 2.6, 8.9, 4.3, yrs, [('Data', dat), ('Simulasi (LPE 0,27726)', sim)], ['0B5E6E', 'FFD23B'], fmt_='0.0', legend=True, fs=10)
    rows = [['Tahun', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025'],
            ['Data'] + [pct(x, 2) for x in dat], ['Simulasi'] + [pct(x, 2) for x in sim]]
    tbl(s, 0.9, 7.05, 8.9, [1.3] + [0.844] * 9, rows, size=9.5, rowh=0.4, center=tuple(range(1, 10)), bold_first=True)
    pic_box(s, MED + 'image53.png', 10.1, 2.05, 9.0, 4.85)
    T(s, 10.1, 6.92, 9.0, 0.35, [[('Data sambungan vs simulasi LPE 0,27726 dan LPE* D-A 0,440 (Buku Gambar 50)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    card(s, 10.1, 7.35, 9.0, 1.75, None, [
        [('Model bergerak stabil 6,3–6,7%/th; data melonjak 2022–2024 (puncak 24,86%). ', 11, False, DARK)],
        [('Simulasi 2025: 26,5 juta vs data 40,7 juta (±35%). LPE 0,440 cocok untuk 2016–2019 tetapi tertinggal lagi sejak 2022. ', 11, False, DARK)],
        [('Keputusan: LPE dan LPD dipertahankan; tidak dikalibrasi.', 11.5, True, TEAL)]], size=11)
    src(s, 'Sumber: Buku Subbab 4.6.4 (Tabel 54, Gambar 50). Nasional: perjalanan wisnus 2024 naik 21,61%.')


def F_ringkasan(D):
    s = D.slide('Lampiran · Ringkasan Kalibrasi Tahap 0–4')
    sub(s, 'Dari tiga parameter yang benar-benar dikalibrasi, tidak satu pun berubah nilai; hanya koreksi Tahap 0 yang dibawa')
    rows = [['Tahap', 'Subsistem', 'Parameter', 'Rentang', 'Nilai turunan', 'Optimum', 'Alasan', 'Keputusan final'],
            ['0', 'Wisatawan', 'LPE, LPD', 'Koreksi penurunan', '0,26864 / 0,20148¹', '0,27726 / 0,207945', 'Selaraskan dengan Euler', 'Diperbarui (BASE 2050 +1,6%)'],
            ['1', 'Akomodasi', 'TPK Ambang', '0,20–0,35', '0,275', '0,350', 'Optimum di batas; gagal generalisasi', 'Dipertahankan 0,275'],
            ['1', 'Akomodasi', 'Laju Demolisi Dasar', '0,02–0,08', '0,05', '0,0600', 'Sama seperti di atas', 'Dipertahankan 0,05'],
            ['2', 'Lahan', 'Laju Konversi Dasar', '0,0034–0,0851 (CI 95%)', '0,0436052', '0,0638662', 'Awalnya memenuhi R4', 'Ditolak di Tahap 4'],
            ['3', 'Wisatawan', 'LPE, LPD', 'Diagnostik', '0,27726 / 0,207945', 'Tidak teridentifikasi (punggung 0,26–0,80)', 'Hanya selisih bersih yang terbaca', 'Dipertahankan'],
            ['4', 'Lahan', 'Konversi hasil Tahap 2', '—', 'v2: 0,0436052', 'v3: 0,0638662', 'Lahan uji penuh rasio 1,32 > 1,05', 'Kembali ke 0,0436052']]
    hl = {(1, 7): GREEN, (2, 7): LIGHT, (3, 7): LIGHT, (4, 7): PINK, (5, 7): LIGHT, (6, 7): PINK}
    tbl(s, 0.9, 2.05, 18.2, [0.8, 1.6, 2.4, 2.4, 2.2, 2.9, 3.0, 2.9], rows, size=10.5, rowh=0.72, center=(0,), hl=hl, bold_first=True)
    T(s, 0.9, 7.25, 18.2, 0.3, [[('¹ Nilai sebelum koreksi penurunan.', 10, False, GREY, True)]])
    flow(s, 0.9, 7.7, 18.2, 1.3, [('Tahap 1', 'artefak data 2018/2019'), ('Tahap 2–4', 'artefak rancangan uji'), ('Tahap 3', 'rezim di luar batas model'), ('Hasil', 'nilai turunan data sudah layak')],
         fills=[LIGHT, LIGHT, LIGHT, TEAL], size=12)
    src(s, 'Sumber: Buku Subbab 4.6.5 (Tabel 55).')
