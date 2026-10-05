# ===================== C. STRUKTUR MODEL =====================
def C_kandidat(D):
    s = D.slide('Lampiran · Hasil Evaluasi Kandidat Variabel CLD')
    sub(s, 'Seluruh kandidat dipertahankan; hanya peran tenaga kerja yang direvisi')
    R = [('Permintaan & daya tarik', 'Jumlah Wisatawan', 'Besarnya aktivitas kunjungan; pusat mekanisme pertumbuhan dan kepadatan', 'Dipertahankan', 'Variabel utama R1, R2, B1, B2'),
         ('', 'Laju Kedatangan Wisatawan', 'Proses perubahan Jumlah Wisatawan', 'Dipertahankan', 'Aliran penghubung daya tarik dan kunjungan'),
         ('', 'Daya Tarik Destinasi Wisata', 'Menghubungkan atraksi, kepadatan, dan daya dukung dengan kedatangan', 'Dipertahankan', 'Penghubung utama loop penguat dan penyeimbang'),
         ('', 'Kepadatan Wisatawan', 'Tekanan jumlah kunjungan terhadap ruang destinasi', 'Dipertahankan', 'Mekanisme pembatas B1'),
         ('Atraksi/ODTW', 'Jumlah ODTW', 'Ketersediaan atraksi pendukung daya tarik', 'Dipertahankan', 'Jalur ekonomi–atraksi R2'),
         ('Ekonomi & investasi', 'Pengeluaran Wisatawan', 'Menyalurkan kunjungan ke aktivitas ekonomi', 'Dipertahankan', 'Jalur ekonomi R2'),
         ('', 'PDRB Sektor Pariwisata', 'Nilai tambah ekonomi aktivitas wisata', 'Dipertahankan', 'Menghubungkan pengeluaran, investasi, kebutuhan TK'),
         ('', 'Investasi Sektor Pariwisata', 'Sumber pengembangan kapasitas', 'Dipertahankan', 'Mendorong pembangunan ODTW dan konstruksi'),
         ('Akomodasi', 'Jumlah Hotel dan Akomodasi', 'Kapasitas akomodasi tersedia', 'Dipertahankan', 'Stock utama subsistem akomodasi'),
         ('', 'Rasio Permintaan thd Kapasitas Kamar', 'Tekanan permintaan relatif terhadap kapasitas', 'Dipertahankan', 'Sinyal konstruksi pada B3'),
         ('', 'Laju Konstruksi Hotel dan Akomodasi', 'Penambahan kapasitas akomodasi', 'Dipertahankan', 'Flow akomodasi; pendorong konversi lahan'),
         ('Lahan & daya dukung', 'Rasio Daya Dukung Lahan', 'Proporsi kapasitas fisik yang masih tersedia', 'Dipertahankan', 'Pembatas daya tarik pada B2'),
         ('Tenaga kerja', 'Tenaga Kerja Pariwisata', 'Keluaran aktivitas ekonomi; tidak diberi pengaruh langsung ke pembangunan ODTW', 'Dipertahankan, peran direvisi', 'Indikator keluaran dan bagian B4'),
         ('', 'Selisih Tenaga Kerja Dibutuhkan', 'Kesenjangan kebutuhan dan TK aktual', 'Dipertahankan', 'Sinyal penyesuaian B4'),
         ('', 'Laju Penyerapan Tenaga Kerja', 'Penyesuaian TK menuju kebutuhan', 'Dipertahankan', 'Flow penyesuaian B4')]
    rows = [['Kelompok', 'Kandidat variabel', 'Hasil evaluasi', 'Status', 'Peran akhir dalam CLD']] + [list(r) for r in R]
    hl = {(13, 3): YEL_L}
    for i in range(1, 16):
        if i != 13: hl[(i, 3)] = GREEN
    gf = tbl(s, 0.9, 2.05, 18.2, [2.4, 3.6, 5.6, 2.2, 4.4], rows, size=10, rowh=0.43, hl=hl, center=(3,))
    for r in range(1, 16):
        c = gf.table.cell(r, 0).text_frame.paragraphs[0]
        if c.runs: c.runs[0].font.bold = True; c.runs[0].font.color.rgb = rgb(TEAL)
    note(s, 'Hubungan langsung Tenaga Kerja → pembangunan ODTW dihapus karena tidak ada dasar kausal yang memadai. Populasi, limbah, dan air (ada di Mai & Smith, 2018) sejak awal di luar batas model, sehingga tidak dihitung sebagai kandidat yang ditolak.', y=9.0, h=0.85)
    src(s, 'Sumber: Buku Subbab 4.1.1 (Tabel 24); kriteria evaluasi pada Tabel 11.')


def C_loop(D):
    s = D.slide('Lampiran · Loop Umpan Balik dan Polaritas Hubungan Kunci')
    sub(s, 'Dua reinforcing loop dan empat balancing loop membentuk hipotesis dinamis penelitian')
    rows = [['Loop', 'Jenis', 'Rantai kausal ringkas', 'Makna'],
            ['R1', 'Reinforcing', 'Jumlah Wisatawan (+) → Laju Kedatangan (+) → Jumlah Wisatawan', 'Pertumbuhan wisatawan bersifat akumulatif.'],
            ['R2', 'Reinforcing', 'Wisatawan (+) → Pengeluaran (+) → PDRB (+) → Investasi (+) → Pembangunan ODTW (+) → ODTW (+) → Daya Tarik (+) → Kedatangan (+) → Wisatawan', 'Loop ekonomi–investasi–atraksi; jalur kerja Insentif Kebijakan.'],
            ['B1', 'Balancing', 'Wisatawan (+) → Kepadatan (+) → Daya Tarik (−) → Kedatangan (−) → Wisatawan', 'Kepadatan menekan daya tarik; rem pertumbuhan.'],
            ['B2', 'Balancing', 'Wisatawan (+) → permintaan/investasi (+) → Konstruksi & Pembangunan ODTW (+) → Konversi Lahan (+) → Lahan Terbangun (+) → RDDL (−) → Daya Tarik (+) → Kedatangan (+) → Wisatawan', 'Ekspansi fasilitas menekan daya dukung lahan; jalur kerja Konservasi Lahan.'],
            ['B3', 'Balancing', 'Hotel (+) → Kapasitas Kamar (+) → Rasio Permintaan/Kapasitas (−) → Konstruksi (+) → Hotel', 'Penambahan kapasitas menahan konstruksi berikutnya.'],
            ['B4', 'Balancing', 'TK (+) → Selisih TK Dibutuhkan (−) → Penyerapan TK (+) → TK', 'Goal-seeking tenaga kerja; dampaknya terbatas pada TK.']]
    hl = {(1, 1): GREEN, (2, 1): GREEN}
    for r in range(3, 7): hl[(r, 1)] = PINK
    tbl(s, 0.9, 2.05, 11.2, [0.7, 1.5, 5.8, 3.2], rows, size=10, rowh=0.95, hl=hl, center=(0, 1))
    pic_box(s, MED + 'image11.png', 12.4, 2.05, 6.7, 6.3)
    T(s, 12.4, 8.4, 6.7, 0.4, [[('Causal loop diagram final (Buku Gambar 7)', 10, False, GREY, True)]], align=PP_ALIGN.CENTER)
    note(s, 'Polaritas dibaca ceteris paribus: tanda (+) berarti kenaikan penyebab membuat akibat lebih tinggi dibanding tanpa kenaikan itu; tanda (−) sebaliknya (Sterman, 2000; Richardson, 1997).', y=9.0, h=0.8)
    src(s, 'Sumber: Buku Subbab 4.1.3 (Tabel 26).')


