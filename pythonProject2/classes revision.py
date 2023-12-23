class Patient:
    def _init_(self,id,age,gender):
        self.id = id
        self.age = age
        self.gender = gender
    def _str_(self):
        return (f'{self.id}\n{self.age}\n{self.gender}')
