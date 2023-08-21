import pandas as pd
import numpy as np
from apps.home.models import *
def parseCSVPenjualan(filePath):
      # CVS Column Names
      colnames = ['Id_Penjualan','Tanggal_Penjualan','Nama_Pembeli','Harga_Jual','Kapasitas', 'Total_Penjualan']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,sep=";", usecols=['Id_Penjualan','Tanggal_Penjualan','Nama_Pembeli','Harga_Jual','Kapasitas', 'Total_Penjualan'],header=0)
      # print(csvData.head(10))
      csvData.dropna(inplace= True)
      print(csvData)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            #  print(i,row['Tanggal'],row['Nama_pembeli'],row['Harga_jual'],row['Kapasitas'],row['Total_penjualan'])
            #  print(i,row['Tanggal'],row['Nama_Pembeli'])
            sql = "INSERT INTO Data_Penjualan (Id_Penjualan,Tanggal_Penjualan, Nama_Pembeli, Harga_Jual, Kapasitas, Total_Penjualan) VALUES (%s, %s, %s, %s, %s,%s)"
            #  sql = "INSERT INTO Data_Penjualan (Tanggal) VALUES (%s)"
            value = (row['Id_Penjualan'],row['Tanggal_Penjualan'],str(row['Nama_Pembeli']),row['Harga_Jual'],row['Kapasitas'],row['Total_Penjualan'])
            conn.execute(sql, value)
            # conn.execute(sql,  if_exists='append')
            # SessionLocal.comit()
            print(i,row['Id_Penjualan'],row['Tanggal_Penjualan'],row['Nama_Pembeli'],row['Harga_Jual'],row['Kapasitas'],row['Total_Penjualan'])

def parseCSVDPemasukan(filePath):
      # CVS Column Names
      colnames = ['Id_Detail_Pemasukan','Tanggal_Detail_Pemasukan','Keterangan_Pemasukan','Nominal_Pemasukan']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,sep=";", usecols=['Id_Detail_Pemasukan','Tanggal_Detail_Pemasukan','Keterangan_Pemasukan','Nominal_Pemasukan'] ,header=0)
      # csvData = pd.read_csv(filePath,sep=";" ,header=0)
      csvData.dropna(inplace= True)
      print(csvData)
      # print(csvData.head(10))

      print(csvData)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            #  print(i,row['Tanggal'],row['Nama_pembeli'],row['Harga_jual'],row['Kapasitas'],row['Total_penjualan'])
            #  print(i,row['Tanggal'],row['Nama_Pembeli'])
            sql = "INSERT INTO Data_Detail_Pemasukan (Id_Detail_Pemasukan, Tanggal_Detail_Pemasukan, Keterangan_Pemasukan , Nominal_Pemasukan) VALUES (%s, %s, %s ,%s)"
            #  sql = "INSERT INTO Data_Penjualan (Tanggal) VALUES (%s)"
            value = (row['Id_Detail_Pemasukan'],row['Tanggal_Detail_Pemasukan'],str(row['Keterangan_Pemasukan']),row['Nominal_Pemasukan'])
            conn.execute(sql, value)
            # conn.execute(sql,  if_exists='append')

            # SessionLocal.comit()
            print(i,row['Id_Detail_Pemasukan'],row['Tanggal_Detail_Pemasukan'],str(row['Keterangan_Pemasukan']),row['Nominal_Pemasukan'])

