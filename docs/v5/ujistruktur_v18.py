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
     'Tidak ada stok yang “bocor”, dan setiap loop dalam CLD bekerja sesuai rancangannya')
head(s, 0.9, 1.95, 7.6, 'Uji kekekalan materi')
qa(s, 0.9, 2.5, 7.6, 1.15, [('Pertanyaan', 'Adakah wisatawan, hotel, ODTW, tenaga kerja, atau lahan yang muncul/hilang di luar aliran?')])
box(s, 0.9, 3.8, 7.6, 1.45, fill=WHITE, line=LINE, paras=[
    [('Stok tahun depan = stok tahun ini + aliran masuk − aliran keluar', 12, True, TEAL)],
    [('Contoh hotel 2025→2026:  ', 11, True, DARK), ('2.291 + 158,17937 − 114,55 = 2.334,62937 unit', 11, False, DARK)],
    [('= nilai stok 2026 hasil simulasi ✓', 11, True, '1E7A43')]])
rows = [['Stok', 'Selisih maks. 2025–2049', 'Status'],
        ['Jumlah Wisatawan', '≈ 0', 'Kekal'], ['Jumlah Hotel dan Akomodasi', '0', 'Kekal'],
        ['Jumlah ODTW', '0', 'Kekal'], ['Tenaga Kerja Pariwisata', '0', 'Kekal'], ['Lahan Terbangun', '0', 'Kekal']]
gf = table(s, 0.9, 5.4, 7.6, [3.4, 2.5, 1.3], rows, size=10.5, rowh=0.53, hl={(r, 2): GREEN for r in range(1, 6)})
for r in range(6):
    for c in (1, 2):
        gf.table.cell(r, c).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

head(s, 8.8, 1.95, 10.3, 'Uji feedback loop', 'satu loop dimatikan, dibandingkan dengan simulasi dasar')
tb(s, 8.8, 2.5, 10.3, 0.4, [[('Jumlah wisatawan tahun 2050 (juta)', 11.5, True, DARK), ('  · loop dimatikan = variabel penutup loop ditahan pada nilai 2025', 10.5, False, GREY)]])
cats = ['Semua rem dimatikan (R1 murni)', 'Goal-seeking tenaga kerja dimatikan', 'Okupansi akomodasi dimatikan',
        'R2 ekonomi–objek wisata dimatikan', 'Daya dukung lahan dimatikan', 'B1 kepadatan dimatikan', 'Simulasi dasar (semua loop aktif)']
vals = [217.37, 96.20, 96.23, 80.24, 111.66, 250.32, 96.20]
cd = CategoryChartData(); cd.categories = cats; cd.add_series('Wisatawan 2050 (juta)', vals)
ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(8.8), Inches(2.85), Inches(10.3), Inches(3.7), cd).chart
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
box(s, 8.8, 6.65, 10.3, 2.25, fill=LIGHT, line=LINE, paras=[
    [('•  B1 kepadatan = rem terkuat: ', 11, True, DARK), ('dimatikan → wisatawan +160,2%, 5 dari 6 variabel berubah >1%.', 11, False, DARK)],
    [('•  Daya dukung lahan: ', 11, True, DARK), ('+16,1%, tetapi satu-satunya yang mengubah 6 dari 6 variabel. ', 11, False, DARK),
     ('R2: ', 11, True, DARK), ('wisatawan −16,6%, ODTW −45,3%.', 11, False, DARK)],
    [('•  Dampak terbatas: ', 11, True, DARK), ('okupansi (hanya hotel −10,0%) dan goal-seeking tenaga kerja (hanya tenaga kerja −43,9%).', 11, False, DARK)],
    [('•  Efek loop tidak bisa dijumlahkan: ', 11, True, DARK), ('B1 saja dimatikan (250,32) > semua rem dimatikan (217,37), karena R2 tetap menaikkan daya tarik hingga 1,0696.', 11, False, DARK)]])
intinya(s, 'Stok hanya berubah lewat alirannya, dan setiap balancing loop yang dimatikan mempercepat pertumbuhan: keenam loop CLD bekerja sesuai rancangan.')
source(s, 'Sumber: Buku Subbab 4.4.3–4.4.4, Tabel 40–42, Gambar 17.', y=10.12)
s.notes_slide.notes_text_frame.text = (
    'Uji kekekalan materi memeriksa apakah setiap stok benar-benar hasil akumulasi alirannya. Contohnya hotel: 2.291 ditambah konstruksi 158,18 dikurangi demolisi 114,55 menghasilkan 2.334,63, '
    'sama persis dengan nilai stok 2026 hasil simulasi. Pada kelima stok selisihnya nol sepanjang 2025 sampai 2049. '
    'Uji feedback loop dilakukan dengan mematikan satu loop pada satu waktu. Rem kepadatan B1 paling kuat: tanpa B1, wisatawan 2050 naik 160 persen. '
    'Daya dukung lahan dampaknya moderat tetapi menyentuh keenam variabel. Mematikan R2 justru menurunkan wisatawan dan paling besar menurunkan ODTW. '
    'Okupansi dan goal-seeking tenaga kerja hanya memengaruhi satu variabel. Menariknya, mematikan B1 saja menghasilkan angka lebih tinggi daripada mematikan semua rem, '
    'karena R2 tetap mendorong daya tarik naik. Jadi efek antarloop tidak bisa dijumlahkan begitu saja.')

# ============================================================ 3/3
s = S[2]
prep(s, 'Uji Struktur (3/3): Kondisi Ekstrem dan Error Integrasi',
     'Pada nilai ekstrem model tetap logis; pelanggaran kecil pada E15 hanya error hitungan numerik')
head(s, 0.9, 1.95, 11.3, 'Uji kondisi ekstrem', '17 uji pada 5 subsistem, dinilai dengan 6 aturan fisik')
rules = ['Stok ≥ 0', 'TPK ≤ 1', 'RDDL ≥ 0', 'Lahan ≤ luas wilayah', 'Daya tarik 0–3', 'Wisatawan ≤ 5× dasar*']
for k, r in enumerate(rules):
    chip(s, 0.9 + k * 1.9, 2.55, 1.8, 0.5, r, size=10.5, bold=True, color=TEAL)
for k, (big, lab, fill, line, col) in enumerate([('15', 'lolos', GREEN, '9BD8AF', '1E7A43'),
                                                 ('2', 'lolos dengan catatan (E02, E15)', YEL_L, YEL, '7A5A00'),
                                                 ('0', 'gagal', LIGHT, LINE, TEAL)]):
    w = [2.6, 5.0, 2.6][k]; x = [0.9, 3.65, 8.8][k]
    box(s, x, 3.2, w, 0.8, fill=fill, line=line, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, margin=0.08,
        paras=[[(big + ' ', 22, True, col), (lab, 12, True, col)]])
box(s, 0.9, 4.1, 11.3, 0.62, fill=WHITE, line=LINE, anchor=MSO_ANCHOR.MIDDLE, paras=[[
    ('4 pembatas ditambahkan setelah uji awal: ', 11, True, TEAL),
    ('TPK ≤ 1 · RDDL ≥ 0 · batas atas komponen kepadatan dan ODTW pada indeks daya tarik', 11, False, DARK)]])
for k, (img, cap) in enumerate([('image21.png', [('E04 · ', 10.5, True, TEAL), ('rasio investasi/PDRB = 0 → TPK naik lalu mendatar tepat di 1,000 (rasio permintaan sampai 2,267)', 10.5, False, DARK)]),
                                ('image22.png', [('E09 · ', 10.5, True, TEAL), ('laju konversi ×10 → RDDL turun tepat ke 0; lahan berhenti di luas wilayah', 10.5, False, DARK)])]):
    x = 0.9 + k * 5.75
    pc = pic(s, MED + img, x, 4.85, w=5.55); pc.line.color.rgb = rgb(LINE); pc.line.width = Pt(1)
    ph = pc.height / E
    tb(s, x, 4.85 + ph + 0.05, 5.55, 0.75, [cap])
