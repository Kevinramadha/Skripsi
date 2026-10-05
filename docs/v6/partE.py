# ===================== E. UJI PERILAKU =====================
# (uji, variabel, versi, n, t, ttab, tren, E1, E2, DC, U1, U2, U3, MAPE)
PARSIAL = [
    ('P1', 'Jumlah Hotel', 'Dengan', 10, 0.618229, 2.119905, 'Tidak berbeda nyata', 0.008855, 0.143521, 0.247555, 0.007792, 0.072583, 0.919624, 7.099679),
    ('P1', 'Jumlah Hotel', 'Tanpa', 8, 0.752682, 2.178813, 'Tidak berbeda nyata', 0.040153, 0.07734, 0.201117, 0.172838, 0.028346, 0.798816, 6.047992),
    ('P1', 'TPK', 'Dengan', 10, 0.92629, 2.119905, 'Tidak berbeda nyata', 0.020386, 1.151307, 0.466664, 0.007226, 0.608475, 0.3843, 18.734633),
    ('P1', 'TPK', 'Tanpa', 8, 1.422143, 2.178813, 'Tidak berbeda nyata', 0.064276, 2.568406, 0.669235, 0.080703, 0.648779, 0.270518, 17.374002),
    ('P1b', 'Jumlah Hotel', 'Dengan', 10, 0.72205, 2.119905, 'Tidak berbeda nyata', 0.020023, 0.21278, 0.286807, 0.027306, 0.109341, 0.863354, 9.662431),
    ('P1b', 'Jumlah Hotel', 'Tanpa', 8, 0.934823, 2.178813, 'Tidak berbeda nyata', 0.01816, 0.12226, 0.231914, 0.029876, 0.059861, 0.910263, 7.86245),
    ('P1b', 'TPK', 'Dengan', 10, 1.149867, 2.119905, 'Tidak berbeda nyata', 0.019287, 1.241551, 0.498509, 0.005366, 0.587138, 0.407496, 20.238999),
    ('P1b', 'TPK', 'Tanpa', 8, 1.685088, 2.178813, 'Tidak berbeda nyata', 0.060963, 2.9435, 0.705311, 0.057245, 0.671889, 0.270867, 19.559769),
    ('P2', 'Jumlah ODTW', 'Dengan', 10, 1.0415, 2.1199, 'Tidak berbeda nyata', 0.0785, 0.362, 0.3688, 0.6686, 0.119, 0.2123, 7.52),
    ('P2', 'Jumlah ODTW', 'Tanpa', 8, 1.2196, 2.1788, 'Tidak berbeda nyata', 0.088, 0.3303, 0.3367, 0.7281, 0.0939, 0.1781, 8.48),
    ('P3', 'Tenaga Kerja', 'Dengan', 10, 0.4108, 2.1199, 'Tidak berbeda nyata', 0.1204, 0.3207, 0.5186, 0.5756, 0.0576, 0.3669, 11.28),
    ('P3', 'Tenaga Kerja', 'Tanpa', 8, 0.3783, 2.1788, 'Tidak berbeda nyata', 0.137, 0.3027, 0.4945, 0.6245, 0.0488, 0.3267, 12.88),
    ('P4', 'Lahan Terbangun', 'Dengan', 10, 0.143962, 2.119905, 'Tidak berbeda nyata', 0.112866, 0.390084, 0.480898, 0.481085, 0.131735, 0.38718, 12.637823),
    ('P4', 'Lahan Terbangun', 'Tanpa', 8, 0.131179, 2.178813, 'Tidak berbeda nyata', 0.112543, 0.391813, 0.48132, 0.424957, 0.147338, 0.427704, 12.941428),
    ('P5', 'Jumlah Wisatawan', 'Dengan', 10, 4.867033, 2.119905, 'Berbeda nyata', 0.177617, 0.576746, 0.420286, 0.420703, 0.538537, 0.040759, 14.249988),
    ('P5', 'Jumlah Wisatawan', 'Tanpa', 8, 5.554363, 2.178813, 'Berbeda nyata', 0.202475, 0.567995, 0.40571, 0.473686, 0.503052, 0.023261, 16.444782)]

