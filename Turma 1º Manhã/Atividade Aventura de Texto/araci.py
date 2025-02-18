def aventura(): 
    print("Bem vindo a grande aventura!")
    print("Você está em uma floresta misteriosa e encontra um caminho dividido.")
    print("Um caminho leva a um castelo abandonado e o outro a uma caverna sombria.")
    print("Você precisa escolher para onde ir.")
    
    escolha1 = input("Para onde deseja ir? (1 - Castelo / 2 - Caverna): ")
    
    if escolha1 == "1":
        print("Você caminha até o castelo e percebe que ele está cheio de segredos.")
        print("Dentro, tem uma biblioteca misteriosa e uma porta secreta.")
        escolha2 = input("Deseja explorar a biblioteca (1) ou abrir a porta secreta (2)? ")
        
        if escolha2 == "1":
            print("Você encontra um livro mágico que lhe concede sabedoria infinita!")
            print("Com esse conhecimento, você se torna o maior sábio do reino.")
            print("FIM FELIZ!")
        else:
            print("A porta secreta leva a um calabouço! Você é capturado por fantasmas!")
            print("Preso para sempre, você se torna uma lenda assombrada.")
            print("FIM ASSUSTADOR!")
            
    
    elif escolha1 == "2":
        print("Você entra na caverna e sente uma presença estranha.")
        print("Lá dentro, você encontra um dragão adormecido e uma ponte quebrada.")
        escolha2 = input("Deseja enfrentar o dragão (1) ou tentar atravessar a ponte (2)? ")
        
        if escolha2 == "1":
            print("Você desafia o dragão e, contra todas as probabilidades, o derrota!")
            print("O povo o proclama um herói lendário.")
            print("FIM GLORIOSO!")
        else:
            print("A ponte estava frágil e você cai em um rio subterrâneo.")
            print("Você nunca mais é visto e sua história se torna um mistério.")
            print("FIM TRÁGICO!")
    
    else:
        print("Escolha inválida. Você fica parado até que a noite caia.")
        print("Monstros aparecem e você desaparece sem deixar rastros.")
        print("FIM?")

aventura()