# Uma das coisas que é possivel fazer é criar estados para que o objeto possa ser melhor controlado ou modificado.
# No exemplo abaixo, o objeto só pode acessar um método "fotografar" se seu atributo "filmando" for False.
# Se ele acessar o método "filmar", o atributo irá mudar para True. Apenas acessando o método "parar_de_filmar" pode
# reverter isso.

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando...')
            return
        print(f'{self.nome} está fotografando...')
    

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_de_filmar()
c1.fotografar()
