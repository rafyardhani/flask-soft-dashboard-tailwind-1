# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps.home.forms import UploadFileForm
from apps.home.parse import *
from flask_login import login_required
from jinja2 import TemplateNotFound
from flask import Flask, render_template, request, redirect, url_for,flash
import os
import numpy as np 
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from apps.home.models import *
from apps.home.clustering import * 
from os.path import join, dirname, realpath
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import calendar
from flask import jsonify
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config["DEBUG"] = True


@blueprint.route('/<template>')
@login_required
def route_template(template):

    # try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    # except TemplateNotFound:
    #     return render_template('home/page-404.html'), 404

    # except:
    #     return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


@blueprint.route('/index.html')
@login_required
def index():
# Deplesi 
    Deplesi = conn.execute("SELECT Bulan, SUM(Deplesi) AS Total_Deplesi, SUM(Selisih_Deplesi) AS Total_Selisih_Deplesi FROM (SELECT DATE_FORMAT(Tanggal_Produksi, '%Y-%m') AS Bulan, Jumlah_Ayam - COALESCE(LAG(Jumlah_Ayam) OVER (PARTITION BY DATE_FORMAT(Tanggal_Produksi, '%Y-%m') ORDER BY Tanggal_Produksi), 0) AS Deplesi, Jumlah_Ayam - COALESCE(LAG(Jumlah_Ayam) OVER (PARTITION BY DATE_FORMAT(Tanggal_Produksi, '%Y-%m') ORDER BY Tanggal_Produksi), Jumlah_Ayam) AS Selisih_Deplesi FROM Data_Produksi) AS Subquery GROUP BY Bulan ORDER BY Bulan;")
    dep = pd.DataFrame(Deplesi, columns = ['Bulan','Total_Deplesi','Total_Selisih_Deplesi'])
    V_t_deplesi = dep[['Total_Selisih_Deplesi']].min()
    V_Deplesi = abs(V_t_deplesi.iloc[0])


   #Bulan Deplesi 
    # Bulan_deplesi = conn.execute("SELECT Bulan, Deplesi FROM (SELECT DATE_FORMAT(Tanggal_Produksi, '%Y-%m') AS Bulan, Jumlah_Ayam - COALESCE(LAG(Jumlah_Ayam) OVER (ORDER BY Id_Produksi), 0) as Deplesi FROM Data_Produksi) AS DeplesiSubquery ORDER BY Deplesi ASC LIMIT 1;")
    Bulan_deplesi = conn.execute("SELECT Bulan, SUM(Deplesi) AS Total_Deplesi, SUM(Selisih_Deplesi) AS Total_Selisih_Deplesi FROM (SELECT DATE_FORMAT(Tanggal_Produksi, '%Y-%m') AS Bulan, Jumlah_Ayam - COALESCE(LAG(Jumlah_Ayam) OVER (PARTITION BY DATE_FORMAT(Tanggal_Produksi, '%Y-%m') ORDER BY Tanggal_Produksi), 0) AS Deplesi, Jumlah_Ayam - COALESCE(LAG(Jumlah_Ayam) OVER (PARTITION BY DATE_FORMAT(Tanggal_Produksi, '%Y-%m') ORDER BY Tanggal_Produksi), Jumlah_Ayam) AS Selisih_Deplesi FROM Data_Produksi) AS Subquery GROUP BY Bulan ORDER BY Bulan;")
    df = pd.DataFrame(Bulan_deplesi,columns=['Bulan','Total_Deplesi','Total_Selisih_Deplesi'])

    for index, row in df.iterrows():
        bulan = row['Bulan']
        total_selisih = row['Total_Selisih_Deplesi']
    
    # Proses perhitungan minimum untuk setiap bulan
        minimum = df[df['Bulan'] <= bulan]['Total_Selisih_Deplesi'].min()
  

    V_bulan_deplesi_terendah = bulan
    year_deplesi, month_deplesi = map(int, V_bulan_deplesi_terendah.split('-'))
    month_name = calendar.month_name[month_deplesi]
    formatted_lowest_deplesi_month = f"{month_name} {year_deplesi}"

    # Periode Deplesi
    df['Bulan'] = pd.to_datetime(df['Bulan'], format='%Y/%m/%d')
    df['Year'] = df['Bulan'].dt.year
    oldest_year_dep = df['Year'].min()
    newest_year_dep = df['Year'].max()

