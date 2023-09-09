## NÃO MECHER NESTA PARTE !!

#
## Essse arquivo foi criado com a intenção de despejar
#  entulho de codigos que toman muitas linhas na main principal
#



#
r = str(open("files/config.txt", "r+").readlines()).replace("\\n", "").replace("['", "").replace("']", "")
r = r.replace(" ", "[CAMPO_ESP__]").replace("[CAMPO_ESP__]", " ").replace("'", "").replace(",", "")

API = str(r.split()[2:3]).replace("['", "").replace("']", "").replace('"', "")

version = str(r.split()[5:6]).replace("['", "").replace("']", "").replace('"', "")
ultima_att = str(r.split()[8:9]).replace("['", "").replace("']", "").replace('"', "").replace("-", " - ")
atualizado_por = str(r.split()[11:12]).replace("['", "").replace("']", "").replace('"', "")
dono = str(r.split()[14:15]).replace("['", "").replace("']", "").replace('"', "")
id_dono = str(r.split()[17:18]).replace("['", "").replace("']", "").replace('"', "")
grupo = str(r.split()[20:21]).replace("['", "").replace("']", "").replace('"', "")
canal = str(r.split()[23:24]).replace("['", "").replace("']", "").replace('"', "")
dev = str(r.split()[26:27]).replace("['", "").replace("']", "").replace('"', "")
id_grupo = str(r.split()[29:30]).replace("['", "").replace("']", "").replace('"', "")


r2 = str(open("files/PhpMyAdmin.txt", "r+").readlines()).replace("\\n", "").replace("['", "").replace("']", "")
r2 = r2.replace(" ", "[CAMPO_ESP__]").replace("[CAMPO_ESP__]", " ").replace("'", "").replace(",", "")
Servidor_bank = str(r2.split()[2:3]).replace("['", "").replace("']", "").replace('"', "") 
User_bank = str(r2.split()[5:6]).replace("['", "").replace("']", "").replace('"', "") 
Database_bank = str(r2.split()[8:9]).replace("['", "").replace("']", "").replace('"', "")
Senha_bank = str(r2.split()[11:12]).replace("['", "").replace("']", "").replace('"', "")

quantidade_minima = 200
limite_aviso = 5
recarga_minima = 10.0

recarga_minima_int = int(recarga_minima)

tempo_pix = 10 # tempo em minutos (Se quiser que seja em segundo, mude o parametro abaixo, Coloque False para segundo e True para minutos sem aspas)
tempo_em_minuto = True # True --> minutos || ou || False --> segundos


id_grupo_backup = "-1001734050054" #id do grupo para backup de dados

msg446 = """<b>✦ Olá, seja bem-vindo(a) {}!

✅ Receba sms de numeros virgens que nunca foram usados!

▻ Numeros de varios Países
▻ Receba sms em varios apps/sites
▻ Serviços baratos
▻ Ativo desde 15/08/2023

Não perca mais dinheiro comprando chip de 15, 20 reais!</b>"""


msg446_es = """<b>✦ ¡Hola, bienvenido {}!

✅ ¡Recibe sms de números vírgenes que nunca han sido usados!

▻ Números de varios países
▻ Reciba sms en múltiples aplicaciones/sitios web
▻ Servicios baratos
▻ Activo desde el 15/08/2023

¡No pierdas más dinero comprando un chip por 15, 20 reales!</b>"""












msg447 = """<b>✦ Olá, seja bem-vindo(a) {}!ㅤ

• USER_ID:
 ↳<code>{}</code>


▻ Numeros virtuais mais barato da web vc só encontra aqui!.</b>""" # {}

msg447_es = """<b>✦ ¡Hola, bienvenido {}!ㅤ

• USER_ID:
 ↳<code>{}</code>


▻ ¡Los números virtuales más baratos de la web que solo puedes encontrar aquí!.</b>"""





menu = "[ Abrir Menu ]💻"
menu_adv = "[ 𝙰𝚋𝚛𝚒𝚛 𝙼𝚎𝚗𝚞 ]"





# messages /about
about_msg1 = f"""<i><b>⭐Versão: <code>{version}</code>
🔨Última atualização: <code>{ultima_att}</code>
📕Atualizado por: <code>{atualizado_por}</code>

➖➖➖➖➖➖➖

✅ <a href='https://t.me/followerspanel_bot'>[{version}]</a> Adicionado novos serviços.

✅ <a href='https://t.me/followerspanel_bot'>[{version}]</a> Corrigido bugs.

✅ <a href='https://t.me/followerspanel_bot'>[{version}]</a> Adicionado novos serviços.
</b></i>
"""


if tempo_em_minuto:
    tmp_px = tempo_pix * 60
    if tmp_px == 60:
        tipo_pixx = "MINUTO"
    else:
        tipo_pixx = "MINUTOS"
else:
    tmp_px = tempo_pix
    if tmp_px == 1:
        tipo_pixx = "SEGUNDO"
    else:
        tipo_pixx = "SEGUNDOS"



#bottons of the system
consultas_p = "🎄 Consultas Públicas"
cheats_ = "🎮 Game Cheat"
keys_steam = "🔑 Keys Steam"
notas_f = "💵 Notas Falsas [❌]"
telegram_sources = "👨‍💻 Bots Source [❌]"
cracked_games = "🕹 Jogos Crakeados"
cousers = "📕Cursos [❌]"
config = "⚙ Configurações"
sos_livre = "☎ SOS" # abrir menu sos (livre)
sos_nafila = "🟡 SOS" # abrir menu sos (na fila)
sos_ocupado = "📞 SOS" # abrir menu sos (ocupado)

sos_cancelar = "❌ Cancelar" # cancelar sos
sos_solicitar = "📞 Solicitar SOS" # abrir chamado
sos_desligar = "☎ Encerrar" # desligar sos

