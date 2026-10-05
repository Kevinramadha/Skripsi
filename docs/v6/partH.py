# ===================== H. SKENARIO KEBIJAKAN =====================
KPI_RUNS = _json.load(open('/tmp/pptwork/v6/kpi_runs.json')) if '_json' in globals() else __import__('json').load(open('/tmp/pptwork/v6/kpi_runs.json'))
SC = {'S1 BAU': 'BAU', 'S2 Sustainable': 'Sustainable', 'S3 Development Priority': 'Dev. Priority'}


def H_tuas(D):
    s = D.slide('Lampiran · Penetapan Tuas Kebijakan dan Rancangan Skenario')
    sub(s, 'Tuas harus lolos tiga kriteria sekaligus; skenario disusun sebagai paket kebijakan')
    K = [('1 · Relevansi struktural', 'Terbukti memengaruhi perilaku model pada analisis sensitivitas.'),
         ('2 · Dasar kebijakan', 'Ada peraturan/dokumen perencanaan: Perda DIY 1/2012 (pembukaan lahan bagi investor) dan Perda DIY 6/2021 (larangan alih fungsi lahan pangan).'),
         ('3 · Keterkendalian', 'Pemerintah punya instrumennya: perizinan dan insentif fiskal; zonasi dan moratorium izin.')]
    for k, (a, b) in enumerate(K):
        x = 0.9 + k * 6.15
        box(s, x, 2.05, 5.9, 1.5, fill=LIGHT, line=LINE, margin=0.18, anchor=MSO_ANCHOR.MIDDLE, paras=[[(a, 13, True, TEAL)], [(b, 11, False, DARK)]])
    T(s, 0.9, 3.65, 18.2, 0.4, [[('Parameter yang hanya memenuhi kriteria 1 (mis. perilaku wisatawan, bobot indeks) tidak dijadikan tuas, tetapi diuji sebagai sumber ketidakpastian pada uji kekokohan.', 11, False, GREY, True)]])
    rows = [['Skenario', 'Insentif Kebijakan', 'Konservasi Lahan', 'Tafsir kebijakan'],
            ['Business-as-Usual (BAU)', '0', '0', 'Tanpa insentif tambahan; kebutuhan lahan fasilitas pariwisata dipenuhi lewat konversi seperti pola historis'],
            ['Sustainable', '0,1', '1,0', 'Dorongan investasi terbatas; kebutuhan lahan fasilitas pariwisata dipenuhi tanpa konversi tambahan'],
            ['Development Priority (DP)', '0,3', '0', 'Ekspansi investasi agresif tanpa pengendalian kebutuhan lahan pariwisata']]
    tbl(s, 0.9, 4.15, 11.6, [2.8, 1.6, 1.6, 5.6], rows, size=11, rowh=0.62, center=(1, 2), bold_first=True, hl={(2, 0): GREEN, (3, 0): YEL_L})
    card(s, 0.9, 6.85, 11.6, 2.25, 'Tiga lapis penetapan nilai tuas', [
        ('Ada instrumennya?', 'dijawab peraturan dan dokumen perencanaan.'),
        ('Besarannya wajar?', 'dijawab variabilitas historis besaran tersebut.'),
        ('Intensitas antarskenario beda?', 'dijawab bentuk respons model pada analisis sensitivitas.'),
        [('Nilai 0,1; 0,3; 1,0 adalah ketetapan peneliti, bukan target resmi pemerintah.', 11, True, RED)]], size=10.5)
    hdr(s, 12.8, 4.15, 6.3, 'Rumus tuas dalam model')
    formula(s, 12.8, 4.7, 6.3, 1.9, ['Investasi = PDRB × r_I × (1 + Insentif)',
                                      'Konversi pariwisata = (Konstr.·a_H + Pemb.ODTW·a_O) × (1 − Konservasi) × RDDL ÷ RDDL_ref'], size=11.5)
    hdr(s, 12.8, 6.85, 6.3, 'Dekomposisi (analisis pendukung)')
    formula(s, 12.8, 7.4, 6.3, 1.7, ['Kontribusi tuas = Keluaran_D − Keluaran_BAU', 'Interaksi = Selisih paket − (Kontr. Insentif + Kontr. Konservasi)'], size=11.5)
    src(s, 'Sumber: Buku Subbab 3.8.1–3.8.2 dan 4.8.1 (Tabel 58).')


