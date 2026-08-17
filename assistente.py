
import webbrowser
from urllib.parse import quote
import random
from datetime import datetime
import os
import ctypes
import sys

##########################
#basicamente a função mais importante do programa por enquanto

def AdminPermission(): #função para programa virar admin 

    
    try:
        ctypes.windll.shell32.IsUserAnAdmin()
        
    except:
        return False

def IsnotAdmin():
    if not AdminPermission():
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None ,  "runas" ,sys.executable , " ". join(sys.argv) , None, 1
            )
            sys.exit()
        except Exception as error:
            print( print(f"Usuário recusou a elevação ou algo deu errado: {error}"))


#########################################
    
    
        
    
        


    

def FirstInicialization(): #Funcção para verificar primeira inicialização
    #procurar pasta BAD-ASSISTENT
    #se ela existe ok se ela n existe
    #criar a pasta completa
    DirectorysinProgramFile = []
    atual = os.getcwd()
    WalkInDirectorys = os.chdir(r"C:\Program Files")
    ExistorNot = os.path.exists(r"C:\Program Files\Bad-Config")
    if ExistorNot == "false":
        try:
            # código que pode dar erro
            os.mkdir(r"C:\Program Files\Bad-Config") 


        except PermissionError: #print do erro 
            print("Não tenho permissão pra criar pastas")
        try: #criar outras pastas dependentes 
            os.chdir(r"C:\Program Files\Bad-Config")
            os.makedirs(r"C:\Program Files\Bad-Config\config", exist_ok=True)
            os.makedirs(r"C:\Program Files\Bad-Config\UserInformations", exist_ok=True)
        except PermissionError: 
                    print("Não tenho permissão pra criar pastas")


            
            

           
    
def Userinformations():
    
    UserBasicInformationsSaveds = {}
    #função que vai funcionar de memoria para o assistente
    #ela sempre vai ler pra ver se n é a primeira inicialização na pasta ou se teve alguma informação diferente  "C:\Program Files\Bad-Config\UserInformations" 

    
    return UserBasicInformationsSaveds


def UserApis():
    Apis = {}
    return Apis




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


def AllFunctions():
    AdminPermission()
    FirstInicialization()

    #####
    #erro em admin permission eu n consigo chamar essa função eu ajeito quando chegar em casa #ass: Noki
    
    ##########################
    #saudações
    """saudações = salute()
    return saudações"""
    
    
    ##########################

    #-------------------------------------

    
    
    
    
def returofallfunctions():
    retorno =  AllFunctions()
    return retorno

    


    




    


    

    