my_items = "📁Meus Items"
buy = "Comprar Agora✅"
lang = "🌐Lang"
suspenso = "🚫 Usuário suspenso 🚫"
indisponivel = "❗ Status: Indisponível"
inativo = "⚠ Conta Inativa ⚠"
err = "Erro ❗"
ranking = "🏆 Ranking"
vips = "⛄Consultas Vips"
b_databases = "🗂 Databases"
analise = "⌛Processando pedido"
reload_success = "Atualizado ✅"
voltar = "🔙 Voltar"
atualizar = "🔄 Atualizar 🔄"
button_fb = "🌐 Facebook"
button_inst = "⭐ Instagram"
button_yt = "🔴 Youtube"
button_tk = "🟣 Tiktok"
button_tele = "🔵 Telegram"
button_tw = "📘 Twitter"
button_sp = "🟢 Spotify"
button_kw = "🟡 Kwai"
button_twi = "🟣 Twitch"
planos = "🎁Planos"
button_historico = "📘 Baixar Histórico"
button_alertar = "Reportar 📫"
button_alertado = "Reportado ✅"
button_settings = "⚙ Settings"
button_ativar = ">> Ativar <<"
button_desativar = ">> Desativar <<"

button_recargadobroON = "Recarga 2X: Ativado✅"
button_recargadobroOFF = "Recarga 2X: Desativado❌"

button_pixON = "/pix: Ativado✅"
button_pixOFF = "/pix: Desativado❌"

button_enviarON = "/enviar: Ativado✅"
button_enviarOFF = "/enviar: Desativado❌"

button_sugerirON = "/sugerir: Ativado✅"
button_sugerirOFF = "/segerir: Desativado❌"


atr = "<<" #"⬅ Atrás"
prox = ">>" #"Próxima ➡"
erro_desc = "Erro desconhecido❗ Volte ao menu."








# cheats
msg_review_cheats = """<b>✦ {}

Categoria: {}
Jogo: {}
Permanente: {}
Dias: {}
Preço: R$ {}

Descrição: {}
</b>"""



msg_review_keysteam = """<b>✦ {}

Categoria: {}
Jogo: {}
Permanente: {}
Preço: R$ {}

Descrição: {}
</b>"""


msg_review_databases = """<b>✦ {}

Tipo de arquivo: Database (DB)
Preço: R$ {}

Descrição: {}
</b>"""


msg_review_crackedgames = """<b>✦ {}

Tipo de arquivo: {}
Preço: R$ {}

Descrição: {}
</b>"""






msg_compra = """<b><i>🎲☃ Documentos disponíveis ({})

🎫 Tipo: <code>{}</code>
📘 Nome: <code>{}</code>
🔑 CPF: <code>***.{}.***.**</code>
📅 Nasc: <code>{}</code>
🌟Score: <code>{}</code>
🎄 Valor: <code>{}</code></i></b>"""


msg_comprav2 = """<b><i>✅☃ Compra realizada !

🎫 Tipo: <code>{}</code>
📘 Nome: <code>{}</code>
🔑 CPF: <code>{}</code>
📅 Nasc: <code>{}</code>
🌟Score: <code>{}</code>
🎄 Valor Pago: <code>{}</code>

<a href='{}'>[ Clique aqui para fazer o download ]</a>
</i></b>"""



msg_cheats = """<b>✦ Escolha um item abaixo

- Saldo: R$ {}
</b>
"""


msg_suporte = """<b>🆘 MENU SOS

 ↳ Status: <code>{}</code>
 ↳ Admin: <code>{}</code>

↳ Esse é um mecanismo de ajuda criado para que os usuários possam solicitar um chat com um dos administradores do sistema.


</b>"""



msg_no_cheats = "<b>😬 Desculpe. Nenhum game cheat disponível no momento.</b>"
msg_no_keysteam = "<b>😬 Desculpe. Nenhuma Key Steam disponível no momento.</b>"
msg_no_database = "<b>😬 Desculpe. Nenhuma database disponível no momento.</b>"
msg_no_games = "<b>😬 Desculpe. Nenhum jogo crackeado disponível no momento.</b>"
msg_no_items = "<b>🍃 Parece tudo tranquilo por aqui. Oq acha de adquirir algo?.</b>"















#msg
inexistente = "❗Usuário não cadastrado. Use /start"



msg_insta1 = """<i><b>⭐Instagram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 1 --> ✨Seguidores mundiais (Melhor opção!)

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para instagram (melhor opção em compensação de preço e qualidade)</code>

⭐Comando(Sem aspas!):
<code>/follow ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/follow @me 1000 1</code></b></i>
"""


msg_insta2 = """<i><b>⭐Instagram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 2 --> ✨Seguidores mundiais (Serviço rapido!)

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para instagram (serviço rapido!)</code>

⭐Comando(Sem aspas!):
<code>/follow ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/follow @me 1000 2</code></b></i>
"""







msg1 = """<i><b>Olá <a href='https://t.me/{}'>{}</a>, Seja bem vindo(a)! ☃

Entre nas nossas comunidades:
👥 <a href='https://t.me/{}'>Grupo ❄</a>
📢 <a href='https://t.me/{}'>Canal ☃</a>
👤 <a href='https://t.me/{}'>Suporte 🌟</a>

☃❄ Compre aqui kit bico de qualidade e no melhor preço !!</b></i>"""


limite_aviso = limite_aviso

msg2 = """<b><i>🔵 Info

⏱Status da conta: <code>{}</code>

📕Avisos: <code>{}/{}</code>

➖➖➖➖➖➖➖➖➖➖➖➖➖
</i></b>
"""


msg4 = """<i><b>🏆Ranking de usuários que mais gastaram saldo!
(Em tempo real)

1º -- <a href='https://t.me/FollowersPanel_bot'>🥇</a> <code>{}</code> <a href='https://t.me/{}'>[💬Chat]</a> 💎Total: <code>R$ {}</code>

2º -- <a href='https://t.me/FollowersPanel_bot'>🥈</a> <code>{}</code> <a href='https://t.me/{}'>[💬Chat]</a> 💎Total: <code>R$ {}</code>

3º -- <a href='https://t.me/FollowersPanel_bot'>🥉</a> <code>{}</code> <a href='https://t.me/{}'>[💬Chat]</a> 💎Total: <code>R$ {}</code>

4º -- <a href='https://t.me/FollowersPanel_bot'>🏅</a> <code>{}</code> <a href='https://t.me/{}'>[💬Chat]</a> 💎Total: <code>R$ {}</code>

5º -- <a href='https://t.me/FollowersPanel_bot'>🎖</a> <code>{}</code> <a href='https://t.me/{}'>[💬Chat]</a> 💎Total: <code>R$ {}</code>


<code>(NOTA: Usuários sem '@nome_de_usuário' não vão aparecer no ranking)</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖</b></i>
"""