def H_indikator(D):
    s = D.slide('Lampiran · Indikator Kinerja dan Aturan Pelaporan Skenario')
    sub(s, 'Sepuluh indikator dalam tiga dimensi keberlanjutan (triple bottom line) ditambah satu indikator skala')
    rows = [['Dimensi', 'Indikator', 'Variabel model', 'Arah', 'Ambang'],
            ['Ekonomi', 'Lapangan kerja pariwisata', 'Tenaga Kerja Pariwisata', 'Maksimum', '—'],
            ['', 'Nilai tambah pariwisata', 'PDRB Sektor Pariwisata', 'Maksimum', '—'],
            ['', 'Investasi kumulatif', 'Akumulasi Investasi', 'Deskriptif', '—'],
            ['', 'Okupansi akomodasi', 'TPK', 'Deskriptif', '—'],
            ['Lingkungan', 'Lahan tersedia untuk konservasi', 'Rasio Daya Dukung Lahan', 'Maksimum', '> 0,331'],
            ['', 'Luas lahan terbangun', 'Lahan Terbangun', 'Minimum', '—'],
            ['', 'Konversi lahan pariwisata kumulatif', 'Akumulasi Konversi Pariwisata', 'Minimum', '—'],
            ['Sosial', 'Indeks kepadatan', 'Kepadatan ÷ Kepadatan Referensi', 'Minimum', '< 2,0'],
            ['', 'Kualitas destinasi', 'Daya Tarik Destinasi Wisata', 'Maksimum', '—'],
            ['Skala', 'Jumlah wisatawan', 'Jumlah Wisatawan', 'Dilaporkan', '—']]
    tbl(s, 0.9, 2.05, 10.6, [1.6, 3.4, 3.4, 1.2, 1.0], rows, size=10.5, rowh=0.5, center=(3, 4), bold_first=True, hl={(5, 4): YEL_L, (8, 4): YEL_L})
    card(s, 11.8, 2.05, 7.3, 2.45, 'Dasar dua ambang', [
        ('RDDL > 0,331:', 'luas Kawasan Pertanian Pangan Berkelanjutan (Perda DIY 6/2021) dibagi luas DIY. Tolok ukur luas, bukan pengendalian spasial.'),
        ('Kepadatan < 2,0:', 'dua kali kepadatan 2025 sebagai sinyal kepadatan berlebih; tidak ada patokan baku, jadi dinyatakan sebagai batasan peneliti.')], size=10.5)
    card(s, 11.8, 4.6, 7.3, 1.75, 'Aturan pelaporan', [
        'Tiap indikator dilaporkan sebagai nilai 2050 dan selisih % terhadap BAU (BAU = pembanding, bukan terbaik/terburuk).',
        'Hanya indikator berarah maks/min yang diperingkat.'], size=10.5)
    card(s, 11.8, 6.45, 7.3, 2.65, 'Tiga larangan', [
        ('1.', 'Tidak menyebut "skenario terbaik" tanpa menyebut dimensinya.'),
        ('2.', 'Tidak membuat skor gabungan atau bobot antarindikator (itu keputusan kebijakan).'),
        ('3.', 'Angka 2050 bukan ramalan, hanya dasar perbandingan.')], size=10.5, fill=PINK, line='F3B9B0')
    src(s, 'Sumber: Buku Subbab 3.8.3 (Tabel 21) dan 4.8.2 (Tabel 59).')