# Keuntugan
    Keuntungan = conn.execute("SELECT A.Total_Pemasukan - B.Total_Pengeluaran AS Keuntungan FROM ( SELECT DATE_FORMAT(Tanggal_Detail_Pemasukan, '%M %Y') AS Bulan_Tahun, SUM(Nominal_Pemasukan) AS Total_Pemasukan FROM Data_Detail_Pemasukan GROUP BY YEAR(Tanggal_Detail_Pemasukan), MONTH(Tanggal_Detail_Pemasukan) ) A JOIN ( SELECT DATE_FORMAT(Tanggal_Detail_Pengeluaran, '%M %Y') AS Bulan_Tahun, SUM(Nominal_Pengeluaran) AS Total_Pengeluaran FROM Data_Detail_Pengeluaran GROUP BY YEAR(Tanggal_Detail_Pengeluaran), MONTH(Tanggal_Detail_Pengeluaran) ) B ON A.Bulan_Tahun = B.Bulan_Tahun ORDER BY A.Bulan_Tahun;")
    V_Keuntungan = pd.DataFrame(Keuntungan,columns=['Keuntungan']).min(axis=0)
    V_untung = V_Keuntungan['Keuntungan']   
    V_untung ="Rp,{:,.2f} Jt".format(V_untung/1000000)
    V_untung = V_untung.replace(',', 'X').replace('.', ',').replace('X', '.')
    
# Bulan Keuntungan
    Bulan_Keuntungan = conn.execute("SELECT KE.Bulan, KE.KE FROM (SELECT DATE_FORMAT(Data_Detail_Pemasukan.Tanggal_Detail_Pemasukan, '%Y-%m') AS Bulan,Data_Detail_Pemasukan.Nominal_Pemasukan - Data_Detail_Pengeluaran.Nominal_Pengeluaran AS KE FROM Data_Detail_Pemasukan INNER JOIN Data_Detail_Pengeluaran ON Data_Detail_Pemasukan.Id_Detail_Pemasukan = Data_Detail_Pengeluaran.Id_Detail_Pengeluaran GROUP BY DATE_FORMAT(Data_Detail_Pemasukan.Tanggal_Detail_Pemasukan, '%Y-%m')) AS KE ORDER BY KE.KE LIMIT 1;")
    df_bulan_Keuntungan = pd.DataFrame(Bulan_Keuntungan, columns=['Bulan','KE'])
    V_bulan_Keuntungan = df_bulan_Keuntungan['Bulan'].iloc[0]
    year_keuntungan, month_Keuntungan = map(int, V_bulan_Keuntungan.split('-'))
    month_name = calendar.month_name[month_Keuntungan]
    formatted_lowest_Keuntungan_month = f"{month_name} {year_keuntungan}"

# Periode   Keuntungan
    df_bulan_Keuntungan['Bulan'] = pd.to_datetime(df_bulan_Keuntungan['Bulan'], format='%Y/%m/%d')
    df_bulan_Keuntungan['Year'] = df_bulan_Keuntungan['Bulan'].dt.year
    oldest_year_Ke = df['Year'].min()
    newest_year_Ke = df['Year'].max()
    
    V_Pembeli_Prioritas = "34"
    V_Total_Pembeli_Prioritas = "61"
    tgl = "2021     - 2022"
    V_Pemasok_Prioritas ="27"
    V_Total_Pemasok_Prioritas ="52"
   
    V_Perkembangan_Deplesi = 7
    V_Perkembangan_Keuntungan = -25

# Pembeli Prioritas
    get_Pembeli_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pembeli")
    df_P_Pembeli= pd.DataFrame(get_Pembeli_Prioritas)
    scaler = MinMaxScaler()
    df_P_Pembeli['Total_Harga_Scaled'] = scaler.fit_transform(df_P_Pembeli[['Total_Pembelian']])
    # Jumlah cluster yang diinginkan
    num_clusters = 2

    # Membuat model K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # Melakukan klastering
    df_P_Pembeli['Cluster'] = kmeans.fit_predict(df_P_Pembeli[['Total_Harga_Scaled']])
    
    cluster_1_count_Pem = len(df_P_Pembeli[df_P_Pembeli['Cluster'] == 1])
    amount_cluster_Pem = len(df_P_Pembeli['Cluster'])
    df_P_Pembeli['Tanggal_Profil_Pembeli'] = pd.to_datetime(df_P_Pembeli['Tanggal_Profil_Pembeli'], format='%Y/%m/%d')
    df_P_Pembeli['Year'] = df_P_Pembeli['Tanggal_Profil_Pembeli'].dt.year
    oldest_year_Pem = df_P_Pembeli['Year'].min()
    newest_year_Pem = df_P_Pembeli['Year'].max()

