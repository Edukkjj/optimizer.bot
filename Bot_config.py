import os
import time
from pywinauto import Application

# Abre as Configurações na Home
os.system("start ms-settings:home")

# Conecta e foca na janela
app = Application(backend="uia").connect(title="Configurações", timeout=20)
janela = app.window(title="Configurações")
janela.set_focus() ## foca a janela
    
# Clica em 'Sistema'

item_sistema = janela.child_window(title="Sistema", control_type="ListItem") ## vai achar o item pelo titulo e tipo.
item_sistema.wait('exists', timeout=10) ## Espera o item 'Sistema' existir
item_sistema.click_input()
print("Sucesso: Item 'Sistema' clicado!")

time.sleep(3) ## espera para a página carregar

# --- grupo Notificações ---
item_notificacoes = janela.child_window(title="Notificações", control_type="ListItem")
item_notificacoes.wait('enabled', timeout=10)
item_notificacoes.click_input()
    
print("Sucesso: Item 'Notificações' clicado manualmente!")

time.sleep(3)  

caixa_notif = janela.child_window(title="Notificações", control_type="Group")
caixa_notif.wait('exists', timeout=10)
caixa_notif.click_input()


    # 1 procurando CheckBox que comece com "Permitir que as notifica..."
caixa_nofic_sons = janela.child_window(
title="Permitir que as notificações reproduzam sons", 
control_type="CheckBox")
caixa_nofic_sons.wait('exists', timeout=10)
try: 
    print("procurando Permitir...")
    janela.set_focus()
    estado = caixa_nofic_sons.get_toggle_state()
    if estado == 0:
        print("Está desativado. ativando...")
        caixa_nofic_sons.click_input()
    else:
        print("Já está ativado.")
        
except Exception as e:
    print(f"Erro: O elemento não foi encontrado na página atual.")

    # 2. procurando CheckBox que comece com "Mostrar notificações na tela de bloqueio"
caixa_bloq = janela.child_window(
title="Mostrar notificações na tela de bloqueio", 
control_type="CheckBox")
caixa_bloq.wait('exists', timeout=10)
try: 
    print("procurando notificações...")
    janela.set_focus()
    estado = caixa_bloq.get_toggle_state() ## cria uma variável para armazenar o estado da caixa de seleção
    if estado == 0: ## 0 é desativado, 1 é ativado, se o estado for 0, ele vai clicar para ativar.
        print("Está desativado. ativando...")
        caixa_bloq.click_input()
    else:
        print("Já está ativado.")
        
except Exception as e: ## se o elemento não for encontrado, ele vai aparecer essa mensagem de erro.
    print(f"Erro: O elemento não foi encontrado na página atual.")

    # 3. procurando CheckBox que comece com "Mostrar lembretes"
caixa_voip = janela.child_window(
title="Mostrar lembretes e chamadas VoIP de entrada na tela de bloqueio", 
control_type="CheckBox")
caixa_voip.wait('exists', timeout=10)
try: 
    print("procurando mostrar...")
    janela.set_focus()
    estado = caixa_voip.get_toggle_state()
    if estado == 1:
        print("Está ativado. Desativando...")
        caixa_voip.click_input()
    else:
        print("Já está desativado.")
        
except Exception as e:
    print(f"Erro: O elemento não foi encontrado na página atual.")
    
    # 4. procurando CheckBox que comece com "mostrar ícone..."
caixa_icone = janela.child_window(
title="Mostrar ícone de sino de notificação",
control_type="CheckBox")
caixa_icone.wait('exists', timeout=10)
try: 
    print("procurando mostrar ícone...")
    janela.set_focus()
    estado = caixa_icone.get_toggle_state()
    if estado == 1:
        print("Está ativado. desativando...")
        caixa_icone.click_input()
    else:
        print("Já está desativado.")
except Exception as e:
    print(f"Erro: O elemento não foi encontrado na página atual.")

