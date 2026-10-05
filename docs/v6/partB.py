# ===================== B. CITRA SATELIT =====================
import csv as _csv, openpyxl as _ox


def B_proxy(D):
    s = D.slide('Lampiran · Usulan Data Proxy Berbasis Citra')
    sub(s, 'Citra dipakai hanya untuk variabel yang data resminya tidak lengkap; tiap usulan diuji dulu sebelum dipakai')
    rows = [['No', 'Variabel model', 'Data resmi tersedia', 'Sumber citra', 'Resolusi spasial', 'Resolusi temporal', 'Variabel pendukung non-citra', 'Variabel citra', 'Metode', 'Hasil uji', 'Status', 'Referensi'],
            ['1', 'Jumlah ODTW', 'BPS 2018–2024 (kosong 2015–2017, 2025)', 'VIIRS DNB Monthly (NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG)', '±500 m', 'Bulanan → komposit tahunan', '—', 'Radiansi cahaya malam (avg_rad)', 'Regresi linear ODTW = a + b·NTL', 'R² selisih 0,405; RMSE LOOCV 5,99%', 'Dipakai', 'Henderson et al. (2012)'],
            ['2', 'Lahan terbangun', 'Tidak ada seri tahunan provinsi yang konsisten (BPS & DLHK fluktuatif)', 'Dynamic World V1 (GOOGLE/DYNAMICWORLD/V1), basis Sentinel-2', '10 m', 'Per citra Sentinel-2 → rata-rata tahunan', '—', 'Probabilitas kelas built', 'Klasifikasi langsung, ambang 0,5', 'OA terbobot 89,95%; Kappa 0,61', 'Dipakai', 'Brown et al. (2022); Olofsson et al. (2014)'],
            ['3', 'Tenaga kerja pariwisata', 'Sakernas 2017–2025 (kosong 2015–2016)', 'VIIRS DNB Monthly', '±500 m', 'Tahunan', '—', 'Radiansi cahaya malam', 'Regresi', 'R² level 0,130; R² selisih 0,070', 'Ditolak', '—'],
            ['4', 'Tenaga kerja pariwisata', 'Sakernas 2017–2025', '— (non-citra)', '—', 'Tahunan', 'PDRB pariwisata (I, R–U)', '—', 'Regresi', 'R² selisih 0,093; rasio TK/PDRB tidak stabil', 'Ditolak → CAGR', '—']]
    hl = {(1, 10): GREEN, (2, 10): GREEN, (3, 10): PINK, (4, 10): PINK}
    gf = tbl(s, 0.9, 2.1, 18.2, [0.45, 1.5, 2.1, 2.5, 1.0, 1.5, 1.4, 1.5, 1.7, 1.9, 1.0, 1.65], rows, size=9.5, rowh=1.2, hl=hl, center=(0, 4, 10))
    gf.table.rows[0].height = Inches(0.6)
    note(s, 'Usulan 3 dan 4 diuji pada notebook ekstrapolasi tenaga kerja: sinyal sektor pariwisata (±6–7% angkatan kerja) tenggelam dalam sinyal NTL agregat, dan rasio TK/PDRB berubah 21,5–29,3 jiwa/miliar Rp. Karena itu TK 2015–2016 diisi dengan ekstrapolasi CAGR.', y=7.75, h=1.0)
    src(s, 'Sumber: Buku Subbab 3.5 dan 4.2; GEE.rtf; notebook “Ekstrapolasi Tenaga Kerja Pariwisata” (repository). Resolusi VIIRS ±500 m mengikuti skala ekstraksi di skrip GEE.')