# Pemasok Prioritas
    get_Pemasok_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pakan")
    df_P_Pemasok= pd.DataFrame(get_Pemasok_Prioritas)
    scaler = MinMaxScaler()
    df_P_Pemasok['Total_Harga_Scaled'] = scaler.fit_transform(df_P_Pemasok[['Total_Harga']])
    # Jumlah cluster yang diinginkan
    num_clusters = 2

    # Membuat model K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # Melakukan klastering
    df_P_Pemasok['Cluster'] = kmeans.fit_predict(df_P_Pemasok[['Total_Harga_Scaled']])
    # def format_currency(amount):
    #     return "Rp.{:,.2f}".format(amount)
    # df['Total_Harga_Formatted'] = df['Total_Harga'].apply(format_currency)
    # kolom_lengkap=  df[['Id_Profil_Pakan', 'Nama_Pemasok', 'Total_Harga', 'Cluster']]
    # sorted_df = kolom_lengkap.sort_values(by='Total_Harga')
    cluster_1_count_Pemasok = len(df_P_Pemasok[df_P_Pemasok['Cluster'] == 1])
    amount_cluster_Pemasok = len(df_P_Pemasok['Cluster'])
    df_P_Pemasok['Tanggal_Profil_Pakan'] = pd.to_datetime(df_P_Pemasok['Tanggal_Profil_Pakan'], format='%Y/%m/%d')
    df_P_Pemasok['Year'] = df_P_Pemasok['Tanggal_Profil_Pakan'].dt.year
    oldest_year_Pemasok = df_P_Pemasok['Year'].min()
    newest_year_Pemasok = df_P_Pemasok['Year'].max()
   


    return render_template('/home/index.html', segment= get_segment(request), Pembeli_Prioritas=V_Pembeli_Prioritas, updated=tgl, Total_Pembeli_Prioritas = V_Total_Pembeli_Prioritas,Pemasok_Prioritas=V_Pemasok_Prioritas,Total_Pemasok_Prioritas=V_Total_Pemasok_Prioritas, Deplesi=V_Deplesi, UntungRugi= V_untung,kenaikan_deplesi=V_Perkembangan_Deplesi , bulan_deplesi=formatted_lowest_deplesi_month ,bulan_utung=formatted_lowest_Keuntungan_month,Kenaikan_Keuntungan =V_Perkembangan_Keuntungan, oldest_year_dep=oldest_year_dep, newest_year_dep=newest_year_dep, oldest_year_Ke=oldest_year_Ke, newest_year_Ke=newest_year_Ke, cluster_1_count_Pem=cluster_1_count_Pem,amount_cluster_Pem=amount_cluster_Pem,oldest_year_Pem=oldest_year_Pem,newest_year_Pem=newest_year_Pem, cluster_1_count_Pemasok=cluster_1_count_Pemasok,amount_cluster_Pemasok=amount_cluster_Pemasok,newest_year_Pemasok=newest_year_Pemasok,oldest_year_Pemasok=oldest_year_Pemasok )
    # return render_template('/home/index.html', segment= get_segment(request),kenaikan_deplesi=V_Perkembangan_Deplesi,Kenaikan_Keuntungan =V_Perkembangan_Keuntungan )



