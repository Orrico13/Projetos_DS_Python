import os
import datetime
import pandas as pd

class Decodificador_Morse:
    def __init__(self,msg,path,dict_m):
        self.msg = msg
        self.path = path
        self.dict_m = dict_m

    def __str__(self): 
        return 'A mensagem a ser decodificada é ' + self.msg

    def decod_palavras(self):
        msg_completa = self.msg
        msg_sep = msg_completa.split("  ")
        return msg_sep

    def decod_mensagem(self):
        # Função que decodifica uma mensagem em morse
        palavras = self.decod_palavras()
        msg_claro = []
        for i in range(len(palavras)):    
            msg_palav = palavras[i].split(" ")
            for letter in msg_palav :
                msg_claro.append(self.dict_m[letter])
            msg_claro.append(' ')
        # return ''.join(msg_claro).rstrip()
        return ''.join(str(v) for v in msg_claro).rstrip()

    def decodificar_e_salvar(self):
        now = datetime.datetime.now()
        msg_final = self.decod_mensagem() 
        df = pd.DataFrame([[msg_final, now]], columns=["mensagem", "datetime"])
        if not os.path.exists(self.path):
            hdr = True
        else:
            hdr = False
        #hdr = not os.path.exists(file_path)
        df.to_csv(self.path, mode='a', index=False, header=hdr)


if __name__ == "__main__":
    msg = input('Escreva a mensagem a ser decodificada: ') 
    file_path = input('Escreva o nome do arquivo a ser salvo (extensão .csv): ')
    dict_morse = pd.read_excel('../Docs/Dicionario_morse.xlsx',dtype={'LETRA_NUM':str})
    dict_morse = dict_morse.set_index('CODIGO_MORSE').T.to_dict('list')
    dict_morse = {chave: valor[0] for chave, valor in dict_morse.items()}
    Decoder = Decodificador_Morse(msg,file_path,dict_morse)
    print(Decoder)
    Decoder.decodificar_e_salvar()
