import tkinter as tk
from tkinter import messagebox


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title("Simulado 2025")
        self.nossaTela.geometry("500x600")  
        
        
        # Aumentei o tamanho da janela para acomodar todos os campos
        
        # Adicionando um rótulo (Label) para o nome do aluno
        self.label1 = tk.Label(self.nossaTela, text="Nome do Aluno:", font=("Arial", 14))
        self.label1.pack(pady=5)

        # Campo de entrada para o nome do aluno
        self.entry_nome = tk.Entry(self.nossaTela, font=("Arial", 14))
        self.entry_nome.pack(pady=5)

        # Adicionando rótulos e campos de entrada para acertos por área

        # Linguagens
        self.label_acertos_linguagens = tk.Label(self.nossaTela, text="Quantidade de acertos (Linguagens):", font=("Arial", 14))
        self.label_acertos_linguagens.pack(pady=5)
        self.entry_acertos_linguagens = tk.Entry(self.nossaTela, font=("Arial", 14))
        self.entry_acertos_linguagens.pack(pady=5)

        # Natureza
        self.label_acertos_natureza = tk.Label(self.nossaTela, text="Quantidade de acertos (Natureza):", font=("Arial", 14))
        self.label_acertos_natureza.pack(pady=5)
        self.entry_acertos_natureza = tk.Entry(self.nossaTela, font=("Arial", 14))
        self.entry_acertos_natureza.pack(pady=5)

        # Humanas
        self.label_acertos_humanas = tk.Label(self.nossaTela, text="Quantidade de acertos (Humanas):", font=("Arial", 14))
        self.label_acertos_humanas.pack(pady=5)
        self.entry_acertos_humanas = tk.Entry(self.nossaTela, font=("Arial", 14))
        self.entry_acertos_humanas.pack(pady=5)

        # Matemática
        self.label_acertos_matematica = tk.Label(self.nossaTela, text="Quantidade de acertos (Matemática):", font=("Arial", 14))
        self.label_acertos_matematica.pack(pady=5)
        self.entry_acertos_matematica = tk.Entry(self.nossaTela, font=("Arial", 14))
        self.entry_acertos_matematica.pack(pady=5)

        # Campo de seleção para a Turma
        self.label_area = tk.Label(self.nossaTela, text="Turma:", font=("Arial", 14))
        self.label_area.pack(pady=5)
        self.area_var = tk.StringVar()
        self.area_dropdown = tk.OptionMenu(self.nossaTela, self.area_var, "1º série A", "1º série B", "2º série A", "2º série B", "3º série A")
        self.area_dropdown.pack(pady=5)

        # Botão para acionar a resposta
        self.button = tk.Button(self.nossaTela, text="Adicionar acertos", font=("Verdana", 12), relief='raised', command=self.resposta)
        self.button.pack(pady=20)

        # Adicionando um rótulo para calcular a nota final
        self.label_final = tk.Label(self.nossaTela, text="Nota Final:", font=("Arial", 14))
        self.label_final.pack(pady=5)

        # Campo de entrada para a nota final
        self.entry_final = tk.Entry(self.nossaTela, font=("Arial", 14), state='readonly')
        self.entry_final.pack(pady=5)

        # Botão para acionar a nota 
        self.button = tk.Button(self.nossaTela, text="Salvar Nota", font=("Verdana", 12), relief='raised', command=self.resposta)
        self.button.pack(pady=20)

        # Dicionário para armazenar as notas por área
        self.nota_areas = {}

    def resposta(self):
        nome = self.entry_nome.get()  # Pega o nome do aluno
        acertos_linguagens = self.entry_acertos_linguagens.get()  # Pega os acertos de Linguagens
        acertos_natureza = self.entry_acertos_natureza.get()  # Pega os acertos de Natureza
        acertos_humanas = self.entry_acertos_humanas.get()  # Pega os acertos de Humanas
        acertos_matematica = self.entry_acertos_matematica.get()  # Pega os acertos de Matemática

        if nome and acertos_linguagens and acertos_natureza and acertos_humanas and acertos_matematica:  # Verifica se todos os campos estão preenchidos
            try:
                # Convertendo as quantidades de acertos para inteiros
                acertos_linguagens = int(acertos_linguagens)
                acertos_natureza = int(acertos_natureza)
                acertos_humanas = int(acertos_humanas)
                acertos_matematica = int(acertos_matematica)

                if any(acerto < 0 for acerto in [acertos_linguagens, acertos_natureza, acertos_humanas, acertos_matematica]):
                    raise ValueError("A quantidade de acertos não pode ser negativa.")

                # Calculando a nota por área
                nota_linguagens = (acertos_linguagens * 1000) / 45
                nota_natureza = (acertos_natureza * 1000) / 45
                nota_humanas = (acertos_humanas * 1000) / 45
                nota_matematica = (acertos_matematica * 1000) / 45

                # Exibindo as notas de cada área em uma caixa de mensagem
                messagebox.showinfo("Notas por Área", f"Linguagens: {nota_linguagens:.2f}\n"
                                                     f"Natureza: {nota_natureza:.2f}\n"
                                                     f"Humanas: {nota_humanas:.2f}\n"
                                                     f"Matemática: {nota_matematica:.2f}")

                # Salvando as notas das áreas
                self.nota_areas = {
                    "Linguagens": nota_linguagens,
                    "Natureza": nota_natureza,
                    "Humanas": nota_humanas,
                    "Matemática": nota_matematica
                }

                # Calculando a média aritmética das notas das áreas
                nota_final = sum(self.nota_areas.values()) / len(self.nota_areas)
                self.entry_final.config(state='normal')  # Permite editar o campo
                self.entry_final.delete(0, tk.END)  # Limpa o campo
                self.entry_final.insert(0, f"{nota_final:.2f}")  # Exibe a nota final
                self.entry_final.config(state='readonly')  # Torna o campo somente leitura

            except ValueError as e:
                messagebox.showwarning("Erro de entrada", f"Valor inválido: {str(e)}")
        else:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos!")


        

# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()
