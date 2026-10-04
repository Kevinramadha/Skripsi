import sys; sys.path.insert(0, '/tmp/pptwork/v5')
from single import make_subset
make_subset('/tmp/pptwork/v5/out7.pptx', [30, 31, 32], '/tmp/pptwork/v5/_base_lahan.pptx')
exec(open('/tmp/pptwork/helpers_v4.py').read())
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
p = Presentation('/tmp/pptwork/v5/_base_lahan.pptx')
NAVY = '0B5E6E'; GREEN = 'C9F0D6'; PINK = 'FDE2DE'
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
    ps = t.text_frame.paragraphs
    ps[0].runs[0].text = title
    for r in ps[0].runs[1:]: r._r.getparent().remove(r._r)
    ps[1].runs[0].text = resume
    for r in ps[1].runs[1:]: r._r.getparent().remove(r._r)
    for sh in [x for x in s.shapes if x.has_text_frame and x.left > 17.9*E and x.top > 10.4*E and x.text_frame.text.strip().isdigit()]:
        set_text(sh, '')
def center_cols(gf, cols, start=0):
    for r in range(start, len(gf.table.rows)):
        for k in cols:
            gf.table.cell(r, k).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
def style_line_chart(c, cols, fmt, lo, hi, dash=()):
    c.has_title = False; c.font.size = Pt(11); c.font.name = F; c.font.color.rgb = rgb(DARK)
    c.has_legend = True; c.legend.position = XL_LEGEND_POSITION.TOP; c.legend.include_in_layout = False
    for k, (ser, col) in enumerate(zip(c.plots[0].series, cols)):
        ser.format.line.color.rgb = rgb(col); ser.format.line.width = Pt(2.75); ser.smooth = False
        ser.marker.size = 8; ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb = rgb(col)
        ser.marker.format.line.color.rgb = rgb(col)
        if k in dash: ser.format.line.dash_style = 4
    c.plots[0].has_data_labels = True
    dl = c.plots[0].data_labels; dl.number_format = fmt; dl.number_format_is_linked = False
    dl.font.size = Pt(9.5); dl.position = XL_LABEL_POSITION.ABOVE
    c.value_axis.minimum_scale = lo; c.value_axis.maximum_scale = hi
    c.value_axis.has_major_gridlines = True; c.value_axis.major_gridlines.format.line.color.rgb = rgb('E3EEF1')
    c.value_axis.tick_labels.font.size = Pt(10); c.category_axis.tick_labels.font.size = Pt(10)
    c.value_axis.tick_labels.number_format = '#,##0'; c.value_axis.tick_labels.number_format_is_linked = False

S = list(p.slides)
# ================= Slide 1: uji akurasi & metrik
s = S[0]
prep(s, 'Estimasi Lahan Terbangun — Uji Akurasi dan Metrik Evaluasi', 'Dynamic World cukup akurat untuk data lahan terbangun: akurasi 89,95%, Kappa 0,61')
box(s, 0.9, 1.95, 18.2, 0.62, fill=NAVY, line=None, paras=[[('Desain uji  ', 13.5, True, YEL),
    ('Peta Dynamic World 2025 (kelas built, probabilitas ≥ 0,5) · 200 titik acak berstrata (100 terbangun, 100 bukan) · rujukan: interpretasi visual citra resolusi tinggi Google Earth', 13, True, WHITE)]], anchor=MSO_ANCHOR.MIDDLE)