PENUH = [
    ('Jumlah Wisatawan', 'Dengan', 7, 4.64978, 2.228139, 'Berbeda nyata', 0.119352, 0.606404, 0.448208, 0.323735, 0.637393, 0.038872, 12.064006),
    ('Jumlah Wisatawan', 'Tanpa', 5, 3.155578, 2.446912, 'Berbeda nyata', 0.169004, 0.580825, 0.425783, 0.573074, 0.394452, 0.032475, 14.236227),
    ('Jumlah Hotel', 'Dengan', 7, 3.603586, 2.228139, 'Berlawanan arah', 0.139902, 0.468544, 0.82277, 0.577892, 0.058366, 0.363742, 13.161944),
    ('Jumlah Hotel', 'Tanpa', 5, 2.774624, 2.446912, 'Berlawanan arah', 0.17251, 0.440646, 0.808151, 0.675784, 0.039641, 0.284575, 16.445764),
    ('Jumlah ODTW', 'Dengan', 7, 1.667635, 2.228139, 'Tidak berbeda nyata', 0.001199, 0.854952, 0.785471, 0.000294, 0.903332, 0.096374, 5.679498),
    ('Jumlah ODTW', 'Tanpa', 5, 1.006787, 2.446912, 'Tidak berbeda nyata', 0.031261, 0.819318, 0.756774, 0.24988, 0.630721, 0.119399, 4.553572),
    ('Tenaga Kerja', 'Dengan', 7, 3.268515, 2.228139, 'Berlawanan arah', 0.118165, 0.327966, 0.886037, 0.499115, 0.024547, 0.476338, 12.391325),
    ('Tenaga Kerja', 'Tanpa', 5, 2.392067, 2.446912, 'Berlawanan arah', 0.167435, 0.032659, 0.822167, 0.778928, 0.00009, 0.220982, 16.380108),
    ('Lahan Terbangun', 'Dengan', 7, 1.023668, 2.228139, 'Tidak berbeda nyata', 0.109863, 0.362729, 0.661896, 0.428648, 0.06401, 0.507342, 13.431953),
    ('Lahan Terbangun', 'Tanpa', 5, 0.977917, 2.446912, 'Tidak berbeda nyata', 0.104434, 0.410822, 0.725377, 0.338098, 0.084068, 0.577834, 13.818964),
    ('TPK', 'Dengan', 7, 1.156824, 2.228139, 'Tidak berbeda nyata', 0.201253, 0.26702, 0.622368, 0.508635, 0.030117, 0.461248, 18.979115),
    ('TPK', 'Tanpa', 5, 6.84152, 2.446912, 'Berlawanan arah', 0.243144, 0.94199, 0.926333, 0.662907, 0.040274, 0.296819, 23.422632),
    ('PDRB Pariwisata', 'Dengan', 7, 1.072726, 2.228139, 'Tidak berbeda nyata', 0.254298, 0.345041, 0.306233, 0.927264, 0.033714, 0.039022, 25.061429),
    ('PDRB Pariwisata', 'Tanpa', 5, 0.014859, 2.446912, 'Tidak berbeda nyata', 0.276085, 0.066709, 0.168033, 0.987799, 0.000514, 0.011686, 27.763054),
    ('Investasi Pariwisata', 'Dengan', 7, 1.090321, 2.228139, 'Tidak berbeda nyata', 0.383913, 0.792659, 0.735625, 0.581431, 0.333402, 0.085168, 33.541699),
    ('Investasi Pariwisata', 'Tanpa', 5, 0.645416, 2.446912, 'Tidak berbeda nyata', 0.404883, 0.798832, 0.755095, 0.605618, 0.305927, 0.088456, 36.249388),
    ('Total Malam Menginap', 'Dengan', 7, 0.041205, 2.228139, 'Tidak berbeda nyata', 0.264267, 0.675683, 0.704146, 0.506001, 0.25936, 0.234639, 29.520468),
    ('Total Malam Menginap', 'Tanpa', 5, 1.860555, 2.446912, 'Berlawanan arah', 0.339464, 0.297581, 0.806028, 0.823551, 0.008298, 0.16815, 32.839093)]


