import tkinter as tk
from tkinter import messagebox

# Função para centralizar a janela na tela
def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2
    root.geometry(f"{largura}x{altura}+{x}+{y}")
    
# Função para converter HH:MM para decimal
def horario_para_decimal(horario):
    horas, minutos = map(int, horario.split(":"))
    return horas + minutos / 60

# Função para converter decimal para HH:MM
def decimal_para_horario(decimal):
    horas = int(decimal)
    minutos = int((decimal - horas) * 60)
    return f"{horas:02d}:{minutos:02d}"

def exibir_horarios(saida_normal):
    # Cria uma nova janela como pop-up
    popup = tk.Toplevel(root)
    popup.title("Horário de Saída")
    popup.configure(bg="#f0f0f0")
    
    # Tamanho e centralização da janela
    largura, altura = 600, 200
    centralizar_janela(popup, largura, altura)
    
    # Título
    titulo_label = tk.Label(
        popup, 
        text="Horário de Saída Calculado", 
        font=("Helvetica", 16, "bold"), 
        bg="#4a7a8c", 
        fg="white", 
        padx=10, 
        pady=10
    )
    titulo_label.pack(fill="x")

    # Mensagem com horário de saída
    msg = f"Horário de saída para cumprir as 8 horas e 48 minutos de trabalho: {saida_normal}"
    msg_label = tk.Label(
        popup, 
        text=msg, 
        font=("Arial", 13), 
        bg="#f0f0f0", 
        fg="#333333", 
        padx=10, 
        pady=10
    )
    msg_label.pack()

    # Botão de fechar
    btn_fechar = tk.Button(
        popup, 
        text="Fechar", 
        font=("Arial", 12), 
        command=popup.destroy,
        bg="#4a7a8c",
        fg="white",
        activebackground="black",
        activeforeground="white"
    )
    btn_fechar.pack(pady=10)

def calcula_horas():
    try:
        # Coleta e conversão de horários inseridos pelo usuário
        hora_entrada = horario_para_decimal(entry_hora_entrada.get())
        saida_almoco = horario_para_decimal(entry_saida_almoco.get())
        entrada_almoco = horario_para_decimal(entry_entrada_almoco.get())

        # Horas fixas de trabalho da manhã e da tarde
        horas_manha = saida_almoco - hora_entrada  # Horas da manhã (08:00 a 12:00)
        horas_tarde = 18.3 - entrada_almoco        # Horas da tarde (13:30 a 18:18)

        # Calcular total de horas trabalhadas
        horas_trabalhadas = horas_manha + horas_tarde
        
        # Horário de saída para 8 horas e 48 minutos trabalhados
        horas_restantes_normal = 8 + (48 / 60) - horas_manha  # Restante para 8 horas e 48 minutos totais
        saida_normal_decimal = entrada_almoco + horas_restantes_normal
        saida_normal = decimal_para_horario(saida_normal_decimal)

        exibir_horarios(saida_normal)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira horários válidos no formato HH:MM.")

# Função para formatar entrada automaticamente
def formatar_horario(event):
    widget = event.widget
    texto = widget.get()

    if len(texto) == 2 and ":" not in texto:
        widget.insert(2, ":")

root = tk.Tk()
root.title("Calculadora de Horário de Saída")

# Definir tamanho da janela e centralizar
largura_janela = 615
altura_janela = 280
centralizar_janela(root, largura_janela, altura_janela)

# Personalização do Label de título
title_label = tk.Label(
    root, 
    text="Calculadora de Horário de Saída", 
    font=("Helvetica", 16, "bold"), 
    bg="#4a7a8c", 
    fg="white", 
    padx=9, 
    pady=9
)
title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

# Personalização dos Labels e Entries
tk.Label(root, text="Hora de Entrada (HH:MM):", font=("Arial", 12), anchor="w").grid(row=1, column=0, padx=20, pady=10, sticky="e")
entry_hora_entrada = tk.Entry(root, font=("Arial", 12), bd=2, relief="sunken", width=20)
entry_hora_entrada.grid(row=1, column=1, padx=50, pady=5)
entry_hora_entrada.bind("<KeyRelease>", formatar_horario)

tk.Label(root, text="Saída para o Almoço (HH:MM):", font=("Arial", 12), anchor="w").grid(row=2, column=0, padx=20, pady=10, sticky="e")
entry_saida_almoco = tk.Entry(root, font=("Arial", 12), bd=2, relief="sunken", width=20)
entry_saida_almoco.grid(row=2, column=1, padx=50, pady=5)
entry_saida_almoco.bind("<KeyRelease>", formatar_horario)

tk.Label(root, text="Entrada do Almoço (HH:MM):", font=("Arial", 12), anchor="w").grid(row=3, column=0, padx=20, pady=10, sticky="e")
entry_entrada_almoco = tk.Entry(root, font=("Arial", 12), bd=2, relief="sunken", width=20)
entry_entrada_almoco.grid(row=3, column=1, padx=50, pady=5)
entry_entrada_almoco.bind("<KeyRelease>", formatar_horario)

# Personalização do Botão
btn_calcular = tk.Button(
    root, 
    text="Calcular Horário de Saída", 
    font=("Arial", 12, "bold"), 
    bg="#4a7a8c", 
    fg="white", 
    activebackground="#45a049", 
    activeforeground="white", 
    relief="raised", 
    bd=1,
    padx=5, 
    pady=5,
    command=calcula_horas
)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=15)

# Adicionar Label com link do GitHub no canto inferior direito
github_label = tk.Label(
    root,
    text="Visite meu GitHub: https://github.com/EduTremea",
    font=("Arial", 10, "italic"),
    fg="#1a0dab",  # cor típica de links
    cursor="hand2"
)
github_label.grid(row=5, column=1, sticky="se", padx=50, pady=10)

# Função para abrir o link do GitHub
def abrir_github(event):
    import webbrowser
    webbrowser.open("https://github.com/EduTremea")

# Vincular o evento de clique ao Label do GitHub
github_label.bind("<Button-1>", abrir_github)

root.configure(bg="#f0f0f0")  # Cor de fundo da janela principal
root.mainloop()
>>>>>>> c388cac (new version)