rows = [['Metrik', 'Rumus', 'Cara membaca / kriteria', 'Hasil', 'IK 95%'],
 ['Overall accuracy (tak terbobot)', 'OA = (n₁₁ + n₀₀) / n', 'Porsi titik yang benar; bias karena sampel 50:50', '80,50%', '74,46–85,39%'],
 ['Overall accuracy terbobot luas (Olofsson dkk., 2014)', 'ÔA = Σ Wᵢ · (nᵢᵢ / nᵢ.) ;  Wᵢ = Aᵢ / A_total', 'Ukuran utama: menyesuaikan dengan luas tiap kelas', '89,95%', '86,05–93,85%'],
 ["User's accuracy (terbangun)", 'UA = n₁₁ / (n₁₁ + n₁₀)', 'Ketepatan peta: yang dipetakan terbangun benar terbangun', '66,00%', '56,67–75,33%'],
 ["Producer's accuracy (terbangun)", 'PA = n₁₁ / (n₁₁ + n₀₁)', 'Kelengkapan: terbangun di lapangan ikut terpetakan', '73,58%', '56,66–90,50%'],
 ['F1-score (terbangun)', 'F1 = 2 · UA · PA / (UA + PA)', 'Gabungan UA dan PA; makin dekat 100% makin baik', '77,19%', '—'],
 ['Koefisien Kappa', 'κ = (pₒ − pₑ) / (1 − pₑ)', 'Landis & Koch (1977): 0,61–0,80 = kesepakatan kuat', '0,61', '0,50–0,72']]
hl = {(2, 3): GREEN, (6, 3): GREEN}
gf = table(s, 0.9, 2.72, 18.2, [3.9, 4.9, 5.1, 1.9, 2.4], rows, size=11.5, rowh=0.62, hl=hl, bold_first_col=True)
center_cols(gf, [3, 4], 1)
for r in (2, 6):
    gf.table.cell(r, 3).text_frame.paragraphs[0].runs[0].font.bold = True
tb(s, 0.9, 7.12, 18.2, 0.35, [('n₁₁ = terbangun benar · n₀₀ = bukan terbangun benar · n₁₀ = commission error (dipetakan terbangun padahal bukan) · n₀₁ = omission error (terbangun tetapi tidak terpetakan) · Aᵢ = luas kelas i di peta · pₒ = kesepakatan teramati · pₑ = kesepakatan karena kebetulan', 10.5, False, GREY, True)])
rows2 = [['Peta \\ Rujukan', 'Bukan terbangun', 'Terbangun'], ['Bukan terbangun', '95', '5'], ['Terbangun', '34', '66']]
gf = table(s, 0.9, 7.75, 6.6, [2.4, 2.1, 2.1], rows2, size=12.5, rowh=0.48, bold_first_col=True, hl={(1, 1): GREEN, (2, 2): GREEN, (2, 1): PINK, (1, 2): LIGHT})
center_cols(gf, [1, 2])
tb(s, 0.9, 9.42, 6.6, 0.3, [('Matriks konfusi (jumlah titik)', 11, True, TEAL)])
box(s, 7.8, 7.75, 5.55, 1.75, fill=LIGHT, paras=[('Kesalahan utama: commission error', 13, True, TEAL),
    ('34 titik dipetakan terbangun padahal bukan, dibanding 5 omission error. Peta cenderung sedikit melebihkan lahan terbangun.', 11.5, False, DARK)])
box(s, 13.55, 7.75, 5.55, 1.75, fill=YEL_L, line=YEL, paras=[('Cek batas probabilitas', 13, True, TEAL),
    ('F1 tertinggi pada batas 0,40–0,45, dekat dengan batas baku 0,5. Batas 0,5 tetap dipakai agar tidak terlalu menyesuaikan sampel.', 11.5, False, DARK)])
source(s, 'Sumber: Buku Subbab 3.5.2 dan 4.2.2, Tabel 31–32; Olofsson dkk. (2014); Landis & Koch (1977).', y=10.12)
s.notes_slide.notes_text_frame.text = ('Akurasi kelas terbangun Dynamic World 2025 diuji dengan 200 titik acak berstrata, dibandingkan dengan interpretasi visual citra resolusi tinggi. '
    'Karena sampel dibuat 50:50 padahal luas lahan terbangun jauh lebih kecil, ukuran utamanya adalah akurasi terbobot luas mengikuti Olofsson dkk.: 89,95 persen. '
    'Kappa 0,61 termasuk kesepakatan kuat. Kesalahan didominasi commission error, 34 titik, artinya peta cenderung sedikit melebihkan lahan terbangun.')

