import tkinter as tk
from tkinter import messagebox

# Cores usadas no código Hex
cinza = "#444642"
dourado = "#D5CB40"

# Janela Principal
janela = tk.Tk()  # Janela principal
janela.title("Calculadora E.D")  # Título
janela.geometry("320x500")  # Dimensões (largura, altura)
janela.resizable(False, False)  # Não deixa redimensionar

# Conteiner (Frame) para o Display de resultados
frame_display = tk.Frame(janela, bg=cinza, highlightbackground="black", highlightthickness=2)
frame_display.pack(side="top", fill="x")  # Preencher na largura

# Conteiner (Frame) para os Botões
frame_botoes = tk.Frame(janela)  # Cria o frame de botões
frame_botoes.pack(side="top", fill="both", expand=True)  # Preencher todo o espaço disponível

# Display (caixa de texto)
entrada_texto = tk.StringVar()  # Guarda o texto do Display e muda o mesmo
entrada_texto.set("0")  # Define um texto inicial no display
display = tk.Entry(frame_display,textvariable=entrada_texto, width=20, font=("Arial", 40), justify="right", bg=cinza, bd=0, highlightthickness=0)  
display.pack(pady=60)  # Ajuste de posição

# Função para adicionar números ao display
def clicar(n):
    entrada_texto.set(entrada_texto.get() + str(n))

# Função para limpar o display
def limpar():
    entrada_texto.set("")

# Função para calcular o resultado
def calcular():
    try:
        # Avalia a expressão e exibe o resultado no display
        resultado = eval(entrada_texto.get())
        entrada_texto.set(resultado)
    except:
        # Em caso de erro na avaliação, exibe "Erro"
        entrada_texto.set("Erro")

# Definir o peso das linhas e colunas para que os botões se ajustem
for i in range(4):
    frame_botoes.grid_columnconfigure(i, weight=1, uniform="equal")
for i in range(4):
    frame_botoes.grid_rowconfigure(i, weight=1, uniform="equal")

# Botões
b1 = tk.Button(frame_botoes, text="1", font="Arial, 20", bg=dourado, command=lambda: clicar(1))
b1.grid(row=0, column=0, sticky="nsew")

b2 = tk.Button(frame_botoes, text="2", font="Arial, 20", bg=dourado, command=lambda: clicar(2))
b2.grid(row=0, column=1, sticky="nsew")

b3 = tk.Button(frame_botoes, text="3", font="Arial, 20", bg=dourado, command=lambda: clicar(3))
b3.grid(row=0, column=2, sticky="nsew")

b4 = tk.Button(frame_botoes, text="4", font="Arial, 20", bg=dourado, command=lambda: clicar(4))
b4.grid(row=1, column=0, sticky="nsew")

b5 = tk.Button(frame_botoes, text="5", font="Arial, 20", bg=dourado, command=lambda: clicar(5))
b5.grid(row=1, column=1, sticky="nsew")

b6 = tk.Button(frame_botoes, text="6", font="Arial, 20", bg=dourado, command=lambda: clicar(6))
b6.grid(row=1, column=2, sticky="nsew")

b7 = tk.Button(frame_botoes, text="7", font="Arial, 20", bg=dourado, command=lambda: clicar(7))
b7.grid(row=2, column=0, sticky="nsew")

b8 = tk.Button(frame_botoes, text="8", font="Arial, 20", bg=dourado, command=lambda: clicar(8))
b8.grid(row=2, column=1, sticky="nsew")

b9 = tk.Button(frame_botoes, text="9", font="Arial, 20", bg=dourado, command=lambda: clicar(9))
b9.grid(row=2, column=2, sticky="nsew")

b0 = tk.Button(frame_botoes, text="0", font="Arial, 20", bg=dourado, command=lambda: clicar(0))
b0.grid(row=3, column=1, sticky="nsew")

# Botões de operações
b_mais = tk.Button(frame_botoes, text="+", font="Arial, 20", bg=dourado, command=lambda: clicar("+"))
b_mais.grid(row=0, column=3, sticky="nsew")

b_menos = tk.Button(frame_botoes, text="-", font="Arial, 20", bg=dourado, command=lambda: clicar("-"))
b_menos.grid(row=1, column=3, sticky="nsew")

b_vezes = tk.Button(frame_botoes, text="*", font="Arial, 20", bg=dourado, command=lambda: clicar("*"))
b_vezes.grid(row=2, column=3, sticky="nsew")

b_dividir = tk.Button(frame_botoes, text="/", font="Arial, 20", bg=dourado, command=lambda: clicar("/"))
b_dividir.grid(row=3, column=3, sticky="nsew")

b_limpar = tk.Button(frame_botoes, text="C", font="Arial, 20", bg=dourado, command=limpar)
b_limpar.grid(row=3, column=0, sticky="nsew")

b_igual = tk.Button(frame_botoes, text="=", font="Arial, 20", bg=dourado, command=calcular)
b_igual.grid(row=3, column=2, sticky="nsew")

# Exibir a Janela
janela.mainloop()
