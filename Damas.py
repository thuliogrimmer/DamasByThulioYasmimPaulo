#Declarações de variáveis.
import time
pecaPreta = 'x'
pecaBranca = 'o'
contador=0
vez=pecaBranca
movi=''
lugar=''
opcao=''
k=0
pecaPretaCapturada=[]
pecaBrancaCapturada=[]

#Introdução 
print("Bem vindo ao jogo de damas v1.0")
input("Digite qualquer botão para continuar ")
#Opções do que fazer:
while opcao!="1":
    print("Selecione o que fazer:")
    print("1 - Player vs Player")
    print("2 - Player vs Computador (em breve!!)")
    print("3 - Créditos")
    print("4 - Manual")
    opcao=input("Digite apenas um número ")
   
    #Manual do jogo
    if opcao=="4":
        print("COMO JOGAR?...")
        time.sleep(2)
        print("")
        print("O jogo de damas é um jogo de dois jogadores que controlam peças em lados opostos ao tabuleiro.")
        time.sleep(2)
        print("")
        print("A primeira jogada deve ser realizada pelo jogador com peças brancas (o).")
        time.sleep(2)
        print("")
        print("Cada jogada consiste em mover a peça para a sua respectiva diagonal.")
        time.sleep(2)
        print("")
        print("Porém, a peça só pode ser movida se cumpre as seguintes restrições:")
        time.sleep(2)
        print("")
        print("A peça escolhida deve ser a peça da vez de jogar (ex: não é possível mover peças brancas quando for a vez do preto)")
        time.sleep(2)
        print("")
        print("As peças só podem ir para a diagonal caso ela não esteja ocupada e exista no tabuleiro.")
        time.sleep(2)
        print("")
        print("Sempre é necessário mover unicamente uma peça na vez do jogador.")
        time.sleep(2)
        print("")
        print("Não é possível voltar peças para suas diagonais.")
        time.sleep(2)
        print("")
        print("Só é possível adiantar uma posição por vez de jogada.")
        time.sleep(4)
        print("COMANDOS PARA MOVER PEÇAS...")
        time.sleep(2)
        print("")
        print("Esse programa consiste em mover peças por meio de comandos dados pelos jogadores")
        time.sleep(2)
        print("")
        print("O primeiro comando será referente a posição da peça que será movida. Se a peça escolhida cumprir todas as restrições estabelecidas, então")
        time.sleep(2)
        print("")
        print("O segundo comando irá aparecer. Ele é referente para onde a peça deve ir, se todas as restrições forem cumpridas, então o tabuleiro será impresso com a peça mexida.")
        time.sleep(2)
        print("")
        print("A sintaxe dos comandos é de número/letra. O tabuleiro possui uma numeração com letras que estabelecem a posição de cada quadrado.")
        time.sleep(2)
        print("")
        print("Ex mover uma peça da posição 3 e na posição b: 3/b.")
        time.sleep(2)
        print("") 
        print("Caso a sintaxe esteja incorreta, ou alguma restrição não for cumprida então o jogador terá que repetir o comando até que seja aceito.")
        print('')
    elif opcao=="3":
        print("Desenvolvedores:")
        print('')
        print("Paulo Henrique da Silva Maia")
        print('')
        print("Thúlio Gomes Pereira")
        print('')
        print("Yasmim da Silva Figuerêido")
        print('')
        time.sleep(1)
        print("Orientador:")
        print('')
        print("Henrique Do Nascimento Cunha")
        print('')
    elif opcao=="2":
        time.sleep(1)
        print('')
        print("EM BREVE!!")
        print('')
    elif opcao!="1":
        time.sleep(1)
        print("Número não identificado.")
        print("Tente novamente!")
        time.sleep(1)
        print("")


#time.sleep(2)
print("")
print("")

#O tabuleiro.
tabuleiro={ "8a":'-',"8b":pecaPreta,"8c":'-',"8d":pecaPreta,"8e":'-',"8f":pecaPreta,"8g":'-',"8h":pecaPreta,
            "7a":pecaPreta,"7b":'-',"7c":pecaPreta,"7d":'-',"7e":pecaPreta,"7f":'-',"7g":pecaPreta,"7h":'-',
            "6a":'-',"6b":pecaPreta,"6c":'-',"6d":pecaPreta,"6e":'-',"6f":pecaPreta,"6g":'-',"6h":pecaPreta,
            "5a":'-',"5b":'-',"5c":'-',"5d":'-',"5e":'-',"5f":'-',"5g":'-',"5h":'-',
            "4a":'-',"4b":'-',"4c":'-',"4d":'-',"4e":'-',"4f":'-',"4g":'-',"4h":'-',
            "3a":pecaBranca,"3b":'-',"3c":pecaBranca,"3d":'-',"3e":pecaBranca,"3f":'-',"3g":pecaBranca,"3h":'-',
            "2a":'-',"2b":pecaBranca,"2c":'-',"2d":pecaBranca,"2e":'-',"2f":pecaBranca,"2g":'-',"2h":pecaBranca,
            "1a":pecaBranca,"1b":'-',"1c":pecaBranca,"1d":'-',"1e":pecaBranca,"1f":'-',"1g":pecaBranca,"1h":'-'}