def H_hasil(D):
    s = D.slide('Lampiran · Hasil Perbandingan Skenario Lengkap, Tahun 2050')
    sub(s, 'Development Priority unggul di ekonomi, Sustainable unggul di lingkungan, BAU unggul di kepadatan')
    R = [('Ekonomi', 'Lapangan kerja pariwisata (jiwa)', '650.355', '667.458', '697.021', 2.63, 7.18, 'Maks', '3 · 2 · 1'),
         ('', 'PDRB pariwisata (miliar Rp)', '40.061', '41.194', '43.152', 2.83, 7.71, 'Maks', '3 · 2 · 1'),
         ('', 'Investasi kumulatif 2025–2050 (miliar Rp)', '37.318', '41.550', '50.133', 11.34, 34.34, 'Deskriptif', '—'),
         ('', 'TPK 2050', '0,3584', '0,3537', '0,3458', -1.30, -3.50, 'Deskriptif', '—'),
         ('Lingkungan', 'Rasio daya dukung lahan', '0,6145', '0,6180', '0,6140', 0.57, -0.09, 'Maks (> 0,331)', '2 · 1 · 3'),
         ('', 'Lahan terbangun (ha)', '122.208', '121.094', '122.377', -0.91, 0.14, 'Min', '2 · 1 · 3'),
         ('', 'Konversi lahan pariwisata kumulatif (ha)', '947,0', '0,0', '1.095,1', -100.0, 15.64, 'Min', '2 · 1 · 3'),
         ('Sosial', 'Indeks kepadatan', '2,3638', '2,4307', '2,5462', 2.83, 7.71, 'Min (< 2,0)', '1 · 2 · 3'),
         ('', 'Daya tarik destinasi', '0,8132', '0,8205', '0,8322', 0.89, 2.33, 'Maks', '3 · 2 · 1'),
         ('Skala', 'Jumlah wisatawan (kunjungan)', '96.197.154', '98.917.127', '103.618.412', 2.83, 7.71, 'Dilaporkan', '—'),
         ('Pelengkap', 'Jumlah hotel (unit)', '5.404', '5.631', '6.033', 4.19, 11.63, 'Deskriptif', '—'),
         ('', 'Jumlah ODTW (unit)', '367', '394', '449', 7.33, 22.22, 'Deskriptif', '—')]
    rows = [['Dimensi', 'Indikator', 'BAU', 'Sustainable', 'Dev. Priority', 'Sust. vs BAU', 'DP vs BAU', 'Arah', 'Peringkat (BAU·S·DP)']]
    hl = {}
    for i, r in enumerate(R, 1):
        rows.append(list(r[:5]) + [pct(r[5], 2, True), pct(r[6], 2, True), r[7], r[8]])
        if r[8] != '—':
            best = r[8].split(' · ').index('1')
            hl[(i, 2 + best)] = GREEN
    tbl(s, 0.9, 2.05, 18.2, [1.6, 4.4, 1.7, 1.7, 1.8, 1.7, 1.6, 1.7, 2.0], rows, size=10.5, rowh=0.47, hl=hl, center=tuple(range(2, 9)))
    note(s, 'Sel hijau = skenario terbaik pada indikator berperingkat. Untuk indikator berarah minimum, selisih negatif berarti lebih baik. Tidak ada skenario yang unggul di ketiga dimensi sekaligus.', y=8.35, h=0.8)
    src(s, 'Sumber: Buku Subbab 4.8.3 (Tabel 60); hasil_simulasi_skenario.xlsx (Tabel 2 KPI, Tabel 3 Peringkat). Hotel dan ODTW dari indikator pelengkap.')


