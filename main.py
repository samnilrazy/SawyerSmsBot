# ---------------------------------------------------|
import requests                                     #| 
import telebot                                      #| 📕Bibliotecas
import time                                         #| ☕Codigo criado e modificado por Sam
import random                                       #|
import json                                         #| ⚙ Versão de teste 1.0
import os                                           #|
import loader                                       #|
import sqlite3                                      #|
import datetime                                     #|
import time                                         #|
# ___________________________________________________|

# 0:00 ●━━━━━━─────── 2:24
#⇆ㅤㅤㅤㅤ◁ㅤㅤ❚❚ㅤㅤ▷ㅤㅤㅤㅤ↻
#os.system("pipreqs . --encoding=utf8") # make requirements.txt (localhost)





# Muito cuidado nessa parte, vc pode sair no prejuízo se não fazer a calibragem correta
# Be very careful in this part, you could end up at a loss if you don't calibrate correctly.
taxa_de_cambio = 0.07  # 1 RUB = 0.06 BRL
taxa_cobrada = 0.42 # 40%










API = loader.API
bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN") # Se vc não souber no minimo onde adquirir esse token não está qualificado(a) a usar o codigo
# If you do not know at least where to purchase this token, you are not qualified to use the code.




bot_about = "✅Online (BETA)\n💠Contratamos divulgador!"
bot_description = "✉ Receba Sms de numeros virtuais virgens"


bot.set_my_short_description(short_description=bot_about)
bot.set_my_description(description=bot_description)

terminate = False # Não mecher! Ferramenta de thread

my_commands = [
    telebot.types.BotCommand("start", "Iniciar o bot") # command - Description
]

# Definir os comandos personalizados usando o método set_my_commands
bot.set_my_commands(my_commands)






@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    chatid = str(call.message.chat.id)
    userid = str(call.from_user.id)
    mensagem = call.message
    username = call.from_user.username
    name = str(call.from_user.first_name)


    atualizar = telebot.types.InlineKeyboardButton("🔄 Reload 🔄", callback_data="menu2")
    voltar = telebot.types.InlineKeyboardButton(loader.voltar, callback_data="menu")

    menu_botoes = telebot.types.InlineKeyboardMarkup()


    MenuCreator(menu_botoes, call) # retorna True ou False
    return call
        




def MenuCreator(menu_botoes, call):
    
    chatid = str(call.message.chat.id)
    try:
        dados = SelectUserById(chatid)

        if dados['status'] != "success":
            try:
                bot.reply_to(mensagem, loader.inexistente)
            except Exception as e:
                print(e)
            return False
        else:
            
            userid = str(call.from_user.id)
            mensagem = call.message
            username = call.from_user.username
            name = str(call.from_user.first_name)

            receber_sms = MakeButton(loader.msg[dados['Lang']]['button_receber_sms'], "menu_receber_sms")
            paises = MakeButton(loader.msg[dados['Lang']]['button_paises'], "paises")
            perfil = MakeButton(loader.msg[dados['Lang']]['button_perfil'], "perfil")
            canal = telebot.types.InlineKeyboardButton(loader.msg[dados['Lang']]['button_canal'], url="https://t.me/SawyerCanal")
            grupo = telebot.types.InlineKeyboardButton(loader.msg[dados['Lang']]['button_grupo'], url="https://t.me/SawyerGrupo")
            add_saldo = MakeButton(loader.msg[dados['Lang']]['button_recarregar'], "adicionarsaldo")
            colaboradores = MakeButton(loader.msg[dados['Lang']]['button_colaboradores'], "colaboradores")


            atualizar_perfil = telebot.types.InlineKeyboardButton("🔄 Reload 🔄", callback_data="reloadperfil")
            voltar_menu = telebot.types.InlineKeyboardButton(loader.voltar, callback_data="menu")
            voltar_menu_sms = telebot.types.InlineKeyboardButton(loader.voltar, callback_data="menu_receber_sms")

            menu_botoes = telebot.types.InlineKeyboardMarkup()
            msg = "Erro interno. Contate o suporte"

            
            

        #UpdateUsername(username, userid) # Desativei, pois o fluxo de upload é muito alto
    except Exception as e:
        print(e)
        return False



    if call.data == "menu":
        menu_botoes.add(receber_sms)
        menu_botoes.add(paises, perfil)
        menu_botoes.add(canal, grupo)
        menu_botoes.add(add_saldo)
        menu_botoes.add(colaboradores)
        
        msg = loader.msg[dados['Lang']]['msg_menu2'].format(name, userid)


    else:
        try:
            #bot.answer_callback_query(call.id, loader.msg32)
            bot.answer_callback_query(call.id, "Somente na versão completa", show_alert=True)
            return True
        except Exception as e:
            print(e)
            return False
    try:
        bot.edit_message_caption(chat_id=chatid, caption=msg, message_id=call.message.id, reply_markup=menu_botoes, parse_mode='HTML')
        return True
    except Exception as e:

        print(e)



