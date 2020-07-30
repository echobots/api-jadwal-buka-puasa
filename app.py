import requests, datetime

# kota = input("masukkan nama kota:")
kota = 'KOTA MEDAN'

def data(city_id, city_name):
    tanggal = datetime.datetime.today().strftime('%Y-%m-%d')
    get_jadwal_sholat = requests.get(f"https://api.banghasan.com/sholat/format/json/jadwal/kota/{ city_id }/tanggal/{ tanggal }")
    jadwal_sholat_result = get_jadwal_sholat.json()
    maghrib = jadwal_sholat_result['jadwal']['data']['maghrib']
    waktu = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Kota : { city_name }\nMaghrib : { maghrib }\n\nTimes : { waktu }')

get_city = requests.get("https://api.banghasan.com/sholat/format/json/kota")
city_result = get_city.json()['kota']
a = False
for item in city_result:
    if kota == item['nama']:
        a = True
        data(item['id'], item['nama'])
    else:
        pass
if a == False:    
    print('kota tidak terdaftar')