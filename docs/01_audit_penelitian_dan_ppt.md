# Audit Penelitian dan PPT Sidang — Tahap A, B, dan Catatan Konflik

Dokumen ini adalah keluaran tahap pertama (belum mengedit PPT). Rujukan utama: **buku skripsi final (docx)**. Repository dipakai sebagai sumber pendukung. Setiap angka di bawah dapat dilacak ke bab/tabel buku atau ke file repository yang disebut.

Singkatan sumber: **[Buku x.y]** = subbab buku; **[Tabel n]/[Gambar n]** = penomoran di Daftar Tabel/Gambar buku; **[Repo: path]** = file di repository; **[PPT-lama Sn]** = slide ke-n pada "PPT Paparan Sidang (Final yg tidak final).pptx".

---

## TAHAP A — Ringkasan Pemahaman Penelitian

### A1. Masalah penelitian
- Pariwisata DIY tumbuh pesat (>40 juta perjalanan wisnus 2025, peringkat 7 nasional; 59,69% perjalanan antarprovinsi; peringkat 1 sub-indeks *Travel and Tourism Demand Drivers* IPKN 2024; prioritas #2 RPJMD; BYP destinasi prioritas Perpres 88/2024) [Buku 1.1].
- Pertumbuhan menekan daya dukung (kepadatan Malioboro, konversi lahan terbangun). Permintaan, akomodasi, ODTW, nilai tambah, tenaga kerja, dan lahan saling terkait secara non-linear dan berjeda waktu, sehingga tidak bisa dianalisis per komponen [Buku 1.1].
- Metode peramalan (ARIMA, VECM, ML) andal untuk proyeksi variabel tunggal tetapi tidak memodelkan *feedback*, akumulasi, dan daya dukung [Buku 1.1].
- Tiga masalah formal [Buku 1.2]: (1) belum ada variabel penyusun CLD untuk model SD kebijakan pariwisata DIY; (2) belum ada model simulasi SD yang memakai citra satelit dan statistik resmi; (3) belum ada aplikasi web yang mengimplementasikan hasil pemodelan dan skenario.

### A2. Research gap [Buku 1.1, 2.3, Tabel 1]
1. Model SD pariwisata umumnya diadaptasi dari kerangka luar negeri; banyak variabelnya (populasi, limbah, air tanah) tidak punya padanan data tahunan provinsi di Indonesia.
2. Model SD bergantung pada statistik agregat yang terbit dengan jeda; integrasi SD dan *remote sensing* untuk pariwisata masih jarang (9 studi pembanding: semua "Citra satelit = Tidak").
3. Hasil pemodelan umumnya berhenti pada grafik statis/laporan; tidak ada yang berbentuk aplikasi web DST.

### A3. Tujuan penelitian (kutipan persis, [Buku 1.3])
- **Tujuan umum:** "mengembangkan dan memvalidasi model sistem dinamis pariwisata yang terintegrasi dengan data citra satelit untuk pemutakhiran data guna mendukung simulasi kebijakan pariwisata di Provinsi DIY."
- **Tujuan 1:** "Mengidentifikasi dan merumuskan variabel-variabel utama penyusun CLD dalam model sistem dinamis kebijakan pariwisata di Provinsi DIY."
- **Tujuan 2:** "Mengembangkan model sistem dinamis yang komprehensif dan memanfaatkan data citra satelit untuk memutakhirkan variabel yang mengalami jeda data, serta menguji validitas strukturnya dan kesesuaiannya terhadap data historis sebagai dasar simulasi kebijakan pariwisata."
- **Tujuan 3:** "Membangun aplikasi berbasis web yang mengimplementasikan hasil pemodelan dan simulasi skenario kebijakan sebagai alat bantu analisis dan pengambilan keputusan."

Catatan penempatan simulasi skenario: Kesimpulan buku butir 2 [Buku 5.1] memasukkan hasil tiga skenario ke dalam jawaban Tujuan 2 ("…dan simulasi terhadap tiga skenario kebijakan menunjukkan…"). Rancangan PPT mengikuti keputusan buku ini: **analisis sensitivitas dan simulasi skenario ditempatkan di akhir Tujuan 2** sebagai bukti bahwa model berfungsi "sebagai dasar simulasi kebijakan", lalu Tujuan 3 mengemas hasil itu ke aplikasi.

### A4. Data [Buku 3.4, Tabel 2, Lampiran 7]
| Kelompok | Variabel | Periode | Sumber |
|---|---|---|---|
| Permintaan | Jumlah wisatawan (wisnus+wisman), total malam menginap, proporsi menginap, lama menginap, pengeluaran per kunjungan | 2015–2025 (pengeluaran 2018–2025) | BPS DIY, BPS RI |
| Akomodasi | Jumlah hotel & akomodasi, kamar, TPK, TPG | 2015–2025 | BPS DIY |
| ODTW | Jumlah ODTW | 2018–2024 (BPS) + estimasi NTL 2015–2017, 2025 | BPS Statistik ODTW |
| Tenaga kerja | TK KBLI I dan R,S,T,U | 2017–2025 | Sakernas |
| Ekonomi | PDRB ADHK I dan R,S,T,U; investasi PMA+PMDN | 2015–2025 | BPS DIY; BKPM |
| Lahan | Lahan terbangun (Dynamic World); luas wilayah 317.036 ha | 2016–2025 (+ekstrapolasi 2015) | GEE; Kepmendagri |
| Citra | NTL VIIRS DNB (nW/cm²/sr) | 2015–2025 | NOAA via GEE |

Tahun dasar 2025, horizon 2050, langkah waktu 1 tahun, integrasi Euler [Buku 3.4, 3.7.3].

### A5. Metode (kerangka 6 tahap, adaptasi Mai & Smith 2018) [Buku 3.1, 3.7, Gambar 5]
1. Pengumpulan & *preprocessing* (perluasan) → 2. Artikulasi masalah & hipotesis dinamis (CLD) → 3. Formulasi model (SFD, parameterisasi) → 4. Pengujian (uji struktur, uji perilaku, **kalibrasi [perluasan, Oliva 2003; Homer 2012]**, analisis sensitivitas) → 5. Perancangan & evaluasi skenario → 6. Implementasi aplikasi web (perluasan).

Perangkat: GEE, Vensim PLE, Python/PySD, Excel/Google Sheets, SDEverywhere, Next.js+TypeScript+Tailwind [Tabel 9].

### A6. Struktur model [Buku 4.1, Tabel 27, Tabel 28]
- 61 variabel: 5 stock, 10 flow, 11 auxiliary, 35 parameter (26 endogen, 35 eksogen).
- Stock & nilai awal 2025: Wisatawan 40.695.654 kunjungan; Hotel & akomodasi 2.291 unit; ODTW 201 unit (estimasi NTL); TK 364.994 jiwa; Lahan terbangun 55.029,54 ha (Dynamic World).
- 6 loop: R1 pertumbuhan wisatawan; R2 ekonomi–investasi–atraksi; B1 kepadatan; B2 daya dukung lahan; B3 okupansi akomodasi; B4 penyesuaian TK (goal-seeking). Satu hubungan dibuang: TK → pembangunan ODTW.
- Persamaan kunci: Laju kedatangan = W × LPE × Daya Tarik; Daya Tarik = 0,40·min(1,5;(ODTW/201)^0,3) + 0,35·min(1;Kref/K) + 0,25·(RDDL/RDDLref); Investasi = PDRB × 0,0488 × (1+Insentif); Konversi lahan pariwisata = (Konstruksi×0,1 + Pembangunan ODTW×0,5) × (1−Konservasi) × (RDDL/RDDLref) [Buku 4.3.1, Lampiran 6].
- Tuas kebijakan: Insentif Kebijakan (jalur R2), Kebijakan Konservasi Lahan (jalur B2).

### A7. Parameterisasi [Buku 3.4.2, 4.3.2, Tabel 33–37, Lampiran 1–5]
Lima kategori: data statistik resmi (11), identitas stock-flow (8), regulasi (2), asumsi pemodelan (8), normalisasi & tuas (6). Hanya parameter tidak pasti yang boleh dikalibrasi. Nilai kunci: LPE 0,27726; LPD 0,207945 (rasio 0,75 = asumsi struktural); TPK Ambang 0,275; Sensitivitas konstruksi 2,31385; Laju demolisi 0,05; Laju konversi dasar 0,0436052 (CI 95%: 0,0034118–0,0851069); bobot 0,40/0,35/0,25; elastisitas 0,3; batas efek ODTW 1,5.

### A8. Pengujian [Buku 4.4–4.7]
- **Uji struktur (6 + kesesuaian):** 0 ketidaksesuaian satuan; kekekalan materi selisih 0 pada 5 stok 2025–2049; uji loop 6/6 berfungsi (B1 terkuat: +160,2% wisatawan 2050 bila dimatikan); uji ekstrem 17 uji → 15 lolos, 2 lolos dengan catatan (E02, E15), 0 gagal, setelah 4 perbaikan struktur (pembatas TPK≤1, RDDL≥0, dua komponen daya tarik); galat integrasi: pelanggaran E15 57,70 ha (0,018%) pada Δt=1 hilang pada Δt=0,25; BASE Δt 1 vs 0,5 berselisih −0,27% s.d. +0,34%.
- **Uji perilaku:** parsial P1–P5 (2016–2025, angka utama tanpa 2020–2021) dan penuh (2019–2025, angka utama dengan COVID). Akomodasi terbaik (P1 hotel DC 0,2011, MAPE 6,05%); wisatawan gagal uji tren (simulasi ~6,4%/th vs data sambungan ~11,7%/th). Uji penuh: DC memburuk karena galat wisatawan merambat (U1 dominan di 6 dari 9 variabel), tetapi MAPE tidak ada yang "buruk".
- **Kalibrasi (Tahap 0–4):** Tahap 0 koreksi penurunan LPE/LPD (0,26864/0,20148 → 0,27726/0,207945; BASE 2050 +1,6%). Tahap 1 (TPK ambang, demolisi): optimum di batas, digerakkan tahun 2019 → dipertahankan. Tahap 2 (laju konversi): optimum 0,0638662, perbaikan 14,76% → **ditolak Tahap 4** (NRMSE lahan uji penuh rasio 1,3241 > 1,05). Tahap 3 (LPE/LPD): punggung keteridentifikasian LPE 0,26–0,80 × rasio 0,60–0,86 → tidak teridentifikasi; kesenjangan berasal dari rezim pemulihan pascapandemi 2022–2024. **Tidak ada parameter yang berubah.**
- **Sensitivitas:** ±10% (32 parameter, 6 keluaran): LPD 42,07% (peringkat 1); asumsi menempati 4 dari 6 peringkat teratas. Rentang penuh: rasio LPD/LPE 153,57 poin (LPE tetap) / 69,65 poin (LPE diturunkan ulang); bobot 48,10; laju konversi 30,64 (lahan 115,70); insentif 10,35; konservasi 0,18 (lahan 0,68).

### A9. Skenario [Buku 3.8, 4.8, Tabel 58–63]
- BAU (0;0), Sustainable (Insentif 0,1; Konservasi 1,0), Development Priority (0,3; 0). Nilai tuas = ketetapan peneliti.
- 10 KPI tiga dimensi + skala; ambang RDDL > 0,331 (Perda DIY 6/2021) dan indeks kepadatan < 2,0 (ketetapan peneliti).

### A10. Hasil utama
- 2050: BAU wisatawan 96,20 juta; Sustainable 98,92 juta; DP 103,62 juta. DP unggul ekonomi (+7,18% TK, +7,71% PDRB vs BAU); Sustainable unggul lingkungan (konversi lahan pariwisata −100%, lahan −0,91%); BAU unggul kepadatan. Tidak ada skenario unggul di semua dimensi.
- Ambang kepadatan 2,0 terlampaui pada ketiga skenario (DP 2041, S 2042, BAU 2043); RDDL ≈0,614 tidak melewati 0,331.
- Dekomposisi: interaksi tuas ≈0,7% dari selisih paket (hampir aditif).
- Kekokohan: 7 KPI berperingkat, 7 kondisi (C0–C6) → peringkat identik (KOKOH).

### A11. Aplikasi [Buku 3.9, 4.9]
- Vensim → SDEverywhere (JS/WebAssembly) → Next.js/TypeScript/Tailwind; https://sistemdinamispariwisata.vercel.app.
- Halaman: Beranda, Model (Struktur & Evaluasi), Skenario (pilih/bandingkan 3 skenario), Simulasi (atur 2 tuas, pilih variabel, 2025–2050).
- Black-box 9/9 Pass. SUS n=10: rata-rata 88,50; median 92,50; SD 13,85; min 60; maks 100 → di atas rata-rata normatif 68; antara *Excellent* (85,5) dan *Best Imaginable* (90,9).

### A12. Kesimpulan & kontribusi [Buku 5.1, 4.10.2]
- Tujuan 1 tercapai (CLD 6 loop; model 5/10/11/35). Tujuan 2 tercapai (valid struktural, memadai per subsistem; kalibrasi tidak mengubah parameter; tidak ada skenario dominan, pola kokoh). Tujuan 3 tercapai (aplikasi lulus fungsional).
- Kontribusi: (a) struktur model yang terpetakan ke statistik resmi Indonesia; (b) pemosisian citra satelit sebagai *estimator/nowcasting*, dengan pelajaran kondisional (klasifikasi langsung vs regresi proksi); (c) protokol pengujian yang membedakan sumber ketidaksesuaian (kalibrasi sebagai instrumen validasi); (d) pemetaan *trade-off* kebijakan yang kokoh; (e) DST web.

---

## TAHAP B — Audit PPT Lama (68 slide)

Desain PPT lama (palet teal–kuning, kartu, tabel rapi, header navigasi bab) **layak dipertahankan**. Masalah utamanya bukan isi, tetapi **urutan** (Metodologi S14–S25 terpisah jauh dari Hasil S26–S47) dan beberapa angka yang tidak sinkron dengan buku.

| Slide lama | Isi | Status | Alasan | Tindakan (slide baru) |
|---|---|---|---|---|
| S1 | Judul & tim | Pertahankan | Sudah benar | → B1 |
| S2 | Alur paparan per bab | Revisi | Masih urutan bab | Ganti jadi alur per tujuan → B2 |
| S3 | Definisi wisata/pariwisata/kebijakan | Pindah | Tidak menggerakkan argumen | → Lampiran L1 |
| S4 | Pariwisata sektor strategis (CAGR, 1,53 miliar, 10%, 2,2%→4,9%, 15,38 juta) | Revisi + gabung | Angka "2,2% → 4,9% (2020→2025)" berbeda dengan buku "2,2% (2020) → 4% (2024)" | Gabung dengan S5 → B3, pakai angka buku |
| S5 | Grafik kontribusi PDB & kunjungan | Gabung | Satu pesan dengan S4 | → B3 |
| S6 | DIY destinasi utama | Pertahankan | Angka sesuai buku | → B4 |
| S7 | Pertumbuhan menekan daya dukung | Pertahankan | Inti masalah | → B5 |
| S8 | Peramalan vs sistem dinamis | Pertahankan | | → B6 |
| S9 | Tiga celah + respons | Pertahankan | Inti *research gap* | → B7 |
| S10 | Masalah → tujuan | Pertahankan | Kutipan tujuan sesuai buku | → B8 (tambah ikon "akan dijawab di bagian …") |
| S11 | Ruang lingkup | Pertahankan | | → B9 |
| S12 | Posisi vs 9 studi | Pertahankan | | → B10 |
| S13 | Kerangka pikir | Pertahankan | Gambar buku | → B11 |
| S14 | Data 2015–2025 | Revisi | Tambah peta wilayah (Gambar 6) | → B12 |
| S15 | Alat & perangkat | Pindah | Detail teknis | → strip kecil di B13; detail ke L2 |
| S16 | Enam tahap penelitian | Revisi (penting) | Perlu kolom "menjawab Tujuan ke-…" | → B13 (slide jembatan) |
| S17 | Citra = estimator | Pindah | Milik Tujuan 2 | → B23 |
| S18 | Alur estimasi ODTW (7 langkah) | Pindah + pecah | Metode langsung diikuti hasil | → B24 (langkah 1–5) dan B25 (uji kelayakan) |
| S19 | Metrik citra NTL & DW | Pecah | Terlalu padat, dua topik | Bagian NTL → B25; bagian DW → B27; ANCOVA → B28 |
| S20 | Pengujian berjenjang (ringkasan) | Hapus/gabung | Tumpang tindih dengan B36, B40, B45, B49 | Isi dijadikan "peta sub-tahap" di divider B22 |
| S21 | Rancangan 7 uji struktur | Pindah | Tepat sebelum hasil uji struktur | → B36 |
| S22 | Rancangan uji perilaku & rumus Barlas | Pindah | Tepat sebelum hasil uji perilaku | → B40 |
| S23 | Protokol kalibrasi | Pindah | Tepat sebelum hasil kalibrasi | → B45 |
| S24 | Rancangan sensitivitas | Pindah | Tepat sebelum hasil sensitivitas | → B49 |
| S25 | Penyaringan tuas | Pindah | Tepat sebelum skenario | → B51 |
| S26 | Evaluasi kandidat CLD | Pertahankan | Hasil Tujuan 1 | → B17 |
| S27 | CLD + 6 loop | Pertahankan | Hasil inti Tujuan 1 | → B19 |
| S28 | 61 variabel, SFD, nilai awal | Pertahankan | | → B30 |
| S29 | Persamaan daya tarik | Pertahankan | | → B31 |
| S30 | Hasil NTL | Pecah | Gabung hasil + validasi | → B25, B26 |
| S31 | Hasil Dynamic World | Pecah | | → B27, B28 |
| S32 | Struktur lolos verifikasi | Pertahankan | | → B37 |
| S33 | Uji loop | Pertahankan | | → B38 |
| S34 | Uji ekstrem + galat integrasi | Revisi | Angka "LPE ≤ ±0,336" perlu dicek (lihat Konflik K6) | → B39 |
| S35 | Penyambungan wisnus | Pertahankan | | → B41 |
| S36 | DC parsial vs penuh + MAPE | Pertahankan | | → B43 |
| S37 | Akar galat tunggal | Pertahankan | | → B44 |
| S38 | Kalibrasi Tahap 0–4 | Pertahankan | | → B46 |
| S39 | Tornado wisatawan | Revisi | Teks "3 dari 4 peringkat teratas" ≠ buku "4 dari 6 peringkat teratas" | → B50 |
| S40 | Asumsi peneliti terbuka | Pindah | Milik parameterisasi | → B35 |
| S41 | Tiga skenario | Pertahankan | | → B52 |
| S42 | KPI 2050 | Pertahankan | | → B53 |
| S43 | Komposisi daya tarik | Pertahankan | | → B54 |
| S44 | Ambang kepadatan | Pertahankan | | → B55 |
| S45 | Dekomposisi | Pertahankan | | → B56 |
| S46 | Kekokohan | Pertahankan | | → B57 |
| S47 | Implikasi kebijakan | Pertahankan | | → B58 |
| S48 | Diskusi | Pertahankan | | → B67 |
| S49 | Arsitektur aplikasi | Pertahankan | | → B62 |
| S50 | Black-box + SUS | Pecah | Dua metode berbeda | → B64 (black-box), B65 (SUS) |
| S51 | Keterbatasan | Revisi kecil | Tambah "responden SUS seluruhnya mahasiswa" (repo) | → B68 |
| S52 | Kesimpulan | Pertahankan | Sesuai buku (+SUS) | → B69 |
| S53 | Saran | Pertahankan | | → B70 |
| S54 | Terima kasih | Pertahankan | | → B71 |
| S55 | Lampiran 35 parameter | Pertahankan | | → L8 |
| S56 | LOOCV NTL | Pertahankan | | → L15 |
| S57 | Akurasi DW | Pertahankan | Label F1 (lihat K8) | → L16 |
| S58 | 10 indikator | Pindah | Dipakai di B52; versi tabel lengkap tetap lampiran | → L27 |
| S59 | Uji perilaku lengkap | Revisi | Tambah baris P5 dan P1b | → L21 |
| S60 | Tampilan aplikasi | Pindah ke utama | Fitur aplikasi wajib tampil | → B63 |
| S61 | SFD penuh | Pertahankan | | → L11 |
| S62 | Aspek dikeluarkan | Pertahankan | | → L6 |
| S63 | 17 uji ekstrem | Pertahankan | | → L18 |
| S64 | Uji loop tabel | Pertahankan | | → L19 |
| S65 | Kalibrasi per tahap | Pertahankan | | → L22–L24 |
| S66 | Tornado 5 keluaran + rentang penuh | Pertahankan | | → L25–L26 |
| S67 | Persamaan kunci | Pertahankan | | → L10 |
| S68 | Data historis | Revisi | Sel lahan 2015 = "ekstrapolasi"; isi 43.037 ha (Master Data) dan perbaiki lampiran buku (K9) | → L12 |

Ringkasan: 0 slide berisi salah total; 47 dipertahankan/dipindah apa adanya, 13 direvisi/dipecah, 2 dihapus/digabung (S3 ke lampiran, S20 dilebur), dan 18 slide baru diperlukan (divider, ringkasan tujuan, metode yang belum tampil, bukti kelayakan model).

---

## Catatan Konflik Angka/Versi (rujukan final = buku)

| Kode | Lokasi | Isi konflik | Keputusan untuk PPT | Saran untuk buku |
|---|---|---|---|---|
| K1 | Abstrak buku | Menyebut "Sentinel-2, Landsat" dan "akan disimulasikan/diimplementasikan" | PPT memakai data final: VIIRS DNB (NTL) dan Dynamic World (berbasis Sentinel-2); tidak menyebut Landsat | Perbarui abstrak (tense lampau, dataset final, angka hasil) |
| K2 | Buku 1.2 | "periode simulasi 2024–2050" vs bagian lain 2025–2050 | 2025–2050 | Ganti 2024 → 2025 |
| K3 | PPT-lama S4 | Kontribusi PDB "2,2% → 4,9% (2020→2025)" vs buku "2,2% (2020) → 4% (2024)" | **Keputusan penulis: pakai 4,9% (data terbaru 2025)** | Perbarui Subbab 1.1 dengan angka dan sumber 2025 agar buku dan PPT sama |
| K4 | Buku 1.1 vs 3.2 | ">40 juta perjalanan 2025" vs ">38 juta pada 2024" | Pakai angka 2025 (>40 juta) secara konsisten | Samakan tahun acuan |
| K5 | Tabel 17 vs Buku 4.4.5 | E15 "×3 (0,806)" vs "0,832"; repo: 0,83178 (= 3 × 0,27726) | 0,832 | 0,806 = 3 × LPE lama; perbarui Tabel 17 |
| K6 | Buku 4.4.5 vs repo `uji_kondisi_ekstrem_v2.ipynb` | Batas keberlakuan "LPE ≈ 0,336 (1,25× nilai dasar)" vs repo "LPE ≤ 0,346575" (= 1,25 × 0,27726). 0,336 ≈ 1,25 × 0,26864 (LPE sebelum koreksi) | **Keputusan penulis: pakai 0,336 sesuai buku.** Catatan: secara aritmetika 0,336 = 1,25 × 0,26864 (LPE sebelum koreksi Tahap 0), bukan nilai hasil kalibrasi; kalibrasi yang ditolak di Tahap 4 adalah laju konversi dasar (0,0638662), bukan LPE | Siapkan jawaban bila penguji menghitung 1,25 × 0,27726 = 0,347 |
| K7 | Buku 4.2.1 & 4.10.1 | "koefisien determinasi model regresi sekitar 0,41" padahal R² level = 0,785; 0,405 adalah R² selisih tahunan | Tulis "R² selisih tahunan 0,405 (R² level 0,785)" | Perjelas label |
| K8 | Tabel 31 | F1 77,19% adalah versi **tak terbobot**, sedangkan OA/UA/PA pada tabel versi terbobot; F1 terbobot = 69,58% [Repo: Uji Akurasi Lokal/Metrik Imbalance] | Beri label "(tak terbobot)" pada F1 dan Kappa | Tambah keterangan |
| K9 | Lampiran 7 buku | Lahan terbangun 2015 tertulis "9443.037,00"; Master Data: 43.037,00 ha (ekstrapolasi) | 43.037 ha (ditandai ekstrapolasi) | Perbaiki salah ketik |
| K10 | Penomoran buku | CLD berlabel "Gambar 7" (bentrok dengan Kerangka Pikir); rujukan silang "Tabel 16" (seharusnya 49), "Tabel 18" (29), "Tabel 20" (60), "Tabel 31" (60), "Gambar 4.32" (47), "Subbab 4.9" untuk skenario (4.8), "Lanjutan Tabel 44" (55), "Gambar 9" untuk tren NTL (11) | Tidak memengaruhi PPT | Perbaiki rujukan silang |
| K11 | Tabel 2 vs repo | TK tersedia 2017–2025, pengeluaran 2018–2025, tetapi Lampiran 7 memuat nilai 2015–2016/2015–2017 tanpa penjelasan. Repo: **ekstrapolasi CAGR mundur** (TK 3,67%/th; pengeluaran 10,27%/th) | Tampilkan sebagai informasi tambahan di lampiran L13, diberi label "dari dokumentasi repository" | Tambahkan ke 3.7.1 sebagai ketidakteraturan ke-5 |
| K12 | Tabel 2 vs repo | Pengeluaran per kunjungan "Tahunan, Nasional"; repo: wisnus spesifik DIY, wisman nasional, digabung rata-rata tertimbang; kurs tengah BI | Pakai deskripsi repo di L13 (tidak mengubah nilai) | Perjelas sumber |
| K13 | Repo `[02] Uji Perilaku/` (v1) | Notebook & grafik lama (P1 memakai input wisatawan; kategori DC "Baik/Cukup/Kurang") sudah digantikan baseline v2 | **Jangan pakai** grafik `[02] Uji Perilaku/*.png`; pakai gambar buku (Gambar 25–41) atau `Kalibrasi/baseline_v2_*.png`. Interpretasi DC ikut buku (0,4–0,7 = rata-rata sampai baik) | — |
| K14 | Tabel 46 | Uji P5 tidak ditabelkan (hanya narasi). Repo: E1 0,2025; E2 0,5680; DC 0,4057 (tanpa COVID); DC 0,4203 (dengan COVID) | Boleh ditampilkan sebagai baris tambahan, diberi catatan sumber | Tambahkan baris P5 |
| K15 | Repo `Data Citra untuk Lahan Terbangun.ipynb` | Keluaran lama "nilai untuk model 67.880 ha; luas 318.580 ha; RDDL ref 0,7869" (berbasis luas lunak terkoreksi) | Abaikan; nilai final 55.029,54 ha; 317.036 ha; 0,826425 | — |
| K16 | Repo SUS (Responses.xlsx) | Seluruh 10 responden berperan "Mahasiswa"; buku tidak menyebut profil responden | Cantumkan di B65 dan keterbatasan (transparansi); tanpa nama responden | Tambahkan profil responden |
| K17 | Buku 5.1 butir 3 | Tidak menyebut skor SUS | PPT menampilkan SUS 88,50 (ada di 4.9.3) | Tambahkan ke kesimpulan |
| K18 | Repo NTL korelasi | Korelasi selisih r = 0,636, p = 0,174 (n = 6 selisih, tidak signifikan pada α 0,05) | Siapkan di lampiran L15 untuk tanya jawab; jangan klaim signifikan | Pertimbangkan menyebut keterbatasan ini |
| K19 | Tabel 21 vs Tabel 60 | TPK termasuk KPI deskriptif, tetapi tidak muncul di Tabel 60. Repo: TPK 2050 BAU 0,3584; S 0,3537; DP 0,3458 | Tampilkan di lampiran L27 sebagai pelengkap | Tambahkan baris TPK |
| K20 | Buku 4.7.1 vs Tabel 56 | Teks buku: asumsi menempati "empat dari enam peringkat teratas"; Tabel 56 hanya menandai 3 asumsi di 6 teratas (peringkat 1, 3, 4). PPT-lama "3 dari 4" konsisten dengan tabel | **Ralat audit awal:** PPT tetap "3 dari 4" | Perbaiki kalimat buku menjadi "tiga dari empat" (atau tiga dari enam) |
| K21 | Buku 4.3.2.4 | Menyebut uji kestabilan horizon diperpanjang sampai 2150, hasilnya tidak disajikan. Repo: puncak wisatawan 122,9 juta pada 2080 lalu turun; RDDL 0,018 pada 2150 | Lampiran L20 (diberi label "tambahan dari repo") | Opsional ditambah |
| K22 | Buku 4.2.1 (validasi spasial) | Pantai Baron disebut "kawasan wisata pantai"; script GEE melabeli "karst/minim aktivitas" | Ikut buku | — |

---

## Informasi Tambahan Penting dari Repository (belum ada di PPT lama)

Semua tidak bertentangan dengan keputusan final buku, dan dapat memperkuat jawaban saat tanya jawab:

1. **Spesifikasi GEE** [Repo: GEE.rtf]: NTL = `NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG`, band `avg_rad`, skala 500 m, batas `FAO/GAUL/2015/level1`; DW = `GOOGLE/DYNAMICWORLD/V1`, band `built` dirata-rata per tahun lalu ≥0,5, skala 10 m, `pixelArea`; titik validasi spasial diberi *buffer* 300 m; sampel akurasi `stratifiedSample` 100/kelas, `seed 2024`.
2. **NTL** [Repo: Pengujian Korelasi NTL terhadap ODTW]: r level 0,886 (p 0,008); r selisih 0,636 (p 0,174); RMSE LOOCV 11,3 unit (rata-rata 188); galat maksimum 8,9%.
3. **DW diagnosis** [Repo: Data Citra untuk Lahan Terbangun.ipynb]: obs/piksel vs tahun r = +0,174 (p 0,631, syarat terpenuhi); luas vs obs r = +0,788 (p 0,0067; 62,2% variasi dijelaskan jumlah observasi); b = 1.059,8 ha per observasi; SD perubahan tahunan turun 12,3% → 6,6%.
4. **DW metrik tambahan** [Repo: Metrik Imbalance]: Balanced Accuracy 83,3%; MCC 0,637; ROC-AUC 0,941 (terbobot); ambang optimum F1/MCC 0,45.
5. **Uji ekstrem v2** [Repo: hasil_uji_kondisi_ekstrem_v2.xlsx]: horizon 2150 (lihat K21).
6. **Faktor sambung** [Repo: Master Data, sheet "Perhitungan faktor sambung"]: g_pra 7,63%/th; g_pasca 15,52%/th; g_wajar 11,58%; lompatan 2,566 → faktor 2,2997.
7. **Parameter hotel** [Repo: Parameter Hotel]: malam tersedia per kamar tahunan 219,9–483,8 (3 tahun >365 → bukti derau data); uji kecocokan ambang: korelasi tertinggi 0,497 pada 0,275.
8. **Kalibrasi Tahap 1** [Repo: kalibrasi_tahap1.ipynb]: grid 31 × 25 = 775 titik; optimum P1 menghasilkan sensitivitas 5,059; uji kepekaan ambang indiferen 2%/5%/10%.
9. **Kalibrasi Tahap 2**: grid 101 titik; himpunan indiferen 5% k = 0,054063–0,072853.
10. **Skenario** [Repo: hasil_simulasi_skenario.xlsx]: 23 run (3×7 + 2 dekomposisi); hotel 2050: 5.404 / 5.631 / 6.033; ODTW 2050: 367 / 394 / 449.
11. **SUS**: profil responden (K16), jawaban per butir tersedia untuk lampiran (anonim R1–R10).

## Peta Gambar Buku → File Media (untuk penyusunan file PPT)

File docx yang diekstrak menghasilkan `word/media/imageN.png`. Pemetaan: Gambar 1 = image2; 2 = image3; 3 = image4; 4 = image5; 5 = image6; 6 (peta DIY) = image7; 7 (kerangka pikir) = image8; 8 = image9; 9 (alur aplikasi) = image10; **CLD = image11**; 10 (SFD) = image12; 11–15 = image13–image17; 16 = image18 + image19; untuk Gambar 17–66 berlaku **imageN = Gambar + 3** (contoh: Gambar 25 P1 hotel = image28; Gambar 57 skenario wisatawan = image60; Gambar 66 halaman simulasi = image69).