def C_peran(D):
    s = D.slide('Lampiran · Peran Variabel Hasil Konversi CLD ke SFD')
    sub(s, '61 variabel: 5 stock, 10 flow, 11 auxiliary, 35 parameter; ditambah nilai awal stock tahun dasar 2025')
    G = [('Stock (5)', TEAL, ['Jumlah Wisatawan', 'Jumlah Hotel dan Akomodasi', 'Jumlah Objek Daya Tarik Wisata', 'Tenaga Kerja Pariwisata', 'Lahan Terbangun']),
         ('Flow (10)', '2A9DB0', ['Laju Kedatangan Wisatawan', 'Laju Penurunan Wisatawan', 'Laju Konstruksi Hotel dan Akomodasi', 'Laju Demolisi Hotel dan Akomodasi', 'Laju Pembangunan/Penambahan ODTW',
                                  'Laju Penutupan ODTW', 'Laju Penyerapan Tenaga Kerja Pariwisata', 'Laju Keluar Tenaga Kerja Pariwisata', 'Laju Konversi Lahan Pariwisata', 'Laju Konversi Lahan Non-Pariwisata']),
         ('Auxiliary (11)', CYAN, ['PDRB Sektor Pariwisata', 'Total Malam Menginap', 'Pengeluaran Wisatawan', 'Tingkat Penghunian Kamar (TPK)', 'Investasi Sektor Pariwisata', 'Daya Tarik Destinasi Wisata',
                                   'Kepadatan Wisatawan', 'Rasio Daya Dukung Lahan', 'Intensitas Tenaga Kerja', 'Tenaga Kerja Dibutuhkan', 'Rasio Permintaan terhadap Kapasitas Kamar'])]
    xs = [0.9, 4.6, 9.0]; ws = [3.5, 4.2, 4.3]
    for (t_, col, items), x, w in zip(G, xs, ws):
        hdr(s, x, 2.05, w, t_, fill=col)
        paras = [[(f'{i + 1}. ', 10.5, True, TEAL), (v, 10.5, False, DARK)] for i, v in enumerate(items)]
        box(s, x, 2.6, w, 4.55, fill=LIGHT, line=LINE, paras=paras, margin=0.15)
    P = ['Pengeluaran per Kunjungan', 'Rasio Nilai Tambah Pariwisata', 'Rasio Investasi thd PDRB', 'Proporsi Wisatawan Menginap', 'Rata-rata Lama Menginap Tamu', 'Tingkat Penghunian Ganda Kamar',
         'Rata-rata Kamar per Unit', 'Malam Tersedia per Kamar', 'Luas Lahan Tersedia', 'Intensitas TK Awal', 'Laju Kenaikan Produktivitas', 'Laju Pertumbuhan Eksternal', 'Laju Penurunan Dasar',
         'Sensitivitas Konstruksi thd TPK', 'TPK Ambang', 'Sensitivitas ODTW thd Investasi', 'Pembangunan ODTW Non Investasi', 'Laju Penutupan Dasar ODTW', 'Laju Konversi Dasar',
         'Laju Demolisi Dasar', 'Laju Keluar Dasar TK', 'Bobot ODTW', 'Bobot Kepadatan', 'Bobot Daya Dukung Lahan', 'Elastisitas Daya Tarik ODTW', 'Batas Maksimum Efek ODTW',
         'Lahan per Hotel dan Akomodasi', 'Lahan per ODTW', 'Waktu Penyesuaian TK', 'ODTW Referensi', 'Kepadatan Referensi', 'RDDL Referensi', 'Tahun Dasar Intensitas TK', 'Insentif Kebijakan', 'Kebijakan Konservasi Lahan']
    hdr(s, 13.6, 2.05, 5.5, 'Parameter (35)', fill=GRY)
    half = 18
    for k, chunk in enumerate([P[:half], P[half:]]):
        paras = [[(f'{i + 1 + k * half}. ', 9, True, GREY), (v, 9, False, DARK)] for i, v in enumerate(chunk)]
        box(s, 13.6 + k * 2.75, 2.6, 2.75, 4.55, fill='F3F5F6', line=LINE, paras=paras, margin=0.08)
    hdr(s, 0.9, 7.35, 18.2, 'Nilai awal stock tahun dasar 2025')
    rows = [['Stock', 'Jumlah Wisatawan', 'Hotel dan Akomodasi', 'Jumlah ODTW', 'Tenaga Kerja Pariwisata', 'Lahan Terbangun'],
            ['Nilai awal', '40.695.654 kunjungan', '2.291 unit', '201 unit', '364.994 jiwa', '55.029,54 ha'],
            ['Sumber', 'BPS DIY', 'BPS DIY', 'BPS DIY & estimasi NTL', 'Sakernas (KBLI I, R–U)', 'Dynamic World']]
    tbl(s, 0.9, 7.9, 18.2, [2.0, 3.3, 3.1, 3.2, 3.3, 3.3], rows, size=10.5, rowh=0.4, center=(1, 2, 3, 4, 5))
    src(s, 'Sumber: Buku Subbab 4.1.4 (Tabel 27–28).', y=10.15)


