import time

def cantar_parabens(nome):
    print("Parabéns pra você,")
    time.sleep(1)
    print("Nesta data querida,")
    time.sleep(1)
    print("Muitas felicidades,")
    time.sleep(1)
    print("Muitos anos de vida!")
    time.sleep(1)
    print()
    print(f"Viva o {nome}! 🎉🎂")
    time.sleep(1)

def exibir_ascii_feliz_aniversario():
    ascii_art = """
     ███████╗███████╗██╗     ██╗███████╗     █████╗ ███╗   ██╗██╗██╗   ██╗ █████╗ ██████╗ ██╗   ██╗
     ██╔════╝██╔════╝██║     ██║██╔════╝    ██╔══██╗████╗  ██║██║██║   ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
     █████╗  █████╗  ██║     ██║███████╗    ███████║██╔██╗ ██║██║██║   ██║███████║██████╔╝ ╚████╔╝ 
     ██╔══╝  ██╔══╝  ██║     ██║╚════██║    ██╔══██║██║╚██╗██║██║╚██╗ ██╔╝██╔══██║██╔═══╝   ╚██╔╝  
     ███████╗███████╗███████╗██║███████║    ██║  ██║██║ ╚████║██║ ╚████╔╝ ██║  ██║██║        ██║   
     ╚══════╝╚══════╝╚══════╝╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝        ╚═╝   
    """
    print(ascii_art)

# Programa principal
nome_aluno = "Francisco De Assis"
cantar_parabens(nome_aluno)
exibir_ascii_feliz_aniversario()