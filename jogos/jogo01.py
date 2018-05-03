#Jogo de perguntas e respostas (modo console)
#fonte interessante: https://biztechmagazine.com/article/2012/05/mothers-technology-10-women-who-invented-and-innovated-tech

class Jogo01:    
    def __init__(self):
        self.cont = 0
    
    def pergunta1(self):
        print("Quem foi Ada Lovelace?")
        print("a) A pessoa que criou o primeiro algoritmo")
        print("b) A pessoa que criou o primeiro computador")
        print("c) A pessoa que criou a Internet")
        print("d) A pessoa que criou o celular")

        resp = input("Resposta: ")

        if (resp == 'a'):
            print("Resposta Correta")
            self.cont+= 1
        else:
            print("Resposta Errada")

        print("\n--------------------------------\n")

    def pergunta2(self):
        print("Quem foi Margaret Hamilton")
        print("a) A pessoa responsavel pela programacao da Internet")
        print("b) A pessoa responsavel pela programacao da Televisao Digital")
        print("c) A pessoa responsavel pela programacao da missao Apolo 11 que levou o homem a Lua")
        print("d) A pessoa responsavel pela programacao de Drones ")

        resp = input("Resposta: ")

        if (resp == 'c'):
            print("Resposta Correta")
            self.cont+= 1
        else:
            print("Resposta Errada")

        print("\n--------------------------------\n")        

    def pergunta3(self):
        print("Quem foi Jennifer Robbins?")
        print("a) A pessoa que criou o primeiro aplicativo para celular")
        print("b) A pessoa que criou o primeiro site comercial")
        print("c) A pessoa que criou o primeiro jogo de computador")
        print("d) A pessoa que criou ")

        resp = input("Resposta: ")

        if (resp == 'b'):
            print("Resposta Correta")
            self.cont+= 1
        else:
            print("Resposta Errada")

        print("\n--------------------------------\n")

    def pergunta4(self):
        print("Quem foi Grace Hopper?")
        print("a) A pessoa que criou os Sistemas Operacionais")
        print("b) A pessoa que criou jogos de computador")
        print("c) A pessoa que criou a Linguagem Python")
        print("d) A pessoa que criou Linguagens de Programacao em linguagem humana")

        resp = input("Resposta: ")

        if (resp == 'd'):
            print("Resposta Correta")
            self.cont+= 1
        else:
            print("Resposta Errada")

        print("\n--------------------------------\n")


    def pergunta5(self):
        print("Quem foi Mary Jackson?")
        print("a) A primeira mulher negra a se tornar engenheira da NASA")
        print("b) A primeira mulher negra a se tornar programadora da NASA")
        print("c) A primeira mulher negra a se tornar engenheira da Microsoft")
        print("d) A primeira mulher negra a se tornar programadora da Microsoft")

        resp = input("Resposta: ")

        if (resp == 'a'):
            print("Resposta Correta")
            self.cont+= 1
        else:
            print("Resposta Errada")

        print("\n--------------------------------\n")

    def relatorio(self):
        print("Total de acertos: ", self.cont)


if __name__ == "__main__":
    jogo = Jogo01()
    jogo.pergunta1()
    jogo.pergunta2()
    jogo.pergunta3()
    jogo.pergunta4()
    jogo.pergunta5()
jogo.relatorio()
