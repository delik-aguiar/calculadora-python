import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacao = operacao_selecionada.get()
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não permitida!")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Erro", "Operação inválida!")
            return
        
        resultado_var.set(f"Resultado: {resultado}")
        log_operacoes(num1, num2, operacao, resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

def log_operacoes(num1, num2, operacao, resultado):
    with open("log_calculadora.txt", "a") as log:
        log.write(f"{num1} {operacao} {num2} = {resultado}\n")

def limpar():
    entrada_num1.delete(0, tk.END)
    entrada_num2.delete(0, tk.END)
    resultado_var.set("Resultado: ")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Tkinter")
janela.geometry("350x300")
janela.resizable(False, False)
janela.configure(bg="#f0f0f0")

# Criando os widgets
frame = ttk.Frame(janela, padding=10)
frame.pack(expand=True)

ttk.Label(frame, text="Número 1:", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=5)
entrada_num1 = ttk.Entry(frame, font=("Arial", 12))
entrada_num1.grid(row=0, column=1, pady=5, padx=5)

ttk.Label(frame, text="Operação:", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=5)
operacao_selecionada = tk.StringVar(value="+")
operacoes = ttk.Combobox(frame, textvariable=operacao_selecionada, values=["+", "-", "*", "/"], font=("Arial", 12))
operacoes.grid(row=1, column=1, pady=5, padx=5)

ttk.Label(frame, text="Número 2:", font=("Arial", 12)).grid(row=2, column=0, pady=5, padx=5)
entrada_num2 = ttk.Entry(frame, font=("Arial", 12))
entrada_num2.grid(row=2, column=1, pady=5, padx=5)

botao_calcular = ttk.Button(frame, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

botao_limpar = ttk.Button(frame, text="Limpar", command=limpar)
botao_limpar.grid(row=4, column=0, columnspan=2, pady=5)

resultado_var = tk.StringVar(value="Resultado: ")
resultado_label = ttk.Label(frame, textvariable=resultado_var, font=("Arial", 14, "bold"), foreground="#007acc")
resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

janela.mainloop()