msg_alert_staffs = """<b>☎ Chamado SOS

 ↳ Solicitado por: <a href='https://t.me/{}'>{}</a>
 ↳ ID: <code>{}</code>
 </b>"""

 ## Atender
 ## Dispensar






adm_accepted_call = """<b>🟢 CHAT CONECTADO

 ↳ Não visualizamos nenhum tipo de conteudo que não seja texto!
 
 ↳ Não envie imagens, audios e documentos
 
 ↳ Seja educado(a) Estamos aqui para ajudar!
 
 ↳ O Chat ficará ativo durante 1hora, se não houver nenhum retorno, o mesmo será cancelado!
 
 ↳ Enviou uma mensagem e até agora não recebeu uma respota? Aguarde, enquanto o chat estiver ativo o administrador respodenderá em breve (Ninguém fica com a cara no telegram 24horas)</b>"""







# voltar


msg_pix_auto = """<i><b>✨ Adição de saldo via  pix 
tornou-se mas fácil! Agora os seus pagamentos serão processado de forma automática pelo bot 🌟

para cria uma transação pelo bot use:
 /pix valor

exemplo: /pix 10

✅🕸 O seu saldo estará disponível em até 1 minuto após o pagamento !</b></i>"""


msg_pix_auto5pt2 = """<i><b>✨ Adição de saldo via  pix 
tornou-se mas fácil! Agora os seus pagamentos serão processado de forma automática pelo bot 🌟

💠 Qual valor deseja recarregar?

❄ Recarregar: {}.00

➖➖➖➖➖➖➖➖➖</b></i>"""

btn_1 = "+1"
btn_5 = "+5"
btn_10 = "+10"

btn_m1 = "-1"
btn_m5 = "-5"
btn_m10 = "-10"

confirmar = "Confirmar ✅"


msg6 = """📕 ID: [<code>{}</code>]

Olá, <a href='https://t.me/{}'>{}</a>, essa conta foi suspensa por um de nossos administradores. Você pode solicitar uma revisão com o suporte. 

<a href='https://t.me/samniilrazy'>[ Clique aqui ]</a>"""




msg7 = """📕 ID: [<code>{}</code>]

⚠ Essa conta foi considerada inativa por um de nossos admninistradores⚠ Use /start para reativar."""


msg8 = """<i><b>☃ Painel SMM

- 💰 Saldo: R$ {}
- 🛒 Pedidos concluídos: {}


✨ Selecione uma categoria abaixo:</b></i>"""


msg9 = """<i><b>🌐 Facebook

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 1 --> ✨Curtidas para páginas

Preço: <code>{} a cada 1000 curtidas</code>
Descrição: <code>Curtidas para páginas do facebook</code>

⭐Comando(Sem aspas!):
<code>/fb ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/fb linkdapagina 1000 1</code></b></i>"""

msg9pt2 = """<i><b>🌐 Facebook

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 2 --> ✨Curtidas para postagens

Preço: <code>{} a cada 1000 curtidas</code>
Descrição: <code>Curtidas para post do facebook</code>

⭐Comando(Sem aspas!):
<code>/fb ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/fb linkdapagina 1000 2</code></b></i>"""




msg10 = """<i><b>⭐Instagram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 3 --> ✨Seguidores mundiais (⚡Instantâneo)

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para instagram (Serviço instantâneo⚡)</code>

⭐Comando(Sem aspas!):
<code>/follow ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/follow @me 1000 3</code></b></i>
"""

msg11 = """<i><b>⭐Instagram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 4 --> ✨Seguidores (Femininas)

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para instagram</code>

⭐Comando(Sem aspas!):
<code>/follow ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/follow @me 1000 4</code></b></i>"""

msg11pt2 = """<i><b>⭐Instagram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 5 --> ✨Seguidores (Masculinos)

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para instagram</code>

⭐Comando(Sem aspas!):
<code>/follow ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/follow @me 1000 5</code></b></i>"""



msg12 = """<i><b>🔴Youtube

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 1 --> ✨Likes para vídeos

Preço: <code>{} a cada 1000 likes</code>
Descrição: <code>Likes para vídeo do youtube</code>

⭐Comando(Sem aspas!):
<code>/youtube ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/youtube link_do_video 1000 1</code></b></i>"""

msg12pt2 = """<i><b>🔴Youtube

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 2 --> ✨Views para youtube

Preço: <code>{} a cada 1000 visualizações</code>
Descrição: <code>Views para vídeo do youtube</code>

⭐Comando(Sem aspas!):
<code>/youtube ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/youtube link_do_video 1000 2</code></b></i>"""

msg12pt3 = """<i><b>🔴Youtube

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 3 --> ✨Inscritos para youtube (ALTA QUALIDADE)

Preço: <code>{} a cada 1000 Inscritos</code>
Descrição: <code>Atenção: você só receberar 10 inscritos diariamente até que seja concluído! O youtube irá zerar os inscritos se forem enviados instantâneos!</code>

⭐Comando(Sem aspas!):
<code>/youtube ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/youtube link_do_canal 1000 3</code></b></i>"""


msg13 = """<i><b>🟣 Tiktok

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 1 --> ✨Seguidores BR

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para tiktok</code>

⭐Comando(Sem aspas!):
<code>/tiktok ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/tiktok link_do_video 1000 1</code></b></i>"""

msg14 = """<i><b>🟣 Tiktok

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 2 --> ✨Curtidas BR

Preço: <code>{} a cada 1000 curtidas</code>
Descrição: <code>Seguidores para tiktok</code>

⭐Comando(Sem aspas!):
<code>/tiktok ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/tiktok link_do_video 1000 2</code></b></i>"""


msg14pt2 = """<i><b>🟣 Tiktok

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 3 --> ✨Visualizações BR

Preço: <code>{} a cada 1000 visualizações</code>
Descrição: <code>Visualizações para tiktok</code>

⭐Comando(Sem aspas!):
<code>/tiktok ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/tiktok link_do_video 1000 3</code></b></i>"""


msg15 = """<i><b>🔵 Telegram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 1 --> ✨Inscritos para canal

Preço: <code>{} a cada 1000 inscritos</code>
Descrição: <code>Inscritos para canal de telegram</code>

⭐Comando(Sem aspas!):
<code>/telegram ´link ou @´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/telegram @channel 1000 1</code></b></i>"""

