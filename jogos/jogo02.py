from tkinter import *

class Application:
    def __init__(self, master=None):
        self.create_gui(master)
        self.cont = 0        
        self.pergunta01()

    def create_gui(self, master, title = None):
        #---------------------------------------------------
        #           Definição dos Containers
        #---------------------------------------------------        
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1["bg"] = "black"
        self.container1.pack()
        
        self.container2 = Frame(master)
        self.container2["pady"] = 50
        self.container2["bg"] = "black"
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3["bg"] = "black"
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["bg"] = "black"
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 5
        self.container5["bg"] = "black"
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 5
        self.container6["bg"] = "black"
        self.container6.pack()


        #---------------------------------------------------
        #               Definição dos Widgets
        #---------------------------------------------------
        self.lbtitulo = Label(self.container1)
        self.lbtitulo["font"] = ("Arial", "20", "bold")
        self.lbtitulo["bg"] = "#665a72"
        self.lbtitulo["foreground"] = "white"
        self.lbtitulo["pady"] = 5
        self.lbtitulo["width"] = 30
        self.lbtitulo["height"] = 2
        self.lbtitulo.pack()

        self.lbimagem = Label(self.container2)
        self.lbimagem["pady"] = 5
        self.lbimagem["bg"] = "black"
        self.lbimagem["width"] = 200
        self.lbimagem["height"] = 200
        self.lbimagem.pack()

        self.bt1 = Button(self.container3)
        self.bt1["font"] = ("Arial", "11", "bold")
        self.bt1["bg"] = "#e84b5e"
        self.bt1["foreground"] = "black"
        self.bt1["pady"] = 10
        self.bt1["width"] = 20
        self.bt1.pack(side=LEFT)

        self.bt2 = Button(self.container3)
        self.bt2["font"] = ("Arial", "11", "bold")
        self.bt2["bg"] = "#f2aa1a"
        self.bt2["foreground"] = "black"
        self.bt2["pady"] = 10
        self.bt2["width"] = 20
        self.bt2.pack(side=LEFT)        
        
        self.bt3 = Button(self.container4)
        self.bt3["font"] = ("Arial", "11", "bold")
        self.bt3["bg"] = "#03b8af"
        self.bt3["foreground"] = "black"
        self.bt3["pady"] = 10
        self.bt3["width"] = 20
        self.bt3.pack(side=LEFT)  

        self.bt4 = Button(self.container4)
        self.bt4["font"] = ("Arial", "11", "bold")
        self.bt4["bg"] = "#049900"
        self.bt4["foreground"] = "black"
        self.bt4["pady"] = 10
        self.bt4["width"] = 20
        self.bt4.pack(side=LEFT)        

        self.lbresultado = Label(self.container5)
        self.lbresultado["font"] = ("Arial", "15", "bold")
        self.lbresultado["foreground"] = "white"
        self.lbresultado["bg"] = "black"
        self.lbresultado["width"] = 30
        self.lbresultado.pack()

        self.btavancar = Button(self.container6)
        self.btavancar["font"] = ("Arial", "10", "bold")
        self.btavancar["pady"] = 5
        self.btavancar["width"] = 20
        self.btavancar["bg"] = "black"
        self.btavancar.pack()
        

    #---------------------------------------------------
    #                  Logica do jogo
    #---------------------------------------------------

    def pergunta01(self):        
        self.lbtitulo["text"] = "PERSONALIDADE 1"
        self.btavancar["text"] = ""        
        
        img = PhotoImage(file='imgs/gracehopper.png')
        self.lbimagem.config(image=img)
        self.lbimagem.image = img

        self.bt1["text"] = "Grace Hopper"
        self.bt1["command"] = lambda: self.resposta('1', 'certa')
        self.bt1["state"] = NORMAL
        
        self.bt2["text"] = "Annie Easley"
        self.bt2["command"] = lambda: self.resposta('1', 'errada')
        self.bt2["state"] = NORMAL
        
        self.bt3["text"] = "Margaret Hamilton"
        self.bt3["command"] = lambda: self.resposta('1', 'errada')
        self.bt3["state"] = NORMAL
        
        self.bt4["text"] = "Dorothy Vaughan"
        self.bt4["command"] = lambda: self.resposta('1', 'errada')
        self.bt4["state"] = NORMAL

    def pergunta02(self):
        self.lbtitulo["text"] = "PERSONALIDADE 2"
        self.btavancar["text"] = ""        
        
        img = PhotoImage(file='imgs/margarethhamilton.png')
        self.lbimagem.config(image=img)       
        self.lbimagem.imagem = img

        self.bt1["text"] = "Grace Hopper"
        self.bt1["command"] = lambda: self.resposta('2', 'errada')
        self.bt1["state"] = NORMAL
        
        self.bt2["text"] = "Annie Easley"
        self.bt2["command"] = lambda: self.resposta('2', 'errada')
        self.bt2["state"] = NORMAL
        
        self.bt3["text"] = "Margaret Hamilton"
        self.bt3["command"] = lambda: self.resposta('2', 'certa')
        self.bt3["state"] = NORMAL
        
        self.bt4["text"] = "Dorothy Vaughan"
        self.bt4["command"] = lambda: self.resposta('2', 'errada')
        self.bt4["state"] = NORMAL

    def pergunta03(self):
        self.lbtitulo["text"] = "PERSONALIDADE 3"
        self.btavancar["text"] = ""        
        
        img = PhotoImage(file='imgs/annieasley.png')
        self.lbimagem.config(image=img)
        self.lbimagem.imagem = img

        self.bt1["text"] = "Grace Hopper"
        self.bt1["command"] = lambda: self.resposta('3', 'errada')
        self.bt1["state"] = NORMAL
        
        self.bt2["text"] = "Annie Easley"
        self.bt2["command"] = lambda: self.resposta('3', 'certa')
        self.bt2["state"] = NORMAL
        
        self.bt3["text"] = "Margaret Hamilton"
        self.bt3["command"] = lambda: self.resposta('3', 'errada')
        self.bt3["state"] = NORMAL
        
        self.bt4["text"] = "Dorothy Vaughan"
        self.bt4["command"] = lambda: self.resposta('3', 'errada')
        self.bt4["state"] = NORMAL

    def resposta(self, pergunta, resposta):
        self.bt1["state"] = DISABLED
        self.bt2["state"] = DISABLED
        self.bt3["state"] = DISABLED
        self.bt4["state"] = DISABLED
        self.btavancar["text"] = ""
        
        if pergunta == '1':
            self.btavancar["command"] = self.pergunta02
        elif pergunta == '2':
            self.btavancar["command"] = self.pergunta03
        elif pergunta == '3':
            self.btavancar["command"] = self.resultado          

        if resposta == 'certa':
            self.cont += 1
            self.btavancar["text"] = "RESPOSTA CORRETA >>"
            self.btavancar["foreground"] = "green"
        else:
            self.btavancar["text"] = "RESPOSTA ERRADA >>"
            self.btavancar["foreground"] = "red"
        
    def resultado(self):        
        self.lbtitulo["text"] = "RESULTADO"
        
        img = PhotoImage(file='imgs/boneco_ok.png')
        self.lbimagem.config(image=img)       
        self.lbimagem.imagem = img

        #self.bt1.destroy()
        #self.bt2.destroy()
        #self.bt3.destroy()
        #self.bt4.destroy()
        self.btavancar.destroy()
        self.container3.destroy()
        self.container4.destroy()
        
        self.lbresultado["text"] = "Total de Acertos: " + str(self.cont)
                    
            
#def sairPrograma():
#    root.destroy()

root = Tk()
root.title("Perguntas e Respostas")
root["bg"] = "black"
#root.geometry("500x300")
Application(root) 
root.mainloop()
