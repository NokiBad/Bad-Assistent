
from ast import Return
import webbrowser
from urllib.parse import quote
import random
from datetime import datetime
import os
import ctypes
import sys
from dotenv import load_dotenv
import json

load_dotenv()

##########################
#basicamente a função mais importante do programa por enquanto

def AdminPermission(): #função para programa virar admin 

    try:
        resultado = ctypes.windll.shell32.IsUserAnAdmin()
        return resultado
    except Exception as e:
            print(f"Erro ao verificar admin: {e}")
            return False
    except:
        return  False
    #LOGICA CONSERTADA
    
   
    
    #LOGICA CONSERTADA
def IsnotAdmin(): 
    if  AdminPermission() == False:
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None ,  "runas" ,sys.executable , " ". join(sys.argv) , None, 1
            )
            sys.exit()

        except Exception as error:
            print(f"Usuário recusou a elevação ou algo deu errado: {error}")
            sys.exit()
#FUNÇÕES DE ADMIN FORAM CONSERTADAS
        
            


#########################################
    
def FirstInicialization(): 
    
            # código que pode dar erro
        try:    
            
            os.makedirs(r"C:\Program Files\Bad-Config\config", exist_ok=True)
            os.makedirs(r"C:\Program Files\Bad-Config\UserInformations", exist_ok=True)
            print("Pastas criadas com sucesso")
        except Exception as  error:
            print(f"algum erro foi encontrado na criação da memoria {error}")
#função de prrimeira inicialização está com a logica certa

#####
        

    


def MemoryExistence():

    try:
        os.chdir(r"C:\Program Files\Bad-Config\UserInformations\AssistentMemory")
        return True

    except:
        print("Memoria não Encontrada")
        return False


def MemoryCreate():
    if MemoryExistence() is False:
        os.makedirs(r"C:\Program Files\Bad-Config\AssistentMemory\TheBrain")
        dados = {}
        with open(r"C:\Program Files\Bad-Config\AssistentMemory\TheBrain\Brain.json","w")  as f:
            f.write(json.dumps(dados))
        print("Memoria criada com sucesso")
#função de memoria usada para ser uma memoria local do assistente, usa json para salvar alterações e coisas feitas pelo usuario
#vai ser implementado uma função de backup, mas só dps que vai ser ligada a essa função e vai deixar mais seguro 


###################




def UserApis():
    Apis = {}
    return Apis
#nada alterado nessa função até agora




def salute():


        Timenow = datetime.now()
        formatedtime = Timenow.strftime("%H")
        
        saudacoes = {
        "madrugada": ["Boa madrugada", "Ainda acordado?", "Madrugada produtiva, então?", "Que horário pra estar por aqui..."],
        "manha": ["Bom dia", "Good morning", "Buenos días", "Bonjour", "Buongiorno", "Guten Morgen", "Ohayou gozaimasu", "Joheun achim"],
        "tarde": ["Boa tarde", "Good afternoon", "Buenas tardes", "Bon après-midi", "Buon pomeriggio", "Guten Tag", "Konnichiwa", "Joheun ohu"],
        "noite": ["Boa noite", "Good evening", "Buenas noches", "Bonsoir", "Buonasera", "Guten Abend", "Konbanwa", "Joheun jeonyeok"]
        }
        if formatedtime >= "01:00" and formatedtime <= "04:30":
            respmad = random.choice(saudacoes["madrugada"])
            print(respmad)
            print("-"*50)
            if respmad != "Boa madrugada":
                print("Isso foi algo tipo (Você Não tem mais nada pra fazer pelo visto)" )
                print("Vamos trabalhar nessa madrugada!!!!")
                print("-"*50)
    
        elif formatedtime > "04:30" and formatedtime <= "12:30":
            respmanha = random.choice(saudacoes["manha"])
            #teste pra ver se é de manhã em portugues
    
            if respmanha != "Bom dia":
    
                print(respmanha)
                print("-"*50)
                print("Isso é um Bom dia em alguma outra lingua")
                print("-"*50)
    
    
        elif formatedtime > "12:30" and formatedtime < "18:00":
            resptarde = random.choice(saudacoes["tarde"])
            #teste para ver se o boa tarde  é em portugues 
            if resptarde != "Boa tarde":
                print(resptarde)
                print("-"*50)
                print("Isso Traduzido vira um Boa tarde, eu acho...")
                print("-"*50)
    
    
        else: #teste se o boa noite foi feito em portugues
            respnoite = random.choice(saudacoes["noite"])
            if respnoite != "Boa noite":
                print(respnoite)
                print("-"*50)
                print("Quis dizer Boa noite 😁")
                print("-"*50)
        
#intelligent search is completed for now (but not is finished)
def IntelligentSearch():

    #BROWSER EXISTENCE
    #lista de  perguntas para o browser
    Q = ["O que você quer pesquisar?",
        "Sobre o que é a busca?",
        "Me diz o termo que você quer buscar.",
        "O que vamos procurar hoje?",
        "Digite o que deseja pesquisar."]
    print(random.choice(Q))
    SearchRequest =  str(input())

    url = f"https://www.google.com/search?q={quote(SearchRequest)}"
    #CONSERTAR ISSO DPS, TEM ALGUM ERRO NA SINTAXE QUE ISSO TÁ PESQUISANDO SEM PEDIR #ass : Noki
    

def UserInput():
    
    Input  = (input(f""))

    #não finalizado

#######################################################
#IMPORTANTISSIMO 
#CONSERTAR AS BURRADAS QUE EU FIZ NESSE CODIGO, NÃO CONSIGO RETORNAR ESSAS FUNÇÕES #Ass:Noki
#######################################################
def AllFunctions():
    IsnotAdmin()
    FirstInicialization()
    MemoryCreate()
    #####
    #erro em admin permission eu n consigo chamar essa função eu ajeito quando chegar em casa #ass: Noki
    
    ##########################
    #saudações
    salute()

    
    
    ##########################

    #-------------------------------------

########
#  TUDO QUE TIVER COM -------> Ass: Noki
AllFunctions()
    


    


    




    


    

    
