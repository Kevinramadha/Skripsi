# ===================== D. UJI STRUKTUR =====================
EDIR = REPO + 'Pengujian Model Sistem Dinamis/[02] Uji Perilaku/Kalibrasi/'


def D_alur(D):
    s = D.slide('Lampiran · Tahapan Uji Struktur: Gambaran Umum')
    sub(s, 'Enam uji dijalankan berurutan sebelum uji perilaku (Barlas, 1996; Sterman, 2000)')
    rows = [['No', 'Uji', 'Yang diperiksa', 'Cara / langkah', 'Kriteria lolos', 'Hasil'],
            ['1', 'Kesesuaian struktur dan parameter', 'Setiap hubungan sebab-akibat dan parameter punya dasar', 'Telusuri tiap variabel terhadap kriteria Tabel 11 dan kategori sumber Tabel 12', 'Semua hubungan berdasar teori/data; tiap parameter masuk satu kategori', 'Lolos'],
            ['2', 'Konsistensi dimensi', 'Satuan di kiri dan kanan setiap persamaan sama', 'Vensim: Units Check lalu Check Model', 'Tidak ada peringatan satuan', 'Lolos'],
            ['3', 'Kecukupan batas model', 'Apa yang dihitung model, apa yang jadi input, apa yang dikeluarkan', 'Susun model boundary chart beserta konsekuensi tiap aspek yang dikeluarkan', 'Variabel penting untuk pertanyaan penelitian sudah endogen', 'Lolos'],
            ['4', 'Kekekalan materi', 'Isi stok hanya berubah lewat aliran yang didefinisikan', 'Bandingkan Sₖ(t+1) dengan Sₖ(t) + masuk − keluar, 2025–2049, lima stok', 'Selisih relatif < 10⁻⁹', 'Lolos'],
            ['5', 'Loop umpan balik', 'Setiap loop CLD benar-benar bekerja sesuai arah', 'Matikan satu loop (tahan variabel penutupnya), bandingkan nilai 2050 dengan simulasi dasar', 'Arah perubahan sesuai jenis loop', 'Lolos'],
            ['6', 'Kondisi ekstrem', 'Model tetap logis pada nilai parameter ekstrem', '17 uji; hipotesis ditulis sebelum simulasi; periksa 6 aturan fisik', 'Keenam aturan terpenuhi dan hipotesis sesuai', '15 lolos, 2 lolos dengan catatan'],
            ['7', 'Galat integrasi', 'Hasil tidak bergantung pada ukuran langkah waktu', 'Jalankan ulang pada Δt 0,5; 0,25; 0,125 tahun', 'Selisih kecil dan mengecil teratur', 'Lolos (Δt = 1 memadai)']]
    hl = {(r, 5): GREEN for r in range(1, 8)}
    hl[(6, 5)] = YEL_L
    tbl(s, 0.9, 2.05, 18.2, [0.6, 2.8, 3.9, 4.6, 3.9, 2.4], rows, size=10.5, rowh=0.82, hl=hl, center=(0, 5))
    note(s, 'Uji 1–2 memeriksa bahan penyusun model, uji 3 menetapkan ranah tafsir, uji 4–5 memeriksa mekanisme di dalam model, dan uji 6–7 memeriksa ketahanan model pada kondisi di luar kebiasaan.', y=9.0, h=0.8)
    src(s, 'Sumber: Buku Subbab 3.7.4 dan 4.4.')


