# Catatan PPT sidang berbasis tujuan

## Revisi dosen (dari "Lengkap_PPT_SIDANG_FINAL.pptx" versi Kevin, 90 → 94 slide)

- Bahasa: 230 kalimat/sel ditulis ulang agar tidak kaku. Istilah diganti: tuas → variabel kebijakan; galat → error; derau → noise; umpan balik → feedback; penguat/penyeimbang → reinforcing/balancing loop; guncangan → shock; ambang → batas; endogen/eksogen → "dihitung di dalam model"/"input dari luar model"; kekokohan → robustness; triangulasi, punggung, substantif, rezim, lebar rentang, dll. diganti kalimat biasa. Daftar lengkap: `docs/v5/rewrite.py`.
- Judul vs resume: baris atas = judul tahapan (32 pt, tebal, tanpa nomor subbab); baris bawah = resume isi slide (19 pt, abu-abu). Daftar: `docs/v5/titles.py`.
- Slide baru 31: Estimasi Lahan Terbangun — Validasi Spasial (Gambar 14–15 buku).
- Lampiran 17 (2 slide): daftar istilah — kode uji (P1–P5, P1b, E01–E17, Tahap 0–4, aturan R1–R4, M1/M2/S/T, D-A/D-B/D-C, C0–C6) dan ukuran/singkatan.
- Lampiran 18: kategori IRTS 2008 dan pemetaan ke KBLI 2020. Daftar 12 kategori IRTS dan kode KBLI-nya berasal dari IRTS 2008/KBLI 2020, bukan dari buku; mohon dicek.
- Koreksi isi: Lampiran 13 sebelumnya menyebut "P1b, versi COVID"; menurut buku P1b = variasi P1 dengan rata-rata kamar per unit aktual.
- Catatan pembicara belum disesuaikan dengan istilah baru.
- Grafik yang bisa diedit (klik kanan → Edit Data) menggantikan gambar pada slide 3 (CAGR), 4 (kontribusi PDB, kunjungan wisman/wisnus), 42 (uji feedback loop), 45 (data wisnus mentah vs tersambung), 47 (DC uji parsial vs penuh), 54 (pengaruh maksimum ±10%), 69 (SUS). Data: buku (Tabel 45, 56, Lampiran 11/8), repo Evaluasi SUS, dan angka pada grafik lama (CAGR, PDB, kunjungan). Kode: `docs/v5/charts_v6.py`.

## Draf v4 – 16 menit (turunan dari v3; v3 tetap disimpan sebagai versi lengkap)

