
import webbrowser
from urllib.parse import quote
import random
from datetime import datetime

def FirstInicialization():
    
def Userinformations():
    
    UserBasicInformationsSaveds = {"Name": "Noki"}
    
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

    

    


    webbrowser.open(url)

def UserInput():
    
    Input  = (input(f""))


def main():
    ##########################
    #saudações
    saudações = salute()
    return saudações
    ##########################

    #-------------------------------------

    
    
    
    


main()

    


    




    


    

    