@blueprint.route('test.html')
@login_required
def test():
    # get_Pembeli_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pakan")
    # df_Pembeli_Prioritas = pd.DataFrame(get_Pembeli_Prioritas)
    
    # def format_currency(amount):
    #     return "Rp.{:,.2f}".format(amount)
    # df_Pembeli_Prioritas['Total_Harga_Formatted'] = df_Pembeli_Prioritas['Total_Harga'].apply(format_currency)
    
    # # format_df_pembeli_prioritas= df_Pembeli_Prioritas[['Id_Profil_Pakan','Nama_Pemasok','Total_Harga']]
    # format_df_pembeli_prioritas = df_Pembeli_Prioritas[['Id_Profil_Pakan', 'Nama_Pemasok', 'Total_Harga_Formatted']]
    # sorted_df = format_df_pembeli_prioritas.sort_values(by='Total_Harga_Formatted')
    # hihi = "30"

    get_Pembeli_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pembeli")
    df= pd.DataFrame(get_Pembeli_Prioritas)
    scaler = MinMaxScaler()
    df['Total_Harga_Scaled'] = scaler.fit_transform(df[['Total_Pembelian']])
    # Jumlah cluster yang diinginkan
    num_clusters = 2

    # Membuat model K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # Melakukan klastering
    df['Cluster'] = kmeans.fit_predict(df[['Total_Harga_Scaled']])
    def format_currency(amount):
        return "Rp.{:,.2f}".format(amount)
    df['Total_Harga_Formatted'] = df['Total_Pembelian'].apply(format_currency)
    # df['Total_Harga_Formatted'] = df['Total_Pembelian']
    kolom_lengkap=  df[['Id_Profil_Pembeli', 'Nama_Profil_Pembeli','Kapasitas_Profil_Pembeli', 'Total_Harga_Formatted', 'Cluster']]
    sorted_df = kolom_lengkap.sort_values(by='Total_Harga_Formatted',ascending=False)
    kolom_lengkap=  df[['Id_Profil_Pembeli', 'Nama_Profil_Pembeli','Kapasitas_Profil_Pembeli', 'Total_Harga_Formatted', 'Cluster']]
    cluster_1_count = len(df[df['Cluster'] == 1])
    amount_cluster = len(df['Cluster'])
    df['Tanggal_Profil_Pembeli'] = pd.to_datetime(df['Tanggal_Profil_Pembeli'], format='%Y/%m/%d')
    df['Year'] = df['Tanggal_Profil_Pembeli'].dt.year
    oldest_year = df['Year'].min()
    newest_year = df['Year'].max()
    
    return render_template('/home/test.html', segment= get_segment(request),data= sorted_df.to_html())

@blueprint.route('/coba.html')
@login_required
def clusterring_pembeli():
    Deplesi = conn.execute("SELECT Bulan, SUM(Deplesi) AS Total_Deplesi, SUM(Selisih_Deplesi) AS Total_Selisih_Deplesi FROM (SELECT DATE_FORMAT(Tanggal_Produksi, '%Y-%m') AS Bulan, Jumlah_Ayam - COALESCE(LAG(Jumlah_Ayam) OVER (PARTITION BY DATE_FORMAT(Tanggal_Produksi, '%Y-%m') ORDER BY Tanggal_Produksi), 0) AS Deplesi, Jumlah_Ayam - COALESCE(LAG(Jumlah_Ayam) OVER (PARTITION BY DATE_FORMAT(Tanggal_Produksi, '%Y-%m') ORDER BY Tanggal_Produksi), Jumlah_Ayam) AS Selisih_Deplesi FROM Data_Produksi) AS Subquery GROUP BY Bulan ORDER BY Bulan;")
    df = pd.DataFrame(Deplesi, columns = ['Bulan','Total_Deplesi','Total_Selisih_Deplesi'])
    # V_t_deplesi = df[['Bulan','Total_Selisih_Deplesi']].min()

    for index, row in df.iterrows():
        bulan = row['Bulan']
        total_selisih = row['Total_Selisih_Deplesi']
    
    # Proses perhitungan minimum untuk setiap bulan
        minimum = df[df['Bulan'] <= bulan]['Total_Selisih_Deplesi'].min()

    # get_Pembeli_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pakan")
    # df= pd.DataFrame(get_Pembeli_Prioritas)
    # scaler = MinMaxScaler()
    # df['Total_Harga_Scaled'] = scaler.fit_transform(df[['Total_Harga']])
    # # Jumlah cluster yang diinginkan
    # num_clusters = 2

    # # Membuat model K-Means
    # kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # # Melakukan klastering
    # df['Cluster'] = kmeans.fit_predict(df[['Total_Harga_Scaled']])
    # def format_currency(amount):
    #     return "Rp.{:,.2f}".format(amount)
    # df['Total_Harga_Formatted'] = df['Total_Harga'].apply(format_currency)
    # kolom_lengkap=  df[['Id_Profil_Pakan', 'Nama_Pemasok', 'Total_Harga_Formatted', 'Cluster']]
    # sorted_df = kolom_lengkap.sort_values(by='Total_Harga_Formatted')
    # cluster_1_count = len(df[df['Cluster'] == 1])
    
    return render_template('/home/coba.html', segment= get_segment(request), data=minimum , bulan =bulan)