def _stat_rows(data, with_uji, main):
    rows = []; hl = {}
    for i, d in enumerate(data, 1):
        if with_uji:
            u, v, ver, n, t, tt, tren, e1, e2, dc, u1, u2, u3, mp = d; pre = [u, v]
        else:
            v, ver, n, t, tt, tren, e1, e2, dc, u1, u2, u3, mp = d; pre = [v]
        ok_tren = tren == 'Tidak berbeda nyata'
        e1s = fmt(e1, 4) + ('' if ok_tren else '*'); e2s = fmt(e2, 4) + ('' if ok_tren else '*')
        dom = max((u1, 'U1'), (u2, 'U2'), (u3, 'U3'))[1]
        rows.append(pre + [('Dengan COVID' if ver == 'Dengan' else 'Tanpa 2020–21') + (' ●' if ver == main else ''), str(n), f'{fmt(t, 3)} / {fmt(tt, 3)}', tren, e1s, e2s, fmt(dc, 4),
                           fmt(u1, 3), fmt(u2, 3), fmt(u3, 3), dom, fmt(mp, 2) + '%'])
        c0 = len(pre)
        hl[(i, c0 + 3)] = GREEN if ok_tren else (PINK if 'Berlawanan' in tren else YEL_L)
        if ok_tren:
            hl[(i, c0 + 4)] = GREEN if e1 <= 0.05 else PINK
            hl[(i, c0 + 5)] = GREEN if e2 <= 0.30 else PINK
        hl[(i, c0 + 6)] = GREEN if dc < 0.4 else (YEL_L if dc <= 0.7 else PINK)
        if ver == main:
            hl[(i, c0)] = LIGHT
    return rows, hl


def E_ukuran(D):
    s = D.slide('Lampiran · Ukuran Penilaian Uji Perilaku (1/2): Urutan dan Rumus')
    sub(s, 'Dinilai berurutan mengikuti Barlas (1989): pola dulu (tren), lalu rata-rata (E1), lalu variasi (E2), terakhir ringkasan (DC)')
    flow(s, 0.9, 2.05, 18.2, 0.95, [('1 · Uji tren', 'arah dan laju'), ('2 · E1', 'rata-rata'), ('3 · E2', 'variasi'), ('4 · DC', 'ringkasan titik'), ('Pelengkap', 'U1–U3 dan MAPE')],
         fills=[TEAL, TEAL, TEAL, TEAL, LIGHT])
    C = [('Uji tren', ['t = |bₛ − bₐ| ÷ √(Var(bₐ) + Var(bₛ))', ('db = 2n − 4; α = 0,05 dua sisi', '')],
          'Membandingkan kemiringan garis regresi simulasi (bₛ) dan data (bₐ). Kalau arah atau lajunya sudah beda, ukuran berikutnya tidak ditafsirkan.', 'Lolos bila t hitung ≤ t tabel dan arah sama'),
         ('E1 · galat rata-rata', ['E1 = |S̄ − Ā| ÷ Ā'],
          'Seberapa jauh rata-rata simulasi dari rata-rata data, dalam proporsi.', 'Pedoman: E1 ≤ 0,05'),
         ('E2 · galat variasi', ['E2 = |σₛ − σₐ| ÷ σₐ'],
          'Seberapa beda besar naik-turunnya (simpangan baku) simulasi dibanding data.', 'Pedoman: E2 ≤ 0,30'),
         ('DC · discrepancy coefficient', ['eᵢ = Aᵢ − Sᵢ', 'DC = SD(e) ÷ (SD(A) + SD(S))'],
          'Ringkasan kecocokan titik demi titik; dipakai untuk melaporkan, bukan sebagai uji.', '< 0,4 baik · 0,4–0,7 cukup (rata-rata sampai baik) · > 0,7 kurang'),
         ('MAPE', ['MAPE = (1/n) Σ |Sᵢ − Aᵢ| ÷ Aᵢ × 100%'],
          'Rata-rata besar kesalahan dalam persen; mudah dibaca awam.', '< 10% sangat baik · 10–20% baik · 20–50% layak · > 50% buruk')]
    for k, (t_, f_, d_, kr) in enumerate(C):
        x = 0.9 + k * 3.7; w = 3.45
        hdr(s, x, 3.25, w, t_, h=0.5)
        formula(s, x, 3.8, w, 1.25, f_, size=11.5)
        box(s, x, 5.15, w, 2.2, fill=LIGHT, line=LINE, margin=0.15, paras=[[(d_, 11, False, DARK)]])
        box(s, x, 7.45, w, 1.1, fill=GREEN, line=None, anchor=MSO_ANCHOR.MIDDLE, margin=0.12, paras=[[(kr, 10.5, True, DARK)]])
    note(s, 'S = simulasi, A = data aktual, garis atas = rata-rata, σ / SD = simpangan baku, n = jumlah tahun. Angka E1 dan E2 adalah pedoman empiris Barlas (1989), bukan ambang uji statistik.', y=8.8, h=0.8, title='Notasi')
    src(s, 'Sumber: Buku Subbab 3.7.4; Barlas (1989); Mai & Smith (2018); kategori MAPE Lewis (1982).')