def B_ntl(D):
    s = D.slide('Lampiran · Pemrosesan Citra NTL (VIIRS) dan Nilainya')
    sub(s, 'NTL diekstraksi di Google Earth Engine dan dirata-ratakan menjadi satu nilai per tahun untuk wilayah DIY')
    hdr(s, 0.9, 2.1, 8.7, 'Tahapan di Google Earth Engine')
    steps(s, 0.9, 2.7, 8.7, [
        ('Batas wilayah', 'FAO/GAUL/2015/level1, ADM1 = Daerah Istimewa Yogyakarta.'),
        ('Koleksi citra', 'NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG, band avg_rad (nW/cm²/sr).'),
        ('Agregasi temporal', 'Komposit bulanan dirata-ratakan menjadi komposit tahunan.'),
        ('Agregasi spasial', 'Rata-rata zonal seluruh piksel DIY pada skala 500 m (reduceRegion mean).')], h=0.85, gap=0.1, size=11)
    formula(s, 0.9, 6.55, 8.7, 1.5, ['NTLₜ = (1/n) · Σᵢ Rᵢ,ₜ     (rata-rata n komposit bulanan pada tahun t)',
                                     'NTL_DIY,ₜ = (1/N) · Σₚ Rₚ,ₜ     (rata-rata N piksel di batas DIY)'], title='Rumus', size=12)
    yrs = [str(y) for y in range(2015, 2026)]
    ntl = [1.261585, 1.054415, 1.438316, 1.668258, 2.004828, 1.827902, 1.540893, 1.483312, 2.512341, 2.457036, 2.287813]
    sm = [16195.96, 13536.36, 18464.79, 21416.74, 25737.55, 23466.22, 19781.65, 19042.44, 32252.89, 31542.89, 29370.45]
    odtw = ['165*', '158*', '171*', '177', '189', '180', '170', '183', '201', '218', '201*']
    rows = [['Tahun', 'NTL rata-rata', 'NTL jumlah', 'ODTW']]
    hl = {}
    for i, (y, a, b, c) in enumerate(zip(yrs, ntl, sm, odtw), 1):
        rows.append([y, fmt(a, 3), fmt(b, 0), c])
        if '*' in c: hl[(i, 3)] = YEL_L
    tbl(s, 10.0, 2.1, 4.6, [0.9, 1.3, 1.3, 1.1], rows, size=10.5, rowh=0.42, center=(0, 1, 2, 3), hl=hl)
    line_chart(s, 14.8, 2.1, 4.3, 3.6, yrs, [('NTL rata-rata', ntl)], [TEAL], fmt_='0.0', legend=False, fs=9)
    card(s, 14.8, 5.85, 4.3, 2.2, 'Cara membaca', ['NTL turun 2020–2022 (pandemi) lalu naik tajam 2023.', 'Rentang data latih 2018–2024: 1,483–2,512; NTL 2016 (1,054) di luar rentang.'], size=10.5, tsize=11.5)
    T(s, 10.0, 7.2, 4.6, 0.5, [[('*estimasi dari regresi NTL', 9.5, False, GREY, True)]])
    note(s, 'NTL rata-rata dipakai sebagai peubah penjelas ODTW. Nilai jumlah (sum) hanya pelengkap. Ekstraksi titik validasi spasial memakai buffer 300 m pada skala 500 m (citra 2025).', y=8.3, h=0.85)
    src(s, 'Sumber: Buku Subbab 3.5.1; GEE.rtf; NTL_DIY_2015_2025.csv (repository).')