@bot.message_handler(commands=['start', 'Start', 'START', 'sTART', 'sTaRt', 'StArT'])
def start(mensagem):
    user_language = mensagem.from_user.language_code #pt-br = portugues brasil, es = espanhol
    username = mensagem.from_user.username
    userid = str(mensagem.from_user.id)
    name = str(mensagem.from_user.first_name)
    chatid = str(mensagem.chat.id)


    if "-" in chatid: # Verifica se o usuario está em grupo
        pass # se em grupo (faz nada)
    else:
        # se não em grupo (continua)
        bot.send_chat_action(chatid, "typing", timeout=1)

        menu_botoes = telebot.types.InlineKeyboardMarkup()
        if user_language in ['pt-br', 'es']:
            button_menu = telebot.types.InlineKeyboardButton(loader.msg[f'{user_language}']['button_menu'], callback_data="menu")
            #msg = loader.msg[f'{user_language}']['msg_menu'].format(name)
            msg = f"<b>Olá {name}. Esta é somente uma versão de teste do bot @SawyerSmsBot!\nCaso queira adquirir o código completo entre contato com @ImNoCheating ou @SawyerID</b>"
        else:
            button_menu = telebot.types.InlineKeyboardButton(loader.msg['pt-br']['button_menu'], callback_data="menu")
            #msg = loader.msg['pt-br']['msg_menu'].format(name)
            msg = f"<b>Olá {name}. Esta é somente uma versão de teste do bot @SawyerSmsBot!\nCaso queira adquirir o código completo entre contato com @ImNoCheating ou @SawyerID</b>"
        
        Select = SelectUserById(userid)

        if Select['status'] == "error": # Usuario sem cadastro
            Cadastro = RegisterUser(userid, username, user_language)

            if Cadastro == True: # cadastro efetuado
                try:
                    menu_botoes.add(button_menu)
                    bot.send_photo(chat_id=chatid, photo=open("img.jpg", "rb"), caption=msg, reply_markup=menu_botoes, parse_mode='HTML')
                except Exception as e: 
                    print(e)
                    
            else:
                try:
                    bot.reply_to(mensagem, "Erro no servidor!")
                    msg = "error"
                except:
                    r = False


        else:
            try:
                lang = Select['Lang']
                button_menu = telebot.types.InlineKeyboardButton(loader.msg[f'{lang}']['button_menu'], callback_data="menu")
                #msg = loader.msg[f'{lang}']['msg_menu'].format(name)
                msg = f"<b>Olá {name}. Esta é somente uma versão de teste do bot @SawyerSmsBot!\nCaso queira adquirir o código completo entre contato com @ImNoCheating ou @SawyerID</b>"
                #bot.send_message(userid, termo, reply_markup=menu_botoes)
                menu_botoes.add(button_menu)
                bot.send_photo(chat_id=chatid, photo=open("img.jpg", "rb"), caption=msg, reply_markup=menu_botoes, parse_mode='HTML')
            except Exception as e: 
                print(e)

                    
            try:
                bot.delete_message(chat_id=userid, message_id=mensagem.id)
            except Exception as e:
                print(e)