def E_tren(D):
    s = D.slide('Lampiran · Ukuran Penilaian Uji Perilaku (2/2): Kategori Hasil Uji Tren')
    sub(s, 'Tiga kemungkinan hasil uji tren dan konsekuensinya terhadap pembacaan E1 dan E2')
    K = [('Tidak berbeda nyata', GREEN, 'Arah kemiringan sama dan t hitung ≤ t tabel.', 'Pola pertumbuhan simulasi sejalan dengan data. E1, E2, dan DC dibaca seperti biasa.',
          'P4 Lahan (tanpa 2020–21): bₐ = 2.042 ha/th, bₛ = 1.914 ha/th; t = 0,131 < 2,179'),
         ('Berbeda nyata', YEL_L, 'Arah kemiringan sama, tetapi t hitung > t tabel.', 'Arahnya benar, tetapi lajunya terlalu cepat atau lambat. E1 dan E2 tidak ditafsirkan; cukup dibaca dari DC dan MAPE.',
          'P5 Wisatawan (tanpa 2020–21): bₐ = 2,85 juta/th, bₛ = 1,26 juta/th; t = 5,554 > 2,179'),
         ('Berlawanan arah', PINK, 'Tanda kemiringan simulasi dan data berbeda (satu naik, satu turun).', 'Pola tidak sesuai sama sekali. E1 dan E2 tidak ditafsirkan; penyebabnya ditelusuri.',
          'Uji penuh Hotel (dengan COVID): bₐ = +66,07 unit/th, bₛ = −40,67 unit/th')]
    for k, (t_, col, syarat, makna, contoh) in enumerate(K):
        x = 0.9 + k * 6.15; w = 5.9
        box(s, x, 2.05, w, 0.7, fill=col, line=None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, paras=[[(t_, 16, True, DARK)]])
        card(s, x, 2.85, w, 1.2, 'Syarat', [syarat], size=11.5)
        card(s, x, 4.15, w, 1.6, 'Artinya', [makna], size=11.5)
        card(s, x, 5.85, w, 1.35, 'Contoh dari hasil penelitian', [contoh], size=11, fill='FFFFFF')
    rows = [['n (tahun dinilai)', '10 (parsial, dengan COVID)', '8 (parsial, tanpa 2020–21)', '7 (penuh, dengan COVID)', '5 (penuh, tanpa 2020–21)'],
            ['db = 2n − 4', '16', '12', '10', '6'],
            ['t tabel (α 0,05 dua sisi)', '2,120', '2,179', '2,228', '2,447']]
    tbl(s, 0.9, 7.45, 18.2, [3.8, 3.6, 3.6, 3.6, 3.6], rows, size=11, rowh=0.42, center=(1, 2, 3, 4), bold_first=True)
    src(s, 'Sumber: Buku Subbab 3.7.4; nilai kemiringan dari hasil_P1_P4_baseline_v2.xlsx dan hasil_uji_perilaku_baseline_v2.xlsx.')


