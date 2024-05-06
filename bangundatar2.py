# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:58:22 2024

@author: ocanh
"""

from bangundatar import Persegi, Lingkaran, Segitiga, PersegiPanjang, Trapesium

persegi = Persegi(4)
lingkaran = Lingkaran(7)
segitiga = Segitiga(6, 4)
persegi_panjang = PersegiPanjang(8, 3)
trapesium = Trapesium(6, 8, 5)

print("Luas Persegi:", persegi.hitung_luas())
print("Luas Lingkaran:", lingkaran.hitung_luas())
print("Luas Segitiga:", segitiga.hitung_luas())
print("Luas Persegi Panjang:", persegi_panjang.hitung_luas())
print("Luas Trapesium:", trapesium.hitung_luas())
