import sys; sys.path.insert(0, '/tmp/pptwork/v5')
from single import make_subset
make_subset('/tmp/pptwork/v5/out7.pptx', [51], '/tmp/pptwork/v5/_base_kh.pptx')
exec(open('/tmp/pptwork/helpers_v4.py').read())
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE
p = Presentation('/tmp/pptwork/v5/_base_kh.pptx')
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


s = p.slides[0]
prep(s, 'Kalibrasi: Hasil Tiap Tahap',
     'Lima tahap dijalankan; dari tiga parameter yang dikalibrasi, tidak ada yang diganti')
C = [('TAHAP 0', 'Membetulkan cara hitung', 'Laju pertumbuhan eksternal (LPE) dan laju penurunan dasar (LPD) wisatawan', [
        ('Yang dilakukan', 'Rumus untuk menghitung LPE dan LPD dicek ulang terhadap persamaan model.'),
        ('Hasilnya', 'Rumus awal menganggap daya tarik 2024 bernilai 1, padahal nilainya 0,99223. Setelah dibetulkan: LPE 0,26864 → 0,27726 dan LPD 0,20148 → 0,207945.'),
        ('Dampak', 'Wisatawan 2050 hanya naik sekitar 1,6%; hasil uji kondisi ekstrem tidak berubah.')],
      'Nilai dibetulkan, bukan dicari ulang (bukan kalibrasi)', YEL, DARK),
     ('TAHAP 1', 'Subsistem akomodasi', 'Batas TPK pemicu pembangunan hotel dan laju demolisi (hotel tutup)', [
        ('Yang dilakukan', '775 pasangan nilai dicoba (batas TPK 0,20–0,35; demolisi 0,02–0,08) dan dibandingkan dengan data hotel (uji P1).'),
        ('Hasilnya', 'Pasangan terbaik (0,350; 0,060) 11,64% lebih cocok, tetapi letaknya di batas atas yang dicoba. Tanpa data 2019, keunggulannya tinggal 5,74%; pada data dengan COVID justru memburuk; pada P1b hanya 4,89%.'),
        ('Artinya', 'Keunggulan nilai baru hanya muncul karena satu tahun data yang janggal.')],
      'Nilai dari data tetap dipakai: batas TPK 0,275; demolisi 0,05', TEAL, WHITE),
     ('TAHAP 2', 'Subsistem lahan', 'Laju konversi dasar (laju lahan berubah menjadi lahan terbangun)', [
        ('Yang dilakukan', 'Nilai 0,0034–0,0851 dicoba dan dibandingkan dengan data lahan terbangun (uji P4).'),
        ('Hasilnya', 'Nilai 0,0639 14,76% lebih cocok dan letaknya di tengah, bukan di tepi. Selisih rata-rata simulasi dan data (U1) turun dari 0,4250 ke 0,0755.'),
        ('Artinya', 'Memenuhi syarat dipakai (R4), tetapi harus diuji dulu pada model penuh (Tahap 4).')],
      'Diterima sementara: 0,0639, lalu diuji di Tahap 4', YEL, DARK),
     ('TAHAP 3', 'Subsistem wisatawan', 'LPE dan LPD (hanya diperiksa, tidak dikalibrasi)', [
        ('Yang dilakukan', 'Tidak dicari nilai terbaik karena keduanya tidak memenuhi syarat dikalibrasi; hanya dihitung berapa LPE yang diminta data.'),
        ('Hasilnya', 'Data meminta LPE 0,410–0,490 (nilai dari data 0,27726). Namun banyak pasangan LPE–LPD yang sama cocoknya, jadi data hanya bisa menentukan selisih keduanya, bukan masing-masing nilai.'),
        ('Penyebab', 'Wisatawan melonjak setelah pandemi (2022–2024, puncak 24,86% per tahun), hal yang tidak dimodelkan.')],
      'Nilai dari data tetap dipakai: LPE 0,27726; LPD 0,207945', TEAL, WHITE),
     ('TAHAP 4', 'Uji pada model penuh', 'Laju konversi 0,0639 hasil Tahap 2', [
        ('Yang dilakukan', 'Nilai 0,0639 dicoba pada model penuh dan uji parsial (13 variabel yang dinilai).'),
        ('Hasilnya', '12 variabel hampir tidak berubah, tetapi lahan terbangun pada uji penuh menjadi 32,4% kurang cocok (batas toleransi 5%; pemicu M1).'),
        ('Penyebab', 'Uji P4 mulai 2016 saat lahan masih rendah, jadi laju lebih cepat membantu. Uji penuh mulai 2019 saat lahan sudah tinggi, jadi laju yang sama membuat simulasi melampaui data.')],
      'Ditolak: laju konversi kembali ke nilai dari data (0,0436)', RED, WHITE)]
