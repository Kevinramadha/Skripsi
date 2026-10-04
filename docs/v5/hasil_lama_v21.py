import sys; sys.path.insert(0, '/tmp/pptwork/v5')
from single import make_subset
make_subset('/tmp/pptwork/v5/out7.pptx', [47, 48], '/tmp/pptwork/v5/_base_hl.pptx')
exec(open('/tmp/pptwork/helpers_v4.py').read())
p = Presentation('/tmp/pptwork/v5/_base_hl.pptx')
S1, S2 = p.slides

def byid(slide, sid):
    for sh in all_text_shapes(slide.shapes):
        if sh.shape_id == sid: return sh
    raise KeyError(sid)

def setp(sh, i, text):
    para = sh.text_frame.paragraphs[i]
    r0 = para.runs[0]
    for r in para.runs[1:]: r._r.getparent().remove(r._r)
    r0.text = text

def setruns(sh, i, texts):
    runs = sh.text_frame.paragraphs[i].runs
    assert len(runs) >= len(texts), (len(runs), texts)
    for r, t in zip(runs, texts): r.text = t
    for r in runs[len(texts):]: r._r.getparent().remove(r._r)

def table_of(slide):
    return [sh for sh in slide.shapes if sh.has_table][0].table

def cell(T, r, c, text):
    para = T.cell(r, c).text_frame.paragraphs[0]
    for x in para.runs[1:]: x._r.getparent().remove(x._r)
    para.runs[0].text = text

# ---------------- slide 1: hasil uji parsial
setp(byid(S1, 11), 1, 'Saat diuji terpisah, tiap subsistem dapat mengikuti pola datanya; hanya subsistem wisatawan yang gagal uji tren')
T = table_of(S1)
cell(T, 0, 0, 'Uji · variabel dinilai'); cell(T, 0, 6, 'Error dominan'); cell(T, 8, 6, 'U1+U2')
for sid in (71,):
    sh = byid(S1, sid); sh.top = Emu(int(7.85 * E))
setp(byid(S1, 71), 0, 'Periode 2016–2025 tanpa 2020–2021. "Sama" = tren simulasi tidak berbeda nyata dengan tren data. E1/E2 P5 tidak dibaca karena trennya sudah berbeda (Barlas, 1989). *DC P5 dihitung dari notebook, tidak tercantum di tabel buku.')
b = byid(S1, 80)
setp(b, 0, 'Wisatawan (P5)')
setp(b, 1, 'Simulasi tumbuh ≈6,4% per tahun, sedangkan data ≈11,7% per tahun. Selisihnya sistematis (U1+U2 ≈ 0,96), bukan acak, sehingga ditelusuri lewat kalibrasi.')
setp(byid(S1, 81), 0, 'Garis hitam = data · garis merah putus-putus = simulasi · area abu-abu = 2020–2021 (COVID). Kiri atas: P1 hotel · kanan atas: P4 lahan · kiri bawah: P5 wisatawan')
setruns(byid(S1, 84), 0, ['Intinya  ', 'Saat input dari subsistem lain diganti data aktual, tiap subsistem dapat mengikuti pola datanya (MAPE seluruhnya < 20%); kelemahan hanya ada pada subsistem wisatawan.'])
S1.notes_slide.notes_text_frame.text = (
    'Pada uji parsial, input dari subsistem lain diganti data aktual, sehingga yang dinilai hanya struktur subsistem itu sendiri. Hasilnya, subsistem akomodasi paling baik: jumlah hotel lolos uji tren, E1, dan E2 dengan DC 0,2011. '
    'P1b sebagai uji kekokohan P1 memberi pola serupa. Seluruh MAPE di bawah 20 persen. Satu-satunya yang gagal uji tren adalah subsistem wisatawan: simulasi tumbuh sekitar 6,4 persen per tahun, '
    'sedangkan data sekitar 11,7 persen. Selisihnya sistematis, bukan acak, sehingga penyebabnya ditelusuri lewat kalibrasi.')

# ---------------- slide 2: hasil uji penuh
setp(byid(S2, 11), 1, 'Saat semua subsistem dijalankan bersama, kecocokan pola melemah karena error dari subsistem wisatawan merambat')
setp(byid(S2, 66), 0, 'DC per variabel: uji parsial vs uji penuh (makin kecil makin baik)')
setp(byid(S2, 67), 0, 'DC 0,4–0,7 = rata-rata sampai baik (Barlas, 1989). TPK justru membaik pada uji penuh. Wisatawan gagal uji tren pada P5 maupun uji penuh.')
T = table_of(S2)
cell(T, 0, 1, 'Variabel uji penuh (MAPE)')
b = byid(S2, 77)
setp(b, 0, 'Mengapa melemah? Wisatawan tumbuh lebih lambat dari data → pengeluaran, PDRB, dan investasi ikut rendah → hotel dan ODTW yang dibangun lebih sedikit. U1 dominan pada 6 dari 9 variabel: error dari satu sumber.')
S2.notes_slide.notes_text_frame.text = (
    'Pada uji penuh, model dijalankan tanpa penggantian data sehingga semua subsistem saling memengaruhi. Grafik ini membandingkan DC uji parsial dan uji penuh. '
    'DC hotel naik dari 0,20 menjadi 0,82, ODTW dari 0,34 menjadi 0,79, dan tenaga kerja dari 0,49 menjadi 0,89. Ini bukan karena struktur subsistemnya salah, '
    'tetapi karena jumlah wisatawan tumbuh lebih lambat dari data, sehingga pengeluaran, PDRB, dan investasi ikut rendah, lalu hotel dan ODTW yang dibangun lebih sedikit. TPK justru membaik. '
    'Dari sisi besaran error, MAPE tetap wajar: ODTW sangat baik, lima variabel baik, tiga variabel ekonomi layak, dan tidak ada yang buruk. '
    'U1 dominan pada enam dari sembilan variabel, artinya error berasal dari satu sumber bersama, yaitu pertumbuhan wisatawan.')
p.save('/tmp/pptwork/v5/hasil_lama_2slide.pptx')
print('ok')
