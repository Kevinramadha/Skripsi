import sys; sys.path.insert(0, '/tmp/pptwork/v5')
from single import make_subset
make_subset('/tmp/pptwork/v5/out7.pptx', [41, 42, 43], '/tmp/pptwork/v5/_base_us.pptx')
exec(open('/tmp/pptwork/helpers_v4.py').read())
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE
p = Presentation('/tmp/pptwork/v5/_base_us.pptx')
GREEN, PINK, NAVY = 'C9F0D6', 'FDE2DE', '0B5E6E'
US = '/tmp/pptwork/v5/us/'


def find_title(slide):
    for sh in slide.shapes:
        if sh.has_text_frame and sh.top is not None and 0.6*E <= sh.top <= 1.3*E and sh.width > 9*E and sh.text_frame.text.strip():
            return sh


def prep(s, title, resume):
    t = find_title(s)
    for sh in list(s.shapes):
        keep = (sh._element is t._element) or sh.top >= 10.3*E or (sh.left >= 18.0*E and sh.top < 1.0*E) or sh.top < 0.45*E
        if not keep:
            sh._element.getparent().remove(sh._element)
    for sh in list(s.shapes):
        if sh.top > 10.3*E and 16.5*E < sh.left < 17.9*E:
            sh._element.getparent().remove(sh._element)
    for sh in [x for x in s.shapes if x.has_text_frame and x.left > 17.9*E and x.top > 10.4*E and x.text_frame.text.strip().isdigit()]:
        set_text(sh, '')
    ps = t.text_frame.paragraphs
    ps[0].runs[0].text = title
    ps[1].runs[0].text = resume


def intinya(s, text, y=9.05, h=0.85):
    return box(s, 0.9, y, 18.2, h, fill=YEL_L, line=YEL, anchor=MSO_ANCHOR.MIDDLE,
               paras=[[('Intinya  ', 14, True, TEAL), (text, 14, False, DARK)]])


def head(s, x, y, w, text, sub=None):
    box(s, x, y, w, 0.5, fill=TEAL, line=None, anchor=MSO_ANCHOR.MIDDLE, margin=0.15,
        paras=[[(text, 13.5, True, WHITE)] + ([('   ' + sub, 11, False, 'D7EEF2')] if sub else [])])


def qa(s, x, y, w, h, rows, size=12.5):
    """rows: list of (label, text[, color])"""
    paras = []
    for r in rows:
        paras.append([(r[0] + '  ', size, True, r[2] if len(r) > 2 else TEAL), (r[1], size, False, DARK)])
    return box(s, x, y, w, h, fill=LIGHT, line=LINE, paras=paras)


def chip(s, x, y, w, h, text, fill=LIGHT, line=LINE, size=10.5, color=DARK, bold=False):
    return box(s, x, y, w, h, fill=fill, line=line, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, margin=0.06,
               paras=[(text, size, bold, color)])


def outline(s, x, y, w, h, color=RED):
    r = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    r.fill.background(); r.line.color.rgb = rgb(color); r.line.width = Pt(2.5); r.shadow.inherit = False
    return r


S = list(p.slides)


# ============================================================ 1/3 (gabungan)
s = S[0]
prep(s, 'Uji Struktur (1/3): Kesesuaian Struktur, Dimensi, dan Batas Model',
     'Setiap hubungan punya dasar, satuan konsisten, dan batas model dinyatakan secara terbuka')
head(s, 0.9, 1.95, 6.45, 'Uji kesesuaian struktur dan parameter')
qa(s, 0.9, 2.5, 6.45, 2.95, [
    ('Pertanyaan', 'Apakah setiap hubungan sebab-akibat dan parameter punya dasar?'),
    ('Cara', 'Setiap variabel ditelusuri; sumber dan landasannya (teori, penelitian terdahulu, regulasi, atau data) dicatat dalam tabel parameter.'),
    ('Hasil', 'Seluruh hubungan memiliki dasar teori atau bukti empiris.', '1E7A43')], size=12)
head(s, 0.9, 5.6, 6.45, 'Uji konsistensi dimensi (satuan)')
qa(s, 0.9, 6.15, 6.45, 2.75, [
    ('Pertanyaan', 'Apakah satuan dalam setiap persamaan sudah sesuai? Misalnya, jumlah wisatawan tidak boleh dijumlahkan dengan luas lahan.'),
    ('Cara', 'Seluruh persamaan diperiksa otomatis dengan fitur Units Check dan Check Model di Vensim.'),
    ('Hasil', 'Tidak ditemukan satuan yang tidak sesuai (pesan Vensim: “Units are OK” dan “Model is OK.”).', '1E7A43')], size=12)
