exec(open('/tmp/pptwork/helpers_v4.py').read())
from pptx import Presentation
p = Presentation('/tmp/pptwork/v5/lahan_evaluasi_3slide.pptx')
NAVY = '0B5E6E'; GREEN = 'C9F0D6'; PINK = 'FDE2DE'
S = list(p.slides)
def find_title(slide):
    for sh in slide.shapes:
        if sh.has_text_frame and sh.top is not None and 0.6*E <= sh.top <= 1.3*E and sh.width > 9*E and sh.text_frame.text.strip():
            return sh
def set_tr(s, title, resume):
    ps = find_title(s).text_frame.paragraphs
    ps[0].runs[0].text = title; ps[1].runs[0].text = resume
def tag(s, txt):
    box(s, 16.3, 10.55, 1.5, 0.42, fill=YEL, line=None, paras=[(txt, 11, True, DARK)], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, margin=0, radius=0.5)

# ---------- Versi A (2 slide)
a1, b, a2 = S[0], S[1], S[2]
set_tr(a1, 'Lahan Terbangun — Uji Akurasi (1/2): Metrik Evaluasi',
       'Dynamic World cukup akurat untuk data lahan terbangun: akurasi 89,95%, Kappa 0,61')
tag(a1, 'Versi A · 1/2')
set_tr(a2, 'Lahan Terbangun — Uji Akurasi (2/2): Letak Kesalahan',
       'Pemeriksaan visual titik sampel (validasi spasial): kesalahan terkumpul di tepi objek')
for sh in a2.shapes:
    if sh.has_text_frame and sh.text_frame.text.startswith('Cara'):
        ps = sh.text_frame.paragraphs
        ps[1].runs[0].text = 'Beberapa dari 200 titik sampel uji akurasi dilihat ulang pada citra resolusi tinggi Google Earth untuk melihat di mana kesalahan terjadi.'
        for r in ps[1].runs[1:]: r._r.getparent().remove(r._r)
    if sh.has_text_frame and sh.text_frame.text.startswith('Kesalahan menumpuk'):
        set_text(sh, 'Dihitung dari 200 titik yang sama dengan slide 1/2, dikelompokkan menurut probabilitas "built"')
tag(a2, 'Versi A · 2/2')

# ---------- Versi B (1 slide) — memakai slide temporal sebagai kanvas
t = find_title(b)
for sh in list(b.shapes):
    keep = (sh._element is t._element) or sh.top >= 10.3*E or (sh.left >= 18.0*E and sh.top < 1.0*E) or sh.top < 0.45*E
    if not keep:
        sh._element.getparent().remove(sh._element)
set_tr(b, 'Estimasi Lahan Terbangun — Uji Akurasi dan Validasi Spasial',
       'Dynamic World cukup akurat (89,95%; Kappa 0,61); kesalahan terkumpul di tepi objek')
box(b, 0.9, 1.95, 18.2, 0.55, fill=NAVY, line=None, paras=[[('Desain uji  ', 12.5, True, YEL),
    ('Peta Dynamic World 2025 (probabilitas built ≥ 0,5) · 200 titik acak berstrata (100 terbangun, 100 bukan) · rujukan: citra resolusi tinggi Google Earth', 12, True, WHITE)]], anchor=MSO_ANCHOR.MIDDLE)
rows = [['Metrik', 'Hasil', 'IK 95%', 'Cara membaca'],
        ['Overall accuracy terbobot luas', '89,95%', '86,05–93,85%', 'Ukuran utama (menyesuaikan luas kelas)'],
        ['Overall accuracy tak terbobot', '80,50%', '74,46–85,39%', 'Bias karena sampel 50:50'],
        ["User's accuracy (terbangun)", '66,00%', '56,67–75,33%', 'Ketepatan peta'],
        ["Producer's accuracy (terbangun)", '73,58%', '56,66–90,50%', 'Kelengkapan peta'],
        ['F1-score (terbangun)', '77,19%', '—', 'Gabungan UA dan PA'],
        ['Koefisien Kappa', '0,61', '0,50–0,72', 'Kesepakatan kuat (Landis & Koch)']]
