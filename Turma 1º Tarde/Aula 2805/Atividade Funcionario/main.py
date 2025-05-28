from classFuncionario import Funcionario

func1 = Funcionario("Janderson", "07498944481", 10000, 24)
func2 = Funcionario("Pedrinho", "12345678910", 1518, 15)
func3 = Funcionario("Isadora", "67898788090", 2000, 16)

func1.setSalario(5000)
func3.setSalario(-2000.01)
func2.setSalario(5000)

func1.mostrarInformacoes()

func2.mostrarInformacoes()

func3.mostrarInformacoes()

print(func3.getCpf("123456"))