y = 1.95
for img, lab in [('dlg18.png', 'Units Check → “Units are OK”'), ('dlg19.png', 'Check Model → “Model is OK.”')]:
    pc = pic(s, US + img, 7.6, y, w=4.55); pc.line.color.rgb = rgb(LINE); pc.line.width = Pt(1)
    ph = pc.height / E
    tb(s, 7.6, y + ph + 0.03, 4.55, 0.35, [[(lab, 11, True, TEAL)]], align=PP_ALIGN.CENTER)
    y += ph + 0.45
head(s, 12.4, 1.95, 6.7, 'Uji kecukupan batas model')
for k, (n, lab, desc, fill, line, col) in enumerate([
        ('26', 'variabel dihitung model', 'nilainya berubah mengikuti hubungan di dalam model', LIGHT, LINE, TEAL),
        ('35', 'variabel input', 'nilainya ditetapkan dari luar: data, regulasi, asumsi, kebijakan', LIGHT, LINE, TEAL),
        ('15', 'aspek di luar cakupan', 'alasan dan dampaknya terhadap hasil dicatat (Lampiran 9)', YEL_L, YEL, '7A5A00')]):
    box(s, 12.4, 2.55 + k * 1.12, 6.7, 1.0, fill=fill, line=line, anchor=MSO_ANCHOR.MIDDLE, margin=0.15,
        paras=[[(n + '  ', 22, True, col), (lab, 13, True, col)], [(desc, 10.5, False, DARK)]])
box(s, 12.4, 5.95, 6.7, 2.95, fill=WHITE, line=LINE, paras=[
    [('Cara membaca hasil model', 12.5, True, TEAL)],
    [('Hasil menggambarkan arah perkembangan jangka panjang dalam kondisi normal, dan ', 11, False, DARK), ('tidak', 11, True, RED), (' dapat dipakai untuk menjelaskan pengaruh:', 11, False, DARK)],
    [('•  harga dan daya saing harga', 11, False, DARK)],
    [('•  promosi dan citra destinasi', 11, False, DARK)],
    [('•  musim ramai/sepi dalam setahun', 11, False, DARK)],
    [('•  kejadian mendadak: pandemi, erupsi, gempa', 11, False, DARK)],
    [('Daftar lengkap 15 aspek: Lampiran 9', 10.5, False, GREY, True)]])
intinya(s, 'Struktur model dapat dipertanggungjawabkan secara teori dan matematis, dan hasilnya dibaca sebagai arah perkembangan jangka panjang dalam kondisi normal.')
source(s, 'Sumber: Buku Subbab 4.4.1–4.4.2, Gambar 16 (dipotong pada pesan Vensim), Tabel 38–39; rincian di Lampiran 9.', y=10.12)
s.notes_slide.notes_text_frame.text = (
    'Uji struktur saya mulai dari tiga pemeriksaan dasar. Pertama, kesesuaian struktur dan parameter: setiap variabel saya telusuri dan sumber serta landasannya saya catat, '
    'sehingga setiap hubungan sebab-akibat punya dasar teori atau bukti empiris. Kedua, konsistensi dimensi: Units Check dan Check Model di Vensim menampilkan "Units are OK" dan "Model is OK", '
    'artinya satuan seluruh persamaan konsisten. Ketiga, kecukupan batas model: model memuat 61 variabel, 26 dihitung di dalam model dan 35 merupakan input yang ditetapkan dari luar, '
    'serta 15 aspek sengaja dikeluarkan beserta konsekuensinya. Karena itu hasil model tidak dipakai untuk menjelaskan harga, promosi, musim, atau kejadian mendadak seperti pandemi dan bencana. Daftar lengkapnya ada di Lampiran 9.')

# ============================================================ 2/3
s = S[1]
prep(s, 'Uji Struktur (2/3): Kekekalan Materi dan Feedback Loop',
     'Jumlah pada setiap stok selalu cocok dengan hitungan tambah-kurangnya, dan setiap loop berpengaruh sesuai rancangan CLD')
head(s, 0.9, 1.95, 7.6, 'Uji kekekalan materi')
qa(s, 0.9, 2.5, 7.6, 1.2, [('Pertanyaan', 'Apakah jumlah pada setiap stok hanya berubah karena yang bertambah dan yang berkurang, tanpa ada selisih yang tidak jelas asalnya?')], size=11.5)
box(s, 0.9, 3.85, 7.6, 1.5, fill=WHITE, line=LINE, paras=[
    [('Jumlah tahun depan = jumlah tahun ini + yang bertambah − yang berkurang', 11.5, True, TEAL)],
    [('Contoh hotel 2025→2026:  ', 11, True, DARK), ('2.291 + 158,18 (dibangun) − 114,55 (ditutup) = 2.334,63 unit', 11, False, DARK)],
    [('= jumlah hotel 2026 pada hasil simulasi ✓', 11, True, '1E7A43')]])