msg15pt2 = """<i><b>🔵 Telegram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 2 --> ✨Membros para grupo

Preço: <code>{} a cada 1000 membros</code>
Descrição: <code>Membros para grupo de telegram</code>

⭐Comando(Sem aspas!):
<code>/telegram ´link ou @´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/telegram @grupo 1000 2</code></b></i>"""


msg16 = """<i><b>🔵 Telegram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 3 --> ✨Views para postagens I

Preço: <code>{} a cada 1000 views</code>
Descrição: <code>1000 Visualizações para as últimas 5 postagens (somente canais)</code>

⭐Comando(Sem aspas!):
<code>/telegram ´link ou @´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/telegram @canal 1000 3</code></b></i>"""

msg16pt2 = """<i><b>🔵 Telegram

- 💰 Saldo: R$ {}
- 🛒 Pedidos concuídos: {}


💎 Tipo 4 --> ✨Views para postagens II

Preço: <code>{} a cada 1000 views</code>
Descrição: <code>1000 Visualizações para as últimas 10 postagens (somente canais)</code>

⭐Comando(Sem aspas!):
<code>/telegram ´link ou @´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/telegram @canal 1000 4</code></b></i>"""





msg18 = """⌛️ Processando seu pedido ⌛️

⏱Status: <code>{}</code>

📕Serviço selecionado: <code>{}</code>

🎲Quantidade: <code>{}</code>
⭐️Destinário: <code>{}</code>

❓ Houve algum erro? você pode cancelar a operação com o comando <code>/cancelar</code>

📕Nota: Caso haja algum problema com o destinário, a operação será cancelada e receberá reembolso do saldo."""


msg19 = '''{
"IN_1": "IN_1 --> ⭐Seguidores mundiais (Instagram)",
"IN_2": "IN_2 --> ⭐Seguidores femininas (Instagram)",
"IN_3": "IN_3 --> ⭐Seguidores masculinos (Instagram)",
"FB_1": "FB_1 --> 🌐Curtidas para fanpage (Facebook)",
"FB_2": "FB_2 --> 🌐Curtidas para postagens (Facebook)",
"YT_1": "YT_1 --> 🔴 Youtube likes 👍",
"YT_2": "YT_2 --> 🔴 Youtube likes 👁",
"TK_1": "TK_1 --> ⚡ Seguidores brasileiros 🟣(Tiktok)",
"TK_2": "TK_2 --> ⚡ Curtidas brasileiras 🟣👍(Tiktok)",
"TK_3": "TK_3 --> ⚡ Views brasileiros 🟣👁(Tiktok)",
"TL_1": "TL_1 --> 💎 Inscritos para canal🔵(Telegram)",
"TL_2": "TL_2 --> 💎 Membros para grupo 🔵(Telegram)",
"TL_3": "TL_3 --> 🔵Views paras postagens I👁(Telegram)",
"TL_4": "TL_4 --> 🔵Views paras postagens II👁(Telegram)",
"TL_5": "TL_5 --> 🔵Views paras postagens III👁(Telegram)",
"TL_6": "TL_6 --> 🔵Views paras postagens IV👁(Telegram)"

}'''


msg20 = """<i><b>📘 Twitter

- 💰 Saldo: <code>R$ {}</code>
- 🛒 Pedidos concuídos: <code>{}</code>


💎 Tipo 1 --> ✨Seguidores

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para twitter</code>

⭐Comando(Sem aspas!):
<code>/tw ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/tw link_ou@fulano 1000 1</code>
</b></i>"""


msg21 = """<i><b>🟢 Spotify

- 💰 Saldo: <code>R$ {}</code>
- 🛒 Pedidos concuídos: <code>{}</code>


💎 Tipo 1 --> ✨Seguidores

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para perfil spotify</code>

⭐Comando(Sem aspas!):
<code>/spotify ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/spotify link_perfil 1000 1</code>
</b></i>"""

msg22 = """<i><b>🟢 Spotify

- 💰 Saldo: <code>R$ {}</code>
- 🛒 Pedidos concuídos: <code>{}</code>


💎 Tipo 2 --> ✨Seguidores para playlist

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para playlists do spotify</code>

⭐Comando(Sem aspas!):
<code>/spotify ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/spotify link_daplaylist 1000 2</code>
</b></i>"""


msg23 = """<i><b>🟡 Kwai

- 💰 Saldo: <code>R$ {}</code>
- 🛒 Pedidos concuídos: <code>{}</code>


💎 Tipo 1 --> ✨Curtidas BR

Preço: <code>{} a cada 1000 curtidas</code>
Descrição: <code>Curtidas para videos do kwai</code>

⭐Comando(Sem aspas!):
<code>/kwai ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/kwai link_video 1000 1</code>
</b></i>"""


msg24 = """<i><b>🟡 Kwai

- 💰 Saldo: <code>R$ {}</code>
- 🛒 Pedidos concuídos: <code>{}</code>


💎 Tipo 2 --> ✨Seguidores BR

Preço: <code>{} a cada 1000 curtidas</code>
Descrição: <code>Seguidores br para kwai</code>

⭐Comando(Sem aspas!):
<code>/kwai ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/kwai link_video 1000 2</code>
</b></i>"""

msg25 = """<i><b>🟣 Twitch

- 💰 Saldo: <code>R$ {}</code>
- 🛒 Pedidos concuídos: <code>{}</code>


💎 Tipo 1 --> ✨Seguidores

Preço: <code>{} a cada 1000 seguidores</code>
Descrição: <code>Seguidores para perfil da twitch</code>

⭐Comando(Sem aspas!):
<code>/twi ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/twi link_perfil 1000 1</code>
</b></i>"""

msg26 = """<i><b>🟣 Twitch

- 💰 Saldo: <code>R$ {}</code>
- 🛒 Pedidos concuídos: <code>{}</code>


💎 Tipo 2 --> ✨Visualização(Live 30Min)

Preço: <code>{} a cada 1000 visualizações</code>
Descrição: <code>Visualizações para live (Duração: 30Minutos)</code>

⭐Comando(Sem aspas!):
<code>/twi ´link´ ´quantidade´ ´tipo´</code>
Exemplo:
<code>/twi link_perfil 1000 2</code>
</b></i>"""


msg27 = "<b><i>☃Meus pedidos\n\n</i></b>" # Cabeçalho

msg28 = """<b><i>ID: <code>{}</code>
Link: <code>{}</code>
Valor Pago: <code>{}</code>
Quantidade: <code>{}</code>
Serviço: <code>{}</code>
Status: <code>{}</code>
➖➖➖➖➖➖➖

</i></b>""" # Ficha