# --- grupo config add ---
caixa_config_ads = janela.child_window(
title="Configurações adicionais",
control_type="Group", depth=None) ## o depth=None é para procurar em toda a árvore de elementos. 
if caixa_config_ads.wait('exists', timeout=10):
   caixa_config_ads.iface_scroll_item.ScrollIntoView() ## rola a página para o elemento ficar visível.
   caixa_config_ads.click_input()
else: 
    print("Elemento não encontrado na árvore. Tentando rolar com teclado...")
    janela.set_focus()
    janela.type_keys("{PGDN}") ## se não achar com iface ele usa a tecla Page Down para rolar.
    caixa_config_ads.click_input()


# 1. procurando CheckBox que comece com "mostrar a..."
caixa_mostrar_config_add = janela.child_window(
title="Mostrar a experiência de boas-vindas do Windows após as atualizações e quando conectado para mostrar as novidades e as sugestões",
control_type="CheckBox")
try: 
    print("procurando mostrar a...")
    caixa_mostrar_config_add.wait('exists', timeout=5)
    caixa_mostrar_config_add.iface_scroll_item.ScrollIntoView()
    janela.set_focus()
    estado = caixa_mostrar_config_add.get_toggle_state()
    if estado == 1:
        print("Está ativado. desativando...")
        caixa_mostrar_config_add.click_input()
    else:
        print("Já está desativado.")
except Exception as e:
    print(f"Erro: O elemento não foi encontrado na página atual.")

time.sleep(1)  

# 2. procurando CheckBox que comece com "sugerir maneiras..."
caixa_sugerir_config_add = janela.child_window(
title="Sugerir maneiras de aproveitar ao máximo o Windows e concluir a configuração deste dispositivo",
control_type="CheckBox")
caixa_sugerir_config_add.wait('exists', timeout=10)
caixa_sugerir_config_add.iface_scroll_item.ScrollIntoView()
try: 
    print("procurando sugerir maneiras...")
    janela.set_focus()
    estado = caixa_sugerir_config_add.get_toggle_state()
    if estado == 1:
        print("Está ativado. desativando...")
        caixa_sugerir_config_add.click_input()
    else:
        print("Já está desativado.")
except Exception as e:
    print(f"Erro: O elemento não foi encontrado na página atual.")

time.sleep(1) 

# 3. procurando CheckBox que comece com "Obtenha dicas..."
caixa_obter_config_add = janela.child_window(
title="Obtenha dicas e sugestões ao usar o Windows",
control_type="CheckBox")
caixa_obter_config_add.wait('exists', timeout=10)
caixa_obter_config_add.iface_scroll_item.ScrollIntoView()
try: 
    print("procurando obter dicas...")
    janela.set_focus()
    estado = caixa_obter_config_add.get_toggle_state()
    if estado == 1:
        print("Está ativado. desativando...")
        caixa_obter_config_add.click_input()
    else:
        print("Já está desativado.")
except Exception as e:
    print(f"Erro: O elemento não foi encontrado na página atual.")

item_sistema = janela.child_window(title="Sistema", control_type="ListItem") ## vai achar o item pelo titulo e tipo.
item_sistema.wait('exists', timeout=10) ## Espera o item 'Sistema' existir
item_sistema.click_input()
print("Sucesso: Item 'Sistema' clicado!")

time.sleep(1) 

# --- grupo energia e bateria ---
grupo_energia_bateria = janela.child_window(title="Energia e bateria",
 control_type="Text")
grupo_energia_bateria.wait('exists', timeout=10)
grupo_energia_bateria.click_input()
    
print("Sucesso: Item 'Energia e bateria' clicado manualmente!")

time.sleep(1)  

# --- modo de energia ---
item_modo_energia = janela.child_window(title="Modo de Energia",
 control_type="Text")
item_modo_energia.wait('exists', timeout=10)
item_modo_energia.click_input()

print("Sucesso: Item 'Modo de Energia' clicado!")

