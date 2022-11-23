# importanto a biblioteca

from tkinter import*


# cores

black = '#000000'
white = '#ffffff'
red = '#FF4367'

# função

def calculo():
    n1 = float(nota_prova.get())
    n2 = float(nota_atividade.get())

    media = float((n1*0.6) + (n2*0.4))
    resultado['text'] = (round(media,1))
    if media >= 5:
        texto_resultado['text'] = ('PARABÉNS APROVADO')
    else:
         texto_resultado['text'] = ('FICOU DE EXAME')




# janela

janela = Tk()
janela.title('V 1.0.0')
janela.geometry('400x450+500+150')
janela.resizable(width=False, height=True)
janela.configure(bg=red)
#janela.iconbitmap(r'icone.ico')



titulo = Label(janela,
               text='CALCULADORA UNIVESP',
               width=25,
               height=2,
               relief='flat',
               anchor='center',
               font='Courier 20 bold',
               bg=red)
titulo.grid(row=1, column=0)

linha = Label(janela,
               text='',
               width=57,
               height=0,
               pady=0,
               anchor='center',
               bg=black)
linha.place(x=0, y=50)


texto_nota_prova = Label(janela,
                         text='NOTA PROVA',
                         width=10,
                         height=2,
                         relief='flat',
                         font='Courier 16 bold',
                         bg=red)
texto_nota_prova.place(x=50, y=70)

texto_nota_atividade = Label(janela,
                         text='ATIVIDADES',
                         width=10,
                         height=2,
                         relief='flat',
                         font='Courier 16 bold',
                         bg=red)
texto_nota_atividade.place(x=50, y=120)

nota_prova = Entry(janela,
                   width=10,
                   justify='center',
                   relief='solid',
                   border=3,
                   font='Courier 12 bold')
nota_prova.place(x=240, y=82)

nota_atividade = Entry(janela,
                       width=10,
                       justify='center',
                       relief='solid',
                       border=3,
                       font='Courier 12 bold')
nota_atividade.place(x=240, y=130)

rodape_2 = Label(janela,
                 text='UTILIZAR O . NO LUGAR DA , NAS NOTAS',
                 width=50,
                 height=1,
                 relief='flat',
                 font='Arial 8 bold',
                 bg=red)
rodape_2.place(x=22, y=170)

calcular = Button(janela,
                  text='CALCULAR',
                  command=calculo,
                  width=10,
                  height=2,
                  border=2,
                  relief='sunken',
                  font='Courier 12 bold',
                  bg=black,
                  fg=red)
calcular.place(x=150, y=200)

resultado = Label(janela,
                        text='----------',
                        width=10,
                        height=2,
                        relief='flat',
                        font='Courier 16 bold',
                        bg=red)
resultado.place(x=138, y=250)

texto_resultado = Label(janela,
                        text='----------',
                        width=30,
                        height=2,
                        relief='flat',
                        font='Courier 16 bold',
                        bg=red)
texto_resultado.place(x=10, y=300)

rodape_1 = Label(janela,
                 text='Contribua Pix: rodrigodevcarvalho@gmail.com',
                 width=50,
                 height=1,
                 relief='flat',
                 font='Arial 8 bold',
                 bg=red)
rodape_1.place(x=22, y=380)

rodape_2 = Label(janela,
                 text='Desenvolvido Por: Rodrigo Carvalho',
                 width=50,
                 height=1,
                 relief='flat',
                 font='Arial 8 bold',
                 bg=red)
rodape_2.place(x=22, y=400)



janela.mainloop()
