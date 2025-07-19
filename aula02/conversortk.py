# 1. Importar a biblioteca customtkinter
import customtkinter

# Função que será chamada quando o botão for clicado (lógica idêntica)
def converter_temperatura():
    try:
        # Pega o valor digitado no campo de entrada
        celsius = float(entry_celsius.get())
        
        # Fórmula de conversão
        fahrenheit = (celsius * 9/5) + 32
        
        # Formata o resultado
        resultado_formatado = f"{fahrenheit:.2f} °F"
        
        # Atualiza o texto do label de resultado
        # Em CustomTkinter, é comum usar .configure() para alterar propriedades
        label_resultado.configure(text=resultado_formatado)
        
    except ValueError:
        # Se o usuário digitar algo que não é um número
        label_resultado.configure(text="Por favor, insira um número válido.")

# --- Configurações de Aparência do CustomTkinter ---
# Define o tema: "System" (segue o sistema), "Dark" (escuro), "Light" (claro)
customtkinter.set_appearance_mode("System")  
# Define a cor padrão dos componentes: "blue", "green", "dark-blue"
customtkinter.set_default_color_theme("blue") 

# 2. Criar a janela principal (agora usando CTk)
janela = customtkinter.CTk()
janela.title("Conversor Moderno")
janela.geometry("400x300")

# 3. Criar os widgets (usando os componentes do CustomTkinter)

# Frame para agrupar os elementos e dar um espaçamento bonito
frame = customtkinter.CTkFrame(master=janela)
frame.pack(pady=20, padx=40, fill="both", expand=True)

# Label para instrução
label_instrucao = customtkinter.CTkLabel(master=frame, text="Digite a temperatura em Celsius:", font=("Roboto", 14))
label_instrucao.pack(pady=12, padx=10)

# Campo de entrada (Entry), com texto de exemplo
entry_celsius = customtkinter.CTkEntry(master=frame, placeholder_text="Ex: 25")
entry_celsius.pack(pady=12, padx=10)

# Botão para executar a conversão
botao_converter = customtkinter.CTkButton(master=frame, text="Converter", command=converter_temperatura)
botao_converter.pack(pady=12, padx=10)

# Label para exibir o resultado
label_resultado = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 20, "bold"))
label_resultado.pack(pady=12, padx=10)

# 4. Iniciar o loop principal da aplicação
janela.mainloop()