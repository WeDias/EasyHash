#!/usr/bin/env python
# -*- coding: utf-8 -*-

# easyhash.py
# GitHub: @WeDias
# GitHub: @pedrohnb

#  MIT License
#
#  Copyright (c) 2020 Wesley Ribeiro Dias, Pedro H. N. Bernardes
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Criptografia:
    """
    class Criptografia: Serve para gerar as hashs md5, sha1, sha256
    que serao utilizadas pela class Aplicacao
    """
    def __init__(self, arquivo: str) -> None:
        """
        :param arquivo: str, local do arquivo que sera lido
        """
        with open(arquivo, 'rb') as arq:
            self.dados = arq.read()

    def md5(self) -> str:
        """
        md5(): Serve para retornar a hash md5
        a partir dos bytes lidos do arquivo
        :return: str, hash md5
        """
        return hashlib.md5(self.dados).hexdigest()

    def sha1(self) -> str:
        """
        sha1(): Serve para retornar a hash sha1
        a partir dos bytes lidos do arquivo
        :return: str, hash sha1
        """
        return hashlib.sha1(self.dados).hexdigest()

    def sha256(self) -> str:
        """
        sha256(): Serve para retornar a hash sha256
        a partir dos bytes lidos do arquivo
        :return: str, hash sha256
        """
        return hashlib.sha256(self.dados).hexdigest()


class Aplicacao:
    """
    class Aplicacao: Serve para criar a tela principal do programa
    onde vai as chamadas das funcoes
    """
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.iconbitmap('img/logo.ico')
        self.janela.title('EasyHash v0.1')
        self.janela.geometry("517x120+600+400")
        self.janela.resizable(False, False)

        self.logo = tk.PhotoImage(file='img/hash_icon.png')
        self.lblogo = tk.Label(image=self.logo)
        self.lblogo.grid(row=0, column=4, padx=165)

        self.selected_option = tk.StringVar()
        self.hash_seletion = ttk.Combobox(self.janela,
                                          width=10,
                                          cursor='hand2',
                                          textvariable=self.selected_option,
                                          state='readonly')

        self.hash_seletion.set('MD5')
        self.hash_seletion["values"] = ("MD5", "SHA-1", "SHA-256")
        self.hash_seletion.grid(row=0, column=0)

        self.icone_botao_arquivo = tk.PhotoImage(file='img/Icone_Pasta.png')
        self.botao_abrir_arquivo = tk.Button(self.janela,
                                             borderwidth=0,
                                             image=self.icone_botao_arquivo,
                                             cursor='hand2',
                                             command=self.botao_arquivo)

        self.botao_abrir_arquivo.grid(row=0, column=1, padx=10)

        self.lb1 = tk.Label()
        self.lb1.place(x=0, y=40)

        self.lbcopy = tk.Label(text='EasyHash, Copyright © 2020 Wesley Ribeiro Dias, Pedro H. N. Bernardes')
        self.lbcopy.place(x=130, y=100)

        self.salvar_imagem = tk.PhotoImage(file='img/salvar_icone.png')
        self.bt_salvar = tk.Button(command=self.salvar_hash,
                                   image=self.salvar_imagem,
                                   borderwidth=0,
                                   state='disable')

        self.bt_salvar.place(x=0, y=90)

        self.hash_final = tk.Text(self.janela, state='disable', height=1, width=64)
        self.hash_final.place(x=0, y=65)
        self.janela.mainloop()

    def botao_arquivo(self) -> None:
        """
        botao_arquivo(): Serve para ler um arquivo do computador
        e a partir deste arquivo gerar a hash, e habilitar o botao salvar
        :return: None
        """
        hash_final_texto = ''
        tipo_hash = self.hash_seletion.get()
        arquivo = askopenfilename()
        if arquivo != '':
            self.bt_salvar['state'] = 'normal'
            self.bt_salvar['cursor'] = 'hand2'
            self.lb1['text'] = f'Hash: {tipo_hash} | Arquivo: {arquivo}'
            if tipo_hash == 'MD5':
                hash_final_texto = Criptografia(arquivo).md5()
            elif tipo_hash == 'SHA-1':
                hash_final_texto = Criptografia(arquivo).sha1()
            elif tipo_hash == 'SHA-256':
                hash_final_texto = Criptografia(arquivo).sha256()
            self.hash_final['state'] = 'normal'
            self.hash_final.delete(0.0, tk.END)
            self.hash_final.insert(0.0, hash_final_texto)
            self.hash_final['state'] = 'disable'

    def salvar_hash(self) -> None:
        """
        salvar_hash(): Serve para salvar a hash gerada em um arquivo de texto
        :return: None
        """
        with open(f'{asksaveasfilename(filetypes=[("Text files", "*.txt")])}.txt', 'w') as arq:
            arq.write(self.hash_final.get(0.0, tk.END))


if __name__ == '__main__':
    run = Aplicacao()