def C_batas(D):
    s = D.slide('Lampiran · Batas Model (1/3): Ringkasan Kecukupan')
    sub(s, 'Model boundary chart: apa yang dihitung model, apa yang menjadi input, dan apa yang sengaja dikeluarkan')
    cols = [('Dihitung model (endogen): 26 variabel', TEAL, ['Jumlah wisatawan, kedatangan, penurunan', 'Jumlah akomodasi, konstruksi, demolisi', 'Jumlah ODTW, pembangunan, penutupan',
                                                                'PDRB, pengeluaran, investasi pariwisata', 'Tenaga kerja, penyerapan, keluar', 'Lahan terbangun dan konversinya',
                                                                'Daya tarik, kepadatan, daya dukung lahan', 'Okupansi dan tekanan permintaan kamar']),
            ('Input dari luar model (eksogen): 35 parameter', '2A9DB0', ['Pendorong permintaan eksternal', 'Perilaku dan karakteristik wisatawan', 'Karakteristik struktural akomodasi',
                                                                          'Koefisien hasil derivasi data historis', 'Koefisien dan batas kebutuhan lahan', 'Parameter dan nilai referensi daya tarik',
                                                                          'Parameter tenaga kerja', 'Pembangunan ODTW non-investasi', 'Dua tuas kebijakan']),
            ('Dikeluarkan: 15 aspek', GRY, ['Pemisahan wisman dan wisnus', 'Harga dan daya saing harga', 'Aksesibilitas dan transportasi', 'Promosi dan citra destinasi', 'Kualitas SDM dan sertifikasi usaha',
                                            'Musim dan fluktuasi bulanan', 'Kejadian mendadak (pandemi, bencana)', 'Persaingan antardestinasi', 'Zonasi rinci RTRW', 'Dampak lingkungan dan daya dukung sosial',
                                            'Distribusi manfaat ekonomi', 'Investasi pemerintah; perpindahan TK; harga lahan'])]
    for k, (t_, col, items) in enumerate(cols):
        x = 0.9 + k * 6.15
        hdr(s, x, 2.1, 5.9, t_, fill=col)
        bullets(s, x + 0.1, 2.75, 5.7, 5.6, items, size=12)
    note(s, 'Konsekuensinya, hasil model dibaca sebagai lintasan jangka panjang dalam kondisi normal; model tidak dipakai menjelaskan harga, promosi, musim, atau kejadian mendadak. Daftar per variabel ada di dua slide berikut.', y=8.6, h=0.95)
    src(s, 'Sumber: Buku Subbab 3.7.4 (Tabel 13) dan 4.4.2.')

    EX = [('Laju Pertumbuhan Eksternal', '0,27726 /th', 'Tren permintaan wisata nasional, di luar kendali DIY'), ('Laju Penurunan Dasar', '0,207945 /th', 'Preferensi dan perpindahan pasar wisatawan'),
          ('Pengeluaran per Kunjungan', '0,00272 miliar Rp', 'Pola belanja wisatawan'), ('Rasio Nilai Tambah Pariwisata', '0,1531', 'Struktur nilai tambah sektor, berubah lambat'),
          ('Rasio Investasi thd PDRB', '0,0488', 'Perilaku investasi historis 2015–2025'), ('Sensitivitas Konstruksi thd TPK', '2,3139', 'Derivasi identitas stok-aliran akomodasi'),
          ('TPK Ambang', '0,275', 'Tingkat hunian pemicu konstruksi, dari data okupansi'), ('Laju Demolisi Dasar', '0,05 /th', 'Umur operasi usaha akomodasi'),
          ('Sensitivitas ODTW thd Investasi', '0,01052', 'Derivasi identitas stok-aliran ODTW'), ('Pembangunan ODTW Non Investasi', '5,427 unit/th', 'Anggaran publik dan inisiatif masyarakat'),
          ('Laju Penutupan Dasar ODTW', '0,0499 /th', 'Umur usaha ODTW, dari distribusi umur BPS'), ('Laju Konversi Dasar', '0,0436 /th', 'Konversi lahan nonpariwisata, di luar fokus model'),
          ('Lahan per Hotel dan Akomodasi', '0,1 ha/unit', 'Asumsi tapak bangunan akomodasi'), ('Lahan per ODTW', '0,5 ha/unit', 'Asumsi tapak fasilitas terbangun ODTW'),
          ('Luas Lahan Tersedia', '317.036 ha', 'Luas wilayah administratif DIY'), ('Proporsi Wisatawan Menginap', '0,2058', 'Pola perilaku wisatawan'),
          ('Rata-rata Lama Menginap Tamu', '1,427 malam', 'Pola perilaku wisatawan'), ('Tingkat Penghunian Ganda Kamar', '2,07', 'Karakteristik penggunaan kamar'),
          ('Rata-rata Kamar per Unit', '21,4168 kamar', 'Karakteristik struktural akomodasi'), ('Malam Tersedia per Kamar', '329,03 malam', 'Hari operasi efektif kamar per tahun'),
          ('Bobot ODTW', '0,40', 'Kerangka teori daya saing destinasi'), ('Bobot Kepadatan', '0,35', 'Kerangka teori, memenuhi syarat kestabilan'), ('Bobot Daya Dukung Lahan', '0,25', 'Kerangka teori'),
          ('Elastisitas Daya Tarik ODTW', '0,3', 'Asumsi diminishing returns'), ('Batas Maksimum Efek ODTW', '1,5', 'Kejenuhan efek ODTW, syarat kestabilan'),
          ('ODTW Referensi', '201 unit', 'Kondisi 2025 untuk normalisasi'), ('Kepadatan Referensi', '128,363 kunj./ha', 'Kondisi 2025'), ('RDDL Referensi', '0,8264', 'Kondisi 2025'),
          ('Tahun Dasar Intensitas TK', '2025', 'Tahun acuan peluruhan intensitas TK'), ('Intensitas TK Awal', '21,5366 jiwa/miliar Rp', 'Produktivitas TK tahun dasar'),
          ('Laju Kenaikan Produktivitas', '0,0110 /th', 'Tren produktivitas riil 2015–2025'), ('Laju Keluar Dasar TK', '0,03 /th', 'Masa kerja sampai usia pensiun'),
          ('Waktu Penyesuaian TK', '1 tahun', 'Kecepatan perekrutan sektor jasa'), ('Insentif Kebijakan', '0 (BAU)', 'Tuas kebijakan, per skenario'), ('Kebijakan Konservasi Lahan', '0 (BAU)', 'Tuas kebijakan, per skenario')]
    for part in range(2):
        s = D.slide(f'Lampiran · Batas Model (2/3): Variabel Eksogen ({part + 1}/2)')
        sub(s, 'Nilai dan alasan setiap parameter diperlakukan sebagai input dari luar model')
        chunk = EX[part * 18:(part + 1) * 18]
        rows = [['No', 'Variabel eksogen', 'Nilai', 'Alasan diperlakukan eksogen']] + [[str(i + 1 + part * 18), a, b, c] for i, (a, b, c) in enumerate(chunk)]
        tbl(s, 0.9, 2.05, 18.2, [0.6, 5.0, 3.2, 9.4], rows, size=10.5, rowh=0.4, center=(0, 2))
        src(s, 'Sumber: Buku Subbab 3.7.4 (Tabel 14) dan 4.4.2 (Tabel 38).')

    s = D.slide('Lampiran · Batas Model (3/3): Aspek yang Dikeluarkan')
    sub(s, 'Setiap aspek dicatat alasan dan konsekuensinya agar jelas sejauh mana kesimpulan berlaku')
    X = [('Pemisahan wisman dan wisnus', 'Wisnus mendominasi kunjungan DIY; menambah stok tanpa pertanyaan kebijakan berbeda', 'Perbedaan pola belanja dan lama tinggal tidak terlihat'),
         ('Harga dan daya saing harga', 'Tidak ada indeks harga pariwisata tingkat provinsi', 'Penyeimbang lewat harga tidak tercakup'),
         ('Aksesibilitas dan transportasi', 'Ditentukan kebijakan nasional', 'Efeknya tersirat dalam laju pertumbuhan eksternal'),
         ('Promosi, pemasaran, citra', 'Data anggaran dan efektivitas promosi tidak tersedia tahunan', 'Tersirat dalam laju pertumbuhan eksternal'),
         ('Kualitas SDM dan sertifikasi', 'Data tidak lengkap; fokus pada jumlah, bukan mutu', 'Perbedaan mutu layanan tidak terlihat'),
         ('Musim dan fluktuasi bulanan', 'Satuan waktu model tahunan', 'Okupansi puncak musim ramai tidak tergambar'),
         ('Kejadian mendadak: pandemi, erupsi, gempa', 'Peristiwa acak di luar struktur umpan balik', 'Lintasan digambarkan tanpa kejadian mendadak'),
         ('Persaingan antardestinasi', 'Membutuhkan model multi-destinasi', 'Perpindahan wisatawan ke destinasi lain tidak dimodelkan'),
         ('Zonasi rinci RTRW dan kawasan lindung', 'Model memakai luas wilayah administratif', 'Daya dukung lahan cenderung terlalu longgar'),
         ('Dampak lingkungan: sampah, air, emisi', 'Data provinsi tidak konsisten', 'Lingkungan hanya diwakili lahan terbangun'),
         ('Daya dukung sosial budaya', 'Sulit diukur kuantitatif di tingkat provinsi', 'Aspek sosial keberlanjutan tidak terwakili'),
         ('Distribusi manfaat ekonomi', 'Model bekerja pada tingkat agregat', 'Tidak menjawab siapa penerima manfaat'),
         ('Investasi pemerintah (APBN/APBD)', 'Data investasi memakai realisasi PMA dan PMDN', 'Pembangunan pemerintah masuk jalur non-investasi eksogen'),
         ('Perpindahan TK antarsektor', 'Sakernas tidak menerbitkan data perpindahan sektor', 'Laju keluar TK merupakan batas bawah'),
         ('Harga dan kepemilikan lahan', 'Tidak ada seri harga lahan tingkat provinsi', 'Hambatan ekonomi konversi lahan tidak dimodelkan')]
    rows = [['No', 'Aspek', 'Alasan dikeluarkan', 'Konsekuensi terhadap hasil']] + [[str(i + 1)] + list(x) for i, x in enumerate(X)]
    tbl(s, 0.9, 2.05, 18.2, [0.6, 4.6, 6.6, 6.4], rows, size=10.5, rowh=0.46, center=(0,))
    src(s, 'Sumber: Buku Subbab 3.7.4 (Tabel 15) dan 4.4.2 (Tabel 39).')


