from datetime import datetime, date


class Cliente:
    def __init__(self, nome, rg, cpf, datanasc, salario, ano):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__datanasc = datanasc
        self.__salario = salario
        self.__ano = ano

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade
  
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_rg(self):
        return self.__rg
        
    def set_rg(self, rg):
        self.__rg = rg
    
    def get_cpf(self):
        return self.__cpf
        
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_datanasc(self):
        return self.__datanasc
        
    def set_datanasc(self, datanasc):
        self.__datanasc = datanasc

    def get_salario(self):
        return self.__salario
        
    def set_salario(self, salario):
        self.__salario = salario

    def ano_nasc(cls, ano, datanasc):
      idade = cls.ano - datanasc
      return cls(idade)

    @property
    def nome(self):
        return self.__nome
    @property
    def rg(self):
        return self.__rg
    @property
    def cpf(self):
        return self.__cpf
    @property
    def datanasc(self):
        return self.__datanasc
    @property
    def salario(self):
        return self.__salario
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @rg.setter
    def rg(self, rg):
        self.__nome = rg

    @cpf.setter
    def cpf(self, cpf):
        self.__nome = cpf

    @datanasc.setter
    def datanasc(self, datanasc):
        self.__datanasc = datanasc

    @salario.setter
    def salario(self, salario):
        self.__salario = salario


        
        
if __name__ == "__main__":
    cliente1 = Cliente("", "", "", "", "", "", "")
		# Utilizando geters e setters
    cliente1.set_nome("José")
    cliente1.set_cpf("12312224925")
    cliente1.set_rg('17.352.193-9')
    cliente1.set_datanasc('1998')
    cliente1.set_salario('R$2000')
    print(cliente1.get_nome())
    print(cliente1.get_cpf())
    print(cliente1.get_rg())
    print(cliente1.get_datanasc())
    print(cliente1.get_salario())

    

    

