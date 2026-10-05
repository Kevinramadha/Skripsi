# ===================== G. ANALISIS SENSITIVITAS =====================
import json as _json
SENS = _json.load(open('/tmp/pptwork/v6/sens.json'))
RANGE_B = {'Rasio LPD/LPE': '0,60–0,90 (LPE tetap)', 'Rasio LPD/LPE (konsisten data)': '0,60–0,90 (LPE diturunkan ulang)', 'Bobot Daya Tarik': '0,50/0,25/0,25; 0,30/0,45/0,25; ⅓ masing-masing',
           'Laju Konversi Dasar (CI 95%)': '0,0034118–0,0851069', 'Elastisitas Daya Tarik ODTW': '0,2–0,4', 'Insentif Kebijakan': '0,1; 0,3; 0,5', 'Laju Penutupan Dasar ODTW': '0,01–0,07',
           'ODTW 2025 (nilai awal & referensi)': '189–218 unit', 'Lahan Per Hotel dan Akomodasi': '0,05–0,2 ha/unit', 'Lahan Per ODTW': '0,1–2,0 ha/unit', 'Kebijakan Konservasi Lahan': '0,25; 0,5; 0,75; 1,0',
           'Laju Demolisi Dasar': '0,02–0,08', 'TPK Ambang': '0,20–0,35', 'Batas Maksimum Efek ODTW': '1,25–1,875', 'Laju Keluar Dasar Tenaga Kerja': '0,05–0,10', 'Laju Kenaikan Produktivitas': '0–0,0154',
           'Waktu Penyesuaian Tenaga Kerja': '2–3 tahun'}
OUTS = ['Wisatawan', 'Lahan', 'PDRB', 'Hotel', 'TK', 'ODTW']


def G_rancangan(D):
    s = D.slide('Lampiran · Analisis Sensitivitas: Rancangan dan Rumus')
    sub(s, 'Dua bagian: ±10% satu per satu (Mai & Smith, 2018) dan rentang penuh untuk parameter asumsi dan tuas kebijakan')
    hdr(s, 0.9, 2.05, 8.95, 'Bagian A · Perubahan ±10%')
    steps(s, 0.9, 2.65, 8.95, [('Ubah satu parameter', '32 parameter, masing-masing −10% dan +10% dari nilai dasar; yang lain tetap.'),
                               ('Hitung perubahan keluaran 2050', 'Untuk enam keluaran: wisatawan, lahan, PDRB, hotel, TK, ODTW.'),
                               ('Peringkatkan', 'Berdasarkan nilai mutlak terbesar dari kedua arah; disajikan sebagai diagram tornado.')], h=0.95, size=11)
    formula(s, 0.9, 5.95, 8.95, 0.9, ['Perubahan % = (Keluaranₚ − Keluaran_BASE) ÷ Keluaran_BASE × 100%'], size=12.5)
    hdr(s, 10.15, 2.05, 8.95, 'Bagian B · Rentang penuh')
    steps(s, 10.15, 2.65, 8.95, [('Pilih kelompok', '17 kelompok: parameter asumsi dan dua tuas kebijakan.'),
                                 ('Jalankan seluruh titik rentang', 'Rentang sama dengan kalibrasi: triangulasi rujukan atau selang kepercayaan 95%.'),
                                 ('Ukur lebar ketidakpastian', 'Selisih hasil tertinggi dan terendah (poin persen terhadap BASE).')], h=0.95, size=11)
    formula(s, 10.15, 5.95, 8.95, 0.9, ['Lebar rentang = Keluaran_maks − Keluaran_min'], size=12.5)
    card(s, 0.9, 7.1, 18.2, 2.0, 'Ketentuan di kedua bagian', [
        ('Pasangan dihitung ulang:', 'LPE–LPD (rasio 0,75); TPK Ambang & Demolisi ↔ Sensitivitas Konstruksi; Penutupan ODTW ↔ Sensitivitas ODTW & Pembangunan Non-Investasi; Luas Lahan ↔ Kepadatan Ref. & RDDL Ref.'),
        ('Bobot Daya Tarik dinormalisasi ulang', 'agar tetap berjumlah 1; LPE dan LPD diturunkan ulang bila indeks Daya Tarik tahun dasar berubah.'),
        ('Tuas kebijakan tidak diuji di Bagian A', '(nilai dasarnya 0); nilai awal stock diubah lewat kondisi awal, bukan konstanta.')], size=10.5)
    src(s, 'Sumber: Buku Subbab 3.7.5.')


def _sens_rows(rows_):
    out = [['Rank', 'Parameter'] + sum([[o + ' −10%', '+10%'] for o in OUTS], [])]
    hl = {}
    for i, r in enumerate(rows_, 1):
        vals = [r[1], r[2], r[4], r[5], r[7], r[8], r[10], r[11], r[13], r[14], r[16], r[17]]
        out.append([str(r[19]), r[0]] + [('0' if abs(v) < 0.005 else fmt(v, 2)).replace('-', '−') for v in vals])
        for j, v in enumerate(vals):
            if abs(v) >= 10: hl[(i, j + 2)] = PINK
            elif abs(v) >= 5: hl[(i, j + 2)] = YEL_L
            elif abs(v) >= 1: hl[(i, j + 2)] = LIGHT
    return out, hl