def E_theil(D):
    s = D.slide('Lampiran · Dekomposisi Galat U1, U2, U3 (Theil)')
    sub(s, 'Bukan untuk menilai besar galat, melainkan untuk menelusuri dari mana galat berasal (Sterman, 1984)')
    formula(s, 0.9, 2.05, 7.0, 3.0, ['MSE = (1/n) Σ (Sᵢ − Aᵢ)²', 'U1 = (S̄ − Ā)² ÷ MSE', 'U2 = (σₛ − σₐ)² ÷ MSE', 'U3 = 2(1 − r) σₛ σₐ ÷ MSE',
                                      ('U1 + U2 + U3 = 1;', '  r = korelasi simulasi dengan data')], title='Rumus', size=13)
    K = [('U1 · bias', PINK, 'Simulasi konsisten lebih tinggi atau lebih rendah dari data sepanjang periode.', 'Galat sistematis → periksa nilai awal/parameter level atau masukan dari hulu.'),
         ('U2 · variasi', YEL_L, 'Naik-turun simulasi lebih besar atau lebih kecil dari data, atau lajunya beda.', 'Galat sistematis → periksa parameter laju atau derau data masukan.'),
         ('U3 · kovariasi', GREEN, 'Simulasi mengikuti pola umum, tetapi tidak meniru loncatan acak tiap tahun.', 'Galat tidak sistematis → wajar, model tidak perlu diubah.')]
    for k, (t_, col, a, b) in enumerate(K):
        y = 2.05 + k * 1.02
        box(s, 8.2, y, 2.4, 0.92, fill=col, line=None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, paras=[[(t_, 13, True, DARK)]])
        box(s, 10.7, y, 8.4, 0.92, fill=LIGHT, line=LINE, anchor=MSO_ANCHOR.MIDDLE, margin=0.15, paras=[[(a, 11, False, DARK)], [(b, 11, True, TEAL)]])
    hdr(s, 0.9, 5.3, 18.2, 'Contoh pembacaan dari hasil penelitian')
    cats = ['P1 Hotel', 'P1 TPK', 'P2 ODTW', 'P4 Lahan', 'P5 Wisatawan', 'Penuh PDRB']
    U = [(0.172838, 0.028346, 0.798816), (0.080703, 0.648779, 0.270518), (0.7281, 0.0939, 0.1781), (0.424957, 0.147338, 0.427704), (0.473686, 0.503052, 0.023261), (0.927264, 0.033714, 0.039022)]
    cd = CategoryChartData(); cd.categories = cats
    for j, nm in enumerate(['U1 bias', 'U2 variasi', 'U3 kovariasi']):
        cd.add_series(nm, [u[j] for u in U])
    ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_STACKED_100, Inches(0.9), Inches(5.85), Inches(10.0), Inches(3.6), cd).chart
    ch.has_title = False; ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout = False
    ch.font.size = Pt(10); ch.font.name = F
    pl = ch.plots[0]; pl.gap_width = 40; pl.overlap = 100
    for sr, col in zip(pl.series, ['E4604F', 'FFD23B', '39C0D3']):
        sr.format.fill.solid(); sr.format.fill.fore_color.rgb = rgb(col)
    pl.has_data_labels = True; pl.data_labels.number_format = '0.00'; pl.data_labels.number_format_is_linked = False; pl.data_labels.font.size = Pt(9)
    ch.category_axis.reverse_order = True
    ch.value_axis.tick_labels.font.size = Pt(9); ch.category_axis.tick_labels.font.size = Pt(10)
    bullets(s, 11.2, 5.95, 7.9, 3.5, [('P1 Hotel:', 'U3 ≈ 0,80 → sisa galat hanya derau; struktur akomodasi sudah tepat.'),
                                       ('P1 TPK:', 'U2 ≈ 0,65 → naik-turun berlebih karena masukan malam menginap berderau.'),
                                       ('P5 Wisatawan:', 'U1 + U2 > 0,95 → galat sistematis; menjadi dasar kalibrasi diagnostik Tahap 3.'),
                                       ('Uji penuh PDRB:', 'U1 ≈ 0,93 → bias level yang merambat dari galat jumlah wisatawan.')], size=11.5)
    src(s, 'Sumber: Buku Subbab 3.7.4; nilai versi tanpa 2020–2021 (parsial) dan dengan COVID (penuh).')


