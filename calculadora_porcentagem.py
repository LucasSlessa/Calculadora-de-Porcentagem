import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import re  # Para expressões regulares

def carregar_tabela():
    # Abre um diálogo para selecionar o arquivo CSV
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if caminho_arquivo:
        try:
            # Carregar a tabela CSV
            df = pd.read_csv(caminho_arquivo, encoding='ISO-8859-1', delimiter=';', on_bad_lines='skip')

            # Função para extrair apenas números (e converter de string para float)
            def extrair_valor(valor):
                # Verifica se o valor é uma string
                if isinstance(valor, str):
                    # Remove tudo que não for dígito ou ponto
                    numeros = re.findall(r'[\d.,]+', valor)
                    if numeros:
                        try:
                            return float(numeros[0].replace(',', '.'))  # Converte a string para float
                        except ValueError:
                            return None  # Retorna None se não puder converter
                return None  # Retorna None se não encontrar números ou não for uma string

            # Aplica a função à coluna "Unnamed: 16"
            df['Unnamed: 16'] = df['Unnamed: 16'].apply(extrair_valor)

            # Somar apenas os valores numéricos, ignorando NaN
            global valor_soma
            valor_soma = df['Unnamed: 16'].sum(skipna=True)

            # Contar quantos valores foram somados
            global contagem_valores
            contagem_valores = df['Unnamed: 16'].count()  # Conta os valores não nulos

            # Atualiza os rótulos na interface
            label_soma.config(text=f"Soma das OM's: {valor_soma:.2f}")
            label_contagem.config(text=f"Quantidade de OM's: {contagem_valores}")

        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar o arquivo: {e}")

def calcular_porcentagem():
    try:
        porcentagem = float(entry_porcentagem.get())
        valor_porcentagem = (porcentagem / 100) * valor_soma
        label_resultado.config(text=f"A porcentagem de {porcentagem}% sobre a soma é: {valor_porcentagem:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para a porcentagem.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de Porcentagem")
janela.geometry("350x300")

# Botão para carregar a tabela
botao_carregar = tk.Button(janela, text="Carregar Tabela CSV", command=carregar_tabela)
botao_carregar.pack(pady=10)

# Label para exibir a soma
label_soma = tk.Label(janela, text="Soma das OM's: ")
label_soma.pack(pady=5)

# Label para exibir a contagem de valores
label_contagem = tk.Label(janela, text="Quantidade de OM's: ")
label_contagem.pack(pady=5)

# Campo para inserir a porcentagem
label_porcentagem = tk.Label(janela, text="Digite a porcentagem que deseja calcular:")
label_porcentagem.pack(pady=5)

entry_porcentagem = tk.Entry(janela)
entry_porcentagem.pack(pady=5)

# Botão para calcular a porcentagem
botao_calcular = tk.Button(janela, text="Calcular Porcentagem", command=calcular_porcentagem)
botao_calcular.pack(pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()