SKG = [(60, 'Jumlah Wisatawan', 57, 'DP tertinggi (103,6 juta), disusul Sustainable (98,9 juta) dan BAU (96,2 juta). Garis berpisah perlahan karena insentif bekerja lewat investasi → ODTW → Daya Tarik.'),
       (61, 'PDRB Sektor Pariwisata', 58, 'Polanya sama dengan wisatawan karena PDRB sebanding dengan jumlah wisatawan: DP +7,71%, Sustainable +2,83% terhadap BAU.'),
       (62, 'Rasio Daya Dukung Lahan', 59, 'Ketiga skenario turun dari 0,826 ke ±0,614 dan tetap jauh di atas ambang 0,331. Sustainable sedikit lebih tinggi (0,6180).'),
       (63, 'Lahan Terbangun', 60, 'Ketiga garis hampir berhimpit: Sustainable hanya 0,91% lebih rendah, karena konversi non-pariwisata tetap berjalan.'),
       (64, 'Indeks Kepadatan', 61, 'Ambang 2,0 terlampaui di semua skenario: DP 2041, Sustainable 2042, BAU 2043. Tuas hanya menggeser waktunya ±2 tahun.')]


def H_grafik(D):
    pages = [SKG[:3], SKG[3:]]
    for pi, pg in enumerate(pages):
        s = D.slide(f'Lampiran · Grafik Skenario 2025–2050 ({pi + 1}/2)')
        sub(s, 'Lintasan tiga skenario: Business-as-Usual, Sustainable, dan Development Priority')
        for j, (im, t_, g, ex) in enumerate(pg):
            x = 0.9 + j * 6.15; w = 5.9
            hdr(s, x, 2.05, w, t_, f'Buku Gambar {g}')
            pic_box(s, MED + f'image{im}.png', x, 2.6, w, 3.6)
            box(s, x, 6.35, w, 2.0, fill=LIGHT, line=LINE, margin=0.18, anchor=MSO_ANCHOR.MIDDLE, paras=[[(ex, 11.5, False, DARK)]])
        if pi == 1:
            x = 0.9 + 2 * 6.15
            hdr(s, x, 2.05, 5.9, 'Tahun ambang kepadatan 2,0 terlampaui')
            rows = [['Skenario', 'Tahun', 'Indeks 2050'], ['Development Priority', '2041', '2,5462'], ['Sustainable', '2042', '2,4307'], ['BAU', '2043', '2,3638']]
            tbl(s, x, 2.6, 5.9, [2.7, 1.4, 1.8], rows, size=11.5, rowh=0.55, center=(1, 2), bold_first=True)
            card(s, x, 4.95, 5.9, 3.4, 'Artinya', [
                'Kedua tuas bekerja di sisi penawaran (investasi dan lahan), sedangkan kepadatan ditentukan permintaan.',
                'Mengendalikan kepadatan butuh instrumen sisi permintaan, misalnya pengaturan sebaran kunjungan antarwaktu dan antarlokasi, yang di luar cakupan model.'], size=11)
        src(s, 'Sumber: Buku Subbab 4.8.3 (Gambar 57–61); hasil_simulasi_skenario.xlsx (Tahun Ambang Kepadatan).')