rows = [['Stok', 'Selisih terbesar 2025–2049', 'Hasil'],
        ['Jumlah Wisatawan', '≈ 0', 'Sesuai'], ['Jumlah Hotel dan Akomodasi', '0', 'Sesuai'],
        ['Jumlah ODTW', '0', 'Sesuai'], ['Tenaga Kerja Pariwisata', '0', 'Sesuai'], ['Lahan Terbangun', '0', 'Sesuai']]
gf = table(s, 0.9, 5.5, 7.6, [3.3, 2.7, 1.2], rows, size=10.5, rowh=0.5, hl={(r, 2): GREEN for r in range(1, 6)})
for r in range(6):
    for c in (1, 2):
        gf.table.cell(r, c).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
tb(s, 0.9, 8.53, 7.6, 0.3, [[('Selisih = hasil simulasi dikurangi hitungan tambah-kurang di atas', 9.5, False, GREY, True)]])

head(s, 8.8, 1.95, 10.3, 'Uji feedback loop', 'satu loop dinonaktifkan, lalu hasilnya dibandingkan dengan simulasi dasar')
tb(s, 8.8, 2.5, 10.3, 0.4, [[('Jumlah wisatawan tahun 2050 (juta)', 11.5, True, DARK), ('  · dinonaktifkan = variabel penghubung loop ditahan tetap pada nilai 2025', 10.5, False, GREY)]])
cats = ['Semua balancing loop nonaktif (tinggal R1)', 'Penyesuaian tenaga kerja nonaktif', 'Okupansi akomodasi nonaktif',
        'R2 ekonomi–objek wisata nonaktif', 'Daya dukung lahan nonaktif', 'B1 kepadatan nonaktif', 'Simulasi dasar (semua loop aktif)']
vals = [217.37, 96.20, 96.23, 80.24, 111.66, 250.32, 96.20]
cd = CategoryChartData(); cd.categories = cats; cd.add_series('Wisatawan 2050 (juta)', vals)
ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(8.8), Inches(2.85), Inches(10.3), Inches(3.45), cd).chart
ch.has_title = False; ch.has_legend = False
ch.font.size = Pt(11); ch.font.name = F; ch.font.color.rgb = rgb(DARK)
pl = ch.plots[0]; pl.gap_width = 40; pl.has_data_labels = True
dl = pl.data_labels; dl.number_format = '0.00'; dl.number_format_is_linked = False; dl.show_value = True
dl.font.size = Pt(11); dl.font.bold = True; dl.position = XL_LABEL_POSITION.OUTSIDE_END
for pt_i, col in enumerate([GREY, CYAN, CYAN, CYAN, CYAN, RED, TEAL]):
    pt = pl.series[0].points[pt_i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(col)
ch.value_axis.minimum_scale = 0; ch.value_axis.maximum_scale = 300
ch.value_axis.has_major_gridlines = True; ch.value_axis.major_gridlines.format.line.color.rgb = rgb('E3EEF1')
ch.value_axis.format.line.fill.background(); ch.value_axis.tick_labels.font.size = Pt(10)
ch.category_axis.tick_labels.font.size = Pt(11); ch.category_axis.format.line.color.rgb = rgb('B8C7CC')
box(s, 8.8, 6.35, 10.3, 2.55, fill=LIGHT, line=LINE, paras=[
    [('•  B1 kepadatan paling berpengaruh: ', 10.5, True, DARK), ('tanpa B1, wisatawan 2050 naik 160,2% dan 5 dari 6 variabel utama* berubah >1%.', 10.5, False, DARK)],
    [('•  Daya dukung lahan: ', 10.5, True, DARK), ('wisatawan naik 16,1%, tetapi memengaruhi keenam variabel utama. ', 10.5, False, DARK),
     ('R2: ', 10.5, True, DARK), ('wisatawan turun 16,6%, ODTW turun 45,3%.', 10.5, False, DARK)],
    [('•  Hanya memengaruhi satu variabel: ', 10.5, True, DARK), ('okupansi akomodasi (jumlah hotel −10,0%) dan penyesuaian tenaga kerja (tenaga kerja −43,9%).', 10.5, False, DARK)],
    [('•  Pengaruh loop tidak bisa dijumlahkan: ', 10.5, True, DARK), ('menonaktifkan B1 saja (250,32 juta) lebih tinggi daripada menonaktifkan semua balancing loop (217,37 juta), karena R2 yang masih aktif terus menaikkan daya tarik hingga 1,0696.', 10.5, False, DARK)],
    [('* wisatawan, hotel, ODTW, tenaga kerja, lahan terbangun, daya tarik', 9.5, False, GREY, True)]])
intinya(s, 'Hitungan setiap stok cocok tanpa selisih, dan setiap balancing loop yang dinonaktifkan membuat pertumbuhan lebih cepat: keenam loop berpengaruh sesuai rancangan CLD.')
source(s, 'Sumber: Buku Subbab 4.4.3–4.4.4, Tabel 40–42, Gambar 17.', y=10.12)
s.notes_slide.notes_text_frame.text = (
    'Uji kekekalan materi memeriksa apakah jumlah pada setiap stok hanya berubah karena yang bertambah dan yang berkurang. Contohnya hotel: 2.291 ditambah 158,18 yang dibangun '
    'dikurangi 114,55 yang ditutup menghasilkan 2.334,63, sama persis dengan jumlah hotel 2026 hasil simulasi. Pada kelima stok selisihnya nol sepanjang 2025 sampai 2049. '
    'Uji feedback loop dilakukan dengan menonaktifkan satu loop pada satu waktu, yaitu menahan variabel penghubung loop tetap pada nilai 2025. Loop kepadatan B1 paling berpengaruh: '
    'tanpa B1, wisatawan 2050 naik 160 persen. Daya dukung lahan pengaruhnya sedang tetapi menyentuh keenam variabel utama. Menonaktifkan R2 justru menurunkan wisatawan dan paling besar menurunkan ODTW. '
    'Okupansi akomodasi dan penyesuaian tenaga kerja hanya memengaruhi satu variabel. Menariknya, menonaktifkan B1 saja menghasilkan angka lebih tinggi daripada menonaktifkan semua balancing loop, '
    'karena R2 tetap menaikkan daya tarik. Jadi pengaruh antarloop tidak bisa dijumlahkan begitu saja.')

# ============================================================ 3/3
s = S[2]
prep(s, 'Uji Struktur (3/3): Kondisi Ekstrem dan Error Integrasi',
     'Saat parameter diberi nilai ekstrem, hasil model tetap masuk akal; selisih kecil pada E15 berasal dari langkah hitung, bukan struktur')
head(s, 0.9, 1.95, 11.3, 'Uji kondisi ekstrem', '17 uji: parameter diberi nilai ekstrem (mis. dinolkan, dikali 10), lalu dicek dengan 6 syarat logis')
rules = ['Stok tidak negatif', 'TPK maks. 1 (100%)', 'RDDL tidak negatif', 'Lahan ≤ luas wilayah', 'Daya tarik 0–3', 'Wisatawan ≤ 5× dasar*']
for k, r in enumerate(rules):
    chip(s, 0.9 + k * 1.9, 2.55, 1.8, 0.5, r, size=10, bold=True, color=TEAL)
for k, (big, lab, fill, line, col) in enumerate([('15', 'lolos', GREEN, '9BD8AF', '1E7A43'),
                                                 ('2', 'lolos dengan catatan (E02, E15)', YEL_L, YEL, '7A5A00'),
                                                 ('0', 'gagal', LIGHT, LINE, TEAL)]):
    w = [2.6, 5.0, 2.6][k]; x = [0.9, 3.65, 8.8][k]
    box(s, x, 3.2, w, 0.8, fill=fill, line=line, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, margin=0.08,
        paras=[[(big + ' ', 22, True, col), (lab, 12, True, col)]])
box(s, 0.9, 4.1, 11.3, 0.62, fill=WHITE, line=LINE, anchor=MSO_ANCHOR.MIDDLE, paras=[[
    ('Uji awal menemukan 4 persamaan yang bisa tidak masuk akal, lalu diberi batas: ', 10.5, True, TEAL),
    ('TPK maks. 1, RDDL min. 0, dan nilai maksimum untuk komponen kepadatan dan ODTW pada daya tarik.', 10.5, False, DARK)]])
for k, (img, cap) in enumerate([('image21.png', [('E04 · ', 10.5, True, TEAL), ('investasi dinolkan → TPK naik lalu berhenti tepat di 1, padahal permintaan kamar mencapai 2,267× kapasitas', 10.5, False, DARK)]),
                                ('image22.png', [('E09 · ', 10.5, True, TEAL), ('konversi lahan non-pariwisata ×10 → RDDL turun tepat ke 0; lahan terbangun berhenti di luas wilayah', 10.5, False, DARK)])]):
    x = 0.9 + k * 5.75
    pc = pic(s, MED + img, x, 4.85, w=5.55); pc.line.color.rgb = rgb(LINE); pc.line.width = Pt(1)
    ph = pc.height / E
    tb(s, x, 4.85 + ph + 0.05, 5.55, 0.75, [cap])
tb(s, 0.9, 7.6, 11.3, 1.35, [[('Bukti lain: ', 10.5, True, TEAL), ('daya tarik tetap 0,60–1,00 pada E01 & E15 (tidak melonjak); E10 dan E11 hasilnya sama persis sesuai dugaan; E12/E13 hanya mengubah tenaga kerja.', 10.5, False, DARK)],
                             [('* E02 & E15 tidak dinilai dengan syarat 5×: ', 10.5, True, '7A5A00'), ('keduanya sengaja menghapus pengurang wisatawan atau melipatgandakan pertumbuhan. Model berlaku selama laju pertumbuhan eksternal (LPE) tidak melebihi sekitar 0,336 (≈1,25× nilai dasar).', 10.5, False, DARK)]])

head(s, 12.5, 1.95, 6.6, 'Uji error integrasi', 'ketelitian langkah hitung')
tb(s, 12.5, 2.5, 6.6, 0.6, [[('Model menghitung per langkah waktu 1 tahun. Pada E15 (LPE ×3), lahan sempat melewati luas wilayah. Salah struktur, atau langkahnya terlalu kasar?', 10, False, DARK)]])
pc = pic(s, MED + 'image27.png', 13.0, 3.15, w=5.6); pc.line.color.rgb = rgb(LINE); pc.line.width = Pt(1)
y0 = 3.15 + pc.height / E + 0.08
rows = [['Langkah hitung', 'Lahan terbangun vs luas wilayah'],
        ['1 tahun', 'melewati 57,70 ha (0,018%)'], ['0,5 tahun', 'melewati 0,01 ha'],
        ['0,25 tahun', 'berhenti di 317.035,82 ha ✓'], ['0,125 tahun', 'hanya beda 0,06 ha dari 0,25']]
gf = table(s, 12.5, y0, 6.6, [2.0, 4.6], rows, size=10, rowh=0.34,
           hl={(1, 1): PINK, (2, 1): YEL_L, (3, 1): GREEN, (4, 1): GREEN})
tb(s, 12.5, y0 + 5 * 0.34 + 0.06, 6.6, 0.95, [[('Selisih hilang saat langkah diperkecil → penyebabnya cara menghitung per langkah, bukan struktur. Simulasi dasar dengan langkah 1 vs 0,5 tahun hanya beda −0,27% s.d. +0,34%, jadi langkah 1 tahun sudah cukup.', 9.5, False, DARK)]])
intinya(s, 'Keempat batas bekerja di seluruh 17 uji, dan selisih pada E15 hilang saat langkah hitung diperkecil: model valid secara struktural dan dapat lanjut ke uji perilaku.')
source(s, 'Sumber: Buku Subbab 4.4.5–4.4.6, Tabel 43–44, Gambar 18, 19, dan 24.', y=10.12)
s.notes_slide.notes_text_frame.text = (
    'Uji kondisi ekstrem memberi nilai ekstrem pada parameter, misalnya dinolkan atau dikali sepuluh, lalu memeriksa apakah hasilnya tetap masuk akal dengan enam syarat, '
    'misalnya TPK tidak boleh lebih dari 100 persen dan lahan terbangun tidak boleh melebihi luas wilayah. Uji awal menemukan empat persamaan yang bisa menghasilkan nilai tidak masuk akal, '
    'lalu saya beri batas. Setelah itu, 15 uji lolos, 2 lolos dengan catatan, dan tidak ada yang gagal. Contohnya, saat investasi dinolkan, TPK berhenti tepat di 100 persen meskipun permintaan kamar 2,27 kali kapasitas, '
    'dan saat konversi lahan dikali sepuluh, rasio daya dukung lahan turun tepat ke nol. E02 dan E15 diberi catatan karena sengaja mendorong model jauh di luar batas berlakunya. '
    'Uji error integrasi memeriksa ketelitian langkah hitung. Model menghitung tahun demi tahun; pada E15 lahan sempat melewati luas wilayah 57,70 hektar. Ketika langkah hitung diperkecil, '
    'selisih itu mengecil lalu hilang pada 0,25 tahun. Artinya penyebabnya cara menghitung, bukan struktur model. Dengan demikian model valid secara struktural dan dapat lanjut ke uji perilaku.')


p.save('/tmp/pptwork/v5/ujistruktur_3slide.pptx')
print('ok')
