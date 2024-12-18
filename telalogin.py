from tkinter import *
from tkinter import messagebox

class TelaSimulado:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulado 2025")
        self.master.geometry("500x600")

        # Widgets
        Label(master, text="Nome do Aluno:", font=("Arial", 14)).pack(pady=5)
        self.entry_nome = Entry(master, font=("Arial", 14))
        self.entry_nome.pack(pady=5)

        self.entries_acertos = {}
        for area in ["Linguagens", "Natureza", "Humanas", "Matemática"]:
            Label(master, text=f"Acertos ({area}):", font=("Arial", 14)).pack(pady=5)
            entry = Entry(master, font=("Arial", 14))
            entry.pack(pady=5)
            self.entries_acertos[area] = entry

        # Dropdown para turma
        Label(master, text="Turma:", font=("Arial", 14)).pack(pady=5)
        self.area_var = StringVar()
        self.area_var.set("Selecione a turma")  # Valor padrão
        self.area_dropdown = OptionMenu(master, self.area_var, "1º série A", "1º série B", "2º série A", "2º série B", "3º série A")
        self.area_dropdown.pack(pady=5)

        # Botão Calcular Nota
        Button(master, text="Calcular Nota", font=("Verdana", 12), command=self.calcular_notas).pack(pady=20)

        # Exibição de Nota Final
        Label(master, text="Nota Final:", font=("Arial", 14)).pack(pady=5)
        self.entry_final = Entry(master, font=("Arial", 14), state='readonly')
        self.entry_final.pack(pady=5)

        # Botão para Salvar Nota
        Button(master, text="Salvar Nota", font=("Verdana", 12), command=self.salvar_nota).pack(pady=20)

   # Salvar no banco MySQL
        nome_aluno = self.entry_nome.get()
        turma = self.area_var.get()

        if nome_aluno and turma:
            conn = conectar_banco()
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO notas (nome, turma, nota) 
                    VALUES (%s, %s, %s) 
                    ON DUPLICATE KEY UPDATE nota = %s
                """, (nome_aluno, turma, nota_final, nota_final))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucesso", f"Nota Final: {nota_final:.2f} salva com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha o nome do aluno e turma!")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))



    def calcular_notas(self):
        try:
            notas = []
            for area, entry in self.entries_acertos.items():
                acertos = int(entry.get())
                if acertos < 0:
                    raise ValueError("A quantidade de acertos não pode ser negativa.")
                nota = (acertos * 1000) / 45
                notas.append(nota)

            nota_final = sum(notas) / len(notas)
            self.entry_final.config(state='normal')
            self.entry_final.delete(0, END)
            self.entry_final.insert(0, f"{nota_final:.2f}")
            self.entry_final.config(state='readonly')

            messagebox.showinfo("Notas Calculadas", f"Nota Final: {nota_final:.2f}")

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def salvar_nota(self):
        nome = self.entry_nome.get()
        turma = self.area_var.get()
        nota_final = self.entry_final.get()

        if not nome or turma == "Selecione a turma" or not nota_final:
            messagebox.showerror("Erro", "Preencha todos os campos antes de salvar a nota.")
        else:
            messagebox.showinfo("Sucesso", f"Nota de {nome} salva com sucesso!\nTurma: {turma}\nNota Final: {nota_final}")

def abrir_tela_admin():
    login.withdraw()
    admin = Toplevel()
    admin.geometry("600x400")
    admin.title("Tela do Admin")
    Label(admin, text="Bem-vindo, Admin!", font=("Arial", 16)).pack(pady=20)

    Button(admin, text="Abrir Simulado", font=("Arial", 12), command=lambda: TelaSimulado(Toplevel())).pack(pady=10)
    Button(admin, text="Voltar", font=("Arial", 12), command=lambda: voltar(admin)).pack(pady=10)

def abrir_tela_aluno():
    login.withdraw()
    aluno = Toplevel()
    aluno.geometry("600x400")
    aluno.title("Tela do Aluno")
    Label(aluno, text="Bem-vindo, Aluno!", font=("Arial", 16)).pack(pady=20)
    Button(aluno, text="Voltar", font=("Arial", 12), command=lambda: voltar(aluno)).pack(pady=10)

def verificar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login", "Login como Admin realizado com sucesso!")
        abrir_tela_admin()
    elif usuario == "aluno" and senha == "4321":
        messagebox.showinfo("Login", "Login como Aluno realizado com sucesso!")
        abrir_tela_aluno()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    campo_usuario.delete(0, 'end')
    campo_senha.delete(0, 'end')

def voltar(janela_atual):
    janela_atual.destroy()
    login.deiconify()

# Janela de Login Principal
login = Tk()
login.geometry("800x500")
login.title("Sistema de Login")

Label(login, text="Entre com o Login", font=("Arial Black", 17)).pack(pady=20)

Label(login, text="Usuário:", font=("Arial", 12)).pack(pady=5)
campo_usuario = Entry(login, font=("Arial", 12), width=30)
campo_usuario.pack(pady=5)

Label(login, text="Senha:", font=("Arial", 12)).pack(pady=5)
campo_senha = Entry(login, font=("Arial", 12), width=30, show='*')
campo_senha.pack(pady=5)

Button(login, text="Entrar no Sistema", bg="#3b3b3b", fg="white", font=("Arial Black", 11), command=verificar_login).pack(pady=20)

login.mainloop()