PARAM = {
 'Data statistik resmi': ('Parameter Berbasis Data Statistik Resmi', 'Diambil langsung atau dihitung sederhana dari data resmi; rujukan mendukung bentuk hubungan, bukan nilainya', [
  ('1', 'Pengeluaran per Kunjungan (e)', '0,00272021 miliar Rp/kunjungan', 'e = Pengeluaran wisatawan₂₀₂₅ ÷ Jumlah wisatawan₂₀₂₅', 'Menjaga jalur ekonomi sisi permintaan; nilai tahun dasar karena seri historis sangat bervariasi', 'BPS: wisnus dan Passenger Exit Survey (wisman)', 'Jones, Munday & Roberts (2003); kerangka TSA'),
  ('2', 'Rasio Nilai Tambah Pariwisata (r_NT)', '0,153094 Dmnl', 'r_NT = PDRB pariwisata₂₀₂₅ ÷ Pengeluaran wisatawan₂₀₂₅', 'Mengubah pengeluaran bruto menjadi nilai tambah agar tidak dihitung ganda', 'PDRB ADHK I, R–U (BPS DIY); pengeluaran wisatawan', 'Jones et al. (2003); TSA'),
  ('3', 'Rasio Investasi thd PDRB (r_I)', '0,0488174 Dmnl', 'r_I = Σ Investasiₜ ÷ Σ PDRBₜ,  t = 2015–2025', 'Rasio kumulatif meredam fluktuasi tahunan investasi', 'PMA + PMDN pariwisata (BKPM); PDRB ADHK (BPS DIY)', 'Harrod (1939); Domar (1946)'),
  ('4', 'Proporsi Wisatawan Menginap (p)', '0,2058 Dmnl', 'p = Wisatawan menginap₂₀₂₅ ÷ Jumlah wisatawan₂₀₂₅', 'Hanya wisatawan menginap yang menimbulkan permintaan kamar', 'Tamu menginap dan jumlah wisatawan, BPS 2025', 'UNWTO (2008), IRTS 2008'),
  ('5', 'Rata-rata Lama Menginap (LOS)', '1,427 malam/kunjungan', 'LOS = Total malam₂₀₂₅ ÷ Wisatawan menginap₂₀₂₅', 'Mengubah wisatawan menginap menjadi permintaan malam', 'Publikasi TPK, BPS DIY', 'Mai & Smith (2018); Alegre & Pou (2006); Gössling et al. (2018)'),
  ('6', 'Tingkat Penghunian Ganda (TPG)', '2,07 orang/kamar', 'Nilai BPS tahun dasar 2025', 'Mengubah malam tamu menjadi malam kamar, konsisten dengan definisi TPK', 'Publikasi TPK, BPS DIY', 'Definisi operasional BPS'),
  ('7', 'Rata-rata Kamar per Unit (K_unit)', '21,4168 kamar/unit', 'K_unit = Jumlah kamar₂₀₂₅ ÷ Jumlah unit₂₀₂₅', 'Menghubungkan stok unit akomodasi dengan kapasitas kamar', 'Statistik Hotel & Akomodasi Lain, BPS DIY', 'Identitas kapasitas; definisi BPS'),
  ('8', 'Malam Tersedia per Kamar (M)', '329,03 malam/kamar', 'M = Σ(Total malamₜ ÷ TPGₜ) ÷ Σ(TPKₜ × Kamarₜ),  2015–2025', 'Kapasitas malam kamar konsisten dengan TPK historis, tidak diasumsikan 365', 'Malam tamu, TPG, TPK, kamar (BPS DIY)', 'Identitas TPK BPS'),
  ('9', 'Luas Lahan Tersedia (A)', '317.036 ha', 'A = luas wilayah administratif DIY', 'Penyebut kepadatan dan batas fisik lahan agregat', 'Kepmendagri, dikutip BPS DIY', 'Definisi batas wilayah penelitian'),
  ('10', 'Intensitas TK Awal (i₀)', '21,5366 jiwa/miliar Rp', 'i₀ = TK pariwisata₂₀₂₅ ÷ PDRB pariwisata₂₀₂₅', 'Kebutuhan TK per unit output pada tahun dasar', 'TK KBLI I, R–U (BPS) dan PDRB ADHK 2025', 'Hamermesh (1993); Kapsos (2005)'),
  ('11', 'Laju Kenaikan Produktivitas (g)', '0,0110205 /tahun', 'ln(TKₜ/PDRBₜ) = a + b·t;  g = −b;  iₜ = i₀·e^(−g(t−2025))', 'Regresi log-linear menjaga intensitas tetap positif', 'Rasio TK/PDRB, BPS 2015–2025', 'Kapsos (2005)')]),
 'Identitas stok-aliran': ('Parameter Hasil Penurunan Identitas Stok-Aliran', 'Diturunkan dari perubahan stok teramati dan komponen alirannya; parameter berpasangan dihitung ulang bersama', [
  ('12', 'Laju Pertumbuhan Eksternal (LPE)', '0,27726 /tahun', 'LPE = g₂₀₂₄→₂₀₂₅ ÷ (DT₂₀₂₄ − r) = 0,06716 ÷ (0,99223 − 0,75)', 'Euler: memakai daya tarik tahun awal periode; berpasangan dengan LPD', 'Wisatawan 2024–2025; daya tarik 2024', 'Sterman (2000); Mai & Smith (2018)'),
  ('13', 'Laju Penurunan Dasar (LPD)', '0,207945 /tahun', 'LPD = r × LPE,  r = 0,75', 'Agar pertumbuhan bersih 2024–2025 direproduksi; r asumsi struktural, diuji sensitivitas', 'Wisatawan 2024–2025; hasil LPE', 'Sterman (2000)'),
  ('14', 'Sensitivitas Konstruksi thd TPK (S_H)', '2,31385 unit/(miliar Rp·tahun)', 'Konstr*ₜ = Hotelₜ − Hotelₜ₋₁ + d_H·Hotelₜ₋₁;  S_H = Σ Konstr*ₜ ÷ Σ[Invₜ·max(0, TPKₜ − TPK*)]', 'Konstruksi bruto tersirat menjaga identitas stok-aliran hotel', 'Hotel dan TPK (BPS); investasi (BKPM) 2015–2025', 'Wheaton & Rossoff (1998); Sterman (2000)'),
  ('15', 'TPK Ambang (TPK*)', '0,275 Dmnl', 'TPK terendah yang masih diikuti konstruksi tersirat positif (TPK 2021 = 0,2748)', 'Ambang hunian sebelum sinyal pembangunan aktif', 'TPK dan hotel, BPS DIY 2015–2025', 'Wheaton & Rossoff (1998), natural occupancy'),
  ('16', 'Sensitivitas ODTW thd Investasi (S_O)', '0,01052 unit/(miliar Rp·tahun)', 'Bruto = ΔODTW + d_O·ODTWₜ₋₁;  S_O = p_swasta·Σ Brutoₜ ÷ Σ Invₜ', 'Memisahkan pembangunan ODTW oleh swasta', 'ODTW BPS/NTL; BKPM; porsi pengelola swasta (Statistik ODTW 2024)', 'Fatina et al. (2023); Sterman (2000)'),
  ('17', 'Pembangunan ODTW Non Investasi (B_O)', '5,427 unit/tahun', 'B_O = (1 − p_swasta)·Σ Bruto ÷ jumlah tahun', 'Pembangunan pemerintah/komunitas di luar PMA+PMDN', 'ODTW 2015–2025; porsi non-swasta Statistik ODTW 2024', 'Formulasi model'),
  ('18', 'Laju Penutupan Dasar ODTW (d_O)', '0,0499327 /tahun', 'Penutupan = ODTW·d_O; d_O dari distribusi lama beroperasi, dikoreksi pertumbuhan stok', 'Mengubah distribusi umur usaha menjadi laju keluar normal', 'Statistik ODTW 2024 BPS; seri ODTW', 'Sterman (2000), average lifetime'),
  ('19', 'Laju Konversi Dasar (k)', '0,0436052 /tahun', 'ln Lₜ = a + β·t;  k = (e^β − 1) ÷ R̄DDL₂₀₁₆–₂₀₂₅ = 0,0354 ÷ 0,8121', 'Tekanan konversi nonpariwisata; perlambatan lewat RDDL', 'Lahan terbangun Dynamic World 2016–2025', 'Mai & Smith (2018)')]),
 'Ketentuan regulasi': ('Parameter Nilai Diadopsi dari Ketentuan Regulasi', 'Angka diambil dari ketentuan peraturan; tetap diuji sensitivitas', [
  ('20', 'Laju Demolisi Dasar (d_H)', '0,05 /tahun', 'd_H = 1 ÷ umur operasi rata-rata = 1 ÷ 20 tahun', 'Laju keluar normal dari konsep average lifetime; 20 tahun ditriangulasi dari umur manfaat bangunan (rentang 0,02–0,082)', 'Ketentuan umur manfaat bangunan permanen', 'Sterman (2000); Mai & Smith (2018); PP 36/2005; UU PPh (penyusutan)'),
  ('21', 'Laju Keluar Dasar TK (d_TK)', '0,03 /tahun', 'd_TK ≈ 1 ÷ (usia pensiun − usia mulai kerja) = 1 ÷ (59 − 25)', 'Seri keluar-masuk sektoral tidak tersedia; diproksi masa kerja efektif', 'PP 45/2015 Pasal 15; usia mulai kerja asumsi operasional', 'Sterman (2000); PP 45/2015')]),
 'Asumsi pemodelan': ('Parameter Asumsi Pemodelan', 'Ditetapkan peneliti berdasarkan teori, lalu diuji ±10% dan pada seluruh rentang nilainya', [
  ('22', 'Bobot ODTW (w_O)', '0,40 Dmnl', 'DT = w_O·min[M, (ODTW/ODTW_ref)^ε] + …', 'Porsi terbesar pada atraksi; tetap memenuhi syarat kestabilan', 'Asumsi; diuji perilaku dan sensitivitas', 'Ritchie & Crouch (2003); Butler (1980); OECD-JRC (2008); Mai & Smith (2018)'),
  ('23', 'Bobot Kepadatan (w_K)', '0,35 Dmnl', '… + w_K·min[1, K_ref ÷ Kepadatan] + …', 'Kepadatan sebagai faktor pembatas', 'Asumsi; sensitivitas', 'Ritchie & Crouch (2003); Butler (1980); OECD-JRC (2008)'),
  ('24', 'Bobot Daya Dukung Lahan (w_L)', '0,25 Dmnl', '… + w_L·(RDDL ÷ RDDL_ref);  w_O + w_K + w_L = 1', 'Menangkap tekanan lahan tanpa mendominasi indeks', 'Asumsi; sensitivitas', 'Ritchie & Crouch (2003); Mai & Smith (2018)'),
  ('25', 'Elastisitas Daya Tarik ODTW (ε)', '0,30 Dmnl', 'Efek ODTW = (ODTW ÷ ODTW_ref)^ε', 'Nilai < 1: diminishing returns', 'Asumsi; diuji 0–1', 'Sterman (2000); Mai & Smith (2018)'),
  ('26', 'Batas Maksimum Efek ODTW (M)', '1,50 Dmnl', 'min[M, (ODTW/ODTW_ref)^ε];  syarat w_O·M < LPD/LPE (0,60 < 0,75)', 'Saturasi efek ODTW maksimum 50% di atas referensi', 'Asumsi struktur; sensitivitas', 'Mai & Smith (2018), bounded multiplier'),
  ('27', 'Lahan per Hotel dan Akomodasi (a_H)', '0,10 ha/unit', 'Konversi pariwisata memuat Konstruksi × a_H', 'Data tapak per usaha tidak tersedia', 'Asumsi; pemeriksaan kewajaran', 'Koefisien fisik model (bukan angka regulasi)'),
  ('28', 'Lahan per ODTW (a_O)', '0,50 ha/unit', 'Konversi pariwisata memuat Pembangunan ODTW × a_O', 'Tapak fasilitas terbangun (parkir, loket, toilet, kios), bukan seluruh luas objek; diuji 0,1–2 ha', 'Komposisi ODTW BPS 2024; asumsi', 'PP 36/2010 Ps. 18; Permen LHK P.8/2019 (pembanding)'),
  ('29', 'Waktu Penyesuaian TK (τ)', '1 tahun', 'Penyerapan = max[0, Keluar + (TK_dibutuhkan − TK) ÷ τ]', 'Batas bawah = TIME STEP 1 tahun agar tidak overshoot pada Euler; diuji 1–3 tahun', 'Asumsi; sensitivitas', 'Sterman (2000); Forrester (1961)')]),
 'Normalisasi dan kebijakan': ('Parameter Normalisasi dan Tuas Kebijakan', 'Nilai acuan tahun dasar untuk normalisasi indeks dan dua tuas skenario kebijakan', [
  ('30', 'ODTW Referensi (ODTW_ref)', '201 unit', 'ODTW_ref = Jumlah ODTW 2025', 'Rasio ODTW bernilai 1 pada tahun dasar', 'ODTW 2025 (estimasi NTL)', 'Kerangka indeks daya tarik model'),
  ('31', 'Kepadatan Referensi (K_ref)', '128,363 kunjungan/ha', 'K_ref = Jumlah wisatawan₂₀₂₅ ÷ A = 40.695.654 ÷ 317.036', 'Kepadatan 2025 sebagai kondisi normal; lebih rendah tidak memberi bonus', 'Wisatawan 2025; luas DIY', 'Ritchie & Crouch (2003); Butler (1980)'),
  ('32', 'RDDL Referensi (RDDL_ref)', '0,826425 Dmnl', 'RDDL_ref = 1 − Lahan₂₀₂₅ ÷ A = 1 − 55.029,54 ÷ 317.036', 'Pengali lahan = 1 pada tahun dasar, menuju 0 saat lahan habis', 'Dynamic World 2025; luas DIY', 'Mai & Smith (2018), limited land multiplier'),
  ('33', 'Tahun Dasar Intensitas TK (t₀)', '2025', 't₀ = tahun dasar model', 'Agar iₜ = i₀ pada tahun dasar', 'Tahun dasar simulasi', 'Nilai acuan matematis'),
  ('34', 'Insentif Kebijakan (I)', 'BAU 0; Sustainable 0,1; DP 0,3', 'Investasi = PDRB × r_I × (1 + I)', 'Tuas skenario jalur R2; ketetapan peneliti, bukan target resmi', 'Ditetapkan peneliti (rentang 0–0,5)', 'UU 10/2009; Perda DIY 1/2012'),
  ('35', 'Kebijakan Konservasi Lahan (C)', 'BAU 0; Sustainable 1,0; DP 0', 'Konversi pariwisata = (Konstr·a_H + Pemb.ODTW·a_O) × (1 − C) × RDDL ÷ RDDL_ref', 'Menahan konversi dari pembangunan pariwisata; tidak menghentikan konversi nonpariwisata', 'Ditetapkan peneliti (rentang 0–1)', 'UU 26/2007; UU 41/2009; Perda DIY 6/2021; Permen LHK P.8/2019')])}