def H_komposisi(D):
    s = D.slide('Lampiran · Komposisi Indeks Daya Tarik dan Dekomposisi Tuas')
    sub(s, 'Kenapa Daya Tarik tertinggi di DP, dan seberapa besar sumbangan masing-masing tuas pada paket Sustainable')
    hdr(s, 0.9, 2.05, 7.6, 'Komposisi Daya Tarik 2050')
    cd = CategoryChartData(); cd.categories = ['BAU', 'Sustainable', 'Dev. Priority']
    for nm, v in [('ODTW', [0.4793, 0.4896, 0.5090]), ('Kepadatan', [0.1481, 0.1440, 0.1375]), ('Daya dukung lahan', [0.1859, 0.1870, 0.1857])]:
        cd.add_series(nm, v)
    ch = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_STACKED, Inches(0.9), Inches(2.6), Inches(7.6), Inches(3.9), cd).chart
    ch.has_title = False; ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout = False; ch.font.size = Pt(10); ch.font.name = F
    pl = ch.plots[0]; pl.gap_width = 60; pl.overlap = 100
    for sr, col in zip(pl.series, ['0B5E6E', 'E4604F', 'FFD23B']):
        sr.format.fill.solid(); sr.format.fill.fore_color.rgb = rgb(col)
    pl.has_data_labels = True; pl.data_labels.number_format = '0.0000'; pl.data_labels.number_format_is_linked = False; pl.data_labels.font.size = Pt(9)
    rows = [['', 'BAU', 'Sust.', 'DP'], ['Total Daya Tarik', '0,8132', '0,8205', '0,8322']]
    tbl(s, 0.9, 6.6, 7.6, [2.8, 1.6, 1.6, 1.6], rows, size=11, rowh=0.42, center=(1, 2, 3), bold_first=True)
    box(s, 0.9, 7.55, 7.6, 1.55, fill=YEL_L, line=YEL, margin=0.18, anchor=MSO_ANCHOR.MIDDLE, paras=[[
        ('Komponen ODTW di DP naik 0,0297, jauh melebihi turunnya kepadatan (0,0106) dan lahan (0,0002). RDDL masih ±0,614, jadi rem lahan belum terasa sampai 2050.', 11, False, DARK)]])
    hdr(s, 8.8, 2.05, 10.3, 'Dekomposisi paket Sustainable terhadap BAU')
    rows = [['Indikator', 'Insentif saja', 'Konservasi saja', 'Paket', 'Interaksi'],
            ['Lapangan kerja (jiwa)', '+15.526', '+1.459', '+17.103', '+118'],
            ['PDRB (miliar Rp)', '+1.026', '+98', '+1.133', '+8'],
            ['Investasi kumulatif (miliar Rp)', '+4.190', '+35', '+4.232', '+6'],
            ['TPK', '−0,00486', '+0,00019', '−0,00467', '0,00000'],
            ['RDDL', '−0,00018', '+0,00351', '+0,00351', '+0,00018'],
            ['Lahan terbangun (ha)', '+57,6', '−1.114,0', '−1.114,0', '−57,6'],
            ['Konversi pariwisata (ha)', '+50,1', '−947,0', '−947,0', '−50,1'],
            ['Indeks kepadatan', '+0,0606', '+0,0058', '+0,0668', '+0,0005'],
            ['Daya tarik', '+0,0064', '+0,0008', '+0,0073', '+0,0001'],
            ['Jumlah wisatawan', '+2.464.305', '+235.896', '+2.719.973', '+19.773'],
            ['Jumlah hotel (unit)', '+214,6', '+10,4', '+226,2', '+1,2'],
            ['Jumlah ODTW (unit)', '+26,6', '+0,3', '+26,9', '+0,05']]
    hl = {}
    for r in (1, 2, 3, 8, 9, 10, 11, 12): hl[(r, 1)] = LIGHT
    for r in (5, 6, 7): hl[(r, 2)] = GREEN
    hl[(6, 4)] = YEL_L; hl[(7, 4)] = YEL_L
    tbl(s, 8.8, 2.6, 10.3, [3.3, 1.8, 1.8, 1.8, 1.6], rows, size=10, rowh=0.41, center=(1, 2, 3, 4), hl=hl, bold_first=True)
    T(s, 8.8, 8.05, 10.3, 1.05, [[('Insentif menggerakkan ekonomi, konservasi menggerakkan lahan; interaksi kecil (±0,7% untuk wisatawan). Pada lahan, interaksi −57,6 ha persis menetralkan tambahan +57,6 ha dari insentif: konversi pariwisata tetap nol tanpa mengorbankan pertumbuhan.', 11, False, DARK)]])
    src(s, 'Sumber: Buku Subbab 4.8.3 (Tabel 61) dan 4.8.4 (Tabel 62); hasil_simulasi_skenario.xlsx (Komposisi Daya Tarik, Tabel 4 Dekomposisi).')


