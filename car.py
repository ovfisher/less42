class Car:
    def __init__(self,made,model):
        self.public_made = made
        self._protected_model = model
        self.__private_year = 2024

    def private_made_model(self):
        return f"public car : {self.public_made},{self._protected_model}."

    def _protected_func(self):
        print('_protected')
    def __private_func(self):
        print('__private')

class ECar(Car):
    def __init__(self,made,model,battery):
        super().__init__(made,model)
        self.battery = battery

    def get_details(self):
        details = f'{self.public_made},{self._protected_model},{self.battery}KWh '
        return details

tesla = ECar('Tesla','Model S',200)
print(tesla.public_made)
print(tesla.private_made_model())

print(tesla._protected_model)
print(tesla._protected_func())

print(tesla._Car__private_year)