#Função de montar o tabuleiro no print.
def montarBulero():
    listinha = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
    for i in range(8):
        p = str(8-i)+" "
        for j in range(8):
            p += tabuleiro.get(str(8-i)+listinha.get(j))+" "
        print(p)
    a = " "
    for i in range(8):
        a+=listinha.get(i)+" "
    print()
    print(a)
    print()
montarBulero()

   
#Restrição caso o formato do input (sintaxe) esteja incorreto.
def restricaoMoviFormato(movi):
    if len(movi)!=2 or movi[0] not in '12345678' or movi[1] not in 'abcdefgh' :
        print("Formato não identificado")
        print("Tente Novamente!!")
        print("")
        return False
    else:
        return True
   
#Restrição caso não haja peça no lugar selecionado.      
def restricaoMoviPeca(movi):
    if tabuleiro[movi]=='-':
        print("Essa jogada não pode ser realizada pois não há nenhuma peça na posicão informada")
        print("Tente novamente!")
        print("")
        return False
    else:
        return True

#Restrição caso a posição informada não exista.  
def restricaoMoviIne(movi):
    if movi not in tabuleiro:
        print("A posição informada não existe.")
        print("Tente novamente!")
        print("")
        return False
    else:
        return True
   
#Restrição caso não seja a vez dessa peça jogar.
def restricaoMoviVez(movi):      
    if tabuleiro[movi]!=vez:
        print("Essa jogada não pode ser realizada pois a peça escolhida é a oposta a sua cor.")
        print("Tente novamente!")
        print("")
        return False
    else:
        return True
#Funções da dama
    
#FUNÇÃO VIRAR DAMA
def dama(lugar2,tabuleiro2,movi2):
    if lugar2[0]=='8' and tabuleiro2[movi2] == 'o':
        tabuleiro2[lugar2] = 'O'
    if lugar2[0]=='1' and tabuleiro2[movi2] == 'x':
        tabuleiro2[lugar2] = 'X'
    return tabuleiro2

#Restrição para jogar com a dama
def restricaoMoviDama(movi):      
    if vez=='x' and tabuleiro[movi]=='O':
        print("Essa jogada não pode ser realizada pois a peça escolhida é a oposta a sua cor.")
        print("Tente novamente!")
        print("")
        return False
    elif vez=='o' and tabuleiro[movi]=='X':
        print("Essa jogada não pode ser realizada pois a peça escolhida é a oposta a sua cor.")
        print("Tente novamente!")
        print("")
        return False
    else:
        return True


#RESTRIÇÕES DOS LUGARES DA PEÇA

       
#Restrição do formato (sintáxe) digitado pelo usuário.   
def restricaoLugarFormato(lugar):
    if len(lugar)!=2 or lugar[0] not in '12345678 ' or lugar[1] not in 'abcdefgh' :
        print("Formato não identificado")
        print("Tente Novamente!!")
        print("")
        return False
    else:
        return True
   
#Restrição de lugares já ocupados por outras peças.
def restricaoLugarOcupado(lugar):
    if tabuleiro[lugar] in 'ox':
        print("Não é possivel mover a peça para um lugar que já tenha outra peça!")
        print("Tente Novamente!!")
        print("")
        return False
    else:
        return True
#Restrição do lugar escolhido não poder ser movido
def restricaoLugarImpo(movi,lugar):
    letrasres = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    if captura(movi,lugar)==False:
        if vez=='o' and int(letrasres[movi[1]])-int(letrasres[lugar[1]]) not in [-1,1] or vez=='x' and int(letrasres[movi[1]])-int(letrasres[lugar[1]]) not in [-1,1] :
            print("Impossível mover a peça para o local escolhido")
            print("Tente Novamente!!")
            print("")
            return False
        else:
            return True
def restricaoLugarImpo(movi,lugar):
    letrasres = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    if captura(movi,lugar)==False:
        if vez=='o' and int(letrasres[movi[1]])-int(letrasres[lugar[1]]) not in [-1,1] or vez=='x' and int(letrasres[movi[1]])-int(letrasres[lugar[1]]) not in [-1,1] :
            print("Impossível mover a peça para o local escolhido")
            print("Tente Novamente!!")
            print("")
            return False
        else:
            return True
    

   