@blueprint.route('/produktivitas.html')
@login_required
def produk():

    # hmp 
    hmp = conn.execute("SELECT DATE_FORMAT(Tanggal_Produksi, '%Y-%m') AS Bulan, SUM(Data_Produksi.Jumlah_Butir)/ SUM(Data_Produksi.Jumlah_Ayam) as diff FROM Data_Produksi GROUP BY Bulan; ")
    df = pd.DataFrame(hmp, columns = ['Bulan','Diff']).min(axis=0)
    V_hmp = df.iloc[1]
    V_hmp = "{:2%}".format(V_hmp)
    df2 = pd.DataFrame(hmp, columns = ['Bulan','Diff']).min(axis=0)
    V_bulan_hmp = df2.iloc[0]

    #bulan HMP 
    HMP_bulan = conn.execute("SELECT HMP.Bulan,HMP.HMP FROM (SELECT DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m') AS Bulan,SUM(DP.Jumlah_Butir) / SUM(DP.Jumlah_Ayam) * 100 AS HMP FROM Data_Produksi DP   WHERE DP.Tanggal_Produksi  GROUP BY DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m')) HMP ORDER BY HMP.HMP ASC LIMIT 1;")
    df_bulan_hmp = pd.DataFrame(HMP_bulan,columns=['Bulan','FCR'])
    V_bulan_hmp = df_bulan_hmp['Bulan'].iloc[0]
    year_hmp, month_hmp = map(int, V_bulan_hmp.split('-'))
    month_name = calendar.month_name[month_hmp]
    formatted_lowest_hmp_month = f"{month_name} {year_hmp}"

    #FCR
    fcr = conn.execute("SELECT DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m') AS Bulan,SUM(DP.Jumlah_Berat_Butir) / SUM(DK.Jumlah_Pakan) AS FCR FROM Data_Produksi DP JOIN Data_Pakan DK ON DP.Tanggal_Produksi = DK.Tanggal_Pakan GROUP BY DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m');")
    df_fcr =  pd.DataFrame(fcr,columns=['Bulan','FCR']).min(axis=0)
    V_fcr =  df_fcr.iloc[1]
    V_FCR_Terendah ="{:.2f}".format(V_fcr)

    #bulan FCR 
    fcr_bulan = conn.execute("SELECT FCR.Bulan,FCR.FCR FROM (SELECT DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m') AS Bulan,SUM(DP.Jumlah_Berat_Butir) / SUM(DK.Jumlah_Pakan) * 100 AS FCR FROM Data_Produksi DP JOIN Data_Pakan DK ON DP.Tanggal_Produksi = DK.Tanggal_Pakan   GROUP BY DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m')) FCR ORDER BY FCR.FCR ASC LIMIT 1;")
    df_bulan_fcr = pd.DataFrame(fcr_bulan,columns=['Bulan','FCR'])
    V_bulan_fcr = df_bulan_fcr['Bulan'].iloc[0]
    year, month = map(int, V_bulan_fcr.split('-'))
    month_name = calendar.month_name[month]
    formatted_lowest_fcr_month = f"{month_name} {year}"
    # V_HMP_Terendah ="100.25%"
    tgl = "2021 - 2022"
    # V_bulan_hmp ="Juni"
    # V_FCR_Terendah ="1.35"
    V_Perkembangan_hmmp =-6
    # V_bulan_fcr ="Juni"
    V_Perkembangan_fcr =-9
    return render_template('/home/produktivitas.html', segment= get_segment(request),updated=tgl, HMP_terendah=V_hmp,bulan_hmp=formatted_lowest_hmp_month,kenaikan_hmp=V_Perkembangan_hmmp,fcr=V_FCR_Terendah,bulan_fcr=formatted_lowest_fcr_month ,kenaikan_fcr=V_Perkembangan_fcr)


