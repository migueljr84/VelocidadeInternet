#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from speedtest import Speedtest
import schedule
from threading import Timer
import datetime

def Velocidade():
    st = Speedtest()
    mb = 10**-6
    data_e_hora_em_texto = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

    download = (st.download()*mb)
    upload = (st.upload()*mb)
    arquivo = open('arq01.csv', 'r') # Abra o arquivo (leitura)
    conteudo = arquivo.readlines()
    conteudo.append("%.2f"%download +";" +data_e_hora_em_texto+ ";"+"D;"+ "\n")   # insira seu conteúdo
    conteudo.append("%.2f"%upload  +";" +data_e_hora_em_texto+ ";"+"U;" + "\n")   # insira seu conteúdo

    arquivo = open('arq01.csv', 'w') # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
    Timer(120, Velocidade).start()
Velocidade()