def B_dw(D):
    s = D.slide('Lampiran · Pemrosesan Citra Dynamic World dan Nilainya')
    sub(s, 'Luas terbangun dihitung dari rata-rata probabilitas kelas built per tahun dengan ambang 0,5')
    hdr(s, 0.9, 2.1, 7.6, 'Tahapan di Google Earth Engine')
    steps(s, 0.9, 2.7, 7.6, [
        ('Koleksi & wilayah', 'GOOGLE/DYNAMICWORLD/V1, difilter batas DIY dan 1 Jan–31 Des tiap tahun.'),
        ('Probabilitas tahunan', 'Band built dirata-ratakan per piksel dari seluruh citra tahun itu.'),
        ('Ambang 0,5', 'Piksel dengan rata-rata probabilitas ≥ 0,5 dihitung sebagai terbangun.'),
        ('Luas', 'Luas piksel (pixelArea) dijumlahkan pada skala 10 m, dibagi 10.000 → hektar.')], h=0.85, gap=0.1, size=11)
    formula(s, 0.9, 6.55, 7.6, 1.55, ['p̄ₚ,ₜ = (1/nₚ,ₜ) · Σ p_built,ₚ,ᵢ',
                                     'Luasₜ = Σₚ Aₚ · 1[p̄ₚ,ₜ ≥ 0,5] ÷ 10.000  (ha)'], title='Rumus', size=12)
    rows = [['Tahun', 'Citra', 'Obs/ piksel', 'Luas ambang 0,5 (dipakai)', 'Luas modus label', 'Luas “lunak” Σp', 'Luas terkoreksi obs.', '% wilayah']]
    dat = [(2016, 53, 4.34, 44561.08, 65365.84, 53500.40, 61642.38), (2017, 97, 7.02, 50223.96, 78496.07, 62526.66, 67827.43), (2018, 194, 16.16, 56624.36, 85766.92, 67507.79, 63121.61),
           (2019, 244, 22.42, 63480.04, 96023.53, 73595.30, 62572.41), (2020, 155, 13.49, 58962.04, 88132.80, 68308.94, 66750.85), (2021, 142, 8.50, 59887.53, 86010.81, 67656.37, 71390.18),
           (2022, 110, 7.07, 57709.08, 81972.46, 65023.78, 70268.98), (2023, 178, 16.74, 75624.40, 108424.94, 79881.05, 74886.97), (2024, 188, 15.16, 73511.57, 104234.99, 77437.32, 74115.33),
           (2025, 152, 9.32, 55029.54, 84720.69, 65018.53, 67879.98)]
    hl = {}
    for i, d in enumerate(dat, 1):
        rows.append([str(d[0]), str(d[1]), fmt(d[2], 2), fmt(d[3], 0), fmt(d[4], 0), fmt(d[5], 0), fmt(d[6], 0), fmt(d[3] / 317036 * 100, 1) + '%'])
        hl[(i, 3)] = GREEN
    tbl(s, 8.8, 2.1, 10.3, [0.8, 0.8, 0.9, 1.7, 1.5, 1.5, 1.6, 1.0], rows, size=10, rowh=0.42, center=tuple(range(8)), hl=hl)
    card(s, 8.8, 6.85, 10.3, 1.3, None, [[('Hijau = nilai yang dipakai model. ', 11, True, '1E7A43'), ('Kolom lain hanya pembanding dari skrip yang sama. Luas terkoreksi = hasil penyesuaian jumlah observasi (diagnosis), tidak menggantikan nilai model.', 11, False, DARK)]])
    note(s, 'Luas naik-turun mengikuti jumlah observasi per piksel (mis. 2019: 22,4 obs → 63.480 ha; 2025: 9,3 obs → 55.030 ha). Inilah dasar diagnosis ketidakstabilan temporal. % wilayah dihitung sendiri terhadap 317.036 ha.', y=8.35, h=0.8)
    src(s, 'Sumber: Buku Subbab 3.5.2 dan 4.2.2; GEE.rtf; DW_Terbangun_TanpaMask_DIY_2016_2025.csv; Lahan_Terbangun_Terkoreksi_DIY_2016_2025.csv.')


def B_kelas(D):
    s = D.slide('Lampiran · Kelas Tutupan Lahan Dynamic World')
    sub(s, 'Dynamic World memberi probabilitas sembilan kelas untuk setiap piksel 10 m; penelitian ini hanya memakai kelas built')
    K = [('0', 'water', 'Air', 'Badan air: sungai, danau, waduk, laut.', '419BDF'),
         ('1', 'trees', 'Pohon', 'Vegetasi pohon rapat: hutan, kebun campuran berkanopi.', '397D49'),
         ('2', 'grass', 'Rumput', 'Padang rumput, lapangan, taman berumput.', '88B053'),
         ('3', 'flooded_vegetation', 'Vegetasi tergenang', 'Vegetasi yang tergenang air: rawa, mangrove.', '7A87C6'),
         ('4', 'crops', 'Tanaman pertanian', 'Lahan budidaya: sawah, ladang.', 'E49635'),
         ('5', 'shrub_and_scrub', 'Semak dan belukar', 'Vegetasi rendah tidak rapat.', 'DFC35A'),
         ('6', 'built', 'Terbangun', 'Permukaan buatan: bangunan, jalan, permukiman, kawasan industri.', 'C4281B'),
         ('7', 'bare', 'Lahan terbuka', 'Tanah, pasir, batuan tanpa vegetasi.', 'A59B8F'),
         ('8', 'snow_and_ice', 'Salju dan es', 'Salju dan es (tidak relevan untuk DIY).', 'B39FE1')]
    for k, (idx, en, idn, desc, col) in enumerate(K):
        x = 0.9 + (k % 3) * 6.13; y = 2.15 + (k // 3) * 2.05
        sw = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(0.9), Inches(1.85))
        sw.fill.solid(); sw.fill.fore_color.rgb = rgb(col); sw.line.fill.background(); sw.adjustments[0] = 0.1
        tb(sw and s, x, y + 0.6, 0.9, 0.6, [[(idx, 22, True, WHITE)]], align=PP_ALIGN.CENTER)
        hi = idx == '6'
        box(s, x + 1.0, y, 4.9, 1.85, fill=YEL_L if hi else LIGHT, line=YEL if hi else LINE, anchor=MSO_ANCHOR.MIDDLE, margin=0.18,
            paras=[[(idn, 14, True, TEAL)], [(en, 11, False, GREY, True)], [(desc, 11, False, DARK)]] + ([[('← dipakai (KELAS_BUILT = 6)', 11, True, RED)]] if hi else []))
    note(s, 'Setiap piksel punya probabilitas 9 kelas (jumlahnya 1) dan satu label kelas dengan probabilitas tertinggi. Penelitian ini memakai rata-rata probabilitas built per tahun dengan ambang 0,5, bukan label modus.', y=8.4, h=0.85)
    src(s, 'Sumber: Brown et al. (2022), Dynamic World; katalog Google Earth Engine GOOGLE/DYNAMICWORLD/V1 (nama dan warna kelas); deskripsi kelas diterjemahkan bebas.')