def H_kokoh(D):
    s = D.slide('Lampiran · Kekokohan Peringkat Skenario (1/2): Kondisi dan Hasil')
    sub(s, 'Tiga skenario dijalankan pada tujuh kondisi parameter; kokoh bila urutan tidak berubah di semua kondisi')
    rows = [['Kode', 'Kondisi parameter', 'Alasan dipilih'],
            ['C0', 'Nilai final', 'Acuan'],
            ['C1', 'Rasio LPD/LPE = 0,65', 'Ketidakpastian terbesar (lebar 153,57 poin); tidak teridentifikasi'],
            ['C2', 'Rasio LPD/LPE = 0,90', 'Ujung atas rentang yang sama'],
            ['C3', 'Bobot ODTW/Kepadatan/Lahan = 0,50/0,25/0,25', 'Lebar 48,10 poin'],
            ['C4', 'Bobot = 0,30/0,45/0,25', 'Kombinasi alternatif bobot'],
            ['C5', 'Laju Konversi Dasar = 0,0034118', 'Batas bawah CI 95% (lebar lahan 115,70 poin)'],
            ['C6', 'Laju Konversi Dasar = 0,0851069', 'Batas atas CI 95%']]
    tbl(s, 0.9, 2.05, 8.9, [0.8, 3.9, 4.2], rows, size=10.5, rowh=0.5, center=(0,), bold_first=True)
    rows2 = [['Indikator', 'Urutan pada C0–C6', 'Status'],
             ['Lapangan kerja pariwisata', 'DP > Sustainable > BAU', 'KOKOH'], ['PDRB pariwisata', 'DP > Sustainable > BAU', 'KOKOH'],
             ['Daya tarik destinasi', 'DP > Sustainable > BAU', 'KOKOH'], ['Rasio daya dukung lahan', 'Sustainable > BAU > DP', 'KOKOH'],
             ['Lahan terbangun', 'Sustainable > BAU > DP', 'KOKOH'], ['Konversi lahan pariwisata', 'Sustainable > BAU > DP', 'KOKOH'],
             ['Indeks kepadatan', 'BAU > Sustainable > DP', 'KOKOH']]
    tbl(s, 10.1, 2.05, 9.0, [3.4, 3.9, 1.7], rows2, size=10.5, rowh=0.5, center=(2,), bold_first=True, hl={(r, 2): GREEN for r in range(1, 8)})
    card(s, 0.9, 6.3, 18.2, 2.0, 'Membaca kekokohan', [
        ('Yang kokoh adalah urutan, bukan angka.', 'Contoh: wisatawan BAU 2050 berkisar 53,4 juta (C2) sampai 154,9 juta (C1), tetapi urutan DP > Sustainable > BAU selalu sama.'),
        ('Kenapa bertahan?', 'Ketiga kelompok indikator digerakkan tuas yang berbeda di jalur yang hampir terpisah (lihat dekomposisi).'),
        ('Konsekuensi:', 'kesimpulan "tidak ada skenario yang unggul di ketiga dimensi" bukan artefak pilihan parameter; tetapi angka proyeksinya tetap bukan ramalan.')], size=11)
    src(s, 'Sumber: Buku Subbab 3.8.4 dan 4.8.5 (Tabel 63); hasil_simulasi_skenario.xlsx (Tabel 5 Kekokohan).')


def H_kokoh2(D):
    s = D.slide('Lampiran · Kekokohan Peringkat Skenario (2/2): Nilai 2050 per Kondisi')
    sub(s, 'Nilai indikator tahun 2050 untuk 21 simulasi (7 kondisi × 3 skenario); sel hijau = terbaik pada kondisi itu')
    R = [r for r in KPI_RUNS[1:] if r[1] in SC]
    rows = [['Kondisi', 'Skenario', 'TK (ribu)', 'PDRB (miliar Rp)', 'Daya Tarik', 'RDDL', 'Lahan (ha)', 'Konversi pariwisata (ha)', 'Indeks kepadatan', 'Wisatawan (juta)']]
    hl = {}
    best = {2: max, 3: max, 4: max, 5: max, 6: min, 7: min, 8: min}
    for i, r in enumerate(R, 1):
        kond = r[0].split(' ', 1)
        rows.append([r[0] if r[1] == 'S1 BAU' else '', SC[r[1]], fmt(r[4] / 1000, 2), fmt(r[5], 0), fmt(r[12], 4), fmt(r[8], 4), fmt(r[9], 0), fmt(r[10], 1), fmt(r[11], 4), fmt(r[13] / 1e6, 2)])
    for g in range(0, len(R), 3):
        grp = R[g:g + 3]
        for c, (src_i, f_) in zip(range(2, 9), [(4, max), (5, max), (12, max), (8, max), (9, min), (10, min), (11, min)]):
            vals = [x[src_i] for x in grp]
            bi = vals.index(f_(vals))
            hl[(g + 1 + bi, c)] = GREEN
    tbl(s, 0.9, 2.05, 18.2, [3.4, 1.7, 1.5, 1.7, 1.4, 1.4, 1.7, 2.0, 1.7, 1.7], rows, size=9.5, rowh=0.33, hl=hl, center=tuple(range(2, 10)))
    src(s, 'Sumber: hasil_simulasi_skenario.xlsx (sheet KPI seluruh run). Pada C6 (konversi tinggi) RDDL turun ke ±0,36, masih di atas ambang 0,331.')