msg29 = "<b><i>🍃 Nenhuma compra realizada ainda :/\nOque acha de fazer uma agora? :)</i></b>"






msg30 = """<i><b>⚙ Configurações administrativas

➖ Recarga em dobro: <code>{}</code>

➖ Comando /pix: <code>{}</code>

➖ Comando /enviar: <code>{}</code>

➖ Comando /sugerir: <code>{}</code>
</b></i>"""


msg31 = "Permissões insuficientes❗"
msg32 = "Página ainda não disponível❗"

# ======================================================================================
# GLOBAL MSG ======================================================================================
# ======================================================================================
# GLOBAL MSG ======================================================================================
# ======================================================================================
# GLOBAL MSG ======================================================================================
# ======================================================================================
# GLOBAL MSG ======================================================================================
globalmsg_1 = """🚬🌝E aí chefe, tem um novo pedido pendente!!

➖Use: /correio (para ver os pedidos)
➖Use: /accept user_id (para atualizar status para 'Trabalhando')
➖Use: /concluir user_id (para remover da lista, e enviar a msg de conclusão)
➖Use: /deny user_id <motivo> (para reprovar)"""
globalmsg_2 = "❗Erro: Você já possui um pedido em processamento!! É permitido somente 1 por vez"

globalmsg_3 = f"Erro: Quantidade mínima é {quantidade_minima}❗"

globalmsg_4 = "Erro: Insira uma quantidade válida de 500 em 500❗\nExemplo: 500, 1000, 1500..."

globalmsg_5 = "❗Erro: saldo insuficiente"

globalmsg_6 = "Erro desconhecido❗ contate o suporte."

globalmsg_7 = "<i><b>Erro 113❗\n\nSe o erro for persistente, clique no botão abaixo para alertar o suporte!!</b></i>" # 113

globalmsg_8 = "Erro 108❗\n\nSe o erro for persistente, clique no botão abaixo para alertar o suporte!!" # 108


# reportado
globalmsg_9 = "<i><b>Erro 113❗(reportado!)\n\nSe o erro for persistente, clique no botão abaixo para alertar o suporte!!</b></i>" #113


globalmsg_10 = "<i><b>Erro 108❗(reportado!)\n\nSe o erro for persistente, clique no botão abaixo para alertar o suporte!!</b></i>" # 108


globalmsg_11 = "<i><b>Pedido Cancelado❗\n\nID: <code>{}</code>\n\n➖ O seu pedido foi cancelado por um de nossos administradores\n\n➖Saldo reembolsado: R$ <code>{}</code>.\n\n📘Principais motivos:\n\n<code>♦ Nome de usuário ou link incorreto</code>\n\n<code>♦ Tentativas de burlar o sistema.</code></b></i>"



globalmsg_12 = "<b>O pix foi desabilitado por um administrador!</b>"

# message /follow
follow_msg1 = "❗Erro: Uso incorreto. Utilize /follow @insta <quantidade> <tipo: [1|2|3]>"
follow_msg2 = globalmsg_3
follow_msg3 = globalmsg_4
follow_msg4 = "Erro❗ O tipo vc deve escolher 1, 2 ou 3"
follow_msg5 = globalmsg_1

follow_msg6 = globalmsg_5
follow_msg7 = globalmsg_2

# message / warn
warn_msg1 = "<i><b>Uso incorreto! Utilize <code>/warn</code> <id do usuário></b></i>"

#messages /enviar
enviar_msg1 = "Usuário não existe ou não possui cadastro❗"
enviar_msg2 = "❗Erro: Aguarde alguns segundos para enviar novamente❗"
enviar_msg3 = "Erro❗: Comando inválido, utilize /enviar <quantidade> <id do seu amigo> <msg pra ele>\n\n➖Exemplo: /enviar 15 1861077089 Olá"
enviar_msg4 = "Erro❗: Você não pode enviar para você mesmo (caso tente burlar, terá seu saldo zerado sem reembolso)"
enviar_msg5 = "❗Mínimo a ser enviado é R$ 1.00"
enviar_msg6 = "Erro❗: Quantidade inválida"
enviar_msg7 = "(Campo não preenchido)"
enviar_msg8 = "Usuário não existe ou não possui cadastro❗"


enviar_msg9 = """<i><b>[ Você recebeu R$ <code>{}</code> ✅ ]


➖➖➖Dados do pagador ➖➖➖

✅ Enviado por: @{}
🆔: <code>{}</code>
💰 Quantia: <code>{}</code>

✉ Mensagem:
<code>{}</code>


➖➖➖➖➖➖➖➖➖➖➖➖</b></i>"""


enviar_msg10 = "Saldo insuficiente❗"

enviar_msg11 = """<i><b>[ 💠Você enviou R$ <code>{}</code> 💠 ]


➖➖➖Pagamento ➖➖➖

✅ Enviado para: <code>{}</code>
💰 Quantia: <code>{}</code>

✉ Mensagem:
<code>{}</code>


➖➖➖➖➖➖➖➖➖➖➖➖</b></i>"""



# messages /pix
pix_msg1 = f"❗Mínimo a ser depositado é R$ {recarga_minima}"
pix_msg2 = "Uso incorreto❗ Use /pix <valor>"
pix_msg3 = """✅Sua transação foi criada !

📔 código copia e cola:
{}

☃ Dica: para copiar o código basta clicar encima dele ❄🎈

💰Valor: {}

🆔 Id transação: <code>{}</code>


⏰ A TRANSAÇÃO EXPIRA EM {} {} ! APÓS O PAGAMENTO, SERÁ CREDITADO O SALDO AUTOMATICAMENTE.

❌ CASO VOCÊ REALIZAR O PAGAMENTO E NÃO RECEBER SEU SALDO, COPIE O ID DA TRANSAÇÃO E CHAME O SUPORTE ❗ --> @{}"""
pix_msg4 = "QRCode Expirado❗"
pix_msg5 = "✅Pagamento Concluido\n✅Saldo adicionado {}"
pix_msg6 = "Você não esta cadastrado no sistema. Envie /start"
pix_msg7 = """💵 Nova recarga realizada!

Id:  {}
Valor: R$ {}

{}"""
pix_msg8 = "QRCode Expirado❗"