def B_odtw_proses(D):
    s = D.slide('Lampiran · Proses Estimasi ODTW dengan NTL: Rumus')
    sub(s, 'Estimasi melalui empat pemeriksaan sebelum nilai dipakai untuk mengisi tahun kosong')
    flow(s, 0.9, 2.1, 18.2, 1.05, [('Pasangkan data', 'NTL & ODTW 2018–2024 (7 titik)'), ('Uji korelasi', 'level dan selisih tahunan'),
                                    ('Regresi linear', 'ODTW = a + b·NTL'), ('LOOCV', 'stabilitas, RMSE relatif'), ('Estimasi + selang 95%', '2015–2017, 2025'), ('Validasi', 'temporal & spasial')],
         fills=[LIGHT] * 5 + [TEAL], size=10.5)
    F = [('Korelasi Pearson (level)', ['r = Σ(xᵢ − x̄)(yᵢ − ȳ) ÷ √[Σ(xᵢ − x̄)² · Σ(yᵢ − ȳ)²]'], 'Berpotensi tinggi hanya karena tren bersama.'),
         ('Korelasi selisih tahunan', ['Δxₜ = xₜ − xₜ₋₁ ;  Δyₜ = yₜ − yₜ₋₁ ;  r_Δ = corr(Δx, Δy)'], 'Syarat layak: R²_Δ ≥ 0,30 (menghindari regresi lancung).'),
         ('Regresi dan selang prediksi 95%', ['ŷ₀ = a + b·x₀', 'ŷ₀ ± t₀,₉₇₅;ₙ₋₂ · s · √[1 + 1/n + (x₀ − x̄)² ÷ Sₓₓ]'], 's = galat baku sisaan; Sₓₓ = Σ(xᵢ − x̄)².'),
         ('Leave-One-Out Cross-Validation', ['ŷ₍₋ᵢ₎ dari model tanpa titik i', 'RMSE = √[(1/k) Σ(ŷ₍₋ᵢ₎ − yᵢ)²];  RMSE relatif = RMSE ÷ ȳ × 100%'], 'Syarat layak: RMSE relatif ≤ 10%.')]
    for k, (t_, ls, c) in enumerate(F):
        x = 0.9 + (k % 2) * 9.2; y = 3.45 + (k // 2) * 2.55
        formula(s, x, y, 9.0, 2.35, ls + [('', '')], title=t_, size=12)
        T(s, x + 0.2, y + 1.85, 8.6, 0.4, [[(c, 10.5, False, GREY, True)]])
    note(s, 'Model final dilatih ulang pada ketujuh titik (bukan subset LOOCV): ODTW = 121,61 + 34,59 × NTL. Hasil lengkap di lampiran LOOCV.', y=8.65, h=0.75)
    src(s, 'Sumber: Buku Subbab 3.5.1 dan 4.2.1.')


def B_loocv(D):
    s = D.slide('Lampiran · Hasil Uji Korelasi, LOOCV, dan Estimasi ODTW')
    sub(s, 'NTL layak sebagai penduga ODTW: R² selisih tahunan 0,405 dan RMSE LOOCV relatif 5,99%')
    hdr(s, 0.9, 2.1, 5.6, 'Uji korelasi dan regresi')
    rows = [['Metrik', 'Nilai', 'Syarat'], ['n titik', '7 (2018–2024)', '—'], ['R² level', '0,785', '—'], ['R² selisih tahunan', '0,405', '≥ 0,30 ✓'],
            ['Intersep a', '121,6137', '—'], ['Kemiringan b', '34,5846', '—'], ['RMSE LOOCV', '11,29 unit', '—'], ['RMSE relatif', '5,99%', '≤ 10% ✓']]
    tbl(s, 0.9, 2.65, 5.6, [2.2, 1.8, 1.6], rows, size=11, rowh=0.44, center=(1, 2), hl={(3, 2): GREEN, (7, 2): GREEN})
    hdr(s, 6.8, 2.1, 6.0, 'LOOCV: tiap tahun diprediksi tanpa dirinya')
    L = [(2018, 177, 179.9, 2.9, 1.6), (2019, 189, 191.3, 2.3, 1.2), (2020, 180, 185.7, 5.7, 3.2), (2021, 170, 176.9, 6.9, 4.0), (2022, 183, 167.9, -15.1, -8.2), (2023, 201, 215.1, 14.1, 7.0), (2024, 218, 198.7, -19.3, -8.9)]
    rows = [['Tahun', 'Aktual', 'Prediksi', 'Selisih', 'Persen']]
    hl = {}
    for i, l in enumerate(L, 1):
        rows.append([str(l[0]), str(l[1]), fmt(l[2], 1), fmt(l[3], 1).replace('-', '−'), fmt(l[4], 1).replace('-', '−') + '%'])
        if abs(l[4]) > 7: hl[(i, 4)] = PINK
    tbl(s, 6.8, 2.65, 6.0, [1.0, 1.1, 1.3, 1.2, 1.4], rows, size=11, rowh=0.44, center=tuple(range(5)), hl=hl)
    hdr(s, 13.1, 2.1, 6.0, 'Estimasi tahun kosong (selang 95%)')
    rows = [['Tahun', 'NTL', 'Estimasi', 'Bawah', 'Atas'], ['2015', '1,262', '165,2', '138,5', '191,9'], ['2016', '1,054', '158,1', '128,9', '187,3'],
            ['2017', '1,438', '171,4', '146,4', '196,3'], ['2025', '2,288', '200,7', '176,7', '224,8']]
    tbl(s, 13.1, 2.65, 6.0, [1.0, 1.1, 1.3, 1.3, 1.3], rows, size=11, rowh=0.44, center=tuple(range(5)))
    card(s, 13.1, 4.95, 6.0, 1.75, None, ['NTL 2016 (1,054) di luar rentang data latih (1,483–2,512), sehingga selangnya paling lebar (±58 unit).',
                                          'Selang 2025 tersempit karena NTL dekat rata-rata data latih.'], size=10.5)
    hdr(s, 0.9, 6.45, 11.9, 'Bacaan')
    bullets(s, 0.9, 7.0, 11.9, 1.9, ['R² level (0,785) jauh di atas R² selisih (0,405): sebagian korelasi level berasal dari tren bersama, sehingga penilaian memakai R² selisih.',
                                     'Galat terbesar pada 2022 (−8,2%) dan 2024 (−8,9%), bertepatan dengan NTL stagnan sementara ODTW naik.',
                                     'ODTW 2025 (201) turun dari 218 pada 2024; selisihnya sedikit di atas 1 × RMSE, sehingga tetap dipakai dan diuji sensitivitas 189–218.'], size=11)
    note(s, 'Nilai yang dipakai di model: 2015 = 165, 2016 = 158, 2017 = 171, 2025 = 201 (dibulatkan).', y=9.15, h=0.6, title='Dipakai')
    src(s, 'Sumber: Buku Subbab 4.2.1 (Tabel 29–30); LOOCV_NTL_ODTW.csv, Pengujian_NTL_ODTW.csv (repository).')


def B_dw_proses(D):
    s = D.slide('Lampiran · Proses Estimasi Lahan Terbangun dan Rumus Uji Akurasi')
    sub(s, 'Luas dibaca langsung dari peta; uji akurasi dan diagnosis hanya untuk menilai kelayakan, tidak mengubah nilai')
    flow(s, 0.9, 2.1, 18.2, 1.05, [('Ekstraksi DW', '2016–2025, ambang 0,5'), ('Ekstrapolasi 2015', 'tren log-linear'), ('Uji akurasi', '200 titik, 2025'),
                                    ('Kepekaan ambang', '0,30–0,95'), ('Diagnosis temporal', 'jumlah observasi'), ('Validasi', 'temporal & spasial')], fills=[LIGHT] * 5 + [TEAL], size=10.5)
    formula(s, 0.9, 3.45, 9.0, 2.9, ['OA = (n₁₁ + n₀₀) ÷ n',
                                     'UA_terbangun = n₁₁ ÷ (n₁₁ + n₁₀)   (precision)',
                                     'PA_terbangun = n₁₁ ÷ (n₁₁ + n₀₁)   (recall)',
                                     'F1 = 2 · UA · PA ÷ (UA + PA)',
                                     'κ = (pₒ − pₑ) ÷ (1 − pₑ)'], title='Metrik akurasi (n_ij: peta i, rujukan j; 1 = terbangun)', size=12.5)
    formula(s, 10.1, 3.45, 9.0, 2.9, ['ÔA = Σᵢ Wᵢ · (nᵢᵢ ÷ nᵢ.),   Wᵢ = Aᵢ ÷ A_total',
                                      'Luasₜ = a + b · Obsₜ',
                                      'Luas_terkoreksi,ₜ = Luasₜ − b · (Obsₜ − Obs_acuan)',
                                      'Syarat: corr(Obs, tahun) tidak signifikan'], title='OA tertimbang luas (Olofsson et al., 2014) dan diagnosis', size=12.5)
    rows = [['Langkah uji akurasi', 'Keterangan'],
            ['Sampel', '200 titik acak berstratifikasi menurut kelas peta: 100 terbangun, 100 bukan terbangun (tahun 2025)'],
            ['Label rujukan', 'Interpretasi visual citra resolusi tinggi Google Earth pada titik yang sama'],
            ['Dua versi', 'Tak tertimbang (deskriptif) dan tertimbang luas (penduga tak bias, karena sampel 50:50 sedangkan luas peta 17:83)'],
            ['Kepekaan ambang', 'Metrik dihitung pada ambang 0,30–0,95 sebagai diagnosis; ambang 0,5 tetap dipakai agar tidak overfitting']]
    tbl(s, 0.9, 6.55, 18.2, [3.2, 15.0], rows, size=10.5, rowh=0.42)
    note(s, 'pₒ = proporsi kesepakatan teramati (= OA); pₑ = proporsi kesepakatan yang diharapkan secara kebetulan. Wᵢ = proporsi luas kelas i pada peta.', y=8.9, h=0.7)
    src(s, 'Sumber: Buku Subbab 3.5.2.')


def B_dw_eval(D):
    s = D.slide('Lampiran · Evaluasi Lahan Terbangun (1/2): Metrik Lengkap')
    sub(s, 'Akurasi keseluruhan tertimbang luas 89,95%; kesalahan didominasi komisi (bukan terbangun ditandai terbangun)')
    hdr(s, 0.9, 2.1, 8.6, 'Hasil uji akurasi (tahun 2025)')
    rows = [['Metrik', 'Nilai', 'IK 95%'], ['Jumlah titik', '200', '—'], ['Overall accuracy (tak tertimbang)', '80,50%', '74,46–85,39%'], ['Overall accuracy (tertimbang luas)', '89,95%', '86,05–93,85%'],
            ["User's accuracy – terbangun", '66,00%', '56,67–75,33%'], ["User's accuracy – bukan terbangun", '95,00%', '90,71–99,29%'], ["Producer's accuracy – terbangun", '73,58%', '56,66–90,50%'],
            ["Producer's accuracy – bukan terbangun", '92,98%', '91,16–94,80%'], ['F1-score terbangun', '77,19%', '—'], ['Koefisien Kappa', '0,6100', '0,5002–0,7198']]
    tbl(s, 0.9, 2.65, 8.6, [4.2, 1.8, 2.6], rows, size=11, rowh=0.44, center=(1, 2), hl={(3, 1): GREEN})
    hdr(s, 9.8, 2.1, 4.4, 'Matriks konfusi (titik)')
    rows = [['Peta \\ Rujukan', 'Bukan', 'Terbangun'], ['Bukan terbangun', '95', '5'], ['Terbangun', '34', '66']]
    tbl(s, 9.8, 2.65, 4.4, [2.0, 1.2, 1.2], rows, size=11.5, rowh=0.55, center=(1, 2), hl={(1, 1): GREEN, (2, 2): GREEN, (2, 1): PINK, (1, 2): YEL_L})
    card(s, 9.8, 4.45, 4.4, 2.0, None, [[('34 komisi', 11, True, RED), (' (peta terbangun, rujukan bukan)', 11, False, DARK)], [('5 omisi', 11, True, '7A5A00'), (' (peta bukan, rujukan terbangun)', 11, False, DARK)]], size=11)
    hdr(s, 14.5, 2.1, 4.6, 'Metrik tambahan')
    rows = [['Metrik', 'Tak tertimbang', 'Tertimbang'], ['Precision (UA)', '66,00%', '66,00%'], ['Recall (PA)', '92,96%', '73,58%'], ['Specificity', '73,64%', '92,98%'],
            ['F1-score', '77,19%', '69,58%'], ['Balanced acc.', '83,30%', '83,28%'], ['MCC', '0,6374', '0,6372'], ['ROC-AUC', '0,9075', '0,9412'], ['PR-AUC', '0,8395', '0,7694']]
    tbl(s, 14.5, 2.65, 4.6, [1.7, 1.45, 1.45], rows, size=10, rowh=0.42, center=(1, 2))
    hdr(s, 0.9, 7.25, 18.2, 'Bacaan')
    bullets(s, 0.9, 7.8, 18.2, 1.3, ['Kappa 0,61 tergolong kesepakatan kuat (Landis & Koch, 1977).',
                                     'Recall terbangun berbalik antara versi tak tertimbang (92,96%) dan tertimbang (73,58%) karena sampel 50:50 sedangkan luas kelas bukan terbangun 82,58% wilayah; karena itu versi tertimbang yang dibaca.'], size=11)
    src(s, 'Sumber: Buku Subbab 4.2.2 (Tabel 31–32); Hasil_UjiAkurasi_DW_2025.csv, Metrik_Imbalance_DW_2025.csv (repository).')

    s = D.slide('Lampiran · Evaluasi Lahan Terbangun (2/2): Ambang dan Validasi')
    sub(s, 'Kesalahan menumpuk di dekat ambang 0,5; Dynamic World lebih konsisten daripada data resmi yang tersedia')
    hdr(s, 0.9, 2.1, 8.9, 'Kepekaan ambang (tertimbang luas)')
    A = [(0.30, .8499, .5121, .8415, .6367), (0.35, .8582, .5291, .8415, .6497), (0.40, .8830, .5877, .8415, .6920), (0.45, .8995, .6461, .7886, .7103), (0.50, .8995, .6600, .7358, .6958),
         (0.55, .9099, .7209, .6912, .7057), (0.60, .8977, .7067, .5909, .6436), (0.65, .8943, .7843, .4459, .5686), (0.70, .8855, .8750, .3122, .4601), (0.75, .8455, 1.0, .0111, .0221)]
    cats = [fmt(a[0], 2) for a in A]
    line_chart(s, 0.9, 2.6, 8.9, 3.5, cats, [('Accuracy', [a[1] for a in A]), ('Precision', [a[2] for a in A]), ('Recall', [a[3] for a in A]), ('F1', [a[4] for a in A])],
               [TEAL, CYAN, YEL, RED], fmt_='0.00', fs=9)
    T(s, 0.9, 6.15, 8.9, 0.6, [[('Ambang ≥ 0,80: tidak ada titik terbangun (precision tak terdefinisi). F1 tertinggi pada 0,45 (0,710); ambang 0,50 dipertahankan.', 10, False, GREY, True)]])
    hdr(s, 10.1, 2.1, 9.0, 'Akurasi menurut probabilitas built')
    rows = [['Selang probabilitas', 'Titik', 'Benar', 'Akurasi'], ['0,00–0,25', '88', '86', '97,7%'], ['0,25–0,50', '12', '9', '75,0%'], ['0,50–0,60', '25', '13', '52,0%'], ['≥ 0,60', '75', '53', '70,7%'], ['Total', '200', '161', '80,5%']]
    tbl(s, 10.1, 2.6, 9.0, [3.0, 1.8, 1.8, 2.4], rows, size=11, rowh=0.42, center=(1, 2, 3), hl={(3, 3): PINK, (1, 3): GREEN})
    T(s, 10.1, 5.2, 9.0, 0.9, [[('Rata-rata probabilitas titik salah 0,574 vs titik benar 0,330. Selang 0,25–0,50 dan ≥ 0,60 dihitung sendiri dari lembar kerja.', 10, False, GREY, True)]])
    hdr(s, 0.9, 6.85, 18.2, 'Validasi temporal: lahan terbangun menurut sumber (ha)')
    rows = [['Sumber', '2015', '2016', '2017', '2018', '2019', 'Pola'],
            ['BPS (lahan bukan pertanian)', '76.334', '77.467', '108.580', '114.942', '70.371', '+40,2% (2016→17), −38,8% (2018→19)'],
            ['DLHK DIY', '75.146', '65.461', '70.371', '70.371', '—', '−12,9% (2015→16)'],
            ['Dynamic World (dipakai)', '43.037*', '44.561', '50.224', '56.624', '63.480', 'naik ±12–13%/tahun, tanpa pembalikan']]
    tbl(s, 0.9, 7.4, 18.2, [3.6, 1.5, 1.5, 1.5, 1.5, 1.5, 7.1], rows, size=10.5, rowh=0.42, center=(1, 2, 3, 4, 5), hl={(3, c): GREEN for c in range(7)})
    src(s, 'Sumber: Buku Subbab 4.2.2 (Gambar 13); Optimasi_Ambang_DW_2025.csv; lembar kerja uji akurasi; Master Data. *ekstrapolasi.', y=10.15)


def B_sampel(D):
    K = {int(float(r['nomor'])): r for r in _csv.DictReader(open(REPO + 'Uji Akurasi Lokal/KunciModel_DW_2025.csv'))}
    ws = _ox.load_workbook(REPO + 'Uji Akurasi Lokal/LembarKerja_UjiAkurasi_DW_2025.xlsx', data_only=True).active
    R = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        n = int(r[0]); k = K[n]
        kd = int(float(k['kelas_dw'])); ref = int(r[3]); pr = float(k['prob'])
        cat = (r[5] or '')
        R.append((n, float(r[1]), float(r[2]), pr, kd, ref, cat))
    lab = {0: 'Bukan', 1: 'Terbangun'}
    for part in range(4):
        chunk = R[part * 50:(part + 1) * 50]
        s = D.slide(f'Lampiran · Sampel Uji Akurasi Lahan Terbangun ({part + 1}/4)')
        sub(s, f'Titik {part * 50 + 1}–{part * 50 + 50} dari 200: kelas peta Dynamic World 2025 dibandingkan label rujukan visual Google Earth')
        for half in range(2):
            rows = [['No', 'Lon', 'Lat', 'Prob. built', 'Peta', 'Rujukan', 'Sesuai']]
            hl = {}
            for i, (n, lo, la, pr, kd, ref, cat) in enumerate(chunk[half * 25:(half + 1) * 25], 1):
                ok = kd == ref
                rows.append([str(n), f'{lo:.5f}'.replace('.', ','), f'{la:.5f}'.replace('.', ','), fmt(pr, 3), lab[kd], lab[ref], '✓' if ok else '✗'])
                if not ok:
                    hl[(i, 6)] = PINK
            tbl(s, 0.9 + half * 9.2, 2.05, 9.0, [0.6, 1.5, 1.5, 1.3, 1.4, 1.4, 0.9], rows, size=8.5, rowh=0.285, center=tuple(range(7)), hl=hl)
        bad = sum(1 for c in chunk if c[4] != c[5])
        src(s, f'Sumber: KunciModel_DW_2025.csv dan LembarKerja_UjiAkurasi_DW_2025.xlsx (repository). Merah muda = tidak sesuai ({bad} titik pada halaman ini). Peta: kelas built bila prob ≥ 0,5.', y=9.6)