def parseCSVDPengeluaran(filePath):
      # CVS Column Names
      colnames = ['Id_Detail_Pengeluaran','Tanggal_Detail_Pengeluaran','Keterangan_Pengeluaran','Nominal_Pengeluaran']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,sep=";",usecols=['Id_Detail_Pengeluaran','Tanggal_Detail_Pengeluaran','Keterangan_Pengeluaran','Nominal_Pengeluaran'] ,header=0)
      # print(csvData.head(10))
      csvData.dropna(inplace= True)
      print(csvData)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            #  print(i,row['Tanggal'],row['Nama_pembeli'],row['Harga_jual'],row['Kapasitas'],row['Total_penjualan'])
            #  print(i,row['Tanggal'],row['Nama_Pembeli'])
            sql = "INSERT INTO Data_Detail_Pengeluaran (Id_Detail_Pengeluaran,Tanggal_Detail_Pengeluaran, Keterangan_Pengeluaran, Nominal_Pengeluaran) VALUES (%s, %s, %s ,%s)"
            #  sql = "INSERT INTO Data_Penjualan (Tanggal) VALUES (%s)"
            value = (row['Id_Detail_Pengeluaran'],row['Tanggal_Detail_Pengeluaran'],str(row['Keterangan_Pengeluaran']),row['Nominal_Pengeluaran'])
            conn.execute(sql, value)
            # conn.execute(sql,  if_exists='append')

            # SessionLocal.comit()
            print(i,row['Id_Detail_Pengeluaran'],row['Tanggal_Detail_Pengeluaran'],str(row['Keterangan_Pengeluaran']),row['Nominal_Pengeluaran'])


def parseCSVPakan(filePath):
      # CVS Column Names
      colnames = ['Id_Pakan','Tanggal_Pakan','Jumlah_Pakan']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,sep=";",usecols=['Id_Pakan','Tanggal_Pakan','Jumlah_Pakan'] ,header=0)
      # print(csvData.head(10))
      csvData.dropna(inplace= True)
      print(csvData)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            #  print(i,row['Tanggal'],row['Nama_pembeli'],row['Harga_jual'],row['Kapasitas'],row['Total_penjualan'])
            #  print(i,row['Tanggal'],row['Nama_Pembeli'])
            sql = "INSERT INTO Data_pakan (Id_Pakan,Tanggal_Pakan,Jumlah_Pakan) VALUES (%s, %s, %s)"
            #  sql = "INSERT INTO Data_Penjualan (Tanggal) VALUES (%s)"
            value = (row['Id_Pakan'],row['Tanggal_Pakan'],str(row['Jumlah_Pakan']))
            conn.execute(sql, value)
            # conn.execute(sql,  if_exists='append')
            # SessionLocal.comit()
            print(i,row['Id_Pakan'],row['Tanggal_Pakan'],str(row['Jumlah_Pakan']))



def parseCSVProduksi(filePath):
      # CVS Column Names
      colnames = ['Id_Produksi','Tanggal_Produksi','Jumlah_Butir','Jumlah_Berat_Butir','Jumlah_Ayam']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,sep=";",usecols=['Id_Produksi','Tanggal_Produksi','Jumlah_Butir','Jumlah_Berat_Butir','Jumlah_Ayam'] ,header=0,decimal=',')
      # print(csvData.head(10))
      csvData.dropna(inplace= True)
      print(csvData)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            sql = "INSERT INTO Data_Produksi (Id_Produksi,Tanggal_Produksi,Jumlah_Butir,Jumlah_Berat_Butir,Jumlah_Ayam) VALUES (%s, %s, %s, %s,%s)"
            #  sql = "INSERT INTO Data_Penjualan (Tanggal) VALUES (%s)"
            value = (row['Id_Produksi'],row['Tanggal_Produksi'],row['Jumlah_Butir'],row['Jumlah_Berat_Butir'],row['Jumlah_Ayam'])
            conn.execute(sql, value)
            print(i,row['Id_Produksi'],row['Tanggal_Produksi'],row['Jumlah_Butir'],row['Jumlah_Berat_Butir'],row['Jumlah_Ayam'])