def G_pm10(D):
    A = SENS['A']
    for k, part in enumerate([A[:16], A[16:]]):
        s = D.slide(f'Lampiran · Hasil Sensitivitas ±10%: Seluruh Parameter ({k + 1}/2)')
        sub(s, 'Perubahan keluaran tahun 2050 (%) terhadap simulasi dasar; diurutkan menurut pengaruh pada Jumlah Wisatawan')
        rows, hl = _sens_rows(part)
        tbl(s, 0.9, 2.05, 18.2, [0.6, 4.0] + [1.1333] * 12, rows, size=9.5, rowh=0.4, hl=hl, center=tuple([0] + list(range(2, 14))))
        T(s, 0.9, 9.0, 18.2, 0.3, [[('Warna: biru muda |x| ≥ 1% · kuning ≥ 5% · merah muda ≥ 10%. "Rank" = peringkat terhadap Jumlah Wisatawan (seri diberi peringkat sama).', 10, False, GREY, True)]])
        if k == 1:
            note(s, 'Batas Maksimum Efek ODTW dan Laju Keluar Dasar TK tidak berpengaruh pada keenam keluaran: batas ODTW tidak pernah aktif, dan keluar TK langsung diganti lewat penyerapan.', y=9.35, h=0.7)
        src(s, 'Sumber: Buku Subbab 4.7.1; hasil_sensitivitas_bagianA_konsisten.xlsx (sheet Peringkat Tornado).')


