import pandas as pd
import numpy as np 
from sklearn.cluster import KMeans
from apps.home.models import *

def pembeli_prioritas ():
    get_Pembeli_Prioritas = conn.execute("SELECT * FROM Data_Profil_Pakan")
    df_Pembeli_Prioritas = pd.DataFrame(get_Pembeli_Prioritas)
   
    return  print(df_Pembeli_Prioritas)