#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests
import argparse
import csv
from datetime import datetime
from bs4 import BeautifulSoup


# In[12]:



# Función para obtener la lista de indices del Ibex 35 de la bolsa de Barcelona
# Tendremos una tabla donde la primera fila el nombre de la empresa y los índices
# El resto de filas contendrá los valores; el valor del primer elemento será una tupla
def getIndexs(UrlBase,UrlRef):
    indexList = []
    UrlIndexPage = UrlBase+UrlRef
    # Data for post form
    data = {'punto':'indice'}    
    page = requests.post(UrlIndexPage)
    #page = requests.get(UrlIndexPage).text 
    soup = BeautifulSoup(page.text, "html.parser")
    tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})           
    # Extraigo los valores de la tabla y sus enlaces
    rowList = []
    for tr in tabla.find_all("tr"):
        cells = tr.findAll('td')        
        colList = []
        for cell in cells:        
            href = ''            
            a= cell.find('a')              
            if (a is not None):                 
                href = a.get('href')                                
                # Append / if needed
                if href[0] !='/':
                    href = '/' + href                                     
            value = [cell.text.strip(),href]                  
            colList.append(value)                                           
        # Append to rowlist    
        rowList.append(colList)           
    return rowList 
    


# In[13]:


# indicar la ruta
urlbase = 'https://www.borsabcn.es'
urlRef= '/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice'
indexList = getIndexs(urlbase,urlRef);
print(indexList)


# In[ ]:





# In[ ]:




