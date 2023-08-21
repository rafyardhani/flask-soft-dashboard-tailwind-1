from apps.home.models import *
import pandas as pd

def deplesi():
    Deplesi = conn.execute("SELECT DATE_FORMAT(Tanggal_Produksi, '%Y-%m') AS Bulan, Jumlah_Ayam FROM Data_Produksi GROUP BY Bulan")
    V_Deplesi = pd.DataFrame(Deplesi, columns = ['Bulans', 'Jumlah_Ayam'])
    V_Deplesi.diff
    print(V_Deplesi)

def hello():
    print("mamama")