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
from tkinter import messagebox as mb
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

    def sha224(self) -> str:
        """
        sha224(): Serve para retornar a hash sha224
        a partir dos bytes lidos do arquivo
        :return: str, hash sha224
        """
        return hashlib.sha224(self.dados).hexdigest()

    def sha256(self) -> str:
        """
        sha256(): Serve para retornar a hash sha256
        a partir dos bytes lidos do arquivo
        :return: str, hash sha256
        """
        return hashlib.sha256(self.dados).hexdigest()

    def sha384(self) -> str:
        """
        sha384(): Serve para retornar a hash sha384
        a partir dos bytes lidos do arquivo
        :return: str, hash sha384
        """
        return hashlib.sha384(self.dados).hexdigest()

    def sha512(self) -> str:
        """
        sha512(): Serve para retornar a hash sha512
        a partir dos bytes lidos do arquivo
        :return: str, hash sha512
        """
        return hashlib.sha512(self.dados).hexdigest()

    def sha3_224(self) -> str:
        """
        sha3_224(): Serve para retornar a hash sha3-224
        a partir dos bytes lidos do arquivo
        :return: str, hash sha3-224
        """
        return hashlib.sha3_224(self.dados).hexdigest()

    def sha3_256(self) -> str:
        """
        sha3_256(): Serve para retornar a hash sha3-256
        a partir dos bytes lidos do arquivo
        :return: str, hash sha3-256
        """
        return hashlib.sha3_256(self.dados).hexdigest()

    def sha3_384(self) -> str:
        """
        sha3_384(): Serve para retornar a hash sha3-384
        a partir dos bytes lidos do arquivo
        :return: str, hash sha3-384
        """
        return hashlib.sha3_384(self.dados).hexdigest()

    def sha3_512(self) -> str:
        """
        sha3_512(): Serve para retornar a hash sha3-512
        a partir dos bytes lidos do arquivo
        :return: str, hash sha3-512
        """
        return hashlib.sha3_512(self.dados).hexdigest()

    def blake2b(self) -> str:
        """
        blake2b(): Serve para retornar a hash blake2b
        a partir dos bytes lidos do arquivo
        :return: str, hash blake2b
        """
        return hashlib.blake2b(self.dados).hexdigest()

    def blake2s(self) -> str:
        """
        blake2s(): Serve para retornar a hash blake2s
        a partir dos bytes lidos do arquivo
        :return: str, hash blake2s
        """
        return hashlib.blake2s(self.dados).hexdigest()


class Aplicacao:
    """
    class Aplicacao: Serve para criar a tela principal do programa
    onde vai ocorrer as chamadas das funcoes
    """
    def __init__(self):
        # --------------------------------------------------------------------------------------------------------------
        # definicoes da janela principal
        self.popup = None
        self.janela = tk.Tk()
        self.janela.iconbitmap('img/icone_easyhash_tela.ico')
        self.janela.title('EasyHash v0.1')
        self.janela.geometry('550x140+600+400')
        self.janela.resizable(False, False)

        # --------------------------------------------------------------------------------------------------------------
        # ComboBox

        self.selected_option = tk.StringVar()
        self.hash_seletion = ttk.Combobox(self.janela,
                                          height=6,
                                          width=10,
                                          cursor='hand2',
                                          textvariable=self.selected_option,
                                          state='readonly')
        self.hash_seletion.set('MD5')
        self.hash_seletion['values'] = ('MD5',
                                        'SHA-1',
                                        'BLAKE2B',
                                        'BLAKE2S',
                                        'SHA-224',
                                        'SHA-256',
                                        'SHA-384',
                                        'SHA-512',
                                        'SHA3-224',
                                        'SHA3-256',
                                        'SHA3-384',
                                        'SHA3-512')
        self.hash_seletion.grid(row=0, column=0)
        # --------------------------------------------------------------------------------------------------------------
        # Botoes

        icone_pasta = tk.PhotoImage(file='img/icone_pasta.png')
        self.bt_abrir_arquivo = tk.Button(self.janela,
                                          borderwidth=0,
                                          image=icone_pasta,
                                          cursor='hand2',
                                          command=self.botao_arquivo)
        self.bt_abrir_arquivo.grid(row=0, column=1, padx=15)

        icone_ajuda = tk.PhotoImage(file='img/icone_ajuda.png')
        self.bt_ajuda = tk.Button(command=self.ajuda,
                                  image=icone_ajuda,
                                  cursor='hand2',
                                  borderwidth=0)
        self.bt_ajuda.grid(row=0, column=2)

        icone_info = tk.PhotoImage(file='img/icone_info.png')
        self.bt_info = tk.Button(command=self.info,
                                 image=icone_info,
                                 cursor='hand2',
                                 borderwidth=0)
        self.bt_info.grid(row=0, column=3, padx=15)

        icone_salvar = tk.PhotoImage(file='img/icone_salvar.png')
        self.bt_salvar = tk.Button(command=self.salvar_hash,
                                   image=icone_salvar,
                                   borderwidth=0,
                                   state='disable')
        self.bt_salvar.place(x=5, y=110)

        icone_copiar = tk.PhotoImage(file='img/icone_copiar.png')
        self.bt_copiar = tk.Button(command=self.copiar,
                                   image=icone_copiar,
                                   borderwidth=0,
                                   state='disable')
        self.bt_copiar.place(x=85, y=110)

        # --------------------------------------------------------------------------------------------------------------
        # Labels

        icone_easyhash = tk.PhotoImage(file='img/icone_easyhash.png')
        self.lblogo = tk.Label(image=icone_easyhash)
        self.lblogo.grid(row=0, column=4, padx=20)

        self.lbinfo = tk.Label(text='Aguardando seleção de arquivo...')
        self.lbinfo.place(x=0, y=50)

        self.lbcopy = tk.Label(text='EasyHash, Copyright © 2020 Wesley Ribeiro Dias, Pedro H. N. Bernardes')
        self.lbcopy.place(x=165, y=120)

        # --------------------------------------------------------------------------------------------------------------
        # Text/Entry

        self.hash_final = tk.Text(self.janela, state='disable', height=2, width=68)
        self.hash_final.place(x=0, y=70)

        # --------------------------------------------------------------------------------------------------------------
        # Fim
        self.janela.mainloop()

    def botao_arquivo(self) -> None:
        """
        botao_arquivo(): Serve para ler um arquivo do computador
        e a partir deste arquivo gerar a hash, e habilitar o botao salvar
        :return: None
        """
        tipo_hash = self.hash_seletion.get()
        arquivo = askopenfilename()
        if arquivo != '':
            self.lbinfo['text'] = f'Hash: {tipo_hash} | Arquivo: {arquivo}'
            arquivo = Criptografia(arquivo)
            if tipo_hash == 'MD5':
                arquivo = arquivo.md5()
            elif tipo_hash == 'SHA-1':
                arquivo = arquivo.sha1()
            elif tipo_hash == 'BLAKE2B':
                arquivo = arquivo.blake2b()
            elif tipo_hash == 'BLAKE2S':
                arquivo = arquivo.blake2s()
            elif tipo_hash == 'SHA-224':
                arquivo = arquivo.sha224()
            elif tipo_hash == 'SHA-256':
                arquivo = arquivo.sha256()
            elif tipo_hash == 'SHA-384':
                arquivo = arquivo.sha384()
            elif tipo_hash == 'SHA-512':
                arquivo = arquivo.sha512()
            elif tipo_hash == 'SHA3-224':
                arquivo = arquivo.sha3_224()
            elif tipo_hash == 'SHA3-256':
                arquivo = arquivo.sha3_256()
            elif tipo_hash == 'SHA3-384':
                arquivo = arquivo.sha3_384()
            elif tipo_hash == 'SHA3-512':
                arquivo = arquivo.sha3_512()
            self.hash_final['state'] = 'normal'
            self.hash_final.delete(0.0, tk.END)
            self.hash_final.insert(0.0, arquivo)
            self.hash_final['state'] = 'disable'
            self.bt_salvar['state'] = 'normal'
            self.bt_salvar['cursor'] = 'hand2'
            self.bt_copiar['state'] = 'normal'
            self.bt_copiar['cursor'] = 'hand2'

    @staticmethod
    def ajuda() -> None:
        """
        ajuda(): Serve para retornar uma tela popup com informacoes de ajuda
        :return: None
        """
        mb.showinfo('Ajuda',
                    '                                    EasyHash Ajuda                              '
                    '------------------------------------------------------------------------------\n'
                    'Como obter hash:\n'
                    'Para obter a hash basta apenas selecionar o tipo de função hash desejada '
                    'e clicar no botão "selecionar arquivo"\n'
                    'Obs.: Por padrão a função hash selecionada é a MD5\n'
                    '------------------------------------------------------------------------------\n'
                    'Para salvar a hash: clique no botão "salvar"\n'
                    '------------------------------------------------------------------------------\n'
                    'para copiar a hash: clique no botão "copiar"\n'
                    '------------------------------------------------------------------------------\n'
                    'Para mais informações: clique no botão "info"\n'
                    '------------------------------------------------------------------------------')

    @staticmethod
    def info() -> None:
        """
        ajuda(): Serve para retornar uma tela popup com informacoes do EasyHash
        :return: None
        """
        mb.showinfo('Info',
                    '                                   EasyHash Info                                '
                    '------------------------------------------------------------------------------\n'
                    'EasyHash é um programa feito para obter hash de arquivos de forma simples '
                    'bastando apenas alguns cliques para realizar tal operação e open source '
                    'sob a MIT License\n'
                    'Desenvolvido utilizando a linguagem Python\n\n'
                    'Desenvolvedores: Wesley Ribeiro Dias, Pedro H. N. Bernardes\n'
                    'Github: @WeDias, @pedrohnb\n'
                    'Codigo fonte: https://github.com/WeDias/EasyHash\n'
                    '------------------------------------------------------------------------------')

    def salvar_hash(self) -> None:
        """
        salvar_hash(): Serve para salvar a hash gerada em um arquivo de texto
        :return: None
        """
        arquivo = asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if arquivo != '':
            with open(f'{arquivo}.txt', 'w+') as arq:
                arq.write(self.hash_final.get(0.0, tk.END))
                mb.showinfo('Salvar', 'Salvo com sucesso !')

    def copiar(self) -> None:
        """
        copiar(): Serve para copiar a hash
        :return: None
        """
        self.janela.clipboard_clear()
        self.janela.clipboard_append(self.hash_final.get(0.0, tk.END))
        mb.showinfo('Copiar', 'Copiado com sucesso !')


if __name__ == '__main__':
    for hash_ in hashlib.algorithms_available:
        print(hash_)
    run = Aplicacao()