def D_dimensi(D):
    s = D.slide('Lampiran · Uji Kesesuaian Struktur dan Konsistensi Dimensi')
    sub(s, 'Langkah pengujian dan tampilan hasil pemeriksaan di Vensim')
    hdr(s, 0.9, 2.05, 6.3, 'Kesesuaian struktur dan parameter')
    steps(s, 0.9, 2.65, 6.3, [('Telusuri hubungan', 'Setiap panah CLD/SFD dicek terhadap kriteria evaluasi struktural (Tabel 11).'),
                              ('Golongkan parameter', '35 parameter: 11 data resmi, 8 identitas stok-aliran, 2 regulasi, 8 asumsi, 6 normalisasi/tuas.'),
                              ('Dokumentasikan', 'Nilai, rumus, dasar, dan rujukan tiap parameter dicatat (lampiran parameter).')], h=1.0, size=11)
    hdr(s, 0.9, 6.05, 6.3, 'Konsistensi dimensi')
    formula(s, 0.9, 6.65, 6.3, 0.95, ['[Aliran] = [Stok] / [Waktu]', ('contoh: Laju Kedatangan (kunjungan/tahun)', '  = Jumlah Wisatawan (kunjungan) × LPE (1/tahun)')], size=12)
    bullets(s, 0.9, 7.75, 6.3, 1.3, ['Model → Units Check: memeriksa satuan semua persamaan.', 'Model → Check Model: memeriksa persamaan yang belum lengkap atau keliru.', 'Hasil: tidak ada peringatan satuan maupun persamaan.'], size=11)
    pic_box(s, MED + 'image9.png', 7.5, 2.05, 3.6, 3.6)
    T(s, 7.5, 5.7, 3.6, 0.35, [[('Menu Units Check & Check Model', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    pic_box(s, MED + 'image18.png', 11.3, 2.05, 7.8, 3.6)
    pic_box(s, MED + 'image19.png', 11.3, 5.75, 7.8, 3.3)
    T(s, 11.3, 9.08, 7.8, 0.35, [[('Hasil Units Check (atas) dan Check Model (bawah): model OK', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    src(s, 'Sumber: Buku Subbab 3.7.4 (Gambar 8) dan 4.4.1 (Gambar 16).')


def D_kekekalan(D):
    s = D.slide('Lampiran · Uji Kekekalan Materi')
    sub(s, 'Isi setiap stok hanya boleh berubah lewat aliran masuk dan keluar yang sudah didefinisikan')
    formula(s, 0.9, 2.05, 8.6, 1.5, ['Sₖ(t+1) = Sₖ(t) + Σ Inflowₖ(t) − Σ Outflowₖ(t)',
                                      'Selisih relatif = maks |Sₖ,simulasi − Sₖ,hitung| ÷ rata-rata Sₖ',
                                      ('Kriteria: kekal bila selisih relatif < 10⁻⁹', '  (sisa pembulatan komputer)')], title='Rumus', size=12.5)
    card(s, 9.8, 2.05, 9.3, 1.5, 'Contoh hitung: Jumlah Hotel dan Akomodasi', [
        [('2.291 + 158,17937 − 114,55 = 2.334,62937 unit', 13, True, DARK)],
        [('stok 2025 + konstruksi − demolisi = stok 2026 hasil simulasi (2.334,62937) → selisih 0', 11, False, GREY)]])
    rows = [['Stok', 'Aliran masuk', 'Aliran keluar', 'Stok 2025', 'Hitung manual 2026', 'Simulasi 2026', 'Selisih maks 2025–2049', 'Status'],
            ['Jumlah Wisatawan', 'Laju Kedatangan', 'Laju Penurunan', '40.695.700*', '43.516.521,93', '43.516.521,93', '≈0 (10⁻⁸)', 'Kekal'],
            ['Jumlah Hotel dan Akomodasi', 'Laju Konstruksi', 'Laju Demolisi', '2.291', '2.334,63', '2.334,63', '0', 'Kekal'],
            ['Jumlah ODTW', 'Laju Pembangunan/Penambahan', 'Laju Penutupan', '201', '205,09', '205,09', '0', 'Kekal'],
            ['Tenaga Kerja Pariwisata', 'Laju Penyerapan', 'Laju Keluar', '364.994', '364.994,46', '364.994,46', '0', 'Kekal'],
            ['Lahan Terbangun', 'Konversi Pariwisata + Non-Pariwisata', '(tidak ada)', '55.029,5', '57.035,45', '57.035,45', '0', 'Kekal']]
    hl = {(r, 7): GREEN for r in range(1, 6)}
    tbl(s, 0.9, 3.85, 18.2, [3.2, 3.4, 2.0, 1.7, 2.2, 2.0, 2.2, 1.5], rows, size=11, rowh=0.62, hl=hl, center=(3, 4, 5, 6, 7), bold_first=True)
    note(s, 'Kelima stok kekal di seluruh periode: tidak ada isi stok yang muncul atau hilang tanpa lewat aliran. *Nilai awal wisatawan di berkas Vensim tercatat 40.695.700 (dibulatkan dari 40.695.654 BPS); pembulatan ini tidak memengaruhi pemeriksaan karena yang diuji adalah selisih antartahun.', y=8.0, h=1.05)
    src(s, 'Sumber: Buku Subbab 3.7.4 dan 4.4.3 (Tabel 40); hasil_uji_loop_dan_kekekalan.xlsx.')


def D_loop(D):
    s = D.slide('Lampiran · Uji Loop Umpan Balik (1/2): Rancangan dan Nilai 2050')
    sub(s, 'Satu loop dimatikan pada satu waktu dengan menahan variabel penutupnya pada nilai tahun dasar')
    rows = [['Loop dimatikan', 'Variabel ditahan', 'Yang diputus'],
            ['B1 kepadatan', 'Kepadatan Wisatawan', 'Wisatawan → Kepadatan → Daya Tarik'],
            ['B2 daya dukung lahan', 'Rasio Daya Dukung Lahan', 'Lahan → RDDL → Daya Tarik dan konversi'],
            ['R2 ekonomi–atraksi', 'Jumlah ODTW', 'Investasi → ODTW → Daya Tarik'],
            ['B3 okupansi hotel', 'Rasio Permintaan thd Kapasitas', 'Hotel → Rasio Permintaan → Konstruksi'],
            ['B4 goal-seeking TK', 'Tenaga Kerja Dibutuhkan', 'Selisih kebutuhan → Penyerapan'],
            ['Semua rem mati (R1 murni)', 'Daya Tarik = 1', 'Seluruh rem sekaligus']]
    tbl(s, 0.9, 2.05, 9.0, [2.7, 2.8, 3.5], rows, size=10.5, rowh=0.55, bold_first=True)
    formula(s, 10.2, 2.05, 8.9, 1.2, ['Selisih % = (X_mati,2050 − X_dasar,2050) ÷ X_dasar,2050 × 100%',
                                       ('Penggantian hanya saat simulasi dijalankan;', ' struktur model tidak diubah.')], title='Rumus', size=12.5)
    card(s, 10.2, 3.45, 8.9, 2.45, 'Cara membaca', [
        'Loop balancing (B) yang dimatikan seharusnya membuat pertumbuhan lebih cepat (selisih positif).',
        'Loop reinforcing (R) yang dimatikan seharusnya membuat pertumbuhan lebih lambat (selisih negatif).',
        'Loop dianggap berjangkauan luas bila mengubah lebih dari 1% pada banyak variabel.'], size=11)
    rows2 = [['Kondisi', 'Wisatawan (juta)', 'Hotel (unit)', 'ODTW (unit)', 'TK (ribu)', 'Lahan (ha)', 'Daya Tarik'],
             ['Simulasi dasar (semua loop aktif)', '96,20', '5.404', '367', '650,36', '122.208', '0,8132'],
             ['B1 kepadatan dimatikan', '250,32', '12.151', '528', '1.585,46', '123.070', '1,0696'],
             ['B2 daya dukung lahan dimatikan', '111,66', '6.081', '384', '745,26', '135.035', '0,8632'],
             ['R2 ekonomi–atraksi dimatikan', '80,24', '4.671', '201', '549,73', '122.109', '0,7635'],
             ['B3 okupansi dimatikan', '96,23', '4.867', '367', '650,56', '122.080', '0,8133'],
             ['B4 goal-seeking TK dimatikan', '96,20', '5.404', '367', '364,99', '122.208', '0,8132'],
             ['Semua rem mati (R1 murni)', '217,37', '10.885', '504', '1.399,44', '122.930', '1,0000']]
    tbl(s, 0.9, 6.2, 18.2, [5.2, 2.3, 2.1, 2.0, 2.1, 2.3, 2.2], rows2, size=11, rowh=0.42, center=(1, 2, 3, 4, 5, 6), hl={(1, c): LIGHT for c in range(7)}, bold_first=True)
    src(s, 'Sumber: Buku Subbab 3.7.4 (Tabel 16) dan 4.4.4 (Tabel 41).')


def D_loop2(D):
    s = D.slide('Lampiran · Uji Loop Umpan Balik (2/2): Selisih dan Grafik')
    sub(s, 'Setiap loop balancing yang dimatikan mempercepat pertumbuhan; mematikan R2 memperlambatnya')
    P = [('B1 kepadatan', [160.2152, 124.8335, 43.8541, 143.7843, 0.7056, 31.5224], '5 dari 6'),
         ('B2 daya dukung lahan', [16.0717, 12.5276, 4.5212, 14.5927, 10.4967, 6.148], '6 dari 6'),
         ('R2 ekonomi–atraksi', [-16.5899, -13.5778, -45.2677, -15.4722, -0.0808, -6.1154], '5 dari 6'),
         ('B3 okupansi', [0.0339, -9.9511, 0.0105, 0.0316, -0.1043, 0.0106], '1 dari 6'),
         ('B4 goal-seeking TK', [0, 0, 0, -43.8777, 0, 0], '1 dari 6'),
         ('Semua rem mati', [125.958, 101.4201, 37.2123, 115.1811, 0.5914, 22.9644], '5 dari 6')]
    rows = [['Loop dimatikan', 'Wisatawan', 'Hotel', 'ODTW', 'TK', 'Lahan', 'Daya Tarik', 'Berubah >1%']]
    hl = {}
    for i, (n, v, k) in enumerate(P, 1):
        rows.append([n] + [pct(x, 1, True) if abs(x) >= 0.05 else '0,0%' for x in v] + [k])
        for j, x in enumerate(v, 1):
            if x >= 1: hl[(i, j)] = GREEN
            elif x <= -1: hl[(i, j)] = PINK
    tbl(s, 0.9, 2.05, 10.4, [2.6, 1.15, 1.0, 1.0, 1.0, 0.95, 1.2, 1.5], rows, size=10.5, rowh=0.55, hl=hl, center=tuple(range(1, 8)), bold_first=True)
    T(s, 0.9, 5.95, 10.4, 0.3, [[('Hijau: naik >1% terhadap simulasi dasar · merah muda: turun >1%', 10, False, GREY, True)]])
    bullets(s, 0.9, 6.35, 10.4, 2.6, [('B1 paling kuat:', 'tanpa rem kepadatan wisatawan 2050 naik 160%.'),
                                       ('R2 terasa paling besar di ODTW', '(−45,3%), sesuai perannya sebagai jalur investasi → atraksi.'),
                                       ('B2 menyentuh semua variabel', 'karena lahan dipakai bersama oleh akomodasi, atraksi, dan kepadatan.'),
                                       ('B3 dan B4 bersifat lokal:', 'hanya mengubah hotel (−10,0%) dan TK (−43,9%).')], size=11.5)
    pic_box(s, MED + 'image20.png', 11.6, 2.05, 7.5, 4.3)
    T(s, 11.6, 6.4, 7.5, 0.35, [[('Lintasan Jumlah Wisatawan 2025–2050 pada keenam kondisi (Buku Gambar 17)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    card(s, 11.6, 6.85, 7.5, 2.15, 'Membaca grafik', [
        'Awal simulasi: semua garis berhimpit karena R1 dan R2 masih dominan.',
        'Jangka panjang: B1 menjadi penentu utama lintasan.',
        'B1 dimatikan (250,32 juta) > semua rem mati (217,37 juta) karena R2 masih aktif menaikkan Daya Tarik ke 1,0696.'], size=10.5)
    src(s, 'Sumber: Buku Subbab 4.4.4 (Tabel 42, Gambar 17); hasil_uji_loop_dan_kekekalan.xlsx.')


EXT = [('E01', 'Wisatawan', 'Laju Pertumbuhan Eksternal = 0', 'Wisatawan turun eksponensial mendekati nol, tidak negatif; Daya Tarik tidak melonjak'),
       ('E02', 'Wisatawan', 'Laju Penurunan Dasar = 0', 'Wisatawan tidak pernah turun; rem tetap menurunkan Daya Tarik di bawah 1'),
       ('E03', 'Ekonomi', 'Pengeluaran per Kunjungan = 0', 'PDRB dan investasi nol; konstruksi berhenti; TPK naik tetapi ≤ 1'),
       ('E04', 'Hotel', 'Rasio Investasi thd PDRB = 0', 'Konstruksi berhenti, akomodasi turun; PDRB tetap tumbuh'),
       ('E05', 'Hotel', 'Laju Demolisi Dasar = 0', 'Akomodasi tidak pernah turun, lebih tinggi dari dasar'),
       ('E06', 'Hotel', 'TPK Ambang = 1', 'Konstruksi berhenti sampai permintaan melebihi 100% kapasitas'),
       ('E07', 'Hotel', 'Proporsi Wisatawan Menginap = 0', 'TPK dan Rasio Permintaan nol; akomodasi turun hanya oleh demolisi'),
       ('E08', 'ODTW', 'Sensitivitas ODTW thd Investasi = 0; Pembangunan Non-Investasi = 0', 'ODTW turun eksponensial; Daya Tarik turun; wisatawan memuncak lalu turun'),
       ('E09', 'Lahan', 'Laju Konversi Dasar ×10 (0,436)', 'Lahan mendekati tetapi tidak melebihi luas wilayah'),
       ('E10', 'Lahan', 'Kebijakan Konservasi Lahan = 1', 'Konversi pariwisata nol; non-pariwisata tetap berjalan'),
       ('E11', 'Lahan', 'Lahan per Hotel dan per ODTW = 0', 'Setara E10'),
       ('E12', 'Tenaga Kerja', 'Laju Kenaikan Produktivitas = 0', 'TK tumbuh sebanding PDRB, lebih tinggi dari dasar'),
       ('E13', 'Tenaga Kerja', 'Laju Keluar Dasar TK = 0', 'TK mengikuti kebutuhan tanpa menumpuk'),
       ('E14', 'Kebijakan', 'Insentif Kebijakan = 5', 'Konstruksi melonjak lalu melambat sendiri; Daya Tarik tidak lepas kendali'),
       ('E15', 'Wisatawan', 'Laju Pertumbuhan Eksternal ×3 (0,832)', 'Seluruh rem struktural bekerja (lahan, okupansi, daya tarik)'),
       ('E16', 'ODTW', 'Laju Penutupan Dasar ODTW = 0', 'ODTW naik monoton, lebih tinggi dari dasar'),
       ('E17', 'Lahan', 'Laju Konversi Dasar = 0', 'Lahan naik sangat lambat; RDDL hampir tidak berubah')]

EXT_VAL = {  # wisatawan juta, hotel, odtw, tk ribu, lahan, tpk maks, rasio maks, rddl min, dt min, status
    'E01': ('0,12', '683', '149', '175,71', '121.226', '0,358', '0,358', '0,618', '0,903', 'Lolos'),
    'E02': ('6.343,72', '254.956', '5.179', '35.985,56', '148.742', '0,511', '0,511', '0,531', '0,758', 'Lolos dgn catatan'),
    'E03': ('71,56', '635', '134', '170,44', '121.169', '1,000', '2,267', '0,618', '0,740', 'Lolos'),
    'E04': ('71,56', '635', '134', '493,42', '121.169', '1,000', '2,267', '0,618', '0,740', 'Lolos'),
    'E05': ('96,27', '6.357', '367', '650,79', '121.826', '0,358', '0,358', '0,616', '0,814', 'Lolos'),
    'E06': ('96,35', '1.821', '367', '651,33', '121.519', '1,000', '1,085', '0,617', '0,814', 'Lolos'),
    'E07': ('96,38', '635', '367', '651,46', '121.366', '0,000', '0,000', '0,617', '0,814', 'Lolos'),
    'E08': ('59,62', '3.667', '56', '416,04', '121.719', '0,386', '0,386', '0,616', '0,698', 'Lolos'),
    'E09': ('47,40', '2.846', '286', '326,91', '317.033', '0,383', '0,383', '0,000', '0,715', 'Lolos'),
    'E10': ('96,43', '5.415', '367', '651,81', '121.094', '0,388', '0,388', '0,618', '0,814', 'Lolos'),
    'E11': ('96,43', '5.415', '367', '651,81', '121.094', '0,388', '0,388', '0,618', '0,814', 'Lolos'),
    'E12': ('96,20', '5.404', '367', '847,26', '122.208', '0,388', '0,388', '0,615', '0,813', 'Lolos'),
    'E13': ('96,20', '5.404', '367', '650,36', '122.208', '0,388', '0,388', '0,615', '0,813', 'Lolos'),
    'E14': ('166,59', '11.355', '2.143', '1.108,34', '124.478', '0,358', '0,358', '0,607', '0,869', 'Lolos'),
    'E15': ('581.801,49', '21.542.004', '353.870', '3.096.262,46', '317.036', '0,633', '0,633', '0,000', '0,600', 'Lolos dgn catatan'),
    'E16': ('127,78', '6.829', '755', '846,35', '122.397', '0,391', '0,391', '0,614', '0,892', 'Lolos'),
    'E17': ('111,39', '6.070', '384', '743,62', '56.161', '0,389', '0,389', '0,823', '0,862', 'Lolos')}


def D_ekstrem(D):
    s = D.slide('Lampiran · Uji Kondisi Ekstrem (1/3): Rancangan dan Aturan Penilaian')
    sub(s, 'Hipotesis perilaku ditulis sebelum simulasi dijalankan agar penilaian tidak menyesuaikan hasil')
    rows = [['Kode', 'Subsistem', 'Parameter & nilai ekstrem', 'Hipotesis perilaku']] + [list(e) for e in EXT]
    tbl(s, 0.9, 2.05, 12.6, [0.8, 1.6, 4.3, 5.9], rows, size=9.5, rowh=0.385, center=(0,), bold_first=True)
    hdr(s, 13.8, 2.05, 5.3, 'Enam aturan logika fisik')
    R = ['Stok tidak boleh negatif', 'TPK ≤ 1', 'RDDL ≥ 0', 'Lahan terbangun ≤ luas wilayah (317.036 ha)', '0 ≤ Daya Tarik ≤ 3', 'Wisatawan akhir ≤ 5 × simulasi dasar*']
    for k, r_ in enumerate(R):
        yy = 2.65 + k * 0.62
        num(s, 13.8, yy + 0.04, k + 1, d=0.45, size=12)
        box(s, 14.4, yy, 4.7, 0.52, fill=LIGHT, line=LINE, anchor=MSO_ANCHOR.MIDDLE, margin=0.12, paras=[[(r_, 11.5, False, DARK)]])
    card(s, 13.8, 6.45, 5.3, 2.4, 'Kategori hasil', [
        ('Lolos:', 'keenam aturan terpenuhi dan hipotesis sesuai.'),
        ('Lolos dengan catatan:', 'kelima aturan lain terpenuhi; aturan 6 tidak diterapkan karena ujinya sengaja menghapus rem (E02, E15).'),
        ('Gagal:', 'ada aturan yang dilanggar.')], size=10.5)
    T(s, 13.8, 8.9, 5.3, 0.5, [[('*Ambang 3 dan 5× ditetapkan peneliti sebagai ambang kewajaran.', 9.5, False, GREY, True)]])
    src(s, 'Sumber: Buku Subbab 3.7.4 (Tabel 17).')


def D_ekstrem2(D):
    s = D.slide('Lampiran · Uji Kondisi Ekstrem (2/3): Nilai Variabel Tahun 2050')
    sub(s, 'Simulasi dasar 2050: wisatawan 96,20 juta; hotel 5.404; ODTW 367; TK 650,36 ribu; lahan 122.208 ha')
    rows = [['Kode', 'Subsistem', 'Parameter diubah', 'Wisatawan (juta)', 'Hotel (unit)', 'ODTW (unit)', 'TK (ribu)', 'Lahan (ha)']]
    rows.append(['Dasar', '—', 'Nilai final', '96,20', '5.404', '367', '650,36', '122.208'])
    for c, sb, p, _ in EXT:
        v = EXT_VAL[c]
        rows.append([c, sb, p, v[0], v[1], v[2], v[3], v[4]])
    hl = {(1, c): LIGHT for c in range(8)}
    hl[(16, 3)] = YEL_L; hl[(3, 3)] = YEL_L; hl[(10, 7)] = YEL_L; hl[(16, 7)] = YEL_L
    tbl(s, 0.9, 2.05, 18.2, [0.9, 1.7, 6.2, 2.0, 1.9, 1.6, 2.0, 1.9], rows, size=9.5, rowh=0.345, hl=hl, center=(0, 3, 4, 5, 6, 7), bold_first=True)
    note(s, 'Nilai besar pada E02 dan E15 adalah konsekuensi desain uji (rem pertumbuhan dihapus/pendorong dilipatgandakan). Lahan E09 (317.033 ha) dan E15 (317.036 ha, Δt 0,25) berhenti tepat di bawah luas wilayah. E10 = E11 persis, sesuai hipotesis.', y=9.2, h=0.8)
    src(s, 'Sumber: Buku Subbab 4.4.5 (Tabel 43); hasil_uji_kondisi_ekstrem_v2.xlsx. E15 dijalankan pada Δt 0,25 tahun.')


def D_ekstrem3(D):
    s = D.slide('Lampiran · Uji Kondisi Ekstrem (3/3): Pemeriksaan Aturan Fisik')
    sub(s, 'Seluruh 17 uji memenuhi aturan fisik dan hipotesisnya; pembatas hasil perbaikan struktur terbukti aktif')
    rows = [['Kode', 'Subsistem', 'TPK maks', 'Rasio Permintaan maks', 'RDDL min', 'Daya Tarik min', 'Hipotesis', 'Status']]
    hl = {}
    for i, (c, sb, _, _) in enumerate(EXT, 1):
        v = EXT_VAL[c]
        rows.append([c, sb, v[5], v[6], v[7], v[8], 'Sesuai', v[9]])
        hl[(i, 7)] = YEL_L if 'catatan' in v[9] else GREEN
        if v[5] == '1,000': hl[(i, 2)] = YEL_L
        if v[7] == '0,000': hl[(i, 4)] = YEL_L
    tbl(s, 0.9, 2.05, 11.6, [0.8, 1.7, 1.3, 2.0, 1.3, 1.5, 1.2, 1.8], rows, size=10, rowh=0.385, hl=hl, center=tuple(range(2, 8)), bold_first=True)
    hdr(s, 12.8, 2.05, 6.3, 'Bukti pembatas bekerja (sel kuning)')
    bullets(s, 12.8, 2.65, 6.3, 3.6, [('TPK ≤ 1:', 'TPK tertahan tepat 1,000 pada E03, E04, E06 walau Rasio Permintaan mencapai 2,267.'),
                                        ('RDDL ≥ 0 dan lahan ≤ wilayah:', 'RDDL menyentuh 0,000 pada E09 dan E15 tanpa menjadi negatif.'),
                                        ('Daya Tarik terkendali:', 'tetap 0,60–1,00 bahkan pada E01 dan E15.'),
                                        ('Pola halus sesuai hipotesis:', 'E10 = E11; E12–E13 hanya mengubah TK; E08 memuncak 2041.')], size=11)
    card(s, 12.8, 6.45, 6.3, 2.45, 'Empat perbaikan struktur sebelumnya', [
        '1. Batas TPK ≤ 1 (min pada Rasio Permintaan).',
        '2. RDDL = max(0, …) agar tidak negatif.',
        '3. Batas atas komponen kepadatan pada Daya Tarik.',
        '4. Batas maksimum efek ODTW pada Daya Tarik.'], size=11)
    src(s, 'Sumber: Buku Subbab 4.4.5 (Tabel 44); hasil_uji_kondisi_ekstrem_v2.xlsx.')


EXPL = {
    'E01': 'Tanpa kedatangan baru, wisatawan meluruh dari 40,7 juta ke 0,12 juta (2050) tanpa pernah negatif. Daya Tarik hanya bergerak di 0,90–1,00 meski kepadatan nyaris nol, tanda batas atas komponen kepadatan bekerja.',
    'E02': 'Tanpa penurunan, wisatawan terus menumpuk sampai 6.343,72 juta. Daya Tarik turun tajam sampai ±2033, sempat naik sampai 2040, lalu turun lagi (min 0,758): rem kepadatan dan lahan tetap aktif. Lolos dengan catatan.',
    'E03': 'Tanpa belanja wisatawan, PDRB nol sepanjang simulasi sehingga investasi dan konstruksi berhenti. TPK naik lalu mendatar tepat di 1,000 sejak ±2036, walau Rasio Permintaan mencapai 2,267.',
    'E04': 'Tanpa investasi, hotel turun dari 2.291 ke 635 unit karena hanya ada demolisi. TPK tertahan di 1,000. PDRB tetap tumbuh karena wisatawan masih berbelanja (TK 2050: 493,42 ribu).',
    'E05': 'Tanpa demolisi, hotel tidak pernah berkurang dan mencapai 6.357 unit (dasar 5.404). Laju konstruksi justru lebih rendah karena kapasitas yang tidak berkurang menurunkan tekanan permintaan.',
    'E06': 'Konstruksi nol sampai ±2035, lalu menyala-mati berulang setiap permintaan melewati kapasitas penuh. Hotel turun lalu bergelombang ke 1.821 unit. TPK tidak pernah > 1; catatan: ambang ekstrem memicu osilasi.',
    'E07': 'Tanpa wisatawan menginap, TPK dan Rasio Permintaan nol sepanjang simulasi. Konstruksi berhenti dan hotel turun hanya karena demolisi, ke 635 unit.',
    'E08': 'Tanpa pembangunan, ODTW turun dari 201 ke 56 unit. Daya Tarik melemah sehingga wisatawan memuncak sekitar 2041 lalu turun ke 59,62 juta, sesuai hipotesis "memuncak lalu menurun".',
    'E09': 'Konversi non-pariwisata 10× membuat lahan naik berbentuk kurva-S dan mendatar di 317.033 ha, tepat di bawah luas wilayah. RDDL turun dan menyentuh 0 tanpa menjadi negatif.',
    'E10': 'Konservasi penuh membuat laju konversi lahan pariwisata nol sepanjang simulasi. Lahan terbangun tetap naik dari konversi non-pariwisata (121.094 ha vs 122.208 ha dasar).',
    'E11': 'Kebutuhan lahan per hotel dan per ODTW dinolkan: konversi pariwisata nol dan seluruh hasil identik dengan E10, sesuai hipotesis.',
    'E12': 'Produktivitas tetap membuat intensitas TK datar di 21,54 jiwa/miliar Rp, sehingga TK tumbuh mengikuti PDRB sampai 847,26 ribu (dasar 650,36 ribu). Variabel lain tidak berubah.',
    'E13': 'Tanpa pekerja keluar, TK tetap mengikuti kebutuhan (650,36 ribu, sama dengan dasar). Yang berubah hanya laju penyerapan, yang lebih rendah karena tidak perlu mengganti pekerja keluar.',
    'E14': 'Insentif 5 membuat hotel naik sampai 11.355 unit. TPK turun cepat ke ±0,28 lalu stabil di ±0,30 karena konstruksi melambat sendiri (loop okupansi). Daya Tarik maks 1,002, tidak lepas kendali.',
    'E15': 'LPE tiga kali membuat wisatawan melonjak eksponensial. Lahan naik kurva-S dan mendatar di 317.035,82 ha (Δt 0,25), RDDL ≈ 0, Daya Tarik di batas bawah 0,600. Lolos dengan catatan; lihat uji galat integrasi.',
    'E16': 'Tanpa penutupan, ODTW naik monoton sampai 755 unit. Daya Tarik lebih tinggi dari dasar (±0,89 vs 0,81) sehingga wisatawan 2050 mencapai 127,78 juta.',
    'E17': 'Tanpa konversi non-pariwisata, lahan hanya bertambah dari konversi pariwisata dan nyaris datar (56.161 ha). RDDL bertahan di sekitar 0,823.'}


def D_ekstrem_grafik(D):
    codes = [e[0] for e in EXT]
    meta = {e[0]: e for e in EXT}
    pages = [codes[i:i + 2] for i in range(0, 17, 2)]
    for pi, pg in enumerate(pages):
        s = D.slide(f'Lampiran · Grafik Uji Kondisi Ekstrem ({pi + 1}/{len(pages)})')
        sub(s, 'Garis biru: simulasi dasar · garis oranye putus-putus: hasil uji')
        for k, c in enumerate(pg):
            y0 = 2.05 + k * 3.55
            pic_box(s, EDIR + f'{c}.png', 0.9, y0, 11.6, 3.35)
            st = EXT_VAL[c][9]
            col = YEL_L if 'catatan' in st else GREEN
            box(s, 12.8, y0, 6.3, 0.5, fill=TEAL, line=None, anchor=MSO_ANCHOR.MIDDLE, margin=0.15,
                paras=[[(c + '  ', 14, True, WHITE), (meta[c][2], 11, False, 'D7EEF2')]])
            box(s, 12.8, y0 + 0.55, 6.3, 2.25, fill=LIGHT, line=LINE, margin=0.18,
                paras=[[('Hipotesis: ', 11, True, TEAL), (meta[c][3], 11, False, DARK)], [(EXPL[c], 11, False, DARK)]])
            box(s, 12.8, y0 + 2.85, 6.3, 0.48, fill=col, line=None, anchor=MSO_ANCHOR.MIDDLE, margin=0.15,
                paras=[[('Status: ' + st.replace('dgn', 'dengan'), 11.5, True, DARK)]])
        if len(pg) == 1:
            note(s, 'Ketujuh belas uji memenuhi keenam aturan fisik dan seluruh hipotesis terkonfirmasi. Model dinyatakan logis secara struktural selama Laju Pertumbuhan Eksternal tidak melampaui sekitar 0,336 (±1,25 × nilai dasar).', y=5.9, h=1.0, title='Rangkuman')
        src(s, 'Sumber: Buku Subbab 4.4.5 (Gambar 18–23); grafik E01–E17 dari Pengujian Model Sistem Dinamis/Kalibrasi.')


def D_galat(D):
    s = D.slide('Lampiran · Uji Galat Integrasi')
    sub(s, 'Memastikan hasil berasal dari struktur model, bukan dari ukuran langkah waktu (Δt) yang terlalu besar')
    formula(s, 0.9, 2.05, 8.6, 1.05, ['Selisih % = (X_Δt − X_Δt=1) ÷ X_Δt=1 × 100%', ('Euler: S(t+Δt) = S(t) + Δt × (masuk − keluar)', '')], title='Rumus', size=12.5)
    hdr(s, 0.9, 3.3, 8.6, 'Pemeriksaan 1 · E15 pada berbagai Δt')
    rows = [['Δt (tahun)', 'Lahan maks (ha)', 'Selisih thd 317.036 ha', 'Konversi pariwisata 2049 (ha)', 'Aturan lahan'],
            ['1', '317.093,70', '+57,70', '823,51', 'Dilanggar'],
            ['0,5', '317.036,01', '+0,01', '88,29', 'Dilanggar'],
            ['0,25 (dipakai)', '317.035,82', '−0,18', '29,79', 'Lolos'],
            ['0,125', '317.035,88', '−0,12', '17,26', 'Lolos']]
    tbl(s, 0.9, 3.85, 8.6, [1.6, 1.8, 1.8, 1.9, 1.5], rows, size=10.5, rowh=0.45, center=(0, 1, 2, 3, 4),
        hl={(1, 4): PINK, (2, 4): PINK, (3, 4): GREEN, (4, 4): GREEN, (3, 0): YEL_L})
    hdr(s, 0.9, 6.25, 8.6, 'Pemeriksaan 2 · Simulasi dasar, Δt 1 vs 0,5')
    rows2 = [['Variabel (2050)', 'Δt = 1', 'Δt = 0,5', 'Selisih'],
             ['Jumlah Wisatawan', '96.197.154', '95.940.352', '−0,27%'],
             ['Lahan Terbangun (ha)', '122.207,62', '122.617,51', '+0,34%'],
             ['Jumlah Hotel', '5.404,37', '5.389,81', '−0,27%'],
             ['Tenaga Kerja', '650.355', '648.572', '−0,27%'],
             ['RDDL', '0,6145', '0,6132', '−0,21%'],
             ['Daya Tarik · ODTW · TPK', '—', '—', '−0,02% s.d. +0,002%']]
    tbl(s, 0.9, 6.8, 8.6, [2.8, 1.9, 1.9, 2.0], rows2, size=10, rowh=0.36, center=(1, 2, 3), bold_first=True)
    pic_box(s, EDIR + 'E15_diagnostik_TIME_STEP.png', 9.8, 2.05, 9.3, 4.6)
    T(s, 9.8, 6.7, 9.3, 0.35, [[('Lahan terbangun pada uji E15 dengan berbagai langkah waktu (Buku Gambar 24)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    card(s, 9.8, 7.15, 9.3, 2.0, 'Kesimpulan', [
        'Pelanggaran E15 (0,018%) mengecil teratur saat Δt diperkecil, jadi sumbernya galat numerik Euler, bukan struktur.',
        'Δt 0,25 dipakai untuk E15 karena sudah konvergen (beda 0,06 ha dengan Δt 0,125).',
        'Pada simulasi dasar selisih hanya −0,27% s.d. +0,34%, sehingga Δt = 1 tahun memadai.'], size=11)
    src(s, 'Sumber: Buku Subbab 4.4.6 (Gambar 24); hasil_uji_kondisi_ekstrem_v2.xlsx (Diagnostik E15, Uji Galat Integrasi).')