def H_implikasi(D):
    s = D.slide('Lampiran · Implikasi Kebijakan Lengkap')
    sub(s, 'Hasil simulasi tidak memberi satu rekomendasi tunggal, tetapi memetakan pertukaran yang harus dipilih')
    I = [('1', 'Prioritas harus dipilih', 'Tidak ada pilihan yang unggul di semua dimensi.',
          'Prioritas ekonomi → DP: TK +7,18%, PDRB +7,71%, tetapi konversi lahan pariwisata +15,64% dan kepadatan tertinggi. Prioritas ruang → Sustainable: konversi pariwisata 0 ha dan ekonomi tetap di atas BAU (+2,63% TK).'),
         ('2', 'Kendali lahan sektor pariwisata terbatas', 'Konservasi menihilkan konversi pariwisata, tetapi lahan terbangun total hanya turun 0,91%.',
          'Konversi pariwisata hanya ±23 ha/th dari ±2.000 ha/th total konversi; sisanya non-pariwisata tetap berjalan. Pengendalian ruang perlu keterpaduan lintas sektor.'),
         ('3', 'Kepadatan tidak teratasi kedua tuas', 'Ambang 2,0 terlampaui 2041–2043 di semua skenario; selisih hanya 2 tahun.',
          'Tuas bekerja di sisi penawaran, kepadatan ditentukan permintaan. Perlu instrumen sisi permintaan: sebaran kunjungan antarwaktu dan antarlokasi.'),
         ('4', 'Ada ketegangan antardokumen kebijakan', 'Perda DIY 1/2012 (lahan baru bagi investor) vs Perda DIY 6/2021 (larangan alih fungsi lahan pangan).',
          'Perbandingan DP dan Sustainable memotret ketegangan ini secara kuantitatif.')]
    for k, (n, t_, a, b) in enumerate(I):
        x = 0.9 + (k % 2) * 9.25; y = 2.05 + (k // 2) * 3.2; w = 8.95
        num(s, x, y + 0.05, int(n), d=0.6, size=16)
        T(s, x + 0.75, y, w - 0.75, 0.6, [[(t_, 15, True, TEAL)]], anchor=MSO_ANCHOR.MIDDLE)
        box(s, x, y + 0.7, w, 0.85, fill=YEL_L, line=None, margin=0.15, anchor=MSO_ANCHOR.MIDDLE, paras=[[(a, 11.5, True, DARK)]])
        box(s, x, y + 1.6, w, 1.35, fill=LIGHT, line=LINE, margin=0.15, anchor=MSO_ANCHOR.MIDDLE, paras=[[(b, 11, False, DARK)]])
    note(s, 'Karena urutan skenario kokoh terhadap asumsi paling tidak pasti, implikasi ini layak menjadi bahan diskusi bagi Pemda DIY dan Dinas Pariwisata; angka absolutnya tetap dibaca sebagai perbandingan, bukan ramalan.', y=8.6, h=0.85)
    src(s, 'Sumber: Buku Subbab 4.8.6.')
