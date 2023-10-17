import tkinter as tk
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2

        label_resultado.config(text=f"resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Error, insira numeros validos")

janela = tk.Tk()
janela.title("Calculadora simples")

entry_num1 = tk.Entry(janela)
entry_num2 = tk.Entry(janela)

botao_calcular = tk.Button(janela, text="calcular", command=calcular)

label_resultado = tk.Label(janela, text="resultado:")

entry_num1.pack()
entry_num2.pack()
botao_calcular.pack()
label_resultado.pack()

janela.mainloop()