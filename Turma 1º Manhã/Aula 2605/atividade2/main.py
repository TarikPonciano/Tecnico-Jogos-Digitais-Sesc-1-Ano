from classFuncionario import Funcionario

func1 = Funcionario("Cleitinho", 3000, "Analista Junior", 21, True)
func1.aumentarSalario(200000)

func2 = Funcionario("Josefina", 5000, "Tech Leader", 30, False)
func2.reduzirSalario(5000)

func1.mostrarInformacoes()

func2.mostrarInformacoes()