def C_parameter(D):
    for key, (title, desc, rows_) in PARAM.items():
        per = 6 if len(rows_) > 6 else len(rows_)
        n = (len(rows_) + per - 1) // per
        if key == 'Identitas stok-aliran': per, n = 4, 2
        if key == 'Asumsi pemodelan': per, n = 4, 2
        for k in range(n):
            chunk = rows_[k * per:(k + 1) * per]
            t_ = f'Lampiran · {title}' + (f' ({k + 1}/{n})' if n > 1 else '')
            s = D.slide(t_)
            sub(s, desc)
            rows = [['No', 'Parameter (notasi)', 'Nilai dan satuan', 'Rumus / cara penentuan', 'Dasar penetapan', 'Data dan sumber', 'Rujukan']] + [list(r) for r in chunk]
            rh = 7.6 / max(len(chunk), 4) if len(chunk) <= 4 else 1.18
            gf = tbl(s, 0.9, 2.05, 18.2, [0.5, 2.5, 2.0, 4.2, 3.4, 2.9, 2.7], rows, size=10.5, rowh=min(rh, 1.75), center=(0,))
            gf.table.rows[0].height = Inches(0.45)
            for r in range(1, len(rows)):
                cell = gf.table.cell(r, 3); cell.fill.solid(); cell.fill.fore_color.rgb = rgb(YEL_L)
                for run in cell.text_frame.paragraphs[0].runs: run.font.italic = True
                c2 = gf.table.cell(r, 1).text_frame.paragraphs[0].runs[0]; c2.font.bold = True; c2.font.color.rgb = rgb(TEAL)
            src(s, 'Sumber: Buku Subbab 3.4.2 (Tabel 3–8), Subbab 4.3 (Tabel 33–37), dan Lampiran 1–5. Rumus ditulis ulang dari buku dalam bentuk yang lebih mudah dibaca.')


