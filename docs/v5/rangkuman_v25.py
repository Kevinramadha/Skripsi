import sys; sys.path.insert(0, '/tmp/pptwork/v5')
from single import make_subset
make_subset('/tmp/pptwork/v5/out7.pptx', [53], '/tmp/pptwork/v5/_base_rk.pptx')
exec(open('/tmp/pptwork/helpers_v4.py').read())
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE
p = Presentation('/tmp/pptwork/v5/_base_rk.pptx')
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
prep(s, 'Rangkuman Kelayakan Model', 'Model sudah cukup layak untuk membandingkan skenario kebijakan')
CARDS = [('Uji struktur', 'Lolos', TEAL, ['Persamaan dan satuannya konsisten', 'Tetap masuk akal saat diberi nilai ekstrem']),
         ('Uji perilaku', 'Cukup baik', '2A9DB0', ['Simulasi cukup dekat dengan data', 'Selisih terbesar ada pada jumlah wisatawan']),
         ('Kalibrasi', 'Nilai tetap', TEAL, ['Tidak ada parameter yang perlu diganti', 'Selisih wisatawan karena lonjakan setelah pandemi'])]
w, g = 5.9, 0.25
for k, (title, status, col, pts) in enumerate(CARDS):
    x = 0.9 + k * (w + g)
    box(s, x, 2.1, w, 2.55, fill=LIGHT, line=LINE, radius=0.05)
    box(s, x, 2.1, w, 1.05, fill=col, line=None, radius=0.1, anchor=MSO_ANCHOR.MIDDLE, margin=0.25,
        paras=[[(title, 12.5, True, 'D7EEF2')], [(status, 20, True, WHITE)]])
    tb(s, x + 0.3, 3.4, w - 0.5, 1.5, [[('✓  ', 14, True, '1E7A43'), (t_, 14, False, DARK)] for t_ in pts])
    if k < 2:
        arrow(s, x + w + 0.02, 3.4, g - 0.04, 0.3)
tb(s, 0.9, 5.15, 18.2, 0.5, [[('Yang perlu diingat saat membaca hasil', 14, True, TEAL)]])
B = ['Dibaca sebagai arah dan perbandingan, bukan angka pasti', 'Belum diuji dengan data baru',
     'Tidak memuat pandemi atau bencana', 'Laju pertumbuhan dan penurunan wisatawan belum bisa dipisahkan']
for k, b_ in enumerate(B):
    x = 0.9 + (k % 2) * 9.2; y = 5.75 + (k // 2) * 0.95
    box(s, x, y, 9.0, 0.72, fill=YEL_L, line=YEL, anchor=MSO_ANCHOR.MIDDLE, margin=0.25,
        paras=[[('!  ', 13, True, '9B2C1F'), (b_, 13, False, DARK)]])
box(s, 0.9, 7.95, 18.2, 1.4, fill=TEAL, line=None, anchor=MSO_ANCHOR.MIDDLE, margin=0.35, paras=[
    [('Kesimpulan', 12.5, True, YEL)],
    [('Model dapat dipakai untuk membandingkan skenario kebijakan 2025–2050: mana yang arahnya lebih baik, dan seberapa besar bedanya.', 14.5, True, WHITE)]])
source(s, 'Sumber: Buku Subbab 4.4–4.6.', y=10.12)
s.notes_slide.notes_text_frame.text = (
    'Jadi, apakah model ini layak dipakai? Ada tiga hal yang saya periksa. Dari uji struktur, persamaan dan satuannya konsisten, dan model tetap masuk akal walaupun diberi nilai ekstrem. '
    'Dari uji perilaku, hasil simulasi cukup dekat dengan data. Selisih terbesar ada pada jumlah wisatawan. Dari kalibrasi, tidak ada nilai parameter yang perlu diganti; '
    'selisih wisatawan itu muncul karena lonjakan wisatawan setelah pandemi, yang memang tidak dimodelkan. '
    'Ada beberapa hal yang perlu diingat: hasilnya dibaca sebagai arah dan perbandingan, bukan angka pasti; model belum diuji dengan data baru; pandemi dan bencana tidak dimodelkan; '
    'dan laju pertumbuhan serta penurunan wisatawan belum bisa dipisahkan oleh data. Dengan catatan itu, model dapat dipakai untuk membandingkan skenario kebijakan sampai 2050.')
p.save('/tmp/pptwork/v5/rangkuman_1slide.pptx')
print('ok')