@blueprint.route('/Pemasok_Prioritas.html')
@login_required
def Pemasok_Prioritas():
    get_Pemasok_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pakan")
    df= pd.DataFrame(get_Pemasok_Prioritas)
    scaler = MinMaxScaler()
    df['Total_Harga_Scaled'] = scaler.fit_transform(df[['Total_Harga']])
    # Jumlah cluster yang diinginkan
    num_clusters = 2

    # Membuat model K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # Melakukan klastering
    df['Cluster'] = kmeans.fit_predict(df[['Total_Harga_Scaled']])
    # def format_currency(amount):
    #     return "Rp.{:,.2f}".format(amount)
    # df['Total_Harga_Formatted'] = df['Total_Harga'].apply(format_currency)
    kolom_lengkap=  df[['Id_Profil_Pakan', 'Nama_Pemasok', 'Total_Harga', 'Cluster']]
    sorted_df = kolom_lengkap.sort_values(by='Total_Harga')
    cluster_1_count = len(df[df['Cluster'] == 1])
    amount_cluster = len(df['Cluster'])
    df['Tanggal_Profil_Pakan'] = pd.to_datetime(df['Tanggal_Profil_Pakan'], format='%Y/%m/%d')
    df['Year'] = df['Tanggal_Profil_Pakan'].dt.year
    oldest_year = df['Year'].min()
    newest_year = df['Year'].max()

    return render_template('/home/Pemasok_Prioritas.html', segment =get_segment(request), data=sorted_df, cluster_1_count=cluster_1_count, amount_cluster=amount_cluster, newest_year=newest_year,oldest_year=oldest_year)


@blueprint.route('/Pembeli_Prioritas.html')
@login_required
def Pembeli_Prioritas():
    get_Pembeli_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pembeli")
    df= pd.DataFrame(get_Pembeli_Prioritas)
    scaler = MinMaxScaler()
    df['Total_Harga_Scaled'] = scaler.fit_transform(df[['Total_Pembelian']])
    # Jumlah cluster yang diinginkan
    num_clusters = 2

    # Membuat model K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # Melakukan klastering
    df['Cluster'] = kmeans.fit_predict(df[['Total_Harga_Scaled']])
    # def format_currency(amount):
    #     return "Rp.{:,.2f}".format(amount).replace(',','.')
    # df['Total_Harga_Formatted'] = df['Total_Pembelian'].apply(format_currency)
    # df['Total_Harga_Formatted'] = df['Total_Pembelian']
    kolom_lengkap=  df[['Id_Profil_Pembeli', 'Nama_Profil_Pembeli','Kapasitas_Profil_Pembeli', 'Total_Pembelian', 'Cluster']]
    sorted_df = kolom_lengkap.sort_values(by='Total_Pembelian',ascending=False)
    # kolom_lengkap=  df[['Id_Profil_Pembeli', 'Nama_Profil_Pembeli','Kapasitas_Profil_Pembeli', 'Total_Harga_Formatted', 'Cluster']]
    cluster_1_count = len(df[df['Cluster'] == 1])
    amount_cluster = len(df['Cluster'])
    df['Tanggal_Profil_Pembeli'] = pd.to_datetime(df['Tanggal_Profil_Pembeli'], format='%Y/%m/%d')
    df['Year'] = df['Tanggal_Profil_Pembeli'].dt.year
    oldest_year = df['Year'].min()
    newest_year = df['Year'].max()
    return render_template('home/Pembeli_Prioritas.html', segment =get_segment(request),data=sorted_df, cluster_1_count=cluster_1_count, amount_cluster=amount_cluster, newest_year=newest_year,oldest_year=oldest_year)


# @blueprint.route('/api/get_fcr_data')
# # @login_required
# def get_fcr_data():
#     fcr_data = conn.execute("SELECT DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m') AS Bulan, FORMAT(SUM(DP.Jumlah_Berat_Butir) / SUM(DK.Jumlah_Pakan), 2) AS FCR FROM Data_Produksi DP JOIN Data_Pakan DK ON DP.Tanggal_Produksi = DK.Tanggal_Pakan GROUP BY DATE_FORMAT(DP.Tanggal_Produksi, '%Y-%m');")
#     fcr_data = [{'Bulan': row[0], 'FCR': row[1]} for row in fcr_data]
    
#     return jsonify(fcr_data)

# @blueprint.route('/api/get_hmp_data')
# # @login_required
# def get_hmp_data():
#     hmp_data = conn.execute("SELECT DATE_FORMAT(Tanggal_Produksi, '%Y-%m') AS Bulan,FORMAT(SUM(Data_Produksi.Jumlah_Butir)/ SUM(Data_Produksi.Jumlah_Ayam), 2) as HMP FROM Data_Produksi GROUP BY Bulan; ")
    
