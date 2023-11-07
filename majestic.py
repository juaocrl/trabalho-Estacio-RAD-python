# importações
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox 
import TKinterModernThemes as TKMT

# arquivos proprietarios
arq_prop = "proprietarios.txt"
arq_prop_leitura = open("proprietarios.txt", "r")
arq_prop_escrita = open("proprietarios.txt", "a")
# arquivos proprietarios

# arquivos Imovel
arq_imovel = "imovel.txt"
arq_imovel_leitura = open("imovel.txt", "r")
arq_imovel_escrita = open("imovel.txt", "a")
# arquivos Imovel

# arquivos Automovel
arq_automovel = "automovel.txt"
arq_automovel_leitura = open("automovel.txt", "r")
arq_automovel_escrita = open("automovel.txt", "a")
# arquivos Automovel

# arquivos administrador
arq_administrador = "administrador.txt"
arq_administrador_leitura = open("administrador.txt", "r")
arq_administrador_escrita = open("administrador.txt", "a")
# arquivos administrador

def onClick_voltar():
    window_inserirprop.root.withdraw()
    window_main.root.deiconify()

def limpardono():
    varnome.set("")
    varcpf.set("")
    varapartemento.set("")
    varBloco.set("")
    varPlaca.set("")
    varModelo.set("")
    varCor.set("")

#----------------EXCLUIR_PROPRIETARIO_INICIO----------------------------------------------------->
def onClick_btnPropDel():
    global txt_PropDel
    window_PropDel = TKMT.ThemedTKinterFrame("Deletar Proprietário", "azure", "dark")
    window_PropDel.root.geometry("300x220")
    LabelPropDel = Label(window_PropDel.root, text="Digite o CPF do proprietário\n que deseja deletar: ")
    LabelPropDel.grid(row=0, column=1, pady=(1,1), padx=(70,70))

    varPropDel = StringVar()
    txt_PropDel = Entry(window_PropDel.root, textvariable=varPropDel)
    txt_PropDel.insert(END, string="")
    txt_PropDel.grid(row=1, column=1,pady=(5,5))

    btn_PropDel = Button(window_PropDel.root, text="Deletar", command=onClick_btnPropDeletou)
    btn_PropDel.grid(row=2, column=1, pady=(10,10))
   