- Slide utama: 25 (1–25), target ±16 menit. Urutan = slide v3 nomor 1, 6, 8, 9, 14, 17, 19, 21, 24, 25, 32, 34, 41, 50, 52, 56, 57, 59, 61, 64, 66, 69, 73, 74, 75.
- Slide 26: indeks slide cadangan dan lampiran (pengganti slide agenda v3).
- Slide 27–72: 46 slide cadangan (penanda abu "Cadangan" di pojok kanan bawah), urutan sama dengan v3.
- Slide 73–88: Lampiran 1–16.
- Dihapus: agenda (v3 #2) dan tiga slide ringkasan per tujuan (v3 #23, #63, #70); isinya tercakup di slide Kesimpulan.
- Penanda W/S diganti dengan pil merah berisi target waktu (mis. 0:45).
- Tambahan isi: kotak "Mengapa DIY?" di slide 2; baris data (2015–2025, tahun dasar 2025, horizon 2050) di slide 5; tombol pada slide pembatas tujuan menjadi "Hasil kunci: slide 8 / 17 / 22".
- Catatan pembicara slide utama = naskah versi 16 menit (`docs/notes_v4.py`). Kode pembangun: `docs/build_v4.py` (input: hasil v3).

## Draf v3 (perubahan dari v2)

- Label tahapan/subbab ditambahkan di atas judul pada 66 slide utama (mis. "4.1.3 · Causal Loop Diagram dan Struktur Feedback Loop"), mengikuti nomor subbab di buku.
- Label: 19 pt tebal, warna 1C8FA0; judul slide diseragamkan 35 pt.
- Tanpa label: slide 1 (judul), 2 (agenda/legenda), slide pembatas Tujuan, slide Ringkasan Hasil per tujuan, slide penutup, dan seluruh lampiran.
- Kode pembangun: `docs/build_deck.py` (blok "v3").

## Draf v2 (perubahan dari v1)
- **Slide 21 (CLD)** dirapikan: gambar CLD di kiri + tabel enam loop (loop, jenis, rantai kausal ringkas, peran dalam model) dari Tabel 26 buku.
- **SFD dipindah ke bagian utama** sebagai slide 34 "Hasil: stock-flow diagram pariwisata DIY" (sub-tahap 2B). Lampiran SFD dihapus; nomor lampiran sesudahnya bergeser satu (Lampiran 9 = batas model, ..., Lampiran 15 = persamaan, Lampiran 16 = data historis).
- **Penanda prioritas** di pojok kanan bawah setiap slide utama: bulat merah **W** = wajib dijelaskan (34 slide), bulat biru **S** = sebut singkat. Legenda ada di slide 2. Lampiran tanpa penanda.
- Total tetap 91 slide: 75 utama + 16 lampiran. Ringkasan hasil kini di slide 23, 63, dan 70.

## Draf v1

Basis: PPT lama (desain, grafik, dan catatan pembicara dipertahankan). 91 slide = **74 utama + 17 lampiran**. Skrip pembangun: `docs/build_deck.py` (python-pptx).

## Urutan akhir (nomor baru ← asal)
| Bagian | Slide baru | Asal |
|---|---|---|
| Pembukaan & Pendahuluan | 1–12 | S1, S2 (revisi alur per tujuan), S4, S5, S6, S7, S8, S9, S10, S11, S12, S13 |
| Metodologi (fondasi) | 13–16 | S14, S16 (+ label "→ Tujuan n" per tahap), S15, **baru: preprocessing** |
| Tujuan 1 | 17–23 | **pembatas**, **baru: metode CLD**, S26, **baru: 18 hubungan kausal**, S27, **baru: batas model**, **baru: Ringkasan Hasil Tujuan 1** |
| Tujuan 2 · 2A Citra | 24–32 | **pembatas**, S17, S18, S19, S30, **baru: estimasi + validasi spasial NTL**, S31, **baru: diagnosis DW (grafik native)**, **baru: simpulan citra** |
| 2B Formulasi | 33–35 | S28, S29, **baru: persamaan subsistem lain** |
| 2C Parameterisasi | 36–38 | **baru: 5 kategori parameter**, **baru: contoh penurunan**, S40 |
| 2D Uji struktur | 39–42 | S21, S32, S33, S34 |
| 2E Uji perilaku & kalibrasi | 43–51 | S22, S35, **baru: hasil uji parsial**, S36, S37, S23, S38, **baru: diagnostik Tahap 3**, **baru: model layak?** |
| 2F Sensitivitas | 52–53 | S24, S39 |
| 2G Skenario | 54–62 | S25, S41, S42, S43, S44, S45, S46, S47, **baru: Ringkasan Hasil Tujuan 2** |
| Tujuan 3 | 63–69 | **pembatas**, **baru: alasan & kebutuhan**, S49, S60 (dipindah dari lampiran), **baru: black-box**, S50, **baru: Ringkasan Hasil Tujuan 3** |
| Penutup | 70–74 | S48, S51, S52, S53, S54 |
| Lampiran 1–17 | 75–91 | S3, S55, S56, S57, **baru L5: data pendukung repo + spesifikasi GEE**, S58, **baru L7: KPI pelengkap**, S59, S61, S62, S63, S64, **baru L13: horizon 2150**, S65, S66, S67, S68 |

S20 (ringkasan pengujian berjenjang) dihapus; isinya dipindah ke slide pembatas Tujuan 2 sebagai peta sub-tahap 2A–2G.

## Perubahan dibanding rancangan dokumen 02
- S4 dan S5 tetap dua slide (tidak digabung) agar grafik lama utuh.
- S18 dan S19 (metode/metrik citra) dipertahankan utuh sebelum slide hasil, tidak dipecah.
- Navigasi atas: Pendahuluan | Metodologi | Tujuan 1 | Tujuan 2 | Tujuan 3 | Penutup; slide Tujuan 2 diberi label sub-tahap (2A–2G).

## Keputusan penulis yang sudah diterapkan
- Skenario berada di Tujuan 2.
- K3: angka 4,9% (2025) dipertahankan di slide 3. **Catatan pembicara slide 4 masih menyebut "4 persen pada 2024"**; sesuaikan bila ingin konsisten.
- K6: angka 0,336 dipertahankan di slide 42.
- K20 (ralat): "3 dari 4 peringkat teratas" di slide 53 sudah konsisten dengan Tabel 56.

## Yang perlu Anda cek di PowerPoint
- Font Canva "Calibri (MS)" dirender dengan font pengganti saat QA; beberapa angka besar di slide 13 (sudah ada sejak PPT lama) tampak menumpuk di pratinjau LibreOffice—cek di PowerPoint.
- Slide baru memakai shape PowerPoint biasa (bisa diedit langsung), grafik DW di slide 31 adalah chart native.