#     # Fetch the data from the database
#     hmp_data = [{'Bulan': row[0], 'HMP': row[1]} for row in hmp_data]
    
# #     # Format HMP values as percentages
# #     for entry in hmp_data:
# #         hmp_percentage = float(entry['HMP']) * 100
# #         entry['HMP'] = f'{hmp_percentage:.2f}%'
    
#     return jsonify(hmp_data)

@blueprint.route('/keuangan.html')
@login_required
def keuangan():
    V_keuntungan_Terendah ="Rp.31.750.230"
    tgl = "2021 - 2022"
    V_bulan_keuntungan ="Juni"
    # V_Total_Keuntungan ="Rp.105.500.300"
    V_Perkembangan_keuntungan =-9
    V_bulan_total_Keuntungan ="Juni"

#  Keuntungan Perbulan 
    # Keuntungan = conn.execute("SELECT  Data_Detail_Pemasukan.Nominal_Pemasukan - Data_Detail_Pengeluaran.Nominal_Pengeluaran  AS Keuntungan FROM Data_Detail_Pemasukan INNER JOIN Data_Detail_Pengeluaran ON Data_Detail_Pemasukan.Id_Detail_Pemasukan = Data_Detail_Pengeluaran.Id_Detail_Pengeluaran")
    # solusi SELECT A.Bulan_Tahun, A.Total_Pemasukan, B.Total_Pengeluaran, A.Total_Pemasukan - B.Total_Pengeluaran AS Keuntungan FROM ( SELECT DATE_FORMAT(Tanggal_Detail_Pemasukan, '%M %Y') AS Bulan_Tahun, SUM(Nominal_Pemasukan) AS Total_Pemasukan FROM Data_Detail_Pemasukan GROUP BY YEAR(Tanggal_Detail_Pemasukan), MONTH(Tanggal_Detail_Pemasukan) ) A JOIN ( SELECT DATE_FORMAT(Tanggal_Detail_Pengeluaran, '%M %Y') AS Bulan_Tahun, SUM(Nominal_Pengeluaran) AS Total_Pengeluaran FROM Data_Detail_Pengeluaran GROUP BY YEAR(Tanggal_Detail_Pengeluaran), MONTH(Tanggal_Detail_Pengeluaran) ) B ON A.Bulan_Tahun = B.Bulan_Tahun ORDER BY A.Bulan_Tahun;
    # V_Keuntungan = pd.DataFrame(Keuntungan, columns=['Keuntungan'])['Keuntungan'].min()

    Keuntungan = conn.execute("SELECT A.Total_Pemasukan - B.Total_Pengeluaran AS Keuntungan FROM ( SELECT DATE_FORMAT(Tanggal_Detail_Pemasukan, '%M %Y') AS Bulan_Tahun, SUM(Nominal_Pemasukan) AS Total_Pemasukan FROM Data_Detail_Pemasukan GROUP BY YEAR(Tanggal_Detail_Pemasukan), MONTH(Tanggal_Detail_Pemasukan) ) A JOIN ( SELECT DATE_FORMAT(Tanggal_Detail_Pengeluaran, '%M %Y') AS Bulan_Tahun, SUM(Nominal_Pengeluaran) AS Total_Pengeluaran FROM Data_Detail_Pengeluaran GROUP BY YEAR(Tanggal_Detail_Pengeluaran), MONTH(Tanggal_Detail_Pengeluaran) ) B ON A.Bulan_Tahun = B.Bulan_Tahun ORDER BY A.Bulan_Tahun;")
    V_Keuntungan = pd.DataFrame(Keuntungan,columns=['Keuntungan']).min(axis=0)
    formatted_keuntungan_Terendah = "Rp,{:,}".format(V_Keuntungan.item())
    formatted_keuntungan_Terendah = formatted_keuntungan_Terendah.replace(',', 'X').replace('.', ',').replace('X', '.')