def E_rancangan(D):
    s = D.slide('Lampiran · Rancangan Uji Parsial, Uji Penuh, dan Alasan Uji P1b')
    sub(s, 'Uji parsial memeriksa struktur tiap subsistem; uji penuh memeriksa apakah galat merambat antarsubsistem')
    rows = [['Uji', 'Subsistem', 'Diganti data aktual', 'Variabel dinilai', 'Periode'],
            ['P1', 'Akomodasi', 'Total malam menginap, investasi', 'Jumlah hotel, TPK', '2016–2025'],
            ['P1b', 'Akomodasi (uji kekokohan)', 'Seperti P1 + rata-rata kamar per unit per tahun', 'Jumlah hotel, TPK', '2016–2025'],
            ['P2', 'ODTW', 'Investasi', 'Jumlah ODTW', '2016–2025'],
            ['P3', 'Tenaga kerja', 'PDRB pariwisata', 'Tenaga kerja pariwisata', '2016–2025'],
            ['P4', 'Lahan', 'Total malam menginap, investasi', 'Lahan terbangun', '2016–2025'],
            ['P5', 'Wisatawan', 'Jumlah ODTW, lahan terbangun', 'Jumlah wisatawan (seri sambungan)', '2016–2025'],
            ['Penuh', 'Seluruh model', 'Tidak ada (semua umpan balik aktif)', '9 variabel', '2019–2025']]
    tbl(s, 0.9, 2.05, 10.6, [0.9, 2.2, 3.4, 2.6, 1.5], rows, size=10.5, rowh=0.5, hl={(2, 0): YEL_L, (2, 1): YEL_L}, center=(0, 4), bold_first=True)
    card(s, 0.9, 6.3, 10.6, 2.75, 'Dua versi perhitungan', [
        ('Dengan COVID:', 'semua tahun dihitung. Angka utama uji penuh, karena tanpa 2020–21 hanya tersisa 5 titik.'),
        ('Tanpa 2020–2021:', 'tahun pandemi dikeluarkan karena model tidak memuat guncangan. Angka utama uji parsial (tersisa 8 dari 10 titik).'),
        ('Uji penuh mulai 2019:', 'data wisnus berganti metode pada 2018→2019 (8,0 → 20,5 juta), sehingga seri sebelum 2019 hanya dipakai P5 lewat penyambungan ×2,2997.')], size=11)
    hdr(s, 11.8, 2.05, 7.3, 'Kenapa ada P1b?')
    T(s, 11.8, 2.6, 7.3, 1.3, [[('P1 memakai rata-rata kamar per unit tetap 21,4168 (nilai 2025) untuk semua tahun. Padahal data tahunannya berubah-ubah. P1b menguji apakah kesimpulan P1 berubah bila nilai tahunan yang sebenarnya dipakai.', 11.5, False, DARK)]])
    yrs = [str(y) for y in range(2016, 2026)]
    K = [20.1821, 22.1917, 20.3271, 19.6571, 19.7413, 20.2748, 20.1562, 20.2654, 26.1165, 21.4168]
    ch = line_chart(s, 11.8, 3.95, 7.3, 3.0, yrs, [('Kamar per unit aktual (P1b)', K), ('Nilai tetap P1 (21,4168)', [21.4168] * 10)], ['0B5E6E', 'E4604F'], fmt_='0.0', dash=[False, True], fs=9)
    box(s, 11.8, 7.05, 7.3, 2.0, fill=GREEN, line=None, margin=0.18, paras=[
        [('Hasil: ', 12, True, TEAL), ('pola P1b sama dengan P1. Jumlah hotel tetap lolos ketiga uji (DC 0,2319 vs 0,2011); TPK tetap jadi titik terlemah (DC 0,7053 vs 0,6692). ', 11.5, False, DARK)],
        [('Kesimpulan uji parsial akomodasi tidak bergantung pada asumsi kamar per unit yang tetap.', 11.5, True, DARK)]])
    src(s, 'Sumber: Buku Subbab 3.7.4 (Tabel 18), 4.5.1–4.5.2; data kamar per unit dari model UJI Parsial P1b v2.')


def E_parsial(D):
    s = D.slide('Lampiran · Hasil Uji Parsial Lengkap (P1–P5, dua versi)')
    sub(s, '● = versi yang dilaporkan sebagai angka utama (tanpa 2020–2021). Periode 2016–2025')
    rows, hl = _stat_rows(PARSIAL, True, 'Tanpa')
    hdr_ = ['Uji', 'Variabel', 'Versi', 'n', 't hitung / t tabel', 'Tren', 'E1', 'E2', 'DC', 'U1', 'U2', 'U3', 'Dominan', 'MAPE']
    hl = {(r + 1 if False else r, c): v for (r, c), v in hl.items()}
    tbl(s, 0.9, 2.05, 18.2, [0.7, 1.9, 1.85, 0.5, 1.75, 2.05, 1.05, 1.05, 1.05, 0.95, 0.95, 0.95, 1.1, 1.35], [hdr_] + rows, size=9.5, rowh=0.385, hl=hl, center=tuple(range(3, 14)), bold_first=True)
    T(s, 0.9, 8.75, 18.2, 0.3, [[('Hijau: memenuhi pedoman · kuning: berbeda nyata / DC cukup · merah muda: tidak memenuhi. *Tren berbeda nyata: E1 dan E2 tidak ditafsirkan.', 10, False, GREY, True)]])
    note(s, 'Semua subsistem lolos uji tren kecuali wisatawan (P5). Hotel paling baik (lolos ketiga uji). Galat P2, P3, P4 didominasi bias (U1); galat P5 sistematis (U1+U2 > 0,95).', y=9.1, h=0.8, title='Intinya')
    src(s, 'Sumber: Buku Subbab 4.5.2 (Tabel 46); hasil_P1_P4_baseline_v2.xlsx, hasil_uji_perilaku.xlsx (P2, P3), hasil_uji_perilaku_baseline_v2.xlsx (P5).')


