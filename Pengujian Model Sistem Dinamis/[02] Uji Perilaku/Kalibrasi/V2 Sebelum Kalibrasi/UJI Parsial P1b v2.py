"""
Python model 'UJI Parsial P1b v2.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np

from pysd.py_backend.statefuls import Integ
from pysd.py_backend.lookups import HardcodedLookups
from pysd import Component

__pysd_version__ = "3.14.3"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent


component = Component()

#######################################################################
#                          CONTROL VARIABLES                          #
#######################################################################

_control_vars = {
    "initial_time": lambda: 2016,
    "final_time": lambda: 2025,
    "time_step": lambda: 1,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


@component.add(name="Time")
def time():
    """
    Current time of the model.
    """
    return __data["time"]()


@component.add(
    name="FINAL TIME", units="Tahun", comp_type="Constant", comp_subtype="Normal"
)
def final_time():
    """
    The final time for the simulation.
    """
    return __data["time"].final_time()


@component.add(
    name="INITIAL TIME", units="Tahun", comp_type="Constant", comp_subtype="Normal"
)
def initial_time():
    """
    The initial time for the simulation.
    """
    return __data["time"].initial_time()


@component.add(
    name="SAVEPER",
    units="Tahun",
    limits=(0.0, np.nan),
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time_step": 1},
)
def saveper():
    """
    The frequency with which output is stored.
    """
    return __data["time"].saveper()


@component.add(
    name="TIME STEP",
    units="Tahun",
    limits=(0.0, np.nan),
    comp_type="Constant",
    comp_subtype="Normal",
)
def time_step():
    """
    The time step for the simulation.
    """
    return __data["time"].time_step()


#######################################################################
#                           MODEL VARIABLES                           #
#######################################################################


@component.add(
    name="Data Total Malam Menginap",
    units="Malam",
    comp_type="Lookup",
    comp_subtype="Normal",
    depends_on={"__lookup__": "_hardcodedlookup_data_total_malam_menginap"},
)
def data_total_malam_menginap(x, final_subs=None):
    return _hardcodedlookup_data_total_malam_menginap(x, final_subs)


_hardcodedlookup_data_total_malam_menginap = HardcodedLookups(
    [2016.0, 2017.0, 2018.0, 2019.0, 2020.0, 2021.0, 2022.0, 2023.0, 2024.0, 2025.0],
    [
        6097320.0,
        10899900.0,
        10293300.0,
        13363900.0,
        4753100.0,
        7379580.0,
        9267220.0,
        11417700.0,
        11503500.0,
        11954100.0,
    ],
    {},
    "interpolate",
    {},
    "_hardcodedlookup_data_total_malam_menginap",
)


@component.add(
    name="Data Kamar per Unit",
    units="Kamar/Unit Akomodasi",
    comp_type="Lookup",
    comp_subtype="Normal",
    depends_on={"__lookup__": "_hardcodedlookup_data_kamar_per_unit"},
)
def data_kamar_per_unit(x, final_subs=None):
    return _hardcodedlookup_data_kamar_per_unit(x, final_subs)


_hardcodedlookup_data_kamar_per_unit = HardcodedLookups(
    [2016.0, 2017.0, 2018.0, 2019.0, 2020.0, 2021.0, 2022.0, 2023.0, 2024.0, 2025.0],
    [
        20.1821,
        22.1917,
        20.3271,
        19.6571,
        19.7413,
        20.2748,
        20.1562,
        20.2654,
        26.1165,
        21.4168,
    ],
    {},
    "interpolate",
    {},
    "_hardcodedlookup_data_kamar_per_unit",
)


@component.add(
    name="Total Malam Menginap",
    units="Malam",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "data_total_malam_menginap": 1},
)
def total_malam_menginap():
    return data_total_malam_menginap(time())


@component.add(
    name='"Rata-rata Kamar per Unit Akomodasi"',
    units="Kamar/Unit Akomodasi",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "data_kamar_per_unit": 1},
)
def ratarata_kamar_per_unit_akomodasi():
    return data_kamar_per_unit(time())


@component.add(
    name="Jumlah Wisatawan",
    units="Kunjungan",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_jumlah_wisatawan": 1},
    other_deps={
        "_integ_jumlah_wisatawan": {
            "initial": {},
            "step": {"laju_kedatangan_wisatawan": 1, "laju_penurunan_wisatawan": 1},
        }
    },
)
def jumlah_wisatawan():
    return _integ_jumlah_wisatawan()


_integ_jumlah_wisatawan = Integ(
    lambda: laju_kedatangan_wisatawan() - laju_penurunan_wisatawan(),
    lambda: 15066300.0,
    "_integ_jumlah_wisatawan",
)


@component.add(
    name="Data Wisatawan",
    units="Kunjungan",
    comp_type="Lookup",
    comp_subtype="Normal",
    depends_on={"__lookup__": "_hardcodedlookup_data_wisatawan"},
)
def data_wisatawan(x, final_subs=None):
    return _hardcodedlookup_data_wisatawan(x, final_subs)


_hardcodedlookup_data_wisatawan = HardcodedLookups(
    [2016.0, 2017.0, 2018.0, 2019.0, 2020.0, 2021.0, 2022.0, 2023.0, 2024.0, 2025.0],
    [
        15066300.0,
        15280500.0,
        18391000.0,
        20520100.0,
        19610100.0,
        22849400.0,
        25755700.0,
        30542600.0,
        38134500.0,
        40695700.0,
    ],
    {},
    "interpolate",
    {},
    "_hardcodedlookup_data_wisatawan",
)


@component.add(
    name="Data Investasi",
    units="Miliar Rupiah",
    comp_type="Lookup",
    comp_subtype="Normal",
    depends_on={"__lookup__": "_hardcodedlookup_data_investasi"},
)
def data_investasi(x, final_subs=None):
    return _hardcodedlookup_data_investasi(x, final_subs)


_hardcodedlookup_data_investasi = HardcodedLookups(
    [2016.0, 2017.0, 2018.0, 2019.0, 2020.0, 2021.0, 2022.0, 2023.0, 2024.0, 2025.0],
    [
        373.842,
        165.391,
        568.334,
        741.448,
        489.693,
        848.804,
        463.589,
        1175.26,
        712.284,
        1325.95,
    ],
    {},
    "interpolate",
    {},
    "_hardcodedlookup_data_investasi",
)


@component.add(
    name="Investasi Sektor Pariwisata",
    units="Miliar Rupiah",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "data_investasi": 1},
)
def investasi_sektor_pariwisata():
    return data_investasi(time())


@component.add(
    name="Intensitas Tenaga Kerja",
    units="Jiwa/Miliar Rupiah",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "intensitas_tenaga_kerja_awal": 1,
        "tahun_dasar_intensitas_tenaga_kerja": 1,
        "laju_kenaikan_produktivitas": 1,
        "time": 1,
    },
)
def intensitas_tenaga_kerja():
    return intensitas_tenaga_kerja_awal() * float(
        np.exp(
            -laju_kenaikan_produktivitas()
            * (time() - tahun_dasar_intensitas_tenaga_kerja())
        )
    )


@component.add(
    name="Tahun Dasar Intensitas Tenaga Kerja",
    units="Tahun",
    comp_type="Constant",
    comp_subtype="Normal",
)
def tahun_dasar_intensitas_tenaga_kerja():
    """
    Tahun acuan Intensitas Tenaga Kerja Awal (TK 2025 ÷ PDRB 2025).
    """
    return 2025


@component.add(
    name="Batas Maksimum Efek ODTW",
    units="Dmnl",
    limits=(1.0, 1.875),
    comp_type="Constant",
    comp_subtype="Normal",
)
def batas_maksimum_efek_odtw():
    """
    Batas kejenuhan efek ODTW terhadap daya tarik: pertambahan ODTW paling banyak menaikkan komponen daya tarik 50% di atas kondisi tahun dasar. Syarat kestabilan: Bobot ODTW × Batas Maksimum < Laju Penurunan Dasar ÷ Laju Pertumbuhan Eksternal (0,40 × 1,5 = 0,60 < 0,75). Diuji sensitivitas 1,25–1,875.
    """
    return 1.5


@component.add(
    name="Daya Tarik Destinasi Wisata",
    units="Dmnl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "bobot_odtw": 1,
        "jumlah_objek_daya_tarik_wisata": 1,
        "odtw_referensi": 1,
        "batas_maksimum_efek_odtw": 1,
        "elastisitas_daya_tarik_odtw": 1,
        "bobot_kepadatan": 1,
        "kepadatan_wisatawan": 1,
        "kepadatan_referensi": 1,
        "rasio_daya_dukung_lahan_referensi": 1,
        "rasio_daya_dukung_lahan": 1,
        "bobot_daya_dukung_lahan": 1,
    },
)
def daya_tarik_destinasi_wisata():
    """
    Komponen kepadatan dibatasi maksimum 1 karena kepadatan di bawah kondisi tahun dasar tidak menambah daya tarik di atas normal. Kepadatan berperan sebagai faktor pembatas (qualifying determinant), bukan pendorong daya tarik (Ritchie & Crouch, 2003; Butler, 1980).
    """
    return (
        bobot_odtw()
        * float(
            np.minimum(
                batas_maksimum_efek_odtw(),
                (jumlah_objek_daya_tarik_wisata() / odtw_referensi())
                ** elastisitas_daya_tarik_odtw(),
            )
        )
        + bobot_kepadatan()
        * float(np.minimum(1, kepadatan_referensi() / kepadatan_wisatawan()))
        + bobot_daya_dukung_lahan()
        * (rasio_daya_dukung_lahan() / rasio_daya_dukung_lahan_referensi())
    )


@component.add(
    name="Laju Konversi Lahan Pariwisata",
    units="Hektar/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "laju_konstruksi_hotel_dan_akomodasi": 1,
        "lahan_per_hotel_dan_akomodasi": 1,
        "lahan_per_odtw": 1,
        "laju_pembangunanpenambahan_odtw": 1,
        "kebijakan_konservasi_lahan": 1,
        "rasio_daya_dukung_lahan_referensi": 1,
        "rasio_daya_dukung_lahan": 1,
    },
)
def laju_konversi_lahan_pariwisata():
    """
    Konversi lahan menjadi lahan terbangun akibat konstruksi akomodasi dan pembangunan ODTW (koefisien kebutuhan lahan per unit), dikurangi proporsi yang ditahan Kebijakan Konservasi Lahan. Memakai laju pembangunan bruto karena lahan tidak kembali saat usaha tutup. Konversi dibatasi ketersediaan lahan melalui faktor Rasio Daya Dukung Lahan terhadap nilai referensinya, yang bernilai 1 pada tahun dasar dan menuju nol saat lahan habis.
    """
    return (
        (
            laju_konstruksi_hotel_dan_akomodasi() * lahan_per_hotel_dan_akomodasi()
            + laju_pembangunanpenambahan_odtw() * lahan_per_odtw()
        )
        * (1 - kebijakan_konservasi_lahan())
        * (rasio_daya_dukung_lahan() / rasio_daya_dukung_lahan_referensi())
    )


@component.add(
    name='"Tingkat Penghunian Kamar (TPK)"',
    units="Dmnl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rasio_permintaan_terhadap_kapasitas_kamar": 1},
)
def tingkat_penghunian_kamar_tpk():
    """
    Tingkat penghunian kamar sesuai definisi BPS: malam kamar terpakai dibagi malam kamar tersedia, dibatasi maksimum 100% karena kamar terpakai tidak dapat melebihi kamar tersedia.
    """
    return float(np.minimum(1, rasio_permintaan_terhadap_kapasitas_kamar()))


@component.add(
    name="Laju Konstruksi Hotel dan Akomodasi",
    units="Unit Akomodasi/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investasi_sektor_pariwisata": 1,
        "sensitivitas_konstruksi_terhadap_tpk": 1,
        "rasio_permintaan_terhadap_kapasitas_kamar": 1,
        "tpk_ambang": 1,
    },
)
def laju_konstruksi_hotel_dan_akomodasi():
    """
    Konstruksi akomodasi baru: investasi (kemampuan membangun) dikali selisih TPK di atas ambang (keinginan membangun); respons pasokan terhadap okupansi (Wheaton & Rossoff, 1998).
    """
    return (
        investasi_sektor_pariwisata()
        * sensitivitas_konstruksi_terhadap_tpk()
        * float(
            np.maximum(0, rasio_permintaan_terhadap_kapasitas_kamar() - tpk_ambang())
        )
    )


@component.add(
    name="Rasio Permintaan terhadap Kapasitas Kamar",
    units="Dmnl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_malam_menginap": 1,
        "tingkat_penghunian_ganda_kamar": 1,
        "malam_tersedia_per_kamar": 1,
        "jumlah_hotel_dan_akomodasi": 1,
        "ratarata_kamar_per_unit_akomodasi": 1,
    },
)
def rasio_permintaan_terhadap_kapasitas_kamar():
    """
    Perbandingan permintaan malam kamar terhadap kapasitas malam kamar tersedia. Nilai > 1 menunjukkan permintaan melampaui kapasitas (permintaan tak terlayani) dan menjadi sinyal pembangunan akomodasi baru.
    """
    return (total_malam_menginap() / tingkat_penghunian_ganda_kamar()) / (
        jumlah_hotel_dan_akomodasi()
        * ratarata_kamar_per_unit_akomodasi()
        * malam_tersedia_per_kamar()
    )


@component.add(
    name='"Laju Pembangunan/Penambahan ODTW"',
    units="Unit/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investasi_sektor_pariwisata": 1,
        "sensitivitas_odtw_terhadap_investasi": 1,
        "laju_pembangunan_odtw_non_investasi": 1,
    },
)
def laju_pembangunanpenambahan_odtw():
    """
    output dihasilkan dari dua faktor produksi, yaitu modal (K) dan tenaga kerja (L), seperti dalam fungsi produksi Cobb-Douglas. Di model ini, "output"-nya adalah ODTW baru. Bentuk penjumlahan linear adalah penyederhanaan supaya masing-masing jalur bisa dibaca terpisah sebagai loop R2 (investasi) dan R3 (tenaga kerja).
    """
    return (
        investasi_sektor_pariwisata() * sensitivitas_odtw_terhadap_investasi()
        + laju_pembangunan_odtw_non_investasi()
    )


@component.add(
    name="Waktu Penyesuaian Tenaga Kerja",
    units="Tahun",
    limits=(1.0, 3.0),
    comp_type="Constant",
    comp_subtype="Normal",
)
def waktu_penyesuaian_tenaga_kerja():
    return 1


@component.add(
    name="Laju Kenaikan Produktivitas",
    units="1/Tahun",
    limits=(0.0, 0.05),
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_kenaikan_produktivitas():
    return 0.0110205


@component.add(
    name="Elastisitas Daya Tarik ODTW",
    units="Dmnl",
    limits=(0.0, 1.0),
    comp_type="Constant",
    comp_subtype="Normal",
)
def elastisitas_daya_tarik_odtw():
    """
    Ditambahkan untuk mencegah model meledak akibat komponen ODTW linear. Rentang 0–1 (1 = linear). Diuji sensitivitas. Elastisitas daya tarik terhadap jumlah ODTW. Nilai < 1 mencerminkan diminishing returns; 1 = linear. Ditambahkan untuk mencegah model meledak akibat komponen ODTW linear. Diuji sensitivitas.
    """
    return 0.3


@component.add(
    name="Laju Penyerapan Tenaga Kerja Pariwisata",
    units="Jiwa/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "laju_keluar_tenaga_kerja_pariwisata": 1,
        "tenaga_kerja_dibutuhkan": 1,
        "waktu_penyesuaian_tenaga_kerja": 1,
        "tenaga_kerja_pariwisata": 1,
    },
)
def laju_penyerapan_tenaga_kerja_pariwisata():
    return float(
        np.maximum(
            0,
            laju_keluar_tenaga_kerja_pariwisata()
            + (tenaga_kerja_dibutuhkan() - tenaga_kerja_pariwisata())
            / waktu_penyesuaian_tenaga_kerja(),
        )
    )


@component.add(
    name="Intensitas Tenaga Kerja Awal",
    units="Jiwa/Miliar Rupiah",
    comp_type="Constant",
    comp_subtype="Normal",
)
def intensitas_tenaga_kerja_awal():
    return 21.5366


@component.add(
    name="Tenaga Kerja Dibutuhkan",
    units="Jiwa",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pdrb_sektor_pariwisata": 1, "intensitas_tenaga_kerja": 1},
)
def tenaga_kerja_dibutuhkan():
    return pdrb_sektor_pariwisata() * intensitas_tenaga_kerja()


@component.add(
    name="Kebijakan Konservasi Lahan",
    units="Dmnl",
    limits=(0.0, 1.0),
    comp_type="Constant",
    comp_subtype="Normal",
)
def kebijakan_konservasi_lahan():
    """
    Tuas kebijakan konservasi lahan (rentang 0–1). 0 = tanpa konservasi (BAU).
    """
    return 0


@component.add(
    name="Lahan Terbangun",
    units="Hektar",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_lahan_terbangun": 1},
    other_deps={
        "_integ_lahan_terbangun": {
            "initial": {},
            "step": {
                "laju_konversi_lahan_non_pariwisata": 1,
                "laju_konversi_lahan_pariwisata": 1,
            },
        }
    },
)
def lahan_terbangun():
    return _integ_lahan_terbangun()


_integ_lahan_terbangun = Integ(
    lambda: laju_konversi_lahan_non_pariwisata() + laju_konversi_lahan_pariwisata(),
    lambda: 44561.1,
    "_integ_lahan_terbangun",
)


@component.add(
    name="Laju Konversi Dasar",
    units="1/Tahun",
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_konversi_dasar():
    return 0.0436052


@component.add(
    name="Laju Pembangunan ODTW Non Investasi",
    units="Unit/Tahun",
    limits=(0.0, 20.0),
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_pembangunan_odtw_non_investasi():
    """
    Pembangunan ODTW oleh pemerintah dan masyarakat (BUMDes, Pokdarwis, komunitas), eksogen. Diturunkan dari identitas stock-flow ODTW 2015–2025 dengan porsi pengelola non-swasta 42,91% (Statistik ODTW 2024, BPS).
    """
    return 5.427


@component.add(
    name="Kepadatan Wisatawan",
    units="Kunjungan/Hektar",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"jumlah_wisatawan": 1, "luas_lahan_tersedia": 1},
)
def kepadatan_wisatawan():
    """
    Intensitas kunjungan wisatawan per hektar wilayah DIY (tourism density). Luas wilayah saling meniadakan dalam rasio terhadap Kepadatan Referensi.
    """
    return jumlah_wisatawan() / luas_lahan_tersedia()


@component.add(
    name="Laju Konversi Lahan Non Pariwisata",
    units="Hektar/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "laju_konversi_dasar": 1,
        "lahan_terbangun": 1,
        "rasio_daya_dukung_lahan": 1,
    },
)
def laju_konversi_lahan_non_pariwisata():
    return laju_konversi_dasar() * lahan_terbangun() * rasio_daya_dukung_lahan()


@component.add(
    name="Laju Kedatangan Wisatawan",
    units="Kunjungan/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "jumlah_wisatawan": 1,
        "laju_pertumbuhan_eksternal": 1,
        "daya_tarik_destinasi_wisata": 1,
    },
)
def laju_kedatangan_wisatawan():
    return (
        jumlah_wisatawan()
        * laju_pertumbuhan_eksternal()
        * daya_tarik_destinasi_wisata()
    )


@component.add(
    name="Luas Lahan Tersedia",
    units="Hektar",
    comp_type="Constant",
    comp_subtype="Normal",
)
def luas_lahan_tersedia():
    return 317036


@component.add(
    name="Rasio Daya Dukung Lahan",
    units="Dmnl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"lahan_terbangun": 1, "luas_lahan_tersedia": 1},
)
def rasio_daya_dukung_lahan():
    """
    Proporsi lahan yang belum terbangun terhadap luas wilayah; dibatasi minimum nol karena lahan tersisa tidak dapat bernilai negatif
    """
    return float(np.maximum(0, 1 - lahan_terbangun() / luas_lahan_tersedia()))


@component.add(
    name="Proporsi Wisatawan Menginap",
    units="Dmnl",
    comp_type="Constant",
    comp_subtype="Normal",
)
def proporsi_wisatawan_menginap():
    return 0.2058


@component.add(
    name="Tingkat Penghunian Ganda Kamar",
    units="Dmnl",
    comp_type="Constant",
    comp_subtype="Normal",
)
def tingkat_penghunian_ganda_kamar():
    return 2.07


@component.add(
    name="Bobot Daya Dukung Lahan",
    units="Dmnl",
    comp_type="Constant",
    comp_subtype="Normal",
)
def bobot_daya_dukung_lahan():
    return 0.25


@component.add(
    name="Rasio Daya Dukung Lahan Referensi",
    units="Dmnl",
    comp_type="Constant",
    comp_subtype="Normal",
)
def rasio_daya_dukung_lahan_referensi():
    return 0.826425


@component.add(
    name="Bobot Kepadatan", units="Dmnl", comp_type="Constant", comp_subtype="Normal"
)
def bobot_kepadatan():
    return 0.35


@component.add(
    name="Bobot ODTW", units="Dmnl", comp_type="Constant", comp_subtype="Normal"
)
def bobot_odtw():
    return 0.4


@component.add(
    name="Insentif Kebijakan",
    units="Dmnl",
    limits=(0.0, 0.5),
    comp_type="Constant",
    comp_subtype="Normal",
)
def insentif_kebijakan():
    """
    Tuas kebijakan insentif investasi pariwisata. 0 = BAU; 0,1 = Sustainable Development; 0,3 = Development Priority. Nilai 0,1 berarti investasi 10% lebih tinggi dari pola historis.
    """
    return 0


@component.add(
    name="Jumlah Hotel dan Akomodasi",
    units="Unit Akomodasi",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_jumlah_hotel_dan_akomodasi": 1},
    other_deps={
        "_integ_jumlah_hotel_dan_akomodasi": {
            "initial": {},
            "step": {
                "laju_konstruksi_hotel_dan_akomodasi": 1,
                "laju_demolisi_hotel_dan_akomodasi": 1,
            },
        }
    },
)
def jumlah_hotel_dan_akomodasi():
    return _integ_jumlah_hotel_dan_akomodasi()


_integ_jumlah_hotel_dan_akomodasi = Integ(
    lambda: laju_konstruksi_hotel_dan_akomodasi() - laju_demolisi_hotel_dan_akomodasi(),
    lambda: 1170,
    "_integ_jumlah_hotel_dan_akomodasi",
)


@component.add(
    name="Jumlah Objek Daya Tarik Wisata",
    units="Unit",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_jumlah_objek_daya_tarik_wisata": 1},
    other_deps={
        "_integ_jumlah_objek_daya_tarik_wisata": {
            "initial": {},
            "step": {"laju_pembangunanpenambahan_odtw": 1, "laju_penutupan_odtw": 1},
        }
    },
)
def jumlah_objek_daya_tarik_wisata():
    return _integ_jumlah_objek_daya_tarik_wisata()


_integ_jumlah_objek_daya_tarik_wisata = Integ(
    lambda: laju_pembangunanpenambahan_odtw() - laju_penutupan_odtw(),
    lambda: 158,
    "_integ_jumlah_objek_daya_tarik_wisata",
)


@component.add(
    name="Kepadatan Referensi",
    units="Kunjungan/Hektar",
    comp_type="Constant",
    comp_subtype="Normal",
)
def kepadatan_referensi():
    return 128.363


@component.add(
    name="Lahan Per Hotel dan Akomodasi",
    units="Hektar/Unit Akomodasi",
    comp_type="Constant",
    comp_subtype="Normal",
)
def lahan_per_hotel_dan_akomodasi():
    return 0.1


@component.add(
    name="Lahan Per ODTW",
    units="Hektar/Unit",
    comp_type="Constant",
    comp_subtype="Normal",
)
def lahan_per_odtw():
    return 0.5


@component.add(
    name="Laju Demolisi Dasar",
    units="1/Tahun",
    limits=(0.0, 0.1),
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_demolisi_dasar():
    """
    Fraksi unit akomodasi yang berhenti beroperasi per tahun (1 ÷ rata-rata umur operasi; Sterman, 2000). Ditetapkan melalui triangulasi: batas bawah umur rencana bangunan 50 tahun (0,02); acuan bangunan permanen 20 tahun (PP 36/2005; UU PPh) dan proksi laju penutupan ODTW DIY (0,05); batas atas penurunan akomodasi DIY 2020–2021 (0,082). Diuji sensitivitas 0,02–0,08, berpasangan dengan Sensitivitas Konstruksi terhadap TPK.
    """
    return 0.05


@component.add(
    name="Laju Demolisi Hotel dan Akomodasi",
    units="Unit Akomodasi/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"jumlah_hotel_dan_akomodasi": 1, "laju_demolisi_dasar": 1},
)
def laju_demolisi_hotel_dan_akomodasi():
    return jumlah_hotel_dan_akomodasi() * laju_demolisi_dasar()


@component.add(
    name="Laju Keluar Tenaga Kerja Pariwisata",
    units="Jiwa/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tenaga_kerja_pariwisata": 1, "laju_keluar_dasar_tenaga_kerja": 1},
)
def laju_keluar_tenaga_kerja_pariwisata():
    return tenaga_kerja_pariwisata() * laju_keluar_dasar_tenaga_kerja()


@component.add(
    name="Laju Penurunan Wisatawan",
    units="Kunjungan/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"jumlah_wisatawan": 1, "laju_penurunan_dasar": 1},
)
def laju_penurunan_wisatawan():
    return jumlah_wisatawan() * laju_penurunan_dasar()


@component.add(
    name="Laju Penutupan Dasar ODTW",
    units="1/Tahun",
    limits=(0.0, 0.1),
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_penutupan_dasar_odtw():
    """
    Diestimasi dari distribusi lama beroperasi ODTW DIY (Statistik ODTW 2024, BPS) dengan teori populasi stabil: porsi umur > T = e^(−(d+g)T); rata-rata umur usaha ±20 tahun. Diuji sensitivitas 0,01–0,07.
    """
    return 0.0499327


@component.add(
    name="Laju Penutupan ODTW",
    units="Unit/Tahun",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"jumlah_objek_daya_tarik_wisata": 1, "laju_penutupan_dasar_odtw": 1},
)
def laju_penutupan_odtw():
    return jumlah_objek_daya_tarik_wisata() * laju_penutupan_dasar_odtw()


@component.add(
    name="Laju Pertumbuhan Eksternal",
    units="1/Tahun",
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_pertumbuhan_eksternal():
    return 0.27726


@component.add(
    name="Malam Tersedia per Kamar",
    units="Malam/Kamar",
    limits=(200.0, 365.0),
    comp_type="Constant",
    comp_subtype="Normal",
)
def malam_tersedia_per_kamar():
    """
    Malam operasional efektif per kamar per tahun. Malam kamar tersedia versi BPS dihitung dari hari hotel beroperasi, bukan hari kalender. Diturunkan: Σ(Malam Tamu ÷ TPG) ÷ Σ(TPK BPS × Jumlah Kamar) 2015–2025, sehingga level TPK model sebanding dengan TPK BPS.
    """
    return 329.03


@component.add(
    name="ODTW Referensi", units="Unit", comp_type="Constant", comp_subtype="Normal"
)
def odtw_referensi():
    return 201


@component.add(
    name="PDRB Sektor Pariwisata",
    units="Miliar Rupiah",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pengeluaran_wisatawan": 1, "rasio_nilai_tambah_pariwisata": 1},
)
def pdrb_sektor_pariwisata():
    return pengeluaran_wisatawan() * rasio_nilai_tambah_pariwisata()


@component.add(
    name="Pengeluaran per Kunjungan",
    units="Miliar Rupiah/Kunjungan",
    comp_type="Constant",
    comp_subtype="Normal",
)
def pengeluaran_per_kunjungan():
    return 0.00272021


@component.add(
    name="Pengeluaran Wisatawan",
    units="Miliar Rupiah",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"jumlah_wisatawan": 1, "pengeluaran_per_kunjungan": 1},
)
def pengeluaran_wisatawan():
    return jumlah_wisatawan() * pengeluaran_per_kunjungan()


@component.add(
    name="Rasio Investasi terhadap PDRB",
    units="Dmnl",
    comp_type="Constant",
    comp_subtype="Normal",
)
def rasio_investasi_terhadap_pdrb():
    """
    Σ Investasi PMA+PMDN ÷ Σ PDRB ADHK pariwisata 2015–2025.
    """
    return 0.0488174


@component.add(
    name="Laju Penurunan Dasar",
    units="1/Tahun",
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_penurunan_dasar():
    return 0.207945


@component.add(
    name='"Rata-rata Lama Menginap Tamu"',
    units="Malam/Kunjungan",
    comp_type="Constant",
    comp_subtype="Normal",
)
def ratarata_lama_menginap_tamu():
    return 1.427


@component.add(
    name="Sensitivitas Konstruksi terhadap TPK",
    units="Unit Akomodasi/(Miliar Rupiah*Dmnl*Tahun)",
    limits=(0.0, 6.0),
    comp_type="Constant",
    comp_subtype="Normal",
)
def sensitivitas_konstruksi_terhadap_tpk():
    """
    Diturunkan dari identitas stock-flow hotel 2015–2025: Σ(ΔHotel + Laju Demolisi Dasar × Hotel) ÷ Σ[Investasi × MAX(0, TPK − TPK Ambang)]. Dihitung ulang berpasangan jika TPK Ambang atau Laju Demolisi Dasar diubah saat uji sensitivitas
    """
    return 2.31385


@component.add(
    name="Sensitivitas ODTW terhadap Investasi",
    units="Unit/(Miliar Rupiah*Tahun)",
    comp_type="Constant",
    comp_subtype="Normal",
)
def sensitivitas_odtw_terhadap_investasi():
    """
    Diturunkan dari identitas stock-flow ODTW 2015–2025 dengan porsi pengelola swasta 57,09% dibagi ΣInvestasi BKPM 2016–2025. Analog kebalikan ICOR (Harrod-Domar).
    """
    return 0.01052


@component.add(
    name="Tenaga Kerja Pariwisata",
    units="Jiwa",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_tenaga_kerja_pariwisata": 1},
    other_deps={
        "_integ_tenaga_kerja_pariwisata": {
            "initial": {},
            "step": {
                "laju_penyerapan_tenaga_kerja_pariwisata": 1,
                "laju_keluar_tenaga_kerja_pariwisata": 1,
            },
        }
    },
)
def tenaga_kerja_pariwisata():
    return _integ_tenaga_kerja_pariwisata()


_integ_tenaga_kerja_pariwisata = Integ(
    lambda: laju_penyerapan_tenaga_kerja_pariwisata()
    - laju_keluar_tenaga_kerja_pariwisata(),
    lambda: 263878,
    "_integ_tenaga_kerja_pariwisata",
)


@component.add(
    name="Laju Keluar Dasar Tenaga Kerja",
    units="1/Tahun",
    limits=(0.0, 0.2),
    comp_type="Constant",
    comp_subtype="Normal",
)
def laju_keluar_dasar_tenaga_kerja():
    """
    Laju keluar = 1 ÷ rata-rata masa kerja (±34 tahun; Sterman, 2000; PP 45/2015). Batas bawah, hanya mencakup pensiun. Diuji sensitivitas 0,05 dan 0,10.
    """
    return 0.03


@component.add(
    name="Rasio Nilai Tambah Pariwisata",
    units="Dmnl",
    comp_type="Constant",
    comp_subtype="Normal",
)
def rasio_nilai_tambah_pariwisata():
    return 0.153094


@component.add(
    name="TPK Ambang",
    units="Dmnl",
    limits=(0.0, 0.5),
    comp_type="Constant",
    comp_subtype="Normal",
)
def tpk_ambang():
    """
    TPK minimum agar konstruksi akomodasi baru terjadi (konsep tingkat hunian alamiah; Wheaton & Rossoff, 1998). Diapit data DIY: konstruksi masih positif pada TPK 2020 (0,289) dan terhenti pada TPK 2021 (0,275); korelasi tertinggi pada uji kecocokan 2016–2025. Diuji sensitivitas 0,20–0,35.
    """
    return 0.275