def G_peringkat(D):
    s = D.slide('Lampiran · Peringkat Sensitivitas ±10% per Keluaran')
    sub(s, 'Lima parameter paling berpengaruh untuk tiap keluaran; peringkat berbeda antarkeluaran')
    A = SENS['A']; idx = {'Wisatawan': (3, 19), 'Lahan': (6, 20), 'PDRB': (9, 21), 'Hotel': (12, 22), 'TK': (15, 23), 'ODTW': (18, 24)}
    for j, o in enumerate(OUTS):
        vi, ri = idx[o]
        top = sorted(A, key=lambda r: -r[vi])[:5]
        x = 0.9 + (j % 3) * 6.15; y = 2.05 + (j // 3) * 3.3; w = 5.9
        hdr(s, x, y, w, o + ' 2050')
        rows = [['#', 'Parameter', '|maks|']] + [[str(n + 1), r[0], fmt(r[vi], 2) + '%'] for n, r in enumerate(top)]
        tbl(s, x, y + 0.5, w, [0.4, 4.1, 1.4], rows, size=9.5, rowh=0.42, center=(0, 2))
    note(s, 'LPD peringkat 1 pada lima keluaran karena pertumbuhan bersih = LPE × Daya Tarik − LPD, dan kedua suku hampir seimbang. Laju Konversi Dasar hanya #13 untuk wisatawan tetapi #1 untuk lahan (6,64%); parameter kapasitas kamar hanya berpengaruh pada hotel (8,80%); Intensitas TK Awal hanya pada TK (10%).', y=8.75, h=1.25, title='Membaca')
    src(s, 'Sumber: Buku Subbab 4.7.1 (Tabel 56); hasil_sensitivitas_bagianA_konsisten.xlsx.')


def G_tornado(D):
    T_ = [(54, 'Jumlah Wisatawan', 'Asumsi menempati 4 dari 6 peringkat teratas: LPD, Bobot Kepadatan, Bobot ODTW (+ Kepadatan Ref.).'),
          (55, 'PDRB Pariwisata', 'Pola sama dengan wisatawan karena PDRB = pengeluaran × rasio nilai tambah; plus dua parameter ekonomi (12,8%).'),
          (56, 'Lahan Terbangun', 'Laju Konversi Dasar (6,64%) dan Luas Lahan Tersedia (2,67%) mendominasi; parameter lain < 0,3%.'),
          (57, 'Jumlah Hotel', 'LPD (37,0%) diikuti tiga parameter kapasitas kamar (8,80%) dan dua parameter permintaan malam (8,19%).'),
          (58, 'Tenaga Kerja', 'LPD (40,1%), lalu parameter ekonomi (12,6%) dan Intensitas TK Awal (10%) yang hanya memengaruhi TK.'),
          (59, 'Jumlah ODTW', 'LPD (16,6%), lalu jalur investasi → ODTW (Sensitivitas ODTW, rasio investasi, ekonomi ±7,2%).')]
    for k in range(2):
        s = D.slide(f'Lampiran · Diagram Tornado Sensitivitas ±10% ({k + 1}/2)')
        sub(s, 'Batang menunjukkan perubahan keluaran 2050 bila parameter diturunkan atau dinaikkan 10%')
        for j, (im, t_, ex) in enumerate(T_[k * 3:(k + 1) * 3]):
            x = 0.9 + j * 6.15; w = 5.9
            hdr(s, x, 2.05, w, t_, f'Buku Gambar {im - 3}')
            pic_box(s, MED + f'image{im}.png', x, 2.6, w, 4.9)
            box(s, x, 7.6, w, 1.5, fill=LIGHT, line=LINE, margin=0.15, anchor=MSO_ANCHOR.MIDDLE, paras=[[(ex, 11, False, DARK)]])
        src(s, 'Sumber: Buku Subbab 4.7.1 (Gambar 51–56).')


def G_rentang(D):
    s = D.slide('Lampiran · Hasil Sensitivitas Rentang Penuh: 17 Kelompok')
    sub(s, 'Hasil terendah dan tertinggi wisatawan 2050 (% thd BASE) serta lebar rentang (poin persen) pada enam keluaran')
    rows = [['Kelompok parameter', 'Rentang uji', 'Wis. min', 'Wis. maks', 'Lebar Wis.', 'Lahan', 'PDRB', 'Hotel', 'TK', 'ODTW']]
    hl = {}
    for i, r in enumerate(SENS['B'], 1):
        rows.append([r[0], RANGE_B.get(r[0], ''), pct(r[1], 2).replace('+', ''), pct(r[2], 2)] + [fmt(v, 2) for v in r[13:19]])
        for j, v in enumerate(r[13:19]):
            if v >= 50: hl[(i, 4 + j)] = PINK
            elif v >= 10: hl[(i, 4 + j)] = YEL_L
            elif v >= 1: hl[(i, 4 + j)] = LIGHT
    for c in range(2):
        hl[(6, c)] = GREEN; hl[(11, c)] = GREEN
    tbl(s, 0.9, 2.05, 18.2, [4.1, 3.9, 1.15, 1.15, 1.3, 1.3, 1.3, 1.3, 1.3, 1.4], rows, size=9.5, rowh=0.38, hl=hl, center=tuple(range(2, 10)))
    T(s, 0.9, 9.0, 18.2, 0.3, [[('Lebar (poin %): biru muda ≥ 1 · kuning ≥ 10 · merah muda ≥ 50. Baris hijau = tuas kebijakan.', 10, False, GREY, True)]])
    note(s, 'Rasio LPD/LPE paling menentukan (lebar 153,57 poin bila LPE tetap; 69,65 bila LPE diturunkan ulang) sekaligus tidak teridentifikasi dari data (Tahap 3 kalibrasi).', y=9.35, h=0.7)
    src(s, 'Sumber: Buku Subbab 4.7.2 (Tabel 57); hasil_sensitivitas_bagianB_konsisten.xlsx (sheet Lebar Rentang, Hasil Rentang Penuh).')


def G_rentang2(D):
    s = D.slide('Lampiran · Rentang Penuh: Sumber Ketidakpastian dan Respons Tuas')
    sub(s, 'Tiga sumber ketidakpastian terbesar dibawa ke uji kekokohan skenario; dua tuas berperilaku sangat berbeda')
    B = [r for r in SENS['B'] if r[13] >= 1 or r[14] >= 0.5]
    cats = [r[0].replace(' (nilai awal & referensi)', '').replace(' (konsisten data)', ' (konsisten)') for r in B]
    hdr(s, 0.9, 2.05, 10.4, 'Lebar rentang (poin %): Jumlah Wisatawan dan Lahan Terbangun 2050')
    ch = bar_chart(s, 0.9, 2.6, 10.4, 6.5, cats, [('Jumlah Wisatawan', [r[13] for r in B]), ('Lahan Terbangun', [r[14] for r in B])], ['0B5E6E', 'FFD23B'], fmt_='0.0', horizontal=True, legend=True, fs=10)
    ch.category_axis.reverse_order = True
    hdr(s, 11.6, 2.05, 7.5, 'Respons dua tuas kebijakan (% thd BASE)')
    rows = [['Nilai', 'Wisatawan', 'Lahan', 'ODTW'],
            ['Insentif 0,1', '+2,56%', '+0,05%', '+7,25%'], ['Insentif 0,5', '+12,92%', '+0,23%', '+37,82%'],
            ['Konservasi 0,25', '+0,06%', '−0,23%', '+0,02%'], ['Konservasi 1,0', '+0,25%', '−0,91%', '+0,07%']]
    tbl(s, 11.6, 2.6, 7.5, [2.4, 1.7, 1.7, 1.7], rows, size=11, rowh=0.45, center=(1, 2, 3), bold_first=True)
    card(s, 11.6, 5.0, 7.5, 4.1, 'Membaca', [
        ('Insentif:', 'respons hampir linear; pengaruh terbesar justru pada ODTW (lebar 30,58 poin).'),
        ('Konservasi:', 'bahkan diterapkan penuh hanya menurunkan lahan 0,91%, karena konversi pariwisata hanya ±23 ha/th dari ±2.000 ha/th total konversi.'),
        ('Dibawa ke uji kekokohan:', 'rasio LPD/LPE, bobot Daya Tarik, dan Laju Konversi Dasar.')], size=11)
    src(s, 'Sumber: Buku Subbab 4.7.2; hasil_sensitivitas_bagianB_konsisten.xlsx. Kelompok dengan lebar < 1 poin (wisatawan) dan < 0,5 poin (lahan) tidak ditampilkan di grafik.')