def E_penuh(D):
    s = D.slide('Lampiran · Hasil Uji Penuh Lengkap (9 variabel, dua versi)')
    sub(s, '● = versi yang dilaporkan sebagai angka utama (dengan COVID). Periode 2019–2025')
    rows, hl = _stat_rows(PENUH, False, 'Dengan')
    hdr_ = ['Variabel', 'Versi', 'n', 't hitung / t tabel', 'Tren', 'E1', 'E2', 'DC', 'U1', 'U2', 'U3', 'Dominan', 'MAPE']
    tbl(s, 0.9, 2.05, 18.2, [2.5, 1.85, 0.5, 1.75, 2.05, 1.1, 1.1, 1.05, 0.95, 0.95, 0.95, 1.1, 1.35], [hdr_] + rows, size=9.5, rowh=0.36, hl=hl, center=tuple(range(2, 13)), bold_first=True)
    T(s, 0.9, 8.95, 18.2, 0.3, [[('*Tren berbeda nyata atau berlawanan arah: E1 dan E2 tidak ditafsirkan (Barlas, 1989).', 10, False, GREY, True)]])
    note(s, 'Hotel, ODTW, TK, dan lahan yang baik di uji parsial memburuk di uji penuh. Penyebabnya satu: wisatawan tumbuh lebih lambat dari data, lalu galatnya merambat lewat pengeluaran → PDRB → investasi. U1 dominan pada 6 dari 9 variabel.', y=9.3, h=0.75, title='Intinya')
    src(s, 'Sumber: Buku Subbab 4.5.3 (Tabel 47); hasil_uji_perilaku_baseline_v2.xlsx.')


GRAF = [  # (gambar buku, judul, interpretasi)
    (25, 'P1 · Jumlah Hotel dan Akomodasi', 'Simulasi mengikuti kenaikan data dengan baik: tren tidak berbeda nyata, E1 0,0402, E2 0,0773, DC 0,2011. Sisa galat didominasi U3 (derau), jadi struktur akomodasi sudah tepat.'),
    (26, 'P1 · Tingkat Penghunian Kamar (TPK)', 'Tren lolos, tetapi simulasi naik-turun jauh lebih tajam dari data (E2 2,5684; U2 dominan). Sumbernya derau data malam menginap 2017 dan 2020 yang dipakai sebagai masukan.'),
    (27, 'P1b · Jumlah Hotel dan Akomodasi', 'Dengan kamar per unit tahunan, pola tetap sama dengan P1 (DC 0,2319; MAPE 7,86%). Kesimpulan P1 kokoh terhadap asumsi kamar per unit.'),
    (28, 'P1b · Tingkat Penghunian Kamar (TPK)', 'Fluktuasi tetap berlebih (E2 2,9435; DC 0,7053). TPK tetap titik terlemah subsistem akomodasi.'),
    (29, 'P2 · Jumlah ODTW', 'Arah kenaikan sama dengan data (tren lolos), tetapi ada selisih level yang konsisten (U1 0,73). DC 0,3367 dan MAPE 8,48%: sangat baik.'),
    (30, 'P3 · Tenaga Kerja Pariwisata', 'Simulasi tumbuh mulus, data melompat pada 2018 dan 2022. Tren lolos; galat bias (U1 0,62), DC 0,4945, MAPE 12,88%: baik.'),
    (31, 'P4 · Lahan Terbangun', 'Simulasi naik halus mengikuti laju konversi, data citra lebih berfluktuasi. Galat terbagi bias dan kovariasi (U1 0,42; U3 0,43). DC 0,4813, MAPE 12,94%.'),
    (32, 'P5 · Jumlah Wisatawan', 'Satu-satunya yang gagal uji tren: simulasi tumbuh ±6,4%/th, data sambungan ±11,7%/th. Galat sistematis (U1 + U2 > 0,95), ditelusuri pada kalibrasi Tahap 3.'),
    (33, 'Uji penuh · Jumlah Wisatawan', 'Polanya sama dengan P5: simulasi naik lebih lambat dari data (tren berbeda nyata). DC 0,4482, MAPE 12,06%. Inilah sumber galat bagi variabel lain.'),
    (34, 'Uji penuh · Jumlah Hotel', 'Simulasi turun sampai 2023 sementara data naik (berlawanan arah), padahal di P1 sangat baik. Artinya galat datang dari hulu: wisatawan rendah → investasi rendah → konstruksi rendah.'),
    (35, 'Uji penuh · Jumlah ODTW', 'Rata-rata hampir tepat (E1 0,0012, MAPE 5,68%), tetapi simulasi terlalu datar dibanding lonjakan data 2023–2024 (E2 0,8550; U2 dominan).'),
    (36, 'Uji penuh · Tenaga Kerja', 'Simulasi menurun, data naik (berlawanan arah). TK bergantung pada PDRB yang ikut rendah karena wisatawan rendah. U1 dominan.'),
    (37, 'Uji penuh · Lahan Terbangun', 'Tren lolos; simulasi di atas data citra pada 2020–2022, mendekat pada 2023–2024, lalu data 2025 turun ke 55.029 ha. DC 0,6619, MAPE 13,43%, U3 dominan.'),
    (38, 'Uji penuh · TPK', 'DC 0,6224, lebih baik dari P1 (0,6692), karena malam menginap kini dihitung model sendiri dan tidak membawa derau data. Galat bias (U1).'),
    (39, 'Uji penuh · PDRB Pariwisata', 'Bentuk pola mirip (DC 0,3062), tetapi levelnya konsisten di bawah data (U1 0,93; MAPE 25,06%). Bias datang dari jumlah wisatawan.'),
    (40, 'Uji penuh · Investasi Pariwisata', 'Data investasi sangat berfluktuasi, simulasi naik halus dan di bawah data (MAPE 33,54%; DC 0,7356). Galat bias dari hulu.'),
    (41, 'Uji penuh · Total Malam Menginap', 'Simulasi naik halus, data jatuh tajam pada 2020 lalu pulih. Level di bawah data (U1 dominan), MAPE 29,52%: layak.')]


