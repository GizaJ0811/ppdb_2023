import requests
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

jalur = "prestasi-rapor"
r = requests.get(f"https://api-v2.ppdb.jabarprov.go.id/portal/registrant?page=1&limit=10&pagination=false&columns[0][key]=name&columns[0][searchable]=true&columns[1][key]=registration_number&columns[1][searchable]=true&filters[0][key]=first_school.npsn&filters[0][value]=20251792&filters[1][key]=option_type&filters[1][value]={jalur}", headers=headers)
data = r.json()

daftar_pendaftar = []
for item in data['result']['itemsList']:
    pendaftar = {
        "Nomer Pendaftar": item["registration_number"],
        "Nama": item["name"],
        "Skor": item["score"],
        "Asal Sekolah": item["school"],
    }
    daftar_pendaftar.append(pendaftar)

df = pd.DataFrame(daftar_pendaftar).sort_values("Skor", ascending=False)
df.to_excel('daftar.xlsx', index=False)