EQ = [
 ('Stock', 'Jumlah Wisatawan', '∫(Laju Kedatangan − Laju Penurunan) dt;  awal 40.695.654', 'Kunjungan', 'Identitas stok-aliran', 'Sterman (2000)'),
 ('Stock', 'Jumlah Hotel dan Akomodasi', '∫(Laju Konstruksi − Laju Demolisi) dt;  awal 2.291', 'Unit', 'Identitas stok-aliran', 'Sterman (2000)'),
 ('Stock', 'Jumlah ODTW', '∫(Laju Pembangunan ODTW − Laju Penutupan ODTW) dt;  awal 201', 'Unit', 'Identitas stok-aliran', 'Sterman (2000)'),
 ('Stock', 'Tenaga Kerja Pariwisata', '∫(Laju Penyerapan TK − Laju Keluar TK) dt;  awal 364.994', 'Jiwa', 'Identitas stok-aliran', 'Sterman (2000)'),
 ('Stock', 'Lahan Terbangun', '∫(Konversi Pariwisata + Konversi Nonpariwisata) dt;  awal 55.029,5', 'Hektar', 'Identitas stok-aliran (tanpa outflow)', 'Sterman (2000)'),
 ('Flow', 'Laju Kedatangan Wisatawan', 'Jumlah Wisatawan × LPE × Daya Tarik', 'Kunjungan/th', 'Pertumbuhan endogen (R1); daya tarik menarik kunjungan', 'Sterman (2000); Mai & Smith (2018); Hu & Ritchie (1993)'),
 ('Flow', 'Laju Penurunan Wisatawan', 'Jumlah Wisatawan × LPD', 'Kunjungan/th', 'Laju keluar proporsional stok', 'Sterman (2000)'),
 ('Flow', 'Laju Konstruksi Hotel dan Akomodasi', 'Investasi × S_H × max(0, Rasio Permintaan − TPK Ambang)', 'Unit/th', 'Konstruksi aktif bila permintaan melewati ambang (B3)', 'Wheaton & Rossoff (1998)'),
 ('Flow', 'Laju Demolisi Hotel dan Akomodasi', 'Jumlah Hotel × Laju Demolisi Dasar', 'Unit/th', 'Average lifetime', 'Sterman (2000); Mai & Smith (2018)'),
 ('Flow', 'Laju Pembangunan/Penambahan ODTW', 'Investasi × S_O + Pembangunan ODTW Non Investasi', 'Unit/th', 'Jalur swasta (R2) dan jalur pemerintah/masyarakat', 'Fatina et al. (2023)'),
 ('Flow', 'Laju Penutupan ODTW', 'Jumlah ODTW × Laju Penutupan Dasar ODTW', 'Unit/th', 'Average lifetime', 'Sterman (2000)'),
 ('Flow', 'Laju Penyerapan TK Pariwisata', 'max[0, Laju Keluar TK + (TK Dibutuhkan − TK) ÷ τ]', 'Jiwa/th', 'Goal-seeking (B4)', 'Sterman (2000)'),
 ('Flow', 'Laju Keluar TK Pariwisata', 'TK Pariwisata × Laju Keluar Dasar TK', 'Jiwa/th', 'Average lifetime (masa kerja)', 'Sterman (2000); PP 45/2015'),
 ('Flow', 'Laju Konversi Lahan Pariwisata', '(Konstruksi × a_H + Pemb. ODTW × a_O) × (1 − C) × RDDL ÷ RDDL_ref', 'Ha/th', 'Ekspansi fasilitas butuh tapak (B2)', 'Mai & Smith (2018); Fatina et al. (2023)'),
 ('Flow', 'Laju Konversi Lahan Nonpariwisata', 'Laju Konversi Dasar × Lahan Terbangun × RDDL', 'Ha/th', 'Tekanan konversi di luar pariwisata, melambat saat lahan menipis', 'Mai & Smith (2018)'),
 ('Aux', 'Daya Tarik Destinasi Wisata', 'w_O·min[M, (ODTW/ODTW_ref)^ε] + w_K·min[1, K_ref/Kepadatan] + w_L·(RDDL/RDDL_ref)', 'Dmnl', 'Indeks berbobot tiga komponen; dua batas atas hasil uji ekstrem', 'Ritchie & Crouch (2003); Saveriades (2000); Mai & Smith (2018)'),
 ('Aux', 'Tingkat Penghunian Kamar (TPK)', 'min(1, Rasio Permintaan thd Kapasitas Kamar)', 'Dmnl', 'Okupansi tidak boleh > 100% (hasil uji ekstrem)', 'Definisi TPK BPS'),
 ('Aux', 'Rasio Permintaan thd Kapasitas Kamar', '(Total Malam ÷ TPG) ÷ (Hotel × K_unit × M)', 'Dmnl', 'Permintaan malam kamar dibanding kapasitas', 'Identitas kapasitas; Wheaton & Rossoff (1998)'),
 ('Aux', 'Total Malam Menginap', 'Jumlah Wisatawan × p_menginap × LOS', 'Malam', 'Hanya wisatawan menginap memakai kamar', 'UNWTO (2008); Mai & Smith (2018)'),
 ('Aux', 'Pengeluaran Wisatawan', 'Jumlah Wisatawan × Pengeluaran per Kunjungan', 'Miliar Rp', 'Identitas agregasi', 'Frechtling (2010); Jones et al. (2003)'),
 ('Aux', 'PDRB Sektor Pariwisata', 'Pengeluaran Wisatawan × r_NT', 'Miliar Rp', 'Pengeluaran menjadi nilai tambah', 'Frechtling (2010); Munjal (2013)'),
 ('Aux', 'Investasi Sektor Pariwisata', 'PDRB × r_I × (1 + Insentif Kebijakan)', 'Miliar Rp', 'Formulasi berbasis rasio historis; tuas insentif', 'Harrod (1939); Domar (1946)'),
 ('Aux', 'Intensitas Tenaga Kerja', 'i₀ × e^(−g·(Tahun − t₀))', 'Jiwa/miliar Rp', 'Produktivitas meningkat, intensitas menurun', 'Kapsos (2005)'),
 ('Aux', 'Tenaga Kerja Dibutuhkan', 'PDRB × Intensitas Tenaga Kerja', 'Jiwa', 'Derived labor demand', 'Hamermesh (1993); Munjal (2013); Sánchez López (2023)'),
 ('Aux', 'Kepadatan Wisatawan', 'Jumlah Wisatawan ÷ Luas Lahan Tersedia', 'Kunjungan/ha', 'Identitas; tekanan kunjungan (B1)', 'Saveriades (2000)'),
 ('Aux', 'Rasio Daya Dukung Lahan', 'max(0, 1 − Lahan Terbangun ÷ Luas Lahan Tersedia)', 'Dmnl', 'Sisa lahan tidak boleh negatif (hasil uji ekstrem)', 'Mai & Smith (2018)')]