# messages /rd
rd_msg1 = "Uso incorreto❗\nUtilize /rd <on|off>"
rd_msg2 = "Saldo em dobro foi ativado✅"
rd_msg3 = "Houve um erro! C326"
rd_msg4 = "Saldo em dobro foi desativado❌"
rd_msg5 = "Houve um erro! C327"
rd_msg6 = ""
rd_msg7 = ""
rd_msg8 = ""
rd_msg9 = ""
rd_msg10 = ""
rd_msg11 = ""
rd_msg12 = ""
rd_msg13 = ""


# messages /ajuda
ajuda_msg1 = '<a href="https://t.me/FollowersPanel_bot">🤔</a>⁉ Precisa de ajuda? <a href="https://t.me/samnilrazy">Clique aqui</a> para falar com suporte!'



# messages /sugerir
s_msg1 = "Uso incorreto❗ Utilize /sugerir <mensagem>"
s_msg2 = """Nova Sugestão ✅

📕De: @{}
🆔: {}

{}✉: {}
"""
s_msg3 = "Sugestão enviada para o suporte✅"
s_msg4 = "Erro inesperado, contate o suporte"
s_msg5 = ""
s_msg6 = ""
s_msg7 = ""
s_msg8 = ""








# messages /correio
c_msg1 = """📫Solicitações: 0


➖➖➖➖➖➖➖➖➖
🍃😎 Nenhuma Solicitação
pendente.
➖➖➖➖➖➖➖➖➖"""
c_msg2 = """📕 Nome: <code>{}</code>
💰 Valor Pago: <code>{}</code>
🆔: <code>{}</code>
🔰 Quantidade: <code>{}</code>
🎁 Tipo: <code>{}</code>
✉ Destinário: <code>{}</code>
⏳ Status: <code>{}</code>
___________________________________"""
c_msg3 = """📫 Solicitações: {}

/deny [userid] [motivo]
/accept [id]
/concluir [id]

Use /id [tipo] para ver qual é o pedido solicitado

➖➖➖➖➖➖➖➖➖\n\n"""
c_msg4 = ""
c_msg5 = ""
c_msg6 = ""
c_msg7 = ""
c_msg8 = ""
c_msg9 = ""
c_msg10 = ""





# messages /accept
ac_msg1 = "❗Erro: Uso incorreto. Utilize /accept <userid>"
ac_msg2 = "📭Nada encontrado! ,_,"
ac_msg3 = "✅Análise completa! O pedido já está sendo enviado ao destinário!!"
ac_msg4 = "✅Análise atualizada para 'Trabalhando' com sucesso!!"
ac_msg5 = ""
ac_msg6 = ""
ac_msg7 = ""
ac_msg8 = ""
ac_msg9 = ""
ac_msg10 = ""



# messages /concluir
cl_msg1 = "❗Erro: Uso incorreto, utilize /concluir <user_id>"
cl_msg2 = "📭Nada encontrado! ,_,"
cl_msg3 = "✅Seu pedido foi concluído com sucesso!!"
cl_msg4 = "✅Análise atualizada para 'Concluída' com sucesso!!"
cl_msg5 = ""
cl_msg6 = ""
cl_msg7 = ""
cl_msg8 = ""
cl_msg9 = ""
cl_msg10 = ""
cl_msg11 = ""
cl_msg12 = ""


# messages /deny
d_msg1 = "❗Erro: Uso incorreto! Utilize /deny <user_id> <motivo>"
d_msg2 = "📭Nada encontrado! ,_,"
d_msg3 = "❗Erro: Usuário não existe"
d_msg4 = """
❗ Pedido Cancelado <a href='https://t.me/FollowersPanel_bot'>❗</a>

➖Olá, o seu pedido foi cancelado por um de nossos administradores. Mas não se preocupe, reembolsamos o seu saldo!!

📕Motivo: <code>{}</code>

🔨Suporte 1: <a href='https://t.me/samniilrazy'>[ Clique aqui ]</a>
🔨Suporte 2: <a href='https://t.me/samnilrazy'>[ Clique aqui ]</a>
________________________________________________"""
d_msg5 = "✅Cancelado"
d_msg6 = ""
d_msg7 = ""
d_msg8 = ""
d_msg9 = ""
d_msg10 = ""
d_msg11 = ""
d_msg12 = ""
d_msg13 = ""
d_msg14 = ""
d_msg15 = ""

# messages /cancelar
clr_msg1 = "📭Você não possui um pedido em andamento! ,_,"
clr_msg2 = "Erro❗ Você não pode utilizar esse comando. A operação já foi iniciada."
clr_msg3 = "❗Erro: Usuário sem cadastro"
clr_msg4 = """
❗ Pedido Cancelado <a href='https://t.me/FollowersPanel_bot'>❗</a>

➖Olá, o seu pedido foi cancelado por um de nossos administradores. Mas não se preocupe, reembolsamos o seu saldo!!

📕Motivo: <code>Solicitado pelo usuário.</code>

🔨Suporte 1: <a href='https://t.me/samniilrazy'>[ Clique aqui ]</a>
🔨Suporte 2: <a href='https://t.me/samnilrazy'>[ Clique aqui ]</a>
________________________________________________"""
clr_msg5 = "✅Cancelado"
clr_msg6 = "❗Erro: Você não está autorizado a utilizar este comando"
clr_msg7 = ""
clr_msg8 = ""
clr_msg9 = ""
clr_msg10 = ""
clr_msg11 = ""
clr_msg12 = ""
clr_msg13 = ""
clr_msg14 = ""
clr_msg15 = ""
clr_msg16 = ""


# messages /facebook

fb_msg1 = "❗Erro: Uso incorreto. Utilize /facebook <link> <quantidade> <tipo: [1|2]>"
fb_msg2 = globalmsg_3
fb_msg3 = globalmsg_4
fb_msg4 = "Erro❗ O <tipo> vc deve escolher entre 1 ou 2"
fb_msg5 = globalmsg_5
fb_msg6 = globalmsg_2
fb_msg7 = ""
fb_msg8 = ""
fb_msg9 = ""
fb_msg10 = ""
fb_msg11 = ""
fb_msg12 = ""
fb_msg13 = ""



# messages /youtube
yt_msg1 = "❗Erro: Uso incorreto. Utilize /youtube <link> <quantidade> <tipo: [1|2]>"
yt_msg2 = globalmsg_3
yt_msg3 = globalmsg_4
yt_msg4 = "Erro❗ O <tipo> vc deve escolher entre 1 ou 2"
yt_msg5 = globalmsg_5
yt_msg6 = globalmsg_2
yt_msg7 = globalmsg_6
yt_msg8 = ""
yt_msg9 = ""
yt_msg10 = ""
yt_msg11 = ""
yt_msg12 = ""
yt_msg13 = ""
yt_msg14 = ""
yt_msg15 = ""
yt_msg16 = ""




# messages /tiktok
tk_msg1 = "❗Erro: Uso incorreto. Utilize /tiktok <destinário> <quantidade> <tipo: [1|2]>"
tk_msg2 = globalmsg_3
tk_msg3 = globalmsg_4
tk_msg4 = "Erro❗ O <tipo> vc deve escolher entre 1 ou 2"
tk_msg5 = globalmsg_1
tk_msg6 = globalmsg_5
tk_msg7 = globalmsg_2
tk_msg8 = ""
tk_msg9 = ""
tk_msg10 = ""
tk_msg11 = ""
tk_msg12 = ""
tk_msg13 = ""



# messages /telegram
tlg_msg1 = "❗Erro: Uso incorreto. Utilize /telegram <destinário> <quantidade> <tipo: [1|2|3|4]>"
tlg_msg2 = globalmsg_3
tlg_msg3 = globalmsg_4
tlg_msg4 = "Erro❗ O <tipo> vc deve escolher entre 1 a 4"
tlg_msg5 = ""
tlg_msg6 = ""
tlg_msg7 = ""
tlg_msg8 = ""
tlg_msg9 = ""
tlg_msg10 = ""
tlg_msg11 = ""
tlg_msg12 = ""
tlg_msg13 = ""
tlg_msg14 = ""
tlg_msg15 = ""

# messages /tw
tw_msg1 = "❗Erro: Uso incorreto. Utilize /tw <destinário> <quantidade> <tipo: [1]>"
tw_msg2 = globalmsg_3
tw_msg3 = globalmsg_4
tw_msg4 = "Erro❗ O <tipo> vc deve escolher 1"
tw_msg5 = ""
tw_msg6 = ""


# messages /sp
sp_msg1 = "❗Erro: Uso incorreto. Utilize /sp <destinário> <quantidade> <tipo: [1, 2]>"
sp_msg2 = globalmsg_3
sp_msg3 = globalmsg_4
sp_msg4 = "Erro❗ O <tipo> vc deve escolher entre 1 ou 2"
sp_msg5 = ""
sp_msg6 = ""


# messages /kw
kw_msg1 = "❗Erro: Uso incorreto. Utilize /sp <destinário> <quantidade> <tipo: [1, 2]>"
kw_msg2 = globalmsg_3
kw_msg3 = globalmsg_4
kw_msg4 = "Erro❗ O <tipo> vc deve escolher entre 1 ou 2"
kw_msg5 = ""
kw_msg6 = ""


twi_msg1 = "❗Erro: Uso incorreto. Utilize /twi <destinário> <quantidade> <tipo: [1, 2]>"
twi_msg2 = globalmsg_3
twi_msg3 = globalmsg_4
twi_msg4 = "Erro❗ O <tipo> vc deve escolher 1 ou 2"
twi_msg5 = ""
twi_msg6 = ""


# message /set and /sethelp
set_msg1 = """📕 Manual do /set

 - O /set é um comando feito para setar cargo, level, saldo e etc...

✅ Modo de uso 1:
<code>/set Level 10</code>

O comando acima irá alterar o level de todos os usuários para 10.



✅ Modo de uso 2:
<code>/set Level 10 1122334455</code>

O comando acima irá alterar o level somente do id colocado no final."""
set_msg2 = "Uso incorreto❗\nUse /sethelp"
set_msg3 = "Código executado com sucesso✅"
set_msg4 = "Houve um erro no seu código❗"
set_msg5 = "Sem permissão❗"




# message /getadmin <password>
getadm_msg1 = "Você agora é um(a) administrador(a)✅"
getadm_msg2 = "Senha incorreta❗"
getadm_msg3 = ""
getadm_msg4 = ""
getadm_msg5 = ""
getadm_msg6 = ""
getadm_msg7 = ""
getadm_msg8 = ""
getadm_msg8 = ""
getadm_msg9 = ""



# message /ban
ban_msg1 = "Uso incorreto❗\nUtilize /ban <id>"
ban_msg2 = "Erro❗ Usuário não existe."
ban_msg3 = ""
ban_msg4 = ""
ban_msg5 = ""
ban_msg6 = ""
ban_msg7 = ""
ban_msg8 = ""
ban_msg9 = ""




# message /unban
unban_msg1 = "Uso incorreto❗\nUtilize /unban <id>"
unban_msg2 = "Erro❗ Usuário não existe."
unban_msg3 = ""
unban_msg4 = ""
unban_msg5 = ""
unban_msg6 = ""
unban_msg7 = ""
unban_msg8 = ""
unban_msg9 = ""
unban_msg10 = ""




# message /kick
kick_msg1 = "Uso incorreto❗\nUtilize /kick <id>"
kick_msg2 = "Erro❗ Usuário não existe."
kick_msg3 = ""
kick_msg4 = ""
kick_msg5 = ""
kick_msg6 = ""



# message /send
send_msg1 = "Uso incorreto❗\nUtilize /send <mensagem>\n(OBS: Html on)"
send_msg2 = ""
send_msg3 = ""
send_msg4 = ""
send_msg5 = ""




