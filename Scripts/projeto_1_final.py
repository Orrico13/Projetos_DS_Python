import os
import datetime
import pandas as pd

def decod_palavras(msg):
    msg_sep = msg.split("  ")
    return msg_sep

def decod_mensagem(msg,dict_m):
    # Função que decodifica uma mensagem em morse
    palavras = decod_palavras(msg=msg)
    msg_claro = []
    for i in range(len(palavras)):    
        msg_palav = palavras[i].split(" ")
        for letter in msg_palav :
            msg_claro.append(dict_m[letter])
        msg_claro.append(' ')
    # return ''.join(msg_claro).rstrip()
    return ''.join(str(v) for v in msg_claro).rstrip()

def decodificar_e_salvar(msg,file_path,dict_m):
    now = datetime.datetime.now()
    msg_final = decod_mensagem(msg=msg,
                               dict_m=dict_m) 
    df = pd.DataFrame([[msg_final, now]], columns=["mensagem", "datetime"])
    if not os.path.exists(file_path):
        hdr = True
    else:
        hdr = False
    #hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode='a', index=False, header=hdr)

if __name__ == "__main__":
    msg = input('Escreva a mensagem a ser decodificada: ') 
    file_path = input('Escreva o nome do arquivo a ser salvo (extensão .csv): ')
    dict_morse = pd.read_excel('../Docs/Dicionario_morse.xlsx',dtype={'LETRA_NUM':str})
    dict_morse = dict_morse.set_index('CODIGO_MORSE').T.to_dict('list')
    dict_morse = {chave: valor[0] for chave, valor in dict_morse.items()}
    decodificar_e_salvar(msg=msg,
                         file_path=file_path,
                         dict_m=dict_morse)