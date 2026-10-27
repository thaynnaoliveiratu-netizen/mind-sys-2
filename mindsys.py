
import customtkinter
from tkinter import messagebox
from datetime import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Mind Sys - Lembretes")
janela.geometry("420x700")


titulo = customtkinter.CTkLabel(
    janela,
    text="MIND SYS",
    font=("Arial", 30, "bold")
)
titulo.pack(pady=13)

subtitulo = customtkinter.CTkLabel(
    janela,
    text="Olá! Coloque o que você quer lembrar."
)
subtitulo.pack(pady=10)


entrada = customtkinter.CTkEntry(
    janela,
    placeholder_text="Digite o seu lembrete...",
    width=330,
    height=35
)
entrada.pack(pady=10)


hora_entrada = customtkinter.CTkEntry(
    janela,
    placeholder_text="Hora do alarme (HH:MM)",
    width=330,
    height=35
)
hora_entrada.pack(pady=10)


lista = customtkinter.CTkTextbox(
    janela,
    width=330,
    height=250,
    font=("Arial", 12)
)
lista.pack(pady=10)


alarmes = []



def adicionar():
    tarefa = entrada.get()
    hora = hora_entrada.get()

    if tarefa == "":
        aviso.configure(text="Digite o seu lembrete primeiro!")
        return

    try:
        datetime.strptime(hora, "%H:%M")
    except ValueError:
        aviso.configure(
            text="Digite a hora corretamente! Exemplo: 14:30"
        )
        return

    lista.insert(
        "end",
        "[ ] " + tarefa + " - Alarme: " + hora + "\n"
    )


    alarmes.append({
        "tarefa": tarefa,
        "hora": hora,
        "avisado": False
    })

    entrada.delete(0, "end")
    hora_entrada.delete(0, "end")

    aviso.configure(text="Lembrete e alarme adicionados!")


def limpar():
    lista.delete("1.0", "end")
    alarmes.clear()
    aviso.configure(text="Todos os lembretes foram removidos!")



def verificar_alarme():
    hora_atual = datetime.now().strftime("%H:%M")

    for alarme in alarmes:

        if alarme["hora"] == hora_atual and not alarme["avisado"]:

            messagebox.showinfo(
                "MIND SYS - ALARME",
                "Está na hora!\n\n" + alarme["tarefa"]
            )

            alarme["avisado"] = True


    janela.after(1000, verificar_alarme)



botao_adicionar = customtkinter.CTkButton(
    janela,
    text="＋ Adicionar lembrete",
    width=340,
    height=35,
    corner_radius=15,
    fg_color="#2574EB",
    command=adicionar
)
botao_adicionar.pack(pady=8)



botao_limpar = customtkinter.CTkButton(
    janela,
    text="－ Tirar lembretes",
    width=340,
    height=35,
    corner_radius=15,
    fg_color="#26DC72",
    command=limpar
)
botao_limpar.pack(pady=5)



aviso = customtkinter.CTkLabel(
    janela,
    text="Seus lembretes estão prontos!",
    font=("Arial", 12)
)
aviso.pack(pady=10)



verificar_alarme()


janela.mainloop()