def onClick_btnPropDeletou():
    # Lê o conteúdo atual do arquivo de proprietários
    cpf_del=txt_PropDel.get()
    with open("proprietarios.txt", "r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
    encontrado = False
    # Procura a linha com o CPF correspondente
    for i, linha in enumerate(linhas):
        dados = linha.strip().split(',')
        if dados[1] == cpf_del:
            encontrado = True
            del linhas[i]
            break         
    if encontrado:
        # Salva as alterações no arquivo
        with open("proprietarios.txt", "w", encoding="UTF-8") as arquivo:
            arquivo.writelines(linhas)
        confirma = f"O proprietário foi deletado com sucesso."
        messagebox.showinfo(message=confirma)
    else:
        nconfirma = (f"Proprietário com CPF {cpf_del} não encontrado.")
        messagebox.showinfo(message=nconfirma)

#----------------EXCLUIR_PROPRIETARIO_FINAL------------------------------------------------------>  
  
#----------------EXCLUIR_IMOVEL_INICIO----------------------------------------------------------->

def onClick_btnImovelDel():
    global txt_Imovel_del
    window_ImovelDel = TKMT.ThemedTKinterFrame("Deletar imovel", "azure", "dark")
    window_ImovelDel.root.geometry("300x220")
    LabelImovelDel = Label(window_ImovelDel.root, text="Digite o Id do imovel do proprietário\n que deseja deletar: ")
    LabelImovelDel.grid(row=0, column=1, pady=(1,1), padx=(70,70))

    varImoveldel = StringVar()
    txt_Imovel_del = Entry(window_ImovelDel.root, textvariable=varImoveldel)
    txt_Imovel_del.insert(END, string="")
    txt_Imovel_del.grid(row=1, column=1,pady=(5,5))

    btn_ImovelDel = Button(window_ImovelDel.root, text="Deletar", command=onClick_btnImovelDeletou)
    btn_ImovelDel.grid(row=2, column=1, pady=(10,10))
    
def onClick_btnImovelDeletou():
       # Lê o conteúdo atual do arquivo de proprietários
    Imovel_del=txt_Imovel_del.get()
    with open("imovel.txt", "r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
    encontrado = False
    # Procura a linha com o CPF correspondente
    for i, linha in enumerate(linhas):
        dados = linha.strip().split(',')
        if dados[1] == Imovel_del:
            encontrado = True
            del linhas[i]
            break
    if encontrado:
        # Salva as alterações no arquivo
        with open("imovel.txt", "w", encoding="UTF-8") as arquivo:
            arquivo.writelines(linhas)
        confirma = (f"O imovel foi deletado com sucesso.")
        messagebox.showinfo(message=confirma)
    else:
        nconfirma = (f"O imovel {Imovel_del} não encontrado.")
        messagebox.showinfo(message=nconfirma)


#----------------EXCLUIR_IMOVEL_FINAL------------------------------------------------------------>

#----------------EXCLUIR_AUTOMOVEL_INICIO-------------------------------------------------------->

def onClick_btnAutoDel():
    global txt_Placa_del
    window_AutoDel = TKMT.ThemedTKinterFrame("Deletar automovel", "azure", "dark")
    window_AutoDel.root.geometry("300x220")
    LabelPropDel = Label(window_AutoDel.root, text="Digite aplaca do automovel\n que deseja deletar: ")
    LabelPropDel.grid(row=0, column=1, pady=(1,1), padx=(70,70))

    varPlacadel = StringVar()
    txt_Placa_del = Entry(window_AutoDel.root, textvariable=varPlacadel)
    txt_Placa_del.insert(END, string="")
    txt_Placa_del.grid(row=1, column=1,pady=(5,5))

    btn_Placa_Del = Button(window_AutoDel.root, text="Deletar", command=onClick_btnAutoDeletou)
    btn_Placa_Del.grid(row=2, column=1, pady=(10,10))

def onClick_btnAutoDeletou():
       # Lê o conteúdo atual do arquivo de proprietários
    placa_del=txt_Placa_del.get()
    with open("automovel.txt", "r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
    encontrado = False
    # Procura a linha com o CPF correspondente
    for i, linha in enumerate(linhas):
        dados = linha.strip().split(',')
        if dados[1] ==  placa_del:
            encontrado = True
            del linhas[i]
            break         
    if encontrado:
        # Salva as alterações no arquivo
        with open("automovel.txt", "w", encoding="UTF-8") as arquivo:
            arquivo.writelines(linhas)
        confirma = f"O automovel foi deletado com sucesso."
        messagebox.showinfo(message=confirma)
    else:
        nconfirma = (f"O automovel com a placa:{placa_del} não encontrado.")
        messagebox.showinfo(message=nconfirma)

#----------------EXCLUIR_AUTOMOVEL_FINAL--------------------------------------------------------->

#----------------EXCLUIR_ADMINISTRADOR_INICIO---------------------------------------------------->

def onClick_btnAdminiDel():
    global txt_AdminiDel
    window_AdminiDel = TKMT.ThemedTKinterFrame("Deletar Proprietário", "azure", "dark")
    window_AdminiDel.root.geometry("300x220")
    LabelAdminiDel = Label(window_AdminiDel.root, text="Digite o CPF do administrador\n que deseja deletar: ")
    LabelAdminiDel.grid(row=0, column=1, pady=(1,1), padx=(70,70))

    varAdminiDel = StringVar()
    txt_AdminiDel = Entry(window_AdminiDel.root, textvariable=varAdminiDel)
    txt_AdminiDel.insert(END, string="")
    txt_AdminiDel.grid(row=1, column=1,pady=(5,5))

    btn_AdminiDel = Button(window_AdminiDel.root, text="Deletar", command=onClick_btnAdminiDeletou)
    btn_AdminiDel.grid(row=2, column=1, pady=(10,10))

def onClick_btnAdminiDeletou():
       # Lê o conteúdo atual do arquivo de proprietários
    AdminiDeletou=txt_AdminiDel.get()
    with open("administrador.txt", "r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
    encontrado = False
    # Procura a linha com o CPF correspondente
    for i, linha in enumerate(linhas):
        dados = linha.strip().split(',')
        if dados[1] == AdminiDeletou:
            encontrado = True
            del linhas[i]
            break         
    if encontrado:
        # Salva as alterações no arquivo
        with open("administrador.txt", "w", encoding="UTF-8") as arquivo:
            arquivo.writelines(linhas)
        confirma = f"O administrador foi deletado com sucesso."
        messagebox.showinfo(message=confirma)
    else:
        nconfirma = (f"O administrador com o CPF: {AdminiDeletou} não encontrado.")
        messagebox.showinfo(message=nconfirma)

#----------------EXCLUIR_ADMINISTRADOR_FINAL----------------------------------------------------->



#----------------EDITAR_PROPRIETARIO_INICIO------------------------------------------------------->
# tela grafica ediçao do proprietario
def onClick_btnPropEdit():
    global cpf_entry,nome_var
    window_main.root.withdraw()
    window_PropEdit = TKMT.ThemedTKinterFrame("Editar cadastro ", "azure", "dark")
    window_PropEdit.root.geometry("600x300")
    
    # Entrada para digitar o CPF
    cpf_label = tk.Label(window_PropEdit.root, text="CPF:")
    cpf_label.grid(row=0, column=0, sticky="e")
    cpf_entry = tk.Entry(window_PropEdit.root)
    cpf_entry.grid(row=0, column=1)

    # Botão para buscar o CPF
    buscar_button = tk.Button(window_PropEdit.root, text="Buscar", command=buscar_cpfProp_edit)
    buscar_button.grid(row=0, column=2)

    # Entradas para nome
    nome_label = tk.Label(window_PropEdit.root, text="Nome:")
    nome_label.grid(row=1, column=0, sticky="e")
    nome_var = tk.StringVar()
    nome_entry = tk.Entry(window_PropEdit.root, textvariable=nome_var)
    nome_entry.grid(row=1, column=1)

    # Botão para salvar a edição na coluna 1 (segunda coluna)
    salvar_button = tk.Button(window_PropEdit.root, text="Salvar Edição", command=salvar_edicao)
    salvar_button.grid(row=2, column=0, columnspan=3)
    window_PropEdit.root.mainloop()
# Função para buscar um CPF no arquivo proprietarios.txt    
def buscar_cpfProp_edit():
    cpf = cpf_entry.get()
    with open('proprietarios.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[1] == cpf:
                nome_var.set(campos[0])
                break
        else:
            print("CPF não encontrado: " + cpf)
# Função para salvar a edição 
def salvar_edicao():
    cpf = cpf_entry.get()
    nome = nome_var.get()
    linhas = []
    with open('proprietarios.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[1] == cpf:
                linhas.append(f'{nome},{cpf}\n')
            else:
                linhas.append(linha)
    with open('proprietarios.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    nome_var.set('')
    cpf_entry.delete(0, 'end')
#----------------EDITAR_PROPRIETARIO_FIM---------------------------------------------------------->

#----------------EDITAR_IMOVEL_INICIO------------------------------------------------------------->
# tela grafica ediçao do Imovel
def onClick_btnImovelEdit():
    global imovel_entry,imovel_var,id_entry
    window_main.root.withdraw()
    window_ImovelEdit = TKMT.ThemedTKinterFrame("Editar cadastro ", "azure", "dark")
    window_ImovelEdit.root.geometry("600x300")
    
    # Entrada para digitar o CPF
    id_label = tk.Label(window_ImovelEdit.root, text="id:")
    id_label.grid(row=0, column=0, sticky="e")

    id_entry = tk.Entry(window_ImovelEdit.root)
    id_entry.grid(row=0, column=1)

    # Botão para buscar o CPF
    buscar_button = tk.Button(window_ImovelEdit.root, text="Buscar", command=buscar_Imovel_edit)
    buscar_button.grid(row=0, column=2)

    # Entradas para nome
    imovel_label = tk.Label(window_ImovelEdit.root, text="Nome:")
    imovel_label.grid(row=1, column=0, sticky="e")


    imovel_var = tk.StringVar()
    imovel_entry = tk.Entry(window_ImovelEdit.root, textvariable=imovel_var)
    imovel_entry.grid(row=1, column=1)

    # Botão para salvar a edição na coluna 1 (segunda coluna)
    salvar_button = tk.Button(window_ImovelEdit.root, text="Salvar Edição", command=salvar_edicao_imovel)
    salvar_button.grid(row=2, column=0, columnspan=3)
    window_ImovelEdit.root.mainloop()
# Função para buscar um imovel no arquivo Imovel.txt    
def buscar_Imovel_edit():
    idimoveledit = id_entry.get()
    with open('imovel.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[1] == idimoveledit:
                imovel_var.set(campos[0])
                break
            else:
                print("ID não encontrado: " + idimoveledit)

# Função para salvar a edição 
def salvar_edicao_imovel():
    idimovel= id_entry.get()
    nomeimovel = imovel_entry.get()
    linhas = []
    with open('imovel.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[1] == idimovel:
                linhas.append(f'{nomeimovel},{idimovel}\n')
            else:
                linhas.append(linha)
    with open('imovel.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    imovel_var.set('')
    id_entry.delete(0, 'end')
#----------------EDITAR_IMOVEL_FIM-------------------------------------------------------------->

#----------------EDITAR_AUTOMOVEL_INICIO-------------------------------------------------------->
# tela grafica ediçao do Imovel
def onClick_btnAutoEdit():
    global placa_entry,modelo_entry,cor_entry,modelo_var,cor_var
    window_main.root.withdraw()
    window_AutoEdit = TKMT.ThemedTKinterFrame("editar cadastro", "azure", "dark")
    window_AutoEdit.root.geometry("600x300")
    
    # Entrada para digitar a placa
    placa_label = tk.Label(window_AutoEdit.root, text="Placa:")
    placa_label.grid(row=0, column=0, sticky="e")

    placa_entry = tk.Entry(window_AutoEdit.root)
    placa_entry.grid(row=0, column=1)

    # Botão para buscar a placa
    buscar_button = tk.Button(window_AutoEdit.root, text="Buscar", command=buscar_automovel_edit)
    buscar_button.grid(row=0, column=2)

    # Entradas para modelo
    modelo_label = tk.Label(window_AutoEdit.root, text="modelo:")
    modelo_label.grid(row=1, column=0, sticky="e")
    modelo_var = tk.StringVar()
    modelo_entry = tk.Entry(window_AutoEdit.root, textvariable=modelo_var)
    modelo_entry.grid(row=1, column=1)
    # Entradas para cor
    cor_label = tk.Label(window_AutoEdit.root, text="cor:")
    cor_label.grid(row=2, column=0, sticky="e")
    cor_var = tk.StringVar()
    cor_entry = tk.Entry(window_AutoEdit.root, textvariable=cor_var)
    cor_entry.grid(row=2, column=1)

    # Botão para salvar a edição na coluna 1 (segunda coluna)
    salvar_button = tk.Button(window_AutoEdit.root, text="Salvar Edição", command=salvar_edicao_automovel)
    salvar_button.grid(row=3, column=0, columnspan=3)
    window_AutoEdit.root.mainloop()
# Função para buscar um imovel no arquivo Imovel.txt    
def buscar_automovel_edit():
    placa = placa_entry.get()
    
    with open('automovel.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[0] == placa:
                modelo_var.set(campos[1])
                cor_var.set(campos[2])
                break
        else:
            print("Placa não encontrada: " + placa)
# Função para salvar a edição 
def salvar_edicao_automovel():
    placa = placa_entry.get()
    modelo = modelo_entry.get()
    cor = cor_entry.get()
    linhas = []
    with open('automovel.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[0] == placa:
                linhas.append(f'{placa},{modelo},{cor}\n')
            else:
                linhas.append(linha)
    with open('automovel.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    modelo_var.set('')
    cor_var.set('')
    placa_entry.delete(0, 'end')
#----------------EDITAR_AUTOMOVEL_FIM---------------------------------------------------------->

#----------------EDITAR_ADMINISTRADOR_INICIO-------------------------------------------------------->
# tela grafica ediçao do Imovel
def onClick_btnAdminiEdit():
    global cpf_entry,nome_var
    window_main.root.withdraw()
    window_AdminiEdit = TKMT.ThemedTKinterFrame("Proprietários cadastrados ", "azure", "dark")
    window_AdminiEdit.root.geometry("600x300")
    
    # Entrada para digitar o CPF
    cpf_label = tk.Label(window_AdminiEdit.root, text="CPF:")
    cpf_label.grid(row=0, column=0, sticky="e")
    cpf_entry = tk.Entry(window_AdminiEdit.root)
    cpf_entry.grid(row=0, column=1)

    # Botão para buscar o CPF
    buscar_button = tk.Button(window_AdminiEdit.root, text="Buscar", command=buscar_cpfAdmin_edit)
    buscar_button.grid(row=0, column=2)

    # Entradas para nome
    nome_label = tk.Label(window_AdminiEdit.root, text="Nome:")
    nome_label.grid(row=1, column=0, sticky="e")
    nome_var = tk.StringVar()
    nome_entry = tk.Entry(window_AdminiEdit.root, textvariable=nome_var)
    nome_entry.grid(row=1, column=1)

    # Botão para salvar a edição na coluna 1 (segunda coluna)
    salvar_button = tk.Button(window_AdminiEdit.root, text="Salvar Edição", command=salvar_edicao_administrador)
    salvar_button.grid(row=2, column=0, columnspan=3)
    window_AdminiEdit.root.root.mainloop()
# Função para buscar um CPF no arquivo administrador.txt    
def buscar_cpfAdmin_edit():
    cpf = cpf_entry.get()
    with open('administrador.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[1] == cpf:
                nome_var.set(campos[0])
                break
        else:
            print("CPF não encontrado: " + cpf)
# Função para salvar a edição 
def salvar_edicao_administrador():
    cpf = cpf_entry.get()
    nome = nome_var.get()
    linhas = []
    with open('administrador.txt', 'r') as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(',')
            if campos[1] == cpf:
                linhas.append(f'{nome},{cpf}\n')
            else:
                linhas.append(linha)
    with open('administrador.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    nome_var.set('')
    cpf_entry.delete(0, 'end')
#----------------EDITAR_ADMINISTRADOR_FIM---------------------------------------------------------->


#----------------EDITAR_FIM---------------------------------------------------------------------->

#----------------REGISTRAR_INICIO---------------------------------------------------------------->

def registrarProp():
    global txt_nome, txt_cpf
    novonome = txt_nome.get()
    novocpf = txt_cpf.get()
    with open(arq_prop, 'a') as f:
        f.write(f"{novonome},{novocpf}\n")
    confirma = f"O proprietário: {novonome} - CPF:{novocpf} foi cadastrado com sucesso."
    messagebox.showinfo(message=confirma)

def registrarImovel():
    global txt_apartemento
    novoid = txt_apartemento_id.get()
    novoapartemento = txt_apartemento.get()
    with open(arq_imovel, 'a') as f:
        f.write(f"{novoapartemento},{novoid}\n")
    confirma = f"O imovel: {novoapartemento} foi cadastrado com sucesso."
    messagebox.showinfo(message=confirma)

def registrarAuto():
    global txt_Placa, txt_Modelo, txt_Cor
    novoPlaca = txt_Placa.get()
    novoModelo = txt_Modelo.get()
    novoCor = txt_Cor.get()
    with open(arq_automovel, 'a') as f:
        f.write(f"{novoPlaca},{novoModelo},{novoCor}\n")
    confirma = f"O automovel: {novoModelo} - Placa:{novoPlaca} foi cadastrado com sucesso."
    messagebox.showinfo(message=confirma)

def registrarAdmin():
    global txt_nome, txt_cpf
    novonome = txt_nome.get()
    novocpf = txt_cpf.get()
    with open(arq_administrador, 'a') as f:
        f.write(f"{novonome},{novocpf}\n")
    confirma = f"O Administrador: {novonome} - CPF:{novocpf} foi cadastrado com sucesso."
    messagebox.showinfo(message=confirma)

#----------------REGISTRAR_FIM-------------------------------------------------------------------->

#----------------TELAS_DE_CONSULTA_INICIO--------------------------------------------------------->

def onClick_btnPropConsul():
    global window_PropConsul
    window_main.root.withdraw()
    window_PropConsul = TKMT.ThemedTKinterFrame("Proprietários cadastrados ", "azure", "dark")
    window_PropConsul.root.geometry("600x300")
    L6 = Label(window_PropConsul.root, text="Proprietários cadastrados")
    L6.grid(row=0, column=1,)
    with open("proprietarios.txt", encoding="UTF-8") as file:
        file_list = []
        for line in file:
            file_list.append(line)
            texto_converte = "\n".join(file_list)
            texto_ja_convertido = re.sub(r'{}', '', texto_converte)
    L7 = Label(window_PropConsul.root, text= texto_ja_convertido )
    L7.grid(row=2, column=1,)
    btn_voltar = Button(window_PropConsul.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=0, column=0,)

def onClick_btnImovelConsul():
    global window_ImovelConsul
    window_main.root.withdraw()
    window_ImovelConsul = TKMT.ThemedTKinterFrame("Imoveis cadastrados ", "azure", "dark")
    window_ImovelConsul.root.geometry("600x300")
    L6 = Label(window_ImovelConsul.root, text="Imoveis cadastrados")
    L6.grid(row=0, column=1,)
    with open("imovel.txt", encoding="UTF-8") as file:
        file_list = []
        for line in file:
            file_list.append(line)
            texto_converte = "\n".join(file_list)
            texto_ja_convertido = re.sub(r'{}', '', texto_converte)
    L7 = Label(window_ImovelConsul.root, text= texto_ja_convertido )
    L7.grid(row=2, column=1,)
    btn_voltar = Button(window_ImovelConsul.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=0, column=0,)

def onClick_btnAutoConsul():
    global window_AutoConsul
    window_main.root.withdraw()
    window_AutoConsul = TKMT.ThemedTKinterFrame("Automóveis cadastrados ", "azure", "dark")
    window_AutoConsul.root.geometry("600x300")
    L6 = Label(window_AutoConsul.root, text="Automóveis cadastrados")
    L6.grid(row=0, column=1,)
    with open("automovel.txt", encoding="UTF-8") as file:
        file_list = []
        for line in file:
            file_list.append(line)
            texto_converte = "\n".join(file_list)
            texto_ja_convertido = re.sub(r'{}', '', texto_converte)
    L7 = Label(window_AutoConsul.root, text= texto_ja_convertido )
    L7.grid(row=2, column=1,)
    btn_voltar = Button(window_AutoConsul.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=0, column=0,)
   
def onClick_btnAdminiConsul():
    global window_inserirprop
    window_main.root.withdraw()
    window_inserirprop = TKMT.ThemedTKinterFrame("Administradores cadastrados", "azure", "dark")
    window_inserirprop.root.geometry("600x300")
    L6 = Label(window_inserirprop.root, text="Administradores cadastrados")
    L6.grid(row=0, column=1,)
    with open("administrador.txt", encoding="UTF-8") as file:
        file_list = []
        for line in file:
            file_list.append(line)
            texto_converte = "\n".join(file_list)
            texto_ja_convertido = re.sub(r'{}', '', texto_converte)
    L7 = Label(window_inserirprop.root, text= texto_ja_convertido )
    L7.grid(row=2, column=1,)
    btn_voltar = Button(window_inserirprop.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=0, column=0,)

#----------------TELAS_DE_CONSULTA_FIM------------------------------------------------------------>

#----------------TELAS_DE_CADASTRO_INICIO--------------------------------------------------------->

def onClick_btnPropCadas():
    global varnome, txt_nome, varcpf, txt_cpf, varBloco, varPlaca, varModelo, varCor, varapartemento, window_PropCadas, txt_apartemento, txt_Bloco, txt_Placa, txt_Modelo, txt_Cor
    window_main.root.withdraw()
    window_PropCadas = TKMT.ThemedTKinterFrame("Novo Proprietário", "azure", "dark")
    window_PropCadas.root.geometry("280x500")

    
    Nome_Completo = Label(window_PropCadas.root, text="Nome Completo:")
    Nome_Completo.grid(row=2, column=0,pady=(5,5))
    CPF_Proprietario = Label(window_PropCadas.root, text="CPF:")
    CPF_Proprietario.grid(row=3, column=0,pady=(5,5))
    
    

    varnome = StringVar()
    txt_nome = Entry(window_PropCadas.root, textvariable=varnome)
    txt_nome.insert(END, string="")
    txt_nome.grid(row=2, column=1,pady=(5,5))
    
    
    varcpf = StringVar()
    txt_cpf = Entry(window_PropCadas.root, textvariable=varcpf)
    txt_cpf.insert(END, string="")
    txt_cpf.grid(row=3, column=1,pady=(5,5))
    btn_inserirdono = Button(window_PropCadas.root, text="Cadastrar", command=registrarProp)
    btn_inserirdono.grid(row=9, column=0, pady=(10,10))
    btn_limpardono = Button(window_PropCadas.root, text="Limpar", command=limpardono)
    btn_limpardono.grid(row=9, column=1, pady=(10,10))
    btn_voltar = Button(window_PropCadas.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=10, column=0, pady=(10,10))
    
def onClick_btnImovelCadas():
    global varnome, txt_nome, varcpf, txt_cpf, varapartemento, window_ImovelCadas, txt_apartemento,  txt_apartemento_id 
    window_main.root.withdraw()
    window_ImovelCadas = TKMT.ThemedTKinterFrame("Novo Imovel", "azure", "dark")
    window_ImovelCadas.root.geometry("280x500")

    Apartemento_Proprietario = Label(window_ImovelCadas.root, text="Apartemento:")
    Apartemento_Proprietario.grid(row=5, column=0,pady=(5,5))

    Apartemento_Proprietario_id = Label(window_ImovelCadas.root, text="id")
    Apartemento_Proprietario_id.grid(row=4, column=0,pady=(5,5))

    varapartementoid= StringVar()
    txt_apartemento_id = Entry(window_ImovelCadas.root, textvariable=varapartementoid)
    txt_apartemento_id.insert(END, string="")
    txt_apartemento_id.grid(row=4, column=1,pady=(5,5))

    varapartemento= StringVar()
    txt_apartemento = Entry(window_ImovelCadas.root, textvariable=varapartemento)
    txt_apartemento.insert(END, string="")
    txt_apartemento.grid(row=5, column=1,pady=(5,5))


    btn_inserirdono = Button(window_ImovelCadas.root, text="Cadastrar", command=registrarImovel)
    btn_inserirdono.grid(row=9, column=0, pady=(10,10))
    btn_limpardono = Button(window_ImovelCadas.root, text="Limpar", command=limpardono)
    btn_limpardono.grid(row=9, column=1, pady=(10,10))
    btn_voltar = Button(window_ImovelCadas.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=10, column=0, pady=(10,10))
    
def onClick_btnAutoCadas():
    global varnome, txt_nome, varcpf, txt_cpf, varBloco, varPlaca, varModelo, varCor, varapartemento, window_inserirprop, txt_apartemento, txt_Bloco, txt_Placa, txt_Modelo, txt_Cor
    window_main.root.withdraw()
    window_AutoCadas = TKMT.ThemedTKinterFrame("Novo Proprietário", "azure", "dark")
    window_AutoCadas.root.geometry("280x500")


    Placa_carro_Proprietario = Label(window_AutoCadas.root, text="Placa:")
    Placa_carro_Proprietario.grid(row=6, column=0,pady=(5,5))
    Modelo_carro_Proprietario = Label(window_AutoCadas.root, text="Modelo:")
    Modelo_carro_Proprietario.grid(row=7, column=0,pady=(5,5))
    Cor_carro_Proprietario = Label(window_AutoCadas.root, text="Cor:")
    Cor_carro_Proprietario.grid(row=8, column=0,pady=(5,5))


    varPlaca = StringVar()
    txt_Placa = Entry(window_AutoCadas.root, textvariable=varPlaca)
    txt_Placa.insert(END, string="")
    txt_Placa.grid(row=6, column=1,pady=(5,5))

    varModelo = StringVar()
    txt_Modelo = Entry(window_AutoCadas.root, textvariable=varModelo)
    txt_Modelo.insert(END, string="")
    txt_Modelo.grid(row=7, column=1,pady=(5,5))

    varCor = StringVar()
    txt_Cor = Entry(window_AutoCadas.root, textvariable=varCor)
    txt_Cor.insert(END, string="")
    txt_Cor.grid(row=8, column=1, pady=(5,5))

    btn_inserirdono = Button(window_AutoCadas.root, text="Cadastrar", command=registrarAuto)
    btn_inserirdono.grid(row=9, column=0, pady=(10,10))
    btn_limpardono = Button(window_AutoCadas.root, text="Limpar", command=limpardono)
    btn_limpardono.grid(row=9, column=1, pady=(10,10))
    btn_voltar = Button(window_AutoCadas.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=10, column=0, pady=(10,10))

def onClick_btnAdminiCadas():
    global varnome, txt_nome, varcpf, txt_cpf, varBloco, varPlaca, varModelo, varCor, varapartemento, window_inserirprop, txt_apartemento, txt_Bloco, txt_Placa, txt_Modelo, txt_Cor
    window_main.root.withdraw()
    window_inserirprop = TKMT.ThemedTKinterFrame("Novo Proprietário", "azure", "dark")
    window_inserirprop.root.geometry("280x500")

    
    Nome_Completo = Label(window_inserirprop.root, text="Nome Completo:")
    Nome_Completo.grid(row=2, column=0,pady=(5,5))
    CPF_Proprietario = Label(window_inserirprop.root, text="CPF:")
    CPF_Proprietario.grid(row=3, column=0,pady=(5,5))
    
    

    varnome = StringVar()
    txt_nome = Entry(window_inserirprop.root, textvariable=varnome)
    txt_nome.insert(END, string="")
    txt_nome.grid(row=2, column=1,pady=(5,5))
    
    
    varcpf = StringVar()
    txt_cpf = Entry(window_inserirprop.root, textvariable=varcpf)
    txt_cpf.insert(END, string="")
    txt_cpf.grid(row=3, column=1,pady=(5,5))
    btn_inserirdono = Button(window_inserirprop.root, text="Cadastrar", command=registrarAdmin)
    btn_inserirdono.grid(row=9, column=0, pady=(10,10))
    btn_limpardono = Button(window_inserirprop.root, text="Limpar", command=limpardono)
    btn_limpardono.grid(row=9, column=1, pady=(10,10))
    btn_voltar = Button(window_inserirprop.root, text="<- Voltar ao menu", command=onClick_voltar)
    btn_voltar.grid(row=10, column=0, pady=(10,10))
      
#----------------TELAS_DE_CADASTRO_FIM------------------------------------------------------------>

def onClick_btnProp():
    window_main = TKMT.ThemedTKinterFrame("Proprietário", "azure", "dark")
    window_main.root.geometry("300x300")
    L1 = Label(window_main.root, text="MENU Proprietário")
    L1.grid(row=1, column=1, pady=(1,1), padx=(70,70))

    #  botão Cadastrar Proprietário
    btn_novoprop = Button(window_main.root, text="Cadastrar Proprietário", command=onClick_btnPropCadas)
    btn_novoprop.grid(row=2, column=1, pady=(2,2), padx=(70,70))

    #  botão Consultar Proprietário
    btn_novoprop = Button(window_main.root, text="Consultar Proprietário", command=onClick_btnPropConsul)
    btn_novoprop.grid(row=3, column=1, pady=(2,2), padx=(70,70))

    #  botão Editar Cadastro do Proprietário 
    btn_novoprop = Button(window_main.root, text="Editar Proprietário", command=onClick_btnPropEdit)
    btn_novoprop.grid(row=4, column=1, pady=(2,2), padx=(70,70))
    #  botão Excluir Cadastro do Proprietário 
    btn_novoprop = Button(window_main.root, text="Excluir Proprietário", command=onClick_btnPropDel)
    btn_novoprop.grid(row=5, column=1, pady=(2,2), padx=(70,70))

    window_main.root.mainloop()

def onClick_btnImovel():
    window_main = TKMT.ThemedTKinterFrame("Imovel", "azure", "dark")
    window_main.root.geometry("300x300")
    L1 = Label(window_main.root, text="MENU Imovel")
    L1.grid(row=1, column=1, pady=(1,1), padx=(70,70))

    # botão Cadastrar Imovel
    btn_novoprop = Button(window_main.root, text="Cadastrar Imovel", command=onClick_btnImovelCadas)
    btn_novoprop.grid(row=2, column=1, pady=(2,2), padx=(70,70))

    # botão Consultar Imovel
    btn_novoprop = Button(window_main.root, text="Consultar Imovel", command=onClick_btnImovelConsul)
    btn_novoprop.grid(row=3, column=1, pady=(2,2), padx=(70,70))

    # botão Editar cadastro  do Imovel 
    btn_novoprop = Button(window_main.root, text="Editar Imovel", command=onClick_btnImovelEdit)
    btn_novoprop.grid(row=4, column=1, pady=(2,2), padx=(70,70))
    # botão Excluir cadastro do Imovel 
    btn_novoprop = Button(window_main.root, text="Excluir Imovel", command=onClick_btnImovelDel)
    btn_novoprop.grid(row=5, column=1, pady=(2,2), padx=(70,70))

def onClick_btnAuto():
    window_main = TKMT.ThemedTKinterFrame("Automovel", "azure", "dark")
    window_main.root.geometry("300x300")
    L1 = Label(window_main.root, text="MENU Automovel")
    L1.grid(row=1, column=1, pady=(1,1), padx=(70,70))

    # botão Cadastrar Automovel
    btn_novoprop = Button(window_main.root, text="Cadastrar Automovel", command=onClick_btnAutoCadas)
    btn_novoprop.grid(row=2, column=1, pady=(2,2), padx=(70,70))

    # botão consultar Automovel
    btn_novoprop = Button(window_main.root, text="Consultar Automovel", command=onClick_btnAutoConsul)
    btn_novoprop.grid(row=3, column=1, pady=(2,2), padx=(70,70))

    # botão editar cadastro do Automovel 
    btn_novoprop = Button(window_main.root, text="Editar Automovel", command=onClick_btnAutoEdit)
    btn_novoprop.grid(row=4, column=1, pady=(2,2), padx=(70,70))
    # botão Excluir cadastro do Automovel 
    btn_novoprop = Button(window_main.root, text="Excluir Automovel", command=onClick_btnAutoDel)
    btn_novoprop.grid(row=5, column=1, pady=(2,2), padx=(70,70))

def onClick_btnAdmini():
    window_main = TKMT.ThemedTKinterFrame("Administrador", "azure", "dark")
    window_main.root.geometry("300x300")
    L1 = Label(window_main.root, text="MENU Administrador")
    L1.grid(row=1, column=1, pady=(1,1), padx=(70,70))

    # janela principal - botão Cadastrar Administrador
    btn_novoprop = Button(window_main.root, text="Cadastrar Administrador", command=onClick_btnAdminiCadas)
    btn_novoprop.grid(row=2, column=1, pady=(2,2), padx=(70,70))

    # janela principal - botão Consultar Administradores
    btn_novoprop = Button(window_main.root, text="Consultar Administrador", command=onClick_btnAdminiConsul)
    btn_novoprop.grid(row=3, column=1, pady=(2,2), padx=(70,70))

    # janela principal - botão editar cadastro Administrador 
    btn_novoprop = Button(window_main.root, text="Editar Administrador", command=onClick_btnAdminiEdit)
    btn_novoprop.grid(row=4, column=1, pady=(2,2), padx=(70,70))
    # janela principal - botão Excluir cadastro Administrador 
    btn_novoprop = Button(window_main.root, text="Excluir Administrador", command=onClick_btnAdminiDel)
    btn_novoprop.grid(row=5, column=1, pady=(2,2), padx=(70,70))


# janela principal - inicio --------------------------------------------------------------------->

window_main = TKMT.ThemedTKinterFrame("Menu", "azure", "dark")
window_main.root.geometry("300x300")
L1 = Label(window_main.root, text="MENU")
L1.grid(row=0, column=1, pady=(1,1), padx=(70,70))

# janela principal - botão Cadastrar Proprietário
btn_novoprop = Button(window_main.root, text="Proprietário", command=onClick_btnProp)
btn_novoprop.grid(row=1, column=1, pady=(2,2), padx=(70,70))

# janela principal - botão consultar Proprietário
btn_novoprop = Button(window_main.root, text="Imovel", command=onClick_btnImovel)
btn_novoprop.grid(row=2, column=1, pady=(2,2), padx=(70,70))

# janela principal - botão editar cadastro Proprietário 
btn_novoprop = Button(window_main.root, text="Automovel", command=onClick_btnAuto)
btn_novoprop.grid(row=3, column=1, pady=(2,2), padx=(70,70))
# janela principal - botão editar cadastro Proprietário 
btn_novoprop = Button(window_main.root, text="Administrador", command=onClick_btnAdmini)
btn_novoprop.grid(row=4, column=1, pady=(2,2), padx=(70,70))

window_main.root.mainloop()

#janela principal - fim --------------------------------------------------------------------------------->

