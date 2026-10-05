# ===================== I. APLIKASI WEB  +  J. KETERBATASAN =====================
SUS = __import__('json').load(open('/tmp/pptwork/v6/sus.json'))
SUS_Q = ['Saya rasa saya akan sering menggunakan aplikasi ini.', 'Saya merasa aplikasi ini terlalu rumit padahal dapat dibuat lebih sederhana.',
         'Saya rasa aplikasi ini mudah digunakan.', 'Saya rasa saya memerlukan bantuan orang teknis untuk dapat menggunakan aplikasi ini.',
         'Saya rasa berbagai fungsi dalam aplikasi ini terpadu dengan baik.', 'Saya rasa terlalu banyak ketidakkonsistenan dalam aplikasi ini.',
         'Saya rasa kebanyakan orang akan cepat memahami cara menggunakan aplikasi ini.', 'Saya rasa aplikasi ini merepotkan untuk digunakan.',
         'Saya merasa yakin saat menggunakan aplikasi ini.', 'Saya perlu mempelajari banyak hal terlebih dahulu sebelum dapat menggunakan aplikasi ini.']


def I_alur(D):
    s = D.slide('Lampiran · Alur Implementasi dan Perangkat Aplikasi Web')
    sub(s, 'Model Vensim yang sudah diuji dijalankan langsung di peramban; antarmuka hanya meneruskan masukan dan menampilkan keluaran')
    pic_box(s, MED + 'image10.png', 0.9, 2.05, 10.4, 5.6, border=False)
    T(s, 0.9, 7.7, 10.4, 0.35, [[('Alur implementasi aplikasi simulasi (Buku Gambar 9)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    rows = [['Komponen', 'Perangkat', 'Fungsi'],
            ['Model', 'Vensim (.mdl)', 'Struktur dan persamaan model yang sudah diuji'],
            ['Konversi model', 'SDEverywhere', 'Menerjemahkan model Vensim ke JavaScript/WebAssembly'],
            ['Antarmuka', 'Next.js + TypeScript', 'Halaman, kontrol tuas, pemanggilan simulasi'],
            ['Tampilan', 'Tailwind CSS', 'Pengaturan gaya dan tata letak'],
            ['Akses', 'sistemdinamispariwisata.vercel.app', 'Aplikasi daring']]
    tbl(s, 11.6, 2.05, 7.5, [1.8, 2.6, 3.1], rows, size=10.5, rowh=0.55, bold_first=True)
    hdr(s, 11.6, 5.55, 7.5, 'Empat halaman utama')
    rows2 = [['Halaman', 'Isi'], ['Beranda', 'Gambaran umum dan navigasi'], ['Model', 'Tab Struktur Model dan Evaluasi Model'],
             ['Skenario', 'Tiga skenario + Bandingkan Semua Skenario'], ['Simulasi', 'Atur dua tuas, pilih variabel, jalankan 2025–2050']]
    tbl(s, 11.6, 6.1, 7.5, [1.8, 5.7], rows2, size=10.5, rowh=0.48, bold_first=True)
    src(s, 'Sumber: Buku Subbab 3.9.1 dan 4.9.1; Climate Interactive (n.d.).')


def I_tampilan(D):
    s = D.slide('Lampiran · Tampilan Halaman Aplikasi')
    sub(s, 'Beranda, Model (struktur dan evaluasi), Skenario, dan Simulasi')
    P = [(65, 'Beranda', 62), (66, 'Model: struktur', 63), (67, 'Model: evaluasi', 64), (68, 'Skenario', 65), (69, 'Simulasi', 66)]
    for k, (im, t_, g) in enumerate(P):
        x = 0.9 + k * 3.68; w = 3.5
        hdr(s, x, 2.05, w, t_, h=0.45)
        pic_box(s, MED + f'image{im}.png', x, 2.6, w, 6.0)
        T(s, x, 8.62, w, 0.3, [[(f'Buku Gambar {g}', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    note(s, 'Halaman Skenario memakai kombinasi tuas yang ditetapkan penelitian; halaman Simulasi membebaskan pengguna mencoba nilai tuas lain dan melihat responsnya.', y=9.05, h=0.75)
    src(s, 'Sumber: Buku Subbab 4.9.1 (Gambar 62–66).')


def I_blackbox(D):
    s = D.slide('Lampiran · Pengujian Fungsional (Black-box Testing)')
    sub(s, 'Sembilan fungsi utama diuji dari masukan dan keluaran, tanpa melihat kode (ISTQB, 2019)')
    rows = [['No', 'Fungsi yang diuji', 'Tindakan / masukan', 'Hasil yang diharapkan', 'Hasil aktual', 'Status'],
            ['1', 'Navigasi aplikasi', 'Pilih menu Beranda, Model, Skenario, Simulasi', 'Halaman sesuai menu', 'Halaman tampil sesuai menu', 'Pass'],
            ['2', 'Tampilan Model', 'Pilih tab Struktur Model / Evaluasi Model', 'Konten sesuai tab', 'Konten tiap tab sesuai', 'Pass'],
            ['3', 'Pemilihan skenario', 'Pilih BAU, Sustainable, atau DP', 'Skenario menjadi aktif', 'Skenario aktif saat dipilih', 'Pass'],
            ['4', 'Perbandingan skenario', 'Aktifkan Bandingkan Semua Skenario', 'Tiga skenario dapat dibandingkan', 'Ketiganya tampil dan dapat dibandingkan', 'Pass'],
            ['5', 'Menjalankan simulasi', 'Tekan Jalankan Simulasi', 'Hasil 2025–2050 tampil', 'Simulasi berjalan, hasil tampil', 'Pass'],
            ['6', 'Pemilihan variabel keluaran', 'Pilih / batalkan variabel output', 'Grafik dan data menyesuaikan', 'Grafik dan data sesuai pilihan', 'Pass'],
            ['7', 'Ubah Insentif Kebijakan', 'Geser kontrol Insentif', 'Nilai berubah dan dipakai simulasi', 'Nilai berubah dan dipakai simulasi', 'Pass'],
            ['8', 'Ubah Konservasi Lahan', 'Geser kontrol Konservasi', 'Nilai berubah dan dipakai simulasi', 'Nilai berubah dan dipakai simulasi', 'Pass'],
            ['9', 'Reset parameter', 'Ubah parameter lalu tekan Reset ke BAU', 'Kembali ke konfigurasi BAU', 'Tombol reset mengembalikan ke BAU', 'Pass']]
    tbl(s, 0.9, 2.05, 13.4, [0.5, 2.5, 3.2, 2.6, 3.1, 1.5], rows, size=10, rowh=0.6, center=(0, 5), hl={(r, 5): GREEN for r in range(1, 10)})
    formula(s, 14.6, 2.05, 4.5, 2.0, ['Keberhasilan = Pass ÷ total × 100%', '= 9 ÷ 9 × 100% = 100%'], title='Rumus', size=12.5)
    box(s, 14.6, 4.25, 4.5, 1.4, fill=TEAL, line=None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, paras=[[('9 / 9 Pass', 26, True, WHITE)], [('tingkat keberhasilan 100%', 12, False, 'D7EEF2')]])
    card(s, 14.6, 5.85, 4.5, 3.2, 'Batas tafsir', [
        'Hanya berlaku untuk sembilan fungsi yang diuji; bukan jaminan aplikasi bebas semua kesalahan.',
        'Tidak menilai kemudahan penggunaan; itu diukur terpisah dengan SUS.'], size=11)
    src(s, 'Sumber: Buku Subbab 3.9.2 (Tabel 22) dan 4.9.2 (Tabel 64); BlackBox.xlsx.')


def I_sus1(D):
    s = D.slide('Lampiran · System Usability Scale (1/3): Instrumen dan Cara Hitung')
    sub(s, 'Sepuluh pernyataan skala Likert 1–5 (Brooke, 1996); butir ganjil bernada positif, butir genap bernada negatif')
    rows = [['No', 'Pernyataan', 'Kontribusi']] + [[str(i + 1), q, 'x − 1' if i % 2 == 0 else '5 − x'] for i, q in enumerate(SUS_Q)]
    hl = {(i + 1, 2): (GREEN if i % 2 == 0 else PINK) for i in range(10)}
    tbl(s, 0.9, 2.05, 10.8, [0.6, 8.6, 1.6], rows, size=10.5, rowh=0.55, center=(0, 2), hl=hl)
    formula(s, 12.0, 2.05, 7.1, 1.8, ['SUS = 2,5 × [ Σ ganjil (x − 1) + Σ genap (5 − x) ]', ('x = jawaban 1–5;', ' hasil 0–100, bukan persen')], title='Rumus', size=13)
    a = SUS[0]['ans']
    odd = [a[i] - 1 for i in range(0, 10, 2)]; even = [5 - a[i] for i in range(1, 10, 2)]
    card(s, 12.0, 4.05, 7.1, 3.0, 'Contoh: responden R1', [
        [('Jawaban: ' + ', '.join(str(v) for v in a), 11.5, False, DARK)],
        [('Ganjil (x − 1): ' + ' + '.join(str(v) for v in odd) + f' = {sum(odd)}', 11.5, False, DARK)],
        [('Genap (5 − x): ' + ' + '.join(str(v) for v in even) + f' = {sum(even)}', 11.5, False, DARK)],
        [(f'SUS = 2,5 × ({sum(odd)} + {sum(even)}) = {fmt(2.5 * (sum(odd) + sum(even)), 1)}', 14, True, TEAL)]], size=11.5)
    card(s, 12.0, 7.25, 7.1, 1.85, 'Responden', [
        '10 responden (mahasiswa) setelah mencoba lima tugas di aplikasi. Jumlah 8–12 pengguna cukup untuk gambaran SUS yang andal (Brooke, 2013; Tullis & Stetson, 2004); dibaca deskriptif.'], size=10.5)
    src(s, 'Sumber: Buku Subbab 3.9.3 (Tabel 23); Brooke (1996, 2013).')


def I_sus2(D):
    s = D.slide('Lampiran · System Usability Scale (2/3): Jawaban dan Skor per Responden')
    sub(s, 'Jawaban asli (1 = sangat tidak setuju … 5 = sangat setuju), kontribusi, dan skor SUS; nama responden tidak ditampilkan')
    rows = [['Resp.'] + [f'B{i}' for i in range(1, 11)] + ['Σ ganjil (x−1)', 'Σ genap (5−x)', 'Skor SUS']]
    hl = {}
    for j, r in enumerate(SUS, 1):
        a = r['ans']; o = sum(a[i] - 1 for i in range(0, 10, 2)); e = sum(5 - a[i] for i in range(1, 10, 2))
        rows.append([f'R{j}'] + [str(v) for v in a] + [str(o), str(e), fmt(r['sus'], 2)])
        for i, v in enumerate(a):
            good = (v >= 4) if i % 2 == 0 else (v <= 2)
            hl[(j, i + 1)] = GREEN if good else (YEL_L if v == 3 else PINK)
    means = [sum(r['ans'][i] for r in SUS) / 10 for i in range(10)]
    rows.append(['Rata-rata'] + [fmt(m, 1) for m in means] + ['', '', '88,50'])
    for c in range(14): hl[(11, c)] = LIGHT
    tbl(s, 0.9, 2.05, 18.2, [1.3] + [1.05] * 10 + [1.85, 1.85, 1.7], rows, size=11, rowh=0.5, center=tuple(range(1, 14)), hl=hl, bold_first=True)
    T(s, 0.9, 8.1, 18.2, 0.3, [[('Hijau: jawaban mendukung kemudahan (butir ganjil ≥ 4, butir genap ≤ 2) · kuning: netral · merah muda: tidak mendukung.', 10, False, GREY, True)]])
    note(s, 'Butir paling positif: B8 tidak merepotkan (rata-rata 1,1) dan B3 mudah digunakan (4,7). Paling rendah: B1 akan sering menggunakan (3,9). Skor terendah R8 (60,00) dan R9 (70,00); delapan responden lain ≥ 85,00.', y=8.5, h=0.8, title='Membaca')
    src(s, 'Sumber: Buku Subbab 4.9.3 (Tabel 65); Evaluasi SUS (Responses).xlsx, dihitung ulang dan sama dengan kolom Skor SUS.')


def I_sus3(D):
    s = D.slide('Lampiran · System Usability Scale (3/3): Ringkasan, Tafsir, dan Masukan')
    sub(s, 'Rata-rata 88,50: di atas rata-rata normatif 68, di antara Excellent (85,5) dan Best Imaginable (90,9)')
    rows = [['Statistik', 'Nilai'], ['Responden', '10'], ['Rata-rata', '88,50'], ['Median', '92,50'], ['Simpangan baku', '13,85'], ['Minimum', '60,00'], ['Maksimum', '100,00']]
    tbl(s, 0.9, 2.05, 4.2, [2.4, 1.8], rows, size=11.5, rowh=0.5, center=(1,), bold_first=True, hl={(2, 1): YEL_L})
    sc = [r['sus'] for r in SUS]
    hdr(s, 5.4, 2.05, 7.0, 'Skor SUS per responden')
    bar_chart(s, 5.4, 2.55, 7.0, 3.4, [f'R{i}' for i in range(1, 11)], [('Skor SUS', sc)], ['39C0D3'], fmt_='0.0', fs=10,
              point_colors=['0B5E6E' if v >= 85 else 'FFD23B' for v in sc])
    hdr(s, 12.7, 2.05, 6.4, 'Adjective rating (Bangor et al., 2009)')
    sc_ = [('Good', '71,4'), ('Excellent', '85,5'), ('Best Imaginable', '90,9')]
    for k, (a, b) in enumerate(sc_):
        box(s, 12.7, 2.6 + k * 0.62, 6.4, 0.52, fill=LIGHT, line=LINE, anchor=MSO_ANCHOR.MIDDLE, margin=0.15, paras=[[(a + '  ', 12, True, TEAL), ('rata-rata ' + b, 11.5, False, DARK)]])
    box(s, 12.7, 4.5, 6.4, 1.45, fill=TEAL, line=None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, paras=[[('88,50', 28, True, WHITE)], [('antara Excellent dan Best Imaginable', 12, False, 'D7EEF2')]])
    hdr(s, 0.9, 6.25, 18.2, 'Jawaban pertanyaan terbuka (yang berisi catatan)')
    rows2 = [['Resp.', 'Bagian yang membingungkan', 'Saran'],
             ['R1', 'Penjelasan teknis; sebaiknya setelah simulasi ada interpretasi tiap grafik (bisa berupa templat mengikuti angka)', 'Tambahkan fitur chatbot ke depannya'],
             ['R5', 'Di bagian tuas kebijakan ada dua garis yang membingungkan', '—'],
             ['R6', 'Bingung dalam menginterpretasikannya', 'Ada interpretasi atau buku panduan'],
             ['R3', 'Tidak ada; semua fitur mudah dipahami', 'Aplikasi sudah sangat baik dan mudah digunakan']]
    tbl(s, 0.9, 6.8, 18.2, [1.0, 9.4, 7.8], rows2, size=10.5, rowh=0.46, center=(0,), bold_first=True)
    src(s, 'Sumber: Buku Subbab 4.9.3 (Tabel 66); Evaluasi SUS (Responses).xlsx. Enam responden lain tidak memberi catatan.')


def J_keterbatasan(D):
    s = D.slide('Lampiran · Keterbatasan Penelitian')
    sub(s, 'Dikelompokkan menjadi keterbatasan data, struktur model, dan penafsiran')
    G = [('Data', TEAL, ['Patahan metode wisnus 2018→2019; faktor sambung tidak pasti (2,22–2,38).',
                         'Lahan terbangun citra berderau (turun 27% dalam dua tahun, tidak mungkin secara fisik).',
                         'ODTW 2015–2017 dan 2025 hasil estimasi NTL dengan R² ±0,41.',
                         'Lonjakan akomodasi 2018 diduga akibat perluasan cakupan pendataan.',
                         'Investasi hanya PMA/PMDN (BKPM): tanpa UMKM dan APBN/APBD.']),
         ('Struktur model', '2A9DB0', ['Guncangan, harga, promosi, musim, dan aspek lingkungan di luar batas model.',
                                       'Daya dukung lahan memakai luas wilayah administratif, sehingga longgar.',
                                       'Permintaan kamar tak terlayani tidak menekan kunjungan.',
                                       'Tenaga kerja hanya indikator keluaran, tanpa umpan balik.',
                                       'Pembangunan ODTW lewat APBD dan pemberdayaan masyarakat tidak bisa diuji sebagai tuas.']),
         ('Penafsiran', 'E4604F', ['Rasio LPD/LPE paling menentukan, tetapi tidak teridentifikasi dari data.',
                                   'Nilai tuas adalah ketetapan peneliti, bukan target resmi.',
                                   'Ambang kepadatan 2,0 ketetapan peneliti: dibaca sebagai sinyal deskriptif.',
                                   'Evaluasi pascakalibrasi memakai data yang sama, bukan validasi independen.',
                                   'Skenario disusun tanpa lokakarya pemangku kepentingan.'])]
    for k, (t_, col, items) in enumerate(G):
        x = 0.9 + k * 6.15; w = 5.9
        box(s, x, 2.05, w, 0.65, fill=col, line=None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, paras=[[(t_, 16, True, WHITE)]])
        for j, it in enumerate(items):
            box(s, x, 2.8 + j * 1.18, w, 1.08, fill=LIGHT, line=LINE, anchor=MSO_ANCHOR.MIDDLE, margin=0.15, paras=[[(it, 11.5, False, DARK)]])
    note(s, 'Karena keterbatasan ini, model dipakai untuk membandingkan arah dan besaran relatif antarskenario, bukan untuk meramalkan angka absolut pada tahun tertentu.', y=8.85, h=0.8, title='Konsekuensi')
    src(s, 'Sumber: Buku Subbab 4.10.1.')