def C_formulasi(D):
    groups = [EQ[:5] + EQ[5:10], EQ[10:15] + EQ[15:18], EQ[18:]]
    for k, g in enumerate(groups):
        s = D.slide(f'Lampiran · Formulasi Stock, Flow, dan Auxiliary ({k + 1}/3)')
        sub(s, 'Persamaan model final (Vensim, integrasi Euler, Δt = 1 tahun): Sₜ₊Δₜ = Sₜ + Δt × (Σ inflow − Σ outflow)')
        rows = [['Peran', 'Variabel', 'Persamaan', 'Satuan', 'Dasar penetapan', 'Rujukan']] + [list(r) for r in g]
        hl = {}
        for i, r in enumerate(g, 1):
            hl[(i, 0)] = {'Stock': 'B7E3EA', 'Flow': 'D7EEF2', 'Aux': 'EEF7F9'}[r[0]]
            hl[(i, 2)] = YEL_L
        rh = 0.75 if len(g) > 8 else 0.85
        gf = tbl(s, 0.9, 2.05, 18.2, [1.0, 3.3, 5.8, 1.6, 3.6, 2.9], rows, size=10.5, rowh=rh, hl=hl, center=(0, 3))
        gf.table.rows[0].height = Inches(0.45)
        for r in range(1, len(rows)):
            for run in gf.table.cell(r, 2).text_frame.paragraphs[0].runs: run.font.italic = True
            c2 = gf.table.cell(r, 1).text_frame.paragraphs[0].runs[0]; c2.font.bold = True; c2.font.color.rgb = rgb(TEAL)
        src(s, 'Sumber: Buku Subbab 4.3 dan Lampiran 6 (Daftar Persamaan); rujukan mengikuti matriks hubungan kausal (Tabel 25). Notasi parameter lihat lampiran parameter.')