#Restrição de lugares que não podem colocar peças no tabuleiro.      
def restricaoLugarPosicao(lugar):
    if int(lugar[0])%2==0 and lugar[1] in 'aceg' or int(lugar[0])%2!=0 and lugar[1] in 'bdfh' :
        print("Não é possível colocar peças nessa posição.")
        print("Tente Novamente!!")
        print("")
        return False
    else:
        return True
   
#Restrição das peças não poderem voltar casas  
def restricaoLugarFrente(lugar):
    if vez==pecaBranca and int(lugar[0])<=int(movi[0]) or vez==pecaPreta and int(lugar[0])>=int(movi[0]):
        print("Só é possível ir para frente com as peças!")
        print("Tente novamente!!")
        print("")
        return False
    else:
        return True
 
#Restrição sobre as peças só poderem ir para uma casa de cada vez.     
def restricaoLugarVez(lugar):
    if vez==pecaBranca and int(lugar[0])-int(movi[0])!=1 or vez==pecaPreta and int(lugar[0])-int(movi[0])!=-1 :
        print("Não é possível andar mais de uma casa por vez!")
        print("Tente novamente!!")
        print("")
        return False
    else:
        return True

   
#Função Captura de peças.  
def captura(movi,lugar):
    numeros = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8}
    letras = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    alfanum = {"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h"}
    capturada = str(int(numeros[movi[0]]+numeros[lugar[0]])//2) + alfanum[str(int(letras[movi[1]]+letras[lugar[1]])//2)]
    if tabuleiro[lugar] == '-' and tabuleiro[capturada]=='x' and vez==pecaBranca:
        pecaPretaCapturada.append("x")
        tabuleiro[capturada]='-'
        print()
        print(f'A peça Preta da posição {capturada} foi capturada.')
        print(*pecaPretaCapturada)
        print()
        return True
    elif tabuleiro[lugar]== '-' and tabuleiro[capturada]=='o' and vez==pecaPreta:
        pecaBrancaCapturada.append("o")
        tabuleiro[capturada]='-'
        print()
        print(f'A peça Branca da posição {capturada} foi capturada.')
        print(*pecaBrancaCapturada)
        print()
        return True
    return False
   


#Função Mover peças.
def mover(pecaMovida,pecaLugar):
    tabuleiro[pecaLugar]=tabuleiro[pecaMovida]
    dama(lugar,tabuleiro,movi)
    tabuleiro[pecaMovida]='-'


while True:
   
    #De quem é a vez
    if vez=='o':
        print("VEZ DAS PEÇAS BRANCAS (o)")
    elif vez=='x':
        print("VEZ DAS PEÇAS PRETAS (x)")
   
   
    #Entrada
   
    movi=input("Peça que será movida (ex: 3g) ").lower()
    lugar=input("Lugar para onde a peça irá (ex: 4h) ").lower()
   
   
    #Verificação das restrições e caso alguma não seja cumprida, será necessário digitar novamente.
    while True:
        k=0
        if restricaoMoviFormato(movi)==False or restricaoLugarFormato(lugar) == False:
            movi=input("Peça que será movida (ex: 3g) ").lower()
            lugar=input("Lugar para onde a peça irá (ex: 4h) ").lower()
        else:
            if tabuleiro[movi] not in ['O','X'] and restricaoLugarImpo(movi,lugar) == False :
                #and int(lugar[0])-int(movi[0]) not in [-1,1]
                
                 #restricaoLugarVez(lugar)
                 k = 1
            if tabuleiro[movi] not in ['O','X']:
                if restricaoMoviPeca(movi)==False or restricaoMoviIne(movi) == False or restricaoMoviVez(movi) == False or restricaoLugarOcupado(lugar)==False or restricaoLugarPosicao(lugar) == False or restricaoLugarFrente(lugar) == False or k>0:
                    movi=input("Peça que será movida (ex: 3g) ").lower()
                    lugar=input("Lugar para onde a peça irá (ex: 4h) ").lower()
                else:
                    break
            else:
                if restricaoMoviPeca(movi)==False or restricaoMoviIne(movi) == False or restricaoLugarFormato(lugar)==False or restricaoLugarOcupado(lugar)==False or restricaoLugarFormato(lugar) == False or restricaoLugarPosicao(lugar) == False or k>0:
                    #restricaoLugarImpo(movi,lugar) == False or
                    movi=input("Peça que será movida (ex: 3g) ").lower()
                    lugar=input("Lugar para onde a peça irá (ex: 4h) ").lower()
                else:
                    break
                
    
    #Se a jogada for possível, então será modificada no tabuleiro e ele será exibido.
    
    mover(movi,lugar)
    montarBulero()
   
    #Verificação de quem é a vez de jogar.
    contador+=1
    if contador%2==0:

       vez=pecaBranca
    else:
        vez=pecaPreta