gf = table(b, 0.9, 2.65, 11.0, [3.6, 1.5, 2.2, 3.7], rows, size=11.5, rowh=0.43, bold_first_col=True, hl={(1, 1): GREEN, (6, 1): GREEN})
for r in range(1, 7):
    for k in (1, 2):
        gf.table.cell(r, k).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
for r in (1, 6):
    gf.table.cell(r, 1).text_frame.paragraphs[0].runs[0].font.bold = True
rows2 = [['Peta \\ Rujukan', 'Bukan', 'Terbangun'], ['Bukan terbangun', '95', '5'], ['Terbangun', '34', '66']]
gf = table(b, 12.2, 2.65, 6.9, [2.7, 2.1, 2.1], rows2, size=12, rowh=0.45, bold_first_col=True, hl={(1, 1): GREEN, (2, 2): GREEN, (2, 1): PINK, (1, 2): LIGHT})
for r in range(3):
    for k in (1, 2):
        gf.table.cell(r, k).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
tb(b, 12.2, 4.05, 6.9, 0.3, [('Matriks konfusi (jumlah titik)', 10.5, True, TEAL)])
box(b, 12.2, 4.45, 6.9, 1.2, fill=LIGHT, paras=[('Kesalahan utama: commission error', 12.5, True, TEAL),
    ('34 titik dipetakan terbangun padahal bukan (vs 5 omission error).', 11, False, DARK)])
pic_fit(b, '/tmp/pptwork/v5/dw_built.png', 0.9, 5.9, 4.9, 3.0)
tb(b, 0.9, 8.88, 4.9, 0.3, [('Contoh titik sampel (titik 69, Google Earth)', 10.5, True, TEAL)], align=PP_ALIGN.CENTER)
rows3 = [['Validasi spasial (200 titik yang sama)', 'Nilai'], ['Rata-rata probabilitas — titik benar', '0,330'],
         ['Rata-rata probabilitas — titik salah', '0,574'], ['Akurasi pada probabilitas 0–0,25', '97,7%'],
         ['Akurasi pada probabilitas 0,5–0,6', '52,0%']]
gf = table(b, 6.05, 5.9, 5.85, [4.5, 1.35], rows3, size=11.5, rowh=0.55, bold_first_col=True, hl={(2, 1): PINK, (3, 1): GREEN, (4, 1): PINK})
for r in range(5):
    gf.table.cell(r, 1).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
box(b, 12.2, 5.9, 6.9, 3.0, fill=LIGHT, paras=[('Di mana kesalahan terjadi?', 12.5, True, TEAL),
    ('Titik yang dicek ulang di Google Earth: titik di kawasan yang jelas terbangun atau jelas bervegetasi sesuai kondisi lapangan. Titik yang salah berada di tepi objek, misalnya tepi jalan yang hanya menutupi ±7 dari 10 m piksel.', 11, False, DARK)])
box(b, 0.9, 9.2, 18.2, 0.75, fill=YEL_L, line=YEL, paras=[[('Kesimpulan  ', 12.5, True, TEAL),
    ('Data Dynamic World layak dipakai; kesalahannya sistematis di tepi objek dan pada piksel campuran, bukan acak.', 12, False, DARK)]], anchor=MSO_ANCHOR.MIDDLE)
source(b, 'Sumber: Buku Subbab 3.5.2 dan 4.2.2, Tabel 31–32, Gambar 14–15. Rumus metrik ditaruh di lampiran.', y=10.1)
b.notes_slide.notes_text_frame.text = ('Versi satu slide: uji akurasi dan validasi spasial digabung. Akurasi terbobot luas 89,95 persen dan Kappa 0,61. '
    'Kesalahan utamanya commission error. Dari 200 titik yang sama, akurasi titik berprobabilitas rendah 97,7 persen, tetapi titik dekat 0,5 hanya 52 persen; '
    'pengecekan visual menunjukkan kesalahan ada di tepi objek. Jadi data layak dipakai, dengan kesalahan yang sistematis.')
tag(b, 'Versi B')
# urutan: A1, A2, B
lst = p.slides._sldIdLst
ids = list(lst)
for el in ids: lst.remove(el)
for el in (ids[0], ids[2], ids[1]): lst.append(el)
p.save('/tmp/pptwork/v5/lahan_versiAB.pptx')
print('ok')
