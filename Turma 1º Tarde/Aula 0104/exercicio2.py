precoLivro = float(input("Digite o preço do livro: "))
ehEstudante = input("Digite se você é estudante (S/N):").strip().upper()

if ehEstudante == "S":
    print("Você é estudante e tem direito a 15% de desconto.")
    desconto = precoLivro * 0.15
else:
    print("Você não é estudante, mas tem direito a 5% de desconto.")
    desconto = precoLivro * 0.05

precoFinal = precoLivro - desconto

print(f"Seu livro custou R$ {precoFinal:.2f}")