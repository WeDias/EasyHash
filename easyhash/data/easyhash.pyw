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
        self.janela.mainloop()

if __name__ == '__main__':
    run = Aplicacao()