def E_grafik(D):
    pages = [GRAF[i:i + 2] for i in range(0, len(GRAF), 2)]
    for pi, pg in enumerate(pages):
        s = D.slide(f'Lampiran · Grafik Uji Perilaku ({pi + 1}/{len(pages)})')
        sub(s, 'Data aktual dibandingkan hasil simulasi; ' + ('uji parsial periode 2016–2025' if pg[0][0] <= 32 else 'uji penuh periode 2019–2025'))
        for k, (g, t_, ex) in enumerate(pg):
            x = 0.9 + k * 9.25; w = 8.95
            hdr(s, x, 2.05, w, t_, f'Buku Gambar {g}')
            pic_box(s, MED + f'image{g + 3}.png', x, 2.6, w, 4.75)
            box(s, x, 7.45, w, 1.65, fill=LIGHT, line=LINE, margin=0.18, anchor=MSO_ANCHOR.MIDDLE, paras=[[('Interpretasi  ', 12, True, TEAL), (ex, 11.5, False, DARK)]])
        if len(pg) == 1:
            hdr(s, 10.15, 2.05, 8.95, 'MAPE uji penuh (versi dengan COVID)')
            cats = ['ODTW', 'Wisatawan', 'Tenaga Kerja', 'Hotel', 'Lahan', 'TPK', 'PDRB', 'Malam Menginap', 'Investasi']
            vals = [5.68, 12.06, 12.39, 13.16, 13.43, 18.98, 25.06, 29.52, 33.54]
            cols = [GREEN.replace('C9F0D6', '2FA36B')] + ['39C0D3'] * 5 + ['FFD23B'] * 3
            chm = bar_chart(s, 10.15, 2.6, 8.95, 4.0, cats, [('MAPE (%)', vals)], ['39C0D3'], fmt_='0.0"%"', horizontal=True, point_colors=cols, fs=10)
            chm.category_axis.reverse_order = True
            T(s, 10.15, 6.62, 8.95, 0.3, [[('Hijau < 10% sangat baik · biru 10–20% baik · kuning 20–50% layak · tidak ada yang > 50%', 10, False, GREY, True)]])
            box(s, 10.15, 7.0, 8.95, 2.1, fill=YEL_L, line=YEL, margin=0.18, anchor=MSO_ANCHOR.MIDDLE, paras=[
                [('Rangkuman  ', 12, True, TEAL), ('Struktur tiap subsistem memadai (uji parsial). Di model penuh, galat pertumbuhan wisatawan merambat ke variabel hilir lewat jalur ekonomi. Akar masalah di satu titik ini ditelusuri lewat kalibrasi diagnostik Tahap 3.', 11.5, False, DARK)]])
        src(s, 'Sumber: Buku Subbab 4.5.2–4.5.3 (Gambar 25–41).')