#  Bulan Keuntungan
    Bulan_Keuntungan = conn.execute("SELECT KE.Bulan, KE.KE FROM (SELECT DATE_FORMAT(Data_Detail_Pemasukan.Tanggal_Detail_Pemasukan, '%Y-%m') AS Bulan,Data_Detail_Pemasukan.Nominal_Pemasukan - Data_Detail_Pengeluaran.Nominal_Pengeluaran AS KE FROM Data_Detail_Pemasukan INNER JOIN Data_Detail_Pengeluaran ON Data_Detail_Pemasukan.Id_Detail_Pemasukan = Data_Detail_Pengeluaran.Id_Detail_Pengeluaran GROUP BY DATE_FORMAT(Data_Detail_Pemasukan.Tanggal_Detail_Pemasukan, '%Y-%m')) AS KE ORDER BY KE.KE LIMIT 1;")
    df_bulan_Keuntungan = pd.DataFrame(Bulan_Keuntungan, columns=['Bulan','KE'])
    V_bulan_Keuntungan = df_bulan_Keuntungan['Bulan'].iloc[0]
    year_keuntungan, month_Keuntungan = map(int, V_bulan_Keuntungan.split('-'))
    month_name = calendar.month_name[month_Keuntungan]
    formatted_lowest_Keuntungan_month = f"{month_name} {year_keuntungan}" 
   
# total keuntungan
    Keuntungan = conn.execute("SELECT  DATE_FORMAT(Data_Detail_Pemasukan.Tanggal_Detail_Pemasukan, '%Y-%m') AS Bulan,Data_Detail_Pemasukan.Nominal_Pemasukan - Data_Detail_Pengeluaran.Nominal_Pengeluaran  AS Keuntungan FROM Data_Detail_Pemasukan INNER JOIN Data_Detail_Pengeluaran ON Data_Detail_Pemasukan.Id_Detail_Pemasukan = Data_Detail_Pengeluaran.Id_Detail_Pengeluaran")
    T_Keuntungan = pd.DataFrame(Keuntungan,columns=['bulan','Keuntungan'])
    keuntungan_Rugi = T_Keuntungan.loc[:,'Keuntungan'].sum()
    formatted_keuntungan = "Rp,{:,} ".format(keuntungan_Rugi)
    formatted_keuntungan = formatted_keuntungan.replace(',', 'X').replace('.', ',').replace('X', '.')
    return render_template('/home/keuangan.html', segment= get_segment(request),updated=tgl, keuntungan_terendah=formatted_keuntungan_Terendah,bulan_keuntungan=formatted_lowest_Keuntungan_month,kenaikan_keuntungan=V_Perkembangan_keuntungan,Total_Keuntungan=formatted_keuntungan,bulan_total_Keuntungan=V_bulan_total_Keuntungan)


# app = Flask(__name__)
# @app.route('/', methods = ['POST','GET'])
# def success():
# 	if request.method == 'POST':
# 		f = request.files['file']
# 		f.save(f.filename)
# 		return render_template("Acknowledgement.html", name = f.filename)

# app = Flask(__name__)

# # Upload folder
# UPLOAD_FOLDER = 'static/files'
# app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
# @app.route('/profile')
# def profile():
#     return render_template('home/profile.html', segment='profile')

# # Get the uploaded files
# @app.route("/upload", methods=['GET', 'POST'])
# def upload():
#       return request.form
#       # get the uploaded file
#       uploaded_file = request.files['file'];
#       if uploaded_file.filename != '':
#            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
#           # set the file path
#            uploaded_file.save(file_path)
#           # save the file
#         # return render_template("Acknowledgment.html", name= uploaded_file.save)
#       return redirect(url_for('upload'))

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@blueprint.route('/upload', methods=['GET',"POST"])
def upload():
    # form = UploadFileForm(request.form)
    # if form.validate_on_submit():
    #     file = form.file.data # First grab the file
    #     return "File has been uploaded."
    if (request.method == 'POST' ):
        path = os.getcwd()
        file = request.files['file']
        
        # typeRequest = reqest['jenis_data']

        if file:
            # return print(file, 'ANJAY')
            # return print(file.filename, 'ANJAY')
            os.makedirs(os.path.join(app.instance_path, 'files'), exist_ok=True)
            file.save(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            # print(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            # print("masuk")
            parseCSVDPemasukan(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            parseCSVDPengeluaran(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            parseCSVPakan(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            parseCSVPenjualan(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            parseCSVProduksi(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            parseCSVPPakan(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
            parseCSVPPembeli(os.path.join(app.instance_path, 'files/', secure_filename(file.filename)))
           
            return render_template('/home/profile.html', segment=get_segment(request))
    

    if (request.method == 'GET'):
        return render_template('/templates/home/profile.html')
