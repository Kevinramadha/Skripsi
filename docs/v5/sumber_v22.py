import sys; sys.path.insert(0, '/tmp/pptwork/v5')
from single import make_subset
make_subset('/tmp/pptwork/v5/out7.pptx', [49], '/tmp/pptwork/v5/_base_sb.pptx')
exec(open('/tmp/pptwork/helpers_v4.py').read())
p = Presentation('/tmp/pptwork/v5/_base_sb.pptx')
S = p.slides[0]

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


setp(byid(S, 11), 1, 'Selisih pada uji penuh berawal dari satu titik, yaitu jumlah wisatawan, lalu terbawa ke variabel lain')
setp(byid(S, 74), 1, '(lebih lambat dari data)')
setp(byid(S, 125), 0, 'Karena wisatawan tumbuh lebih lambat dari data, variabel di sepanjang jalur ini ikut meleset dari data')
setp(byid(S, 128), 0, 'Buktinya: sumber selisihnya sama')
b = byid(S, 129)
setp(b, 0, 'Pada 6 dari 9 variabel, selisih terbesar berasal dari beda rata-rata (U1), bukan naik-turun tanpa pola.')
setp(b, 1, 'Hotel dan ODTW cocok saat diuji sendiri (DC 0,20 dan 0,34), tetapi meleset saat digabung (DC 0,82 dan 0,79).')
setp(b, 2, 'Uji P5 dan uji penuh sama-sama menunjukkan wisatawan tumbuh lebih lambat.')
setp(byid(S, 132), 0, 'Penyebabnya bukan nilai parameter')
setp(byid(S, 133), 0, 'Data wisatawan DIY melonjak saat pemulihan pascapandemi: tumbuh 12,72% (2022), 18,59% (2023), dan 24,86% (2024), '
                      'sedangkan simulasi hanya sekitar 6,3–6,7% per tahun. Lonjakan ini berada di luar cakupan model, jadi selisihnya bukan '
                      'karena nilai parameter subsistem wisatawan yang keliru. Hal ini diperiksa pada kalibrasi Tahap 3.')
S.notes_slide.notes_text_frame.text = (
    'Selisih pada uji penuh bisa ditelusuri ke satu titik, yaitu jumlah wisatawan. Karena wisatawan tumbuh lebih lambat dari data, pengeluaran wisatawan, PDRB, dan investasi ikut lebih rendah, '
    'sehingga hotel dan ODTW yang dibangun lebih sedikit, lalu tenaga kerja dan lahan terbangun ikut meleset. Buktinya ada tiga. Pertama, pada enam dari sembilan variabel, selisih terbesar berasal dari beda rata-rata. '
    'Kedua, hotel dan ODTW cocok dengan data saat diuji sendiri, tetapi meleset saat dijalankan bersama subsistem wisatawan. Ketiga, uji P5 dan uji penuh sama-sama menunjukkan wisatawan tumbuh lebih lambat. '
    'Penyebabnya bukan nilai parameter: data wisatawan DIY melonjak 12,72, 18,59, dan 24,86 persen pada 2022 sampai 2024 saat pemulihan pascapandemi, sedangkan simulasi hanya sekitar 6,5 persen per tahun. '
    'Lonjakan ini berada di luar cakupan model, dan hal ini saya periksa pada kalibrasi Tahap 3.')
p.save('/tmp/pptwork/v5/sumber_1slide.pptx')
print('ok')