msg = {
    "pt-br": {
        "button_menu": "ABRIR MENU ✅",
        "msg_menu": f"{msg446}",
        "msg_menu2": f"{msg447}",
        "button_receber_sms": f"Receber SMS ✉",
        "button_perfil": "📫 Perfil",
        "button_recarregar": "Adicionar saldo ✨",
        "button_paises": "Países 🏴‍☠️",
        "button_canal": "Canal 📣",
        "button_grupo": "Grupo 📣",
        "msg_sms": """<b>✦ {} ({})

- Saldo:  <code>R$ {}</code>

⚡Numeros disponíveis: {}
💳Preço: R$ {}</b>""",
        "msg_menu_paises": """<b>✦ Escolha um país abaixo

Se estiver procurando um país que não esteja sendo mostrado na lista, entre em contato com o suporte para que seja adicionado.</b>""",
        "msg_pais_atualizado": "<b>Novo país selecionado: {}</b>",
        "msg_menu_sms": """✦ Escolha uma opção abaixo
✦ País Selecionado: {}

(caso a opção desejada não esteja no menu, contate o suporte e peça para que seja a adicionado)""",
        "msg_perfil": """<b><i>🌟 Perfil:
-  ID: <code>{}</code>
-  Username: <a href='https://t.me/{}'>{}</a>
-  Cargo: <code>{}</code>

🕸❄️ Carteira:
-  Saldo:  <code>R$ {}</code></i></b>""",
        "msg_alert_notrublos": "Erro: API sem resposta",
        "msg_insufficient_founds": "Erro: Você não tem saldo suficiente❗",
        "msg_number_generated": """<b>✦ {} ({})

Numero: <code>+{}</code>
Status: <code>Aguardando Sms...</code>

Expira as: <code>{}</code></b>""",
        "msg_unknown_error": "Erro desconhecido",
        "button_cancel_sms": "Cancelar ❌",
        "msg_sms_canceled": "<b>✦ Recebimento cancelado com sucesso! Não se preocupe, vc foi reembolsado(a)</b>",
        "msg_blocked": "Você deve aguardar uns minutos antes de cancelar❗",
        "msg_sms_expired": "<b>Numero de telefone expirado❗</b>",
        "msg_not_dis": "Sem numero disponíveis para esse serviço no país selecionado❗",
        "msg_recarregar": """<i><b>✨ Adição de saldo simplificada!

 ↳ CHAVE: <code>samnilrazy@gmail.com</code>

 ↳ Para garantir uma experiência fluida, após realizar o pagamento, envie o comprovante para o suporte
em <a href='https://t.me/SawyerID'>Sawyer</a> (DICA: Apenas clique no nome!). Assim que recebermos o comprovante, o pagamento imediatamente e atualizará o saldo em sua conta.

 ↳ Em breve o pix automatico estará funcionando (pois exige um esforço e cuidado a mais para que não haja erros)

 ↳ Recarga Mínima R$ 10.0 (Não aceitamos menos)</b></i>""",
        "button_colaboradores": "Colaboradores 👨‍💻",
        "msg_colaboradores": """ <b>✦ Aqui está a lista de Progamadores de Rank: S 🏴‍☠️

 ↳ <a href='https://t.me/SawyerID'>🥇Sawyer(Fundador)</a>: Deu inicio ao projeto

 ↳ <a href='https://t.me/ImNoCheating'>🥈ImNoCheating(SubDono)</a>: Ajudou a progamar

 ↳ <a href='https://chat.openai.com'>🥉ChatGPT(Mestre)</a>: Compartilhou conhecimento raro


✦ Quem sabe algum dia seu nome pode estar nessa lista! Fique ligado!</b>

"""






        
    },



    "es": {
        "button_menu": "ABRIR MENÚ ✅",
        "msg_menu": f"{msg446_es}",
        "msg_menu2": f"{msg447_es}",
        "button_receber_sms": f"recibir SMS ✉",
        "button_perfil": "📫 Perfil",
        "button_recarregar": "Agregar Saldo ✨",
        "button_paises": "Países 🏴‍☠️",
        "button_canal": "Canal 📣",
        "button_grupo": "Grupo 📣",
        "msg_sms": """<b>✦ {} ({})

- Saldo:  <code>R$ {}</code>

⚡Números disponibles: {}
💳Precio: R$ {}</b>""",
        "msg_menu_paises": """<b>✦ Elija un país a continuación

Si está buscando un país que no se muestra en la lista, comuníquese con soporte para agregarlo.</b>""",
        "msg_pais_atualizado": "<b>Nuevo país seleccionado: {}</b>",
        "msg_menu_sms": """✦ Elija una opción a continuación
✦ País seleccionado: {}

(si la opción deseada no está en el menú, póngase en contacto con soporte y solicite que se agregue)""",
        "msg_perfil": """<b><i>🌟 Perfil:
-  ID: <code>{}</code>
-  Username: <a href='https://t.me/{}'>{}</a>
-  Cargo: <code>{}</code>

🕸❄️ Carteira:
-  Saldo:  <code>R$ {}</code></i></b>""",
        "msg_alert_notrublos": "Error: la API no responde",
        "msg_insufficient_founds": "Error: No tienes saldo suficiente❗",
        "msg_number_generated": """<b>✦ {} ({})

Numero: <code>+{}</code>
Estado: <code>Esperando SMS...</code>

Expira a las: <code>{}</code></b>""",
        "msg_unknown_error": "Erro desconhecido",
        "button_cancel_sms": "Cancelar ❌",
        "msg_sms_canceled": "<b>✦ ¡Recibido cancelado con éxito! No te preocupes, te reembolsaron</b>",
        "msg_blocked": "Debes esperar unos minutos antes de cancelar❗",
        "msg_sms_expired": "<b>Número de teléfono vencido❗</b>",
        "msg_not_dis": "No hay números disponibles para este servicio en el país seleccionado❗",
        "msg_recargar": """<i><b>✨ ¡Saldo añadido fácil!

 ↳ CLAVE: <code>samnilrazy@gmail.com</code>

 ↳ Para garantizar una experiencia sin problemas, después de realizar el pago, envíe el recibo a soporte
en <a href='https://t.me/SawyerID'>Sawyer</a> (CONSEJO: ¡simplemente haga clic en el nombre!). Una vez que recibamos el recibo, el pago se realizará de inmediato y se actualizará el saldo en su cuenta.

 ↳ En breve estará funcionando el pix automático (ya que requiere más esfuerzo y cuidado para que no haya errores)

 ↳ Recarga mínima R$ 10,0 (No aceptamos menos)</b></i>""",
        "button_colaboradores": "Colaboradores 👨‍💻",
        "msg_colaboradores": """ <b>✦ Aquí está la lista de Desarrolladores de Rank: S 🏴‍☠️

 ↳ <a href='https://t.me/SawyerID'>🥇Sawyer(Fundador)</a>: Comenzó el proyecto

 ↳ <a href='https://t.me/ImNoCheating'>🥈ImNoCheating(Sub Owner)</a>: ayudó a programar

 ↳ <a href='https://chat.openai.com'>🥉ChatGPT(Master)</a>: conocimiento raro compartido


✦ ¡Tal vez algún día tu nombre pueda estar en esa lista! ¡Estad atentos!</b>

"""








    }
}
