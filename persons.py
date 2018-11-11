from datetime import datetime

class Person:

    def __init__(self, nome, dt_nasc):
        self.__nome = nome
        self.__dt_nasc = dt_nasc

    @property
    def idade(self):
        diferanca = datetime.strptime(self.dt_nasc, '%Y-%m-%d') - datetime.now()
        return abs(diferanca.days / 365)

    @property
    def person(self):
        return self.__nome, self.dt_nasc, self.idade

    @property
    def dt_nasc(self):
        return self.__dt_nasc

    @dt_nasc.setter
    def dt_nasc(self, dt_nasc):
        self.__dt_nasc = dt_nasc

