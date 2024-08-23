#linkedin: 1alvaropaiva

from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

#criacao de janelas
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# dividindo a janela em 2 frames
frame_superior = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_superior.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_inferior = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_inferior.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurando o frame superior (palavra login como titulo da janela)
l_nome = Label(frame_superior, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x= 5, y=5)
l_linha = Label(frame_superior, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x= 10, y=45)

#credenciais pro login
credenciais = ['alvaro', '26917360']

#funcao q verifica login e senha pra entrar
def verificar_senha():
    nome = e_nome.get()
    senha = e_pw.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo, admin')
    elif credenciais [0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo novamente, ' + credenciais[0])

        # apaga o frame de baixo e o de cima apos logar
        for widget in frame_inferior.winfo_children():
            widget.destroy()
        for widget in frame_superior.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique o nome e/ou a senha')

#funcao apos a verificacao
def nova_janela():
    l_nome = Label(frame_superior, text='Usuário: ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)
    l_linha = Label(frame_superior, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_inferior, text='Seja bem vindo ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)


#configurando o frame inferior (nome)
l_nome = Label(frame_inferior, text='Nome:', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x= 10, y=20)
e_nome = Entry(frame_inferior, width= 25, justify='left', font=("",15), highlightthickness= 1, relief='solid')
e_nome.place(x= 14, y=50)

#configurando o frame inferior (senha)
l_pw = Label(frame_inferior, text='Senha:', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_pw.place(x= 10, y=95)
e_pw = Entry(frame_inferior, width= 25, show='*', justify='left', font=("",15), highlightthickness= 1, relief='solid')
e_pw.place(x= 14, y=130)

#configurando o botaozinho
botao_confirmar = Button(frame_inferior, command=verificar_senha, text='ENTRAR', width=39, height= 2, font=('Ivy 8 bold'), bg=co2, fg=co1,relief= RAISED, overrelief=RIDGE)
botao_confirmar.place(x= 15, y=180)

janela.mainloop()