w, g = 3.5, 0.175
for k, (tag, title, par, items, badge, bfill, bcol) in enumerate(C):
    x = 0.9 + k * (w + g)
    paras = [[(tag, 9.5, True, GREY)], [(title, 12.5, True, TEAL)], [(par, 10, True, DARK, True)]]
    for lab, txt in items:
        paras.append([(lab + ':  ', 10.5, True, TEAL), (txt, 10.5, False, DARK)])
    box(s, x, 1.95, w, 6.55, fill=LIGHT, line=LINE, paras=paras, margin=0.14)
    box(s, x + 0.12, 7.62, w - 0.24, 0.75, fill=bfill, line=None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, margin=0.06,
        paras=[[(badge, 10, True, bcol)]])
    if k < 4:
        arrow(s, x + w - 0.02, 4.9, g + 0.04, 0.3)
box(s, 0.9, 8.65, 18.2, 1.3, fill=TEAL, line=None, anchor=MSO_ANCHOR.MIDDLE, margin=0.25, paras=[
    [('Hasil akhir: dari 3 parameter yang dikalibrasi (batas TPK, laju demolisi, laju konversi), tidak ada yang diganti', 13.5, True, YEL)],
    [('Nilai yang dihitung dari data sudah layak dipakai. Selisih pada jumlah wisatawan bukan karena nilai parameter yang salah, tetapi karena lonjakan wisatawan setelah pandemi yang berada di luar cakupan model.', 11, False, WHITE)]])
source(s, 'Sumber: Buku Subbab 4.6 (Tabel 48–55). R4 dan M1 = aturan keputusan dan pemicu penolakan pada slide sebelumnya (Tabel 19–20).', y=10.12)
s.notes_slide.notes_text_frame.text = (
    'Kalibrasi dijalankan dalam lima tahap. Tahap 0 bukan kalibrasi: saya membetulkan rumus LPE dan LPD karena rumus awal menganggap daya tarik 2024 bernilai 1, padahal 0,99223. Dampaknya kecil, dan hasil uji ekstrem tidak berubah. '
    'Tahap 1 pada akomodasi: pasangan nilai terbaik memang 11,64 persen lebih cocok, tetapi letaknya di batas atas, dan tanpa data 2019 keunggulannya tinggal 5,74 persen. Jadi keunggulannya hanya karena satu tahun data yang janggal, dan nilai dari data tetap dipakai. '
    'Tahap 2 pada lahan: laju konversi 0,0639 lebih cocok 14,76 persen dan memenuhi syarat, sehingga diterima sementara. '
    'Tahap 3 pada wisatawan hanya pemeriksaan: data meminta LPE yang lebih tinggi, tetapi data hanya bisa menentukan selisih LPE dan LPD, dan penyebab selisihnya adalah lonjakan wisatawan setelah pandemi. '
    'Tahap 4 menguji hasil Tahap 2 pada model penuh: lahan terbangun justru 32,4 persen kurang cocok, karena uji penuh dimulai dari lahan yang sudah tinggi. Hasilnya ditolak. '
    'Jadi dari tiga parameter yang dikalibrasi, tidak ada yang diganti.')
p.save('/tmp/pptwork/v5/kalibrasi_hasil_1slide.pptx')
print('ok')
