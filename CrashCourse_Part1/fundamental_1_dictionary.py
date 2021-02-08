"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
jadi dalam arti umum tipe data ini sama halnya dengan kamus
misal : {key:value}
bhs. ing
son : anak
mother : ibu
"""

# contoh kode
# kamus_ind_eng={}
# kamus_ind_eng['anak'] = 'son'
# kamus_ind_eng['istri'] = 'wive'
# kamus_ind_eng['ayah'] = 'father'
# kamus_ind_eng['ibu'] = 'mother'

# kalau di singkat
kamus_ind_eng = {'anak': 'son', 'istri': 'wive', 'ayah': 'father', 'ibu': 'mother'}

print (kamus_ind_eng)
print (kamus_ind_eng['anak'])

print ('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver disekitar pemakai app')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'Irwan', 'jarak': 100, },
        {'nama': 'Eko', 'jarak': 200, },
        {'nama': 'Rendi', 'jarak': 200, },
        {'nama': 'Reza', 'jarak': 1000, }
    ]
}
print (data_dari_server_gojek)
print (f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print (f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print (f"Driver #2 {data_dari_server_gojek['driver_list'][1]}")
print (f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
