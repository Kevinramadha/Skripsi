import sys, os, re
sys.path.insert(0, '/tmp/pptwork/v5')
exec(open('/tmp/pptwork/v6/lamp_lib.py').read())
prs = Presentation('/tmp/pptwork/v6/final_in.pptx')
D = Deck(prs, prs.slides[74])
for P in 'ABCDEFGHI':
    exec(open(f'/tmp/pptwork/v6/part{P}.py').read())

SECTIONS = [  # (kode, judul, [items]) item = int (slide lama, 1-based) atau nama fungsi
    ('A', 'Data dan penyusunan data', [57, 'A_sumber', 'A_historis', 'A_sambung', 51, 'A_ekstrapolasi', 75]),
    ('B', 'Citra satelit: NTL dan Dynamic World', ['B_proxy', 'B_ntl', 'B_dw', 'B_kelas', 54, 'B_odtw_proses', 'B_loocv', 53, 'B_dw_proses', 'B_dw_eval', 52, 'B_sampel']),
    ('C', 'Struktur model', [56, 'C_kandidat', 55, 'C_loop', 'C_peran', 'C_batas', 58, 'C_parameter', 'C_formulasi']),
    ('D', 'Uji struktur', ['D_alur', 'D_dimensi', 'D_kekekalan', 'D_loop', 'D_loop2', 'D_ekstrem', 'D_ekstrem2', 'D_ekstrem3', 'D_ekstrem_grafik', 'D_galat', 68]),
    ('E', 'Uji perilaku', ['E_ukuran', 'E_tren', 'E_theil', 'E_rancangan', 'E_parsial', 'E_penuh', 'E_grafik']),
    ('F', 'Kalibrasi', ['F_protokol', 'F_tahap0', 'F_tahap1', 'F_tahap1b', 'F_tahap2', 'F_tahap4', 'F_tahap3', 'F_tahap3b', 'F_ringkasan']),
    ('G', 'Analisis sensitivitas', ['G_rancangan', 'G_pm10', 'G_peringkat', 'G_tornado', 'G_rentang', 'G_rentang2']),
    ('H', 'Skenario kebijakan', ['H_tuas', 'H_indikator', 'H_hasil', 63, 'H_grafik', 'H_komposisi', 'H_kokoh', 'H_kokoh2', 'H_implikasi']),
    ('I', 'Aplikasi web', ['I_alur', 'I_tampilan', 'I_blackbox', 'I_sus1', 'I_sus2', 'I_sus3']),
    ('J', 'Keterbatasan dan daftar istilah', ['J_keterbatasan', 73, 74])]

old = list(prs.slides)
daftar = D.slide('Daftar Lampiran')
order = []          # list of (slide, section)
for code, name, items in SECTIONS:
    for it in items:
        if isinstance(it, int):
            order.append((old[it - 1], code, 'old'))
        else:
            n0 = len(D.new)
            globals()[it](D)
            for sl in D.new[n0:]:
                order.append((sl, code, 'new'))


def title_shape(sl):
    for sh in sl.shapes:
        if sh.shape_id in (13, 14) and sh.has_text_frame and sh.text_frame.text.strip():
            return sh
    return None


def base_title(t):
    t = re.sub(r'^Lampiran( \d+)? · ', '', t.split('\n')[0])
    return re.sub(r' \(\d+/\d+\)$', '', t).strip()


# nomor lampiran: slide berurutan dengan judul dasar sama (beda (k/n)) memakai nomor yang sama
num_of = []; n = 0; prev = None
for sl, code, kind in order:
    tsh = title_shape(sl)
    bt = base_title(tsh.text_frame.text) if tsh else id(sl)
    if bt != prev:
        n += 1
    num_of.append(n); prev = bt

sec_range = {}
toc_titles = {}
for (sl, code, kind), k in zip(order, num_of):
    lo, hi = sec_range.get(code, (k, k)); sec_range[code] = (min(lo, k), max(hi, k))
    tsh = title_shape(sl)
    toc_titles.setdefault(code, [])
    bt = base_title(tsh.text_frame.text)
    if not toc_titles[code] or toc_titles[code][-1][1] != bt:
        toc_titles[code].append((k, bt))
    # ganti judul
    r = tsh.text_frame.paragraphs[0].runs[0]
    txt = re.sub(r'^Lampiran( \d+)? · ', '', r.text)
    r.text = f'Lampiran {k} · ' + txt
    full = tsh.text_frame.paragraphs[0].text
    if tsh.shape_id == 14:   # slide definisi (judul sempit)
        r.font.size = Pt(30)
    elif len(full) > 64:
        r.font.size = Pt(26 if len(full) > 72 else 28)
    elif len(full) > 52 and (r.font.size is None or r.font.size.pt > 30):
        r.font.size = Pt(30)

# isi slide Daftar Lampiran
s = daftar
sub(s, 'Lampiran dikelompokkan mengikuti alur penelitian; nomor di kiri adalah nomor lampiran')
for j, (code, name, items) in enumerate(SECTIONS):
    col, row = j % 2, j // 2
    x = 0.9 + col * 9.25; y = 2.0 + row * 1.6; w = 8.95
    lo, hi = sec_range[code]
    box(s, x, y, 1.6, 1.45, fill=TEAL, line=None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER,
        paras=[[(f'{lo}–{hi}' if hi > lo else str(lo), 15, True, WHITE)]])
    names = '; '.join(t for _, t in toc_titles[code])
    if len(names) > 230:
        names = names[:227].rsplit(';', 1)[0] + '; …'
    box(s, x + 1.7, y, w - 1.7, 1.45, fill=LIGHT, line=LINE, margin=0.15, anchor=MSO_ANCHOR.MIDDLE,
        paras=[[(name, 13, True, TEAL)], [(names, 9.5, False, DARK)]])

# urutkan ulang: 50 slide utama, Daftar, lalu lampiran; buang lampiran lama yang digantikan
sldIdLst = prs.slides._sldIdLst
ids = {sl.slide_id: el for sl, el in zip(prs.slides, list(sldIdLst))}
keep = [sl for sl in old[:50]] + [daftar] + [sl for sl, _, _ in order]
keep_ids = [sl.slide_id for sl in keep]
for el in list(sldIdLst):
    sldIdLst.remove(el)
dropped = []
for sl in prs.slides._sldIdLst:  # empty now
    pass
for sid in keep_ids:
    sldIdLst.append(ids[sid])
for sl, el in zip(list(old), []):
    pass
# lepas relasi slide lama yang tidak dipakai
kept_set = set(keep_ids)
for sid, el in ids.items():
    if sid not in kept_set:
        rId = el.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        dropped.append(rId)
        prs.part.drop_rel(rId)

# nomor halaman
for i, sl in enumerate(prs.slides, 1):
    if i <= 50:
        continue
    for sh in sl.shapes:
        if not sh.has_text_frame or sh.top < Inches(9.6):
            continue
        t = sh.text_frame.text.strip()
        if (sh.shape_id == 25 and t == '') or (t.isdigit() and len(t) <= 3):
            p = sh.text_frame.paragraphs[0]
            if p.runs:
                p.runs[0].text = str(i)
                for rr in p.runs[1:]: rr.text = ''

OUT = sys.argv[1]
prs.save(OUT)
print('total slides', len(prs.slides), 'lampiran', len(order) + 1, 'dropped', len(dropped))
open('/tmp/pptwork/v6/lamp_count.txt', 'w').write(str(len(prs.slides)))
