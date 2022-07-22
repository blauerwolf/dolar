#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------
# dolar.py
# autor: Ernesto Ardenghi
# -------------------------------------------------------------------
# Obtiene el valor del dolar desde dolarhoy.net
# -------------------------------------------------------------------


from bs4 import BeautifulSoup
import requests
import re
import sys


# Funcion para la consulta al valor de toner de la pagina web de la impresora
def dolar_status(protocolo, url):
    
    # Utilizo las utilidades de parseo de html
    
    try:
        data = requests.get(protocolo + '://' + url).text
        soup = BeautifulSoup(data, "html.parser")
               
        div1 = soup.find('div', {'class': 'venta'})
        div2 = div1.findChildren('div')        
        
        y=[re.sub(r'<.+?>',r'',str(a)) for a in div2]
        return y[1]
        
    
    except requests.exceptions.RequestException as e:
        #print(e)
        # Si no está disponible la página
        return 'No disponible'

    

# Cuerpo principal de la rutina
protocolo = 'https'
url = 'www.dolarhoy.com'

CRED = '\033[41m'
CEND = '\33[1m'
SYMBOL = ''

status = dolar_status(protocolo, url)

print("\n\33[0m%s%sValor del Dolar promedio Venta:\33[0m %s%s%s\33[0m\n" % (CRED, CEND,CRED,CEND, status))