# ================= Slide 2: validasi temporal
s = S[1]
prep(s, 'Estimasi Lahan Terbangun — Validasi Temporal', 'Dynamic World naik konsisten, sedangkan data resmi BPS dan DLHK tidak konsisten')
yrs = [str(y) for y in range(2015, 2026)]
DW = [43037, 44561, 50224, 56624, 63480, 58962, 59888, 57709, 75624, 73512, 55030]
cd = CategoryChartData(); cd.categories = yrs
cd.add_series('Dynamic World (dipakai di model)', DW)
cd.add_series('BPS (lahan bukan pertanian)', [76334, 77467, 108580, 114942, 70371, None, None, None, None, None, None])
cd.add_series('DLHK DIY', [75146, 65461, 70371, 70371, None, None, None, None, None, None, None])
ch = s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(0.9), Inches(1.95), Inches(11.0), Inches(6.9), cd).chart
style_line_chart(ch, [NAVY, RED, 'E0A800'], '#,##0', 30000, 125000)
from pptx.enum.chart import XL_LABEL_POSITION as LP
dls = ch.plots[0].series[2].data_labels
dls.show_value = True; dls.position = LP.BELOW; dls.number_format = '#,##0'; dls.number_format_is_linked = False; dls.font.size = Pt(9.5)
dls.font.color.rgb = rgb('9A6B00')
dlb = ch.plots[0].series[1].data_labels
dlb.show_value = True; dlb.position = LP.ABOVE; dlb.number_format = '#,##0'; dlb.number_format_is_linked = False; dlb.font.size = Pt(9.5)
dlb.font.color.rgb = rgb(RED)
tb(s, 0.9, 8.85, 11.0, 0.35, [('Luas lahan terbangun DIY (ha). Nilai Dynamic World 2015 adalah hasil ekstrapolasi tren.', 10.5, False, GREY, True)])
rows = [['Perubahan', 'BPS', 'DLHK', 'Dynamic World'],
        ['2015→2016', '+1,5%', '−12,9%', '+3,5%*'], ['2016→2017', '+40,2%', '+7,5%', '+12,7%'],
        ['2017→2018', '+5,9%', '0,0%', '+12,7%'], ['2018→2019', '−38,8%', '—', '+12,1%']]
hl = {(2, 1): PINK, (4, 1): PINK, (1, 2): PINK}
for r in (2, 3, 4): hl[(r, 3)] = GREEN
gf = table(s, 12.3, 1.95, 6.8, [1.9, 1.5, 1.5, 1.9], rows, size=12.5, rowh=0.5, hl=hl, bold_first_col=True)
center_cols(gf, [1, 2, 3])
tb(s, 12.3, 4.5, 6.8, 0.3, [('*2015 berdasarkan nilai ekstrapolasi', 10, False, GREY, True)])
box(s, 12.3, 4.95, 6.8, 1.75, fill=LIGHT, paras=[('Hasil 2015–2019', 13.5, True, TEAL),
    ('BPS naik 40,2% lalu turun 38,8%; DLHK turun 12,9%. Dynamic World naik stabil ±12–13% per tahun, sehingga tetap dipilih.', 11.5, False, DARK)])
box(s, 12.3, 6.85, 6.8, 2.35, fill=YEL_L, line=YEL, paras=[('Setelah 2019: naik-turun karena jumlah observasi', 13, True, TEAL),
    ('Luas berkorelasi dengan jumlah observasi citra per piksel (r = 0,788; p = 0,007), bukan dengan tahun (r = 0,174; p = 0,631). Penurunan 27% pada 2023→2025 adalah noise; dicatat sebagai keterbatasan.', 11.5, False, DARK)])
source(s, 'Sumber: Buku Subbab 3.5.2 dan 4.2.2, Gambar 13; Master Data (BPS, DLHK DIY, Dynamic World); notebook "Data Citra untuk Lahan Terbangun".', y=10.12)
s.notes_slide.notes_text_frame.text = ('Validasi temporal membandingkan Dynamic World dengan data resmi pada tahun yang tersedia, 2015 sampai 2019. '
    'Data BPS naik 40,2 persen lalu turun 38,8 persen, dan DLHK turun 12,9 persen; keduanya tidak konsisten dan tidak sejalan. '
    'Dynamic World naik stabil sekitar 12 sampai 13 persen per tahun, sehingga tetap dipilih. Setelah 2019 data Dynamic World naik-turun, '
    'dan diagnosis menunjukkan naik-turunnya mengikuti jumlah observasi citra, bukan perubahan lahan. Ini saya catat sebagai keterbatasan.')

# ================= Slide 3: validasi spasial
s = S[2]
prep(s, 'Estimasi Lahan Terbangun — Validasi Spasial', 'Kesalahan Dynamic World terkumpul di tepi objek, bukan tersebar acak')
D = '/tmp/pptwork/v5/'
pic_fit(s, D + 'dw_nonbuilt.png', 0.9, 1.95, 5.9, 3.6)
pic_fit(s, D + 'dw_built.png', 6.95, 1.95, 5.9, 3.6)
tb(s, 0.9, 5.6, 5.9, 0.35, [('Titik 8: bukan terbangun (vegetasi)', 11.5, True, TEAL)], align=PP_ALIGN.CENTER)
tb(s, 6.95, 5.6, 5.9, 0.35, [('Titik 69: terbangun (atap bangunan)', 11.5, True, TEAL)], align=PP_ALIGN.CENTER)
rows = [['Kelompok titik', 'Nilai'], ['Rata-rata probabilitas "built" — titik benar', '0,330'],
        ['Rata-rata probabilitas "built" — titik salah', '0,574'],
        ['Akurasi pada probabilitas 0–0,25', '97,7%'], ['Akurasi pada probabilitas 0,5–0,6', '52,0%']]
gf = table(s, 13.2, 1.95, 5.9, [4.4, 1.5], rows, size=12, rowh=0.62, bold_first_col=True,
           hl={(3, 1): GREEN, (4, 1): PINK, (2, 1): PINK})
center_cols(gf, [1])
tb(s, 13.2, 5.15, 5.9, 0.5, [('Kesalahan menumpuk pada titik yang probabilitasnya dekat batas 0,5', 11, False, GREY, True)])
cards = [('Cara', 'Titik sampel uji akurasi dicek ulang pada citra resolusi tinggi Google Earth: kelas Dynamic World dibandingkan dengan kondisi lapangan.'),
         ('Titik yang tepat', 'Kawasan yang jelas terbangun atau jelas bervegetasi: kelas prediksi sesuai kondisi lapangan.'),
         ('Titik yang salah', 'Di tepi objek, misalnya tepi jalan yang perkerasannya hanya menutupi ±7 dari 10 m piksel (piksel campuran).')]
for k, (h, b) in enumerate(cards):
    box(s, 0.9 + k * 6.13, 6.15, 5.95, 1.75, fill=LIGHT, paras=[(h, 13.5, True, TEAL), (b, 12, False, DARK)])
box(s, 0.9, 8.1, 18.2, 1.0, fill=YEL_L, line=YEL, paras=[[('Kesimpulan  ', 13.5, True, TEAL),
    ('Kesalahan bersifat sistematis di tepi objek dan pada piksel campuran, bukan acak di seluruh wilayah; data tetap layak dipakai.', 12.5, False, DARK)]], anchor=MSO_ANCHOR.MIDDLE)
source(s, 'Sumber: Buku Subbab 3.5.2 dan 4.2.2, Gambar 14–15; sampel uji akurasi Dynamic World 2025 (Google Earth).', y=10.12)
s.notes_slide.notes_text_frame.text = ('Validasi spasial: titik-titik dari uji akurasi saya cek ulang di citra resolusi tinggi. Titik yang benar berada di kawasan yang jelas terbangun atau jelas bervegetasi. '
    'Titik yang salah umumnya di tepi objek, misalnya tepi jalan yang hanya menutupi sekitar 7 dari 10 meter piksel. '
    'Ini didukung angka: akurasi pada probabilitas rendah 97,7 persen, tetapi pada probabilitas dekat 0,5 hanya 52 persen. Jadi kesalahannya sistematis, bukan acak.')
p.save('/tmp/pptwork/v5/lahan_evaluasi_3slide.pptx')
print('ok', len(p.slides))