def parseCSVPPakan(filePath):
      # CVS Column Names
      colnames = ['Id_Profil_Pakan','Tanggal_Profil_Pakan','Nama_Pemasok','Harga_Satuan_Pakan_1','Jenis_Pakan_1','Harga_Satuan_Pakan_2','Jenis_Pakan_2','Harga_Satuan_Pakan_3','Jenis_Pakan_3','Harga_Satuan_Pakan_4','Jenis_Pakan_4','Total_Harga']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,sep=";",usecols=['Id_Profil_Pakan','Tanggal_Profil_Pakan','Nama_Pemasok','Harga_Satuan_Pakan_1','Jenis_Pakan_1','Harga_Satuan_Pakan_2','Jenis_Pakan_2','Harga_Satuan_Pakan_3','Jenis_Pakan_3','Harga_Satuan_Pakan_4','Jenis_Pakan_4','Total_Harga'] ,header=0,decimal=',')
      # print(csvData.head(10))
      csvData.dropna(inplace= True)
      print(csvData)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            sql = "INSERT INTO Data_Profil_Pakan (Id_Profil_Pakan,Tanggal_Profil_Pakan, Nama_Pemasok, Harga_Satuan_Pakan_1, Jenis_Pakan_1 , Harga_Satuan_Pakan_2 , Jenis_Pakan_2 , Harga_Satuan_Pakan_3 , Jenis_Pakan_3 , Harga_Satuan_Pakan_4 , Jenis_Pakan_4 , Total_Harga) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s)"
            #  sql = "INSERT INTO Data_Penjualan (Tanggal) VALUES (%s)"
            value = (row['Id_Profil_Pakan'],row['Tanggal_Profil_Pakan'],row['Nama_Pemasok'],row['Harga_Satuan_Pakan_1'],row['Jenis_Pakan_1'],row['Harga_Satuan_Pakan_2'],row['Jenis_Pakan_2'],row['Harga_Satuan_Pakan_3'],row['Jenis_Pakan_3'],row['Harga_Satuan_Pakan_4'],row['Jenis_Pakan_4'],row['Total_Harga'])
            conn.execute(sql, value)
            print(i,row['Id_Profil_Pakan'],row['Tanggal_Profil_Pakan'],row['Nama_Pemasok'],row['Harga_Satuan_Pakan_1'],row['Jenis_Pakan_1'],row['Harga_Satuan_Pakan_2'],row['Jenis_Pakan_2'],row['Harga_Satuan_Pakan_3'],row['Jenis_Pakan_3'],row['Harga_Satuan_Pakan_4'],row['Jenis_Pakan_4'],row['Total_Harga'])

def parseCSVPPembeli(filePath):
      # CVS Column Names
      colnames = ['Id_Profil_Pembeli','Nama_Profil_Pembeli','Harga_Satuan','Kapasitas_Profil_Pembeli','Total_Pembelian','Tanggal_Profil_Pembeli']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,sep=";",usecols=['Id_Profil_Pembeli','Nama_Profil_Pembeli','Harga_Satuan','Kapasitas_Profil_Pembeli','Total_Pembelian','Tanggal_Profil_Pembeli'] ,header=0,decimal=',')
      # print(csvData.head(10))
      csvData.dropna(inplace= True)
      print(csvData)
      # Loop through the Rows
      for i,row in csvData.iterrows():
            sql = "INSERT INTO Data_Profil_Pembeli (Id_Profil_Pembeli,Nama_Profil_Pembeli, Harga_Satuan, Kapasitas_Profil_Pembeli, Total_Pembelian,Tanggal_Profil_Pembeli) VALUES (%s, %s, %s, %s,%s,%s)"
            #  sql = "INSERT INTO Data_Penjualan (Tanggal) VALUES (%s)"
            value = (row['Id_Profil_Pembeli'],row['Nama_Profil_Pembeli'],row['Harga_Satuan'],row['Kapasitas_Profil_Pembeli'],row['Total_Pembelian'],row['Tanggal_Profil_Pembeli'])
            conn.execute(sql, value)
            print(i,row['Id_Profil_Pembeli'],row['Nama_Profil_Pembeli'],row['Harga_Satuan'],row['Kapasitas_Profil_Pembeli'],row['Total_Pembelian'],row['Tanggal_Profil_Pembeli'])