tb(s, 0.9, 7.55, 11.3, 1.3, [[('Bukti lain: ', 11.5, True, TEAL), ('daya tarik tetap 0,60–1,00 pada E01 & E15; E10 = E11 identik; E12/E13 hanya mengubah tenaga kerja. ', 11.5, False, DARK),
                             ('* E02 & E15 dikecualikan dari aturan 5×: ', 11.5, True, '7A5A00'), ('rem sengaja dihilangkan/pendorong diperbesar. Batas berlaku model: LPE ≲ 0,336 (≈1,25× nilai dasar).', 11.5, False, DARK)]])

head(s, 12.5, 1.95, 6.6, 'Uji error integrasi', 'lanjutan E15')
tb(s, 12.5, 2.5, 6.6, 0.6, [[('Pada E15 (LPE ×3), dt 1 tahun, lahan sempat melewati luas wilayah. Salah struktur atau error hitungan?', 10.5, False, DARK)]])
pc = pic(s, MED + 'image27.png', 13.0, 3.1, w=5.6); pc.line.color.rgb = rgb(LINE); pc.line.width = Pt(1)
y0 = 3.1 + pc.height / E + 0.08
rows = [['Langkah waktu (dt)', 'Lahan vs luas wilayah'],
        ['1 tahun', 'lewat 57,70 ha (0,018%)'], ['0,5 tahun', 'lewat 0,01 ha'],
        ['0,25 tahun', 'berhenti 317.035,82 ha ✓'], ['0,125 tahun', 'beda 0,06 ha dari dt 0,25']]
gf = table(s, 12.5, y0, 6.6, [2.3, 4.3], rows, size=10, rowh=0.34,
           hl={(1, 1): PINK, (2, 1): YEL_L, (3, 1): GREEN, (4, 1): GREEN})
tb(s, 12.5, y0 + 5 * 0.34 + 0.06, 6.6, 0.9, [[('Selisih mengecil seiring dt diperkecil → error numerik (metode Euler), bukan struktur. Simulasi dasar dt 1 vs 0,5: −0,27% s.d. +0,34% → dt 1 tahun memadai.', 10, False, DARK)]])
intinya(s, 'Keempat pembatas bekerja di seluruh 17 uji ekstrem, dan model valid secara struktural sehingga dapat dilanjutkan ke uji perilaku.')
source(s, 'Sumber: Buku Subbab 4.4.5–4.4.6, Tabel 43–44, Gambar 18, 19, dan 24.', y=10.12)
s.notes_slide.notes_text_frame.text = (
    'Uji kondisi ekstrem menguji 17 kombinasi nilai ekstrem pada lima subsistem dengan enam aturan fisik, misalnya TPK tidak boleh lebih dari satu dan lahan tidak boleh melebihi luas wilayah. '
    'Uji awal menemukan empat titik struktur yang bisa melanggar aturan, lalu diperbaiki dengan menambahkan pembatas. Setelah perbaikan, 15 uji lolos, 2 lolos dengan catatan, dan tidak ada yang gagal. '
    'Buktinya, pada E04 TPK mendatar tepat di satu meskipun rasio permintaan mencapai 2,27, dan pada E09 rasio daya dukung lahan turun tepat ke nol. '
    'E02 dan E15 diberi catatan karena sengaja mendorong model jauh di luar batas berlakunya, yaitu laju pertumbuhan eksternal sekitar 0,336. '
    'Pada E15, lahan sempat melewati luas wilayah 57,70 hektar dengan langkah waktu satu tahun. Ketika langkah waktu diperkecil, pelanggarannya menyusut lalu hilang pada 0,25 tahun. '
    'Artinya ini error hitungan numerik, bukan kesalahan struktur. Dengan demikian model valid secara struktural dan dapat dilanjutkan ke uji perilaku.')

p.save('/tmp/pptwork/v5/ujistruktur_3slide.pptx')
print('ok')