def SelectUserById(userid): # retorna em json. Se houver erro: return json["status": "error"] ||||||| Se não: ["Id": "0", "UserId": "000000000", "Username": "asjda", "Saldo": 0.00, "SaldoG": 0.00, "QtdPedidos": "4", "Level": 1, "Rank": "Pombo", "Cargo": "Adm", "Warns": 3, "Termo": "sim","Condition": "livre", "Call": "nenhum", "status": "success"]
    
    fim = ExecAndReturnAllv2(f"SELECT * FROM Sawyer_Users WHERE User_Id = '{userid}'")

    if fim == "None" or fim == "[]" or fim == []:
        r = '["status": "error"]'
        r = r.replace("[", "{").replace("]", "}")

        r = json.loads(r)
        return r

    else:
        # ['2', '923321120', 'ImNoCheating', '0.00', '9577', 'Administrador', '0', 'pplyimghdj', '0']
        var_id = RemoveCharsForSplit(fim[0:1])
        var_user_id = RemoveCharsForSplit(fim[1:2])
        var_username = RemoveCharsForSplit(fim[2:3])
        var_saldo = float(RemoveCharsForSplit(fim[3:4]))
        var_cargo = RemoveCharsForSplit(fim[4:5])
        var_condition = RemoveCharsForSplit(fim[5:6])
        var_call = RemoveCharsForSplit(fim[6:7])
        var_pais = RemoveCharsForSplit(fim[7:8])
        var_lang = RemoveCharsForSplit(fim[8:9])
        json_model = f'["ID": "{var_id}", "USER_ID": "{var_user_id}", "Username": "{var_username}", "Saldo": {var_saldo}, "Cargo": "{var_cargo}", "Condition": "{var_condition}", "Call": "{var_call}", "Pais": "{var_pais}", "Lang": "{var_lang}", "status": "success"]'

        json_model = json_model.replace("[", "{").replace("]", "}")
        ObjectJsonUser = json.loads(json_model)

        return ObjectJsonUser



def MakeButton(name_b, callback_):
    return telebot.types.InlineKeyboardButton(name_b, callback_data=callback_)



def UpdateUsername(username, userid):
    ExecAndCommit(f"UPDATE Sawyer_Users SET Username = '{username}' WHERE User_Id = '{userid}'")



def RegisterUser(userid, username, user_language): # retorna True se der certo. Se der errado retorna False 
    if user_language == "pt-br":
        user_pais = 73
    elif user_language == "es":
        user_pais = 56
    else:
        user_pais = 73
    query = "INSERT INTO Sawyer_Users (ID, USER_ID, USERNAME, Saldo, Cargo, Condition, Call, Pais, Lang) VALUES (NULL,'{}', '{}', '0.00', 'Usuario', 'livre', 'nenhum', '{}', '{}')".format(userid, username, user_pais, user_language)
    ExecAndCommit(query)
        

    return True



def ExecAndCommit(script):
    connection = sqlite3.connect('files/database.db')
    cursor = connection.cursor()
    cursor.execute(script)
    fim = cursor.fetchall() ## ESTA VARIAVEL RECEBE RESULTS
    connection.commit()


def ExecAndReturnAllv2(script):
    connection = sqlite3.connect('files/database.db')
    cursor = connection.cursor()
    cursor.execute(script) # 0 a 10 é 1registro
    retorno = cursor.fetchall()

    results = str(retorno).replace("[", "").replace("(", "").replace("]", "").replace(")", "").replace(" ", "").replace("'", "").replace(",", " ").split()
    return results


def DATA():
    ################################################################################################
    # Obtém a data atual
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")

    return data_atual




def HORA():
    # Obtém a hora atual no fuso horário de Brasília
    fuso_horario_brasilia = datetime.timezone(datetime.timedelta(hours=-3))
    hora_atual_brasilia = datetime.datetime.now(fuso_horario_brasilia).strftime("%H:%M")
    ################################################################################################

    return hora_atual_brasilia


def adicionar_minutos(horario, minutos):
    horario_objeto = datetime.datetime.strptime(horario, "%H:%M")
    horario_novo = horario_objeto + datetime.timedelta(minutes=minutos)
    return horario_novo.strftime("%H:%M")



def ConversorRublosToReais(rublos):
    reais = rublos * taxa_de_cambio
    return reais


def CobrarTaxa(reais):
    taxa = reais * taxa_cobrada
    total = reais + taxa
    total_arredondado = round(total, 2)  # Arredonda para 2 casas decimais
    return total_arredondado



def Formatar(valor):
    x = '%.2f' % float(valor)
    return x




def RemoveCharsForSplit(x):
    x = str(x).replace("[", "").replace("]", "").replace('"', "").replace("'", "").replace(" ", "_")
    return x



bot.polling()


