"""
Multiple inheritance and data for using in this program:
 - Manufacturer: 'BMW' and 'Mercedes'
 - Model of 'BMW': 'X1', 'X2', 'X5', 'X6'
 - Model of 'Mercedes': 'C-Class', 'S-Class', 'G-Class', 'E-Class'
 - Fuel: 'Petrol', 'Diesel'
"""
print(__doc__)


class CarModel:
    """
    Class for initiating variables
    """
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    def car_model(self):
        """
        Function for printing manufacturer and model of the car
        :return: manufacturer and model of the car
        """
        print(f'Chosen car is {self.manufacturer} {self.model}')


class Engine(CarModel):
    """
    Class for engine description
    """
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def engine_volume(self):
        """
        Function for displaying engine volume of certain car
        :return: engine volume
        """
        if self.manufacturer == 'BMW':
            if self.model in ('X5', 'X6'):
                print(f'The volume of {self.manufacturer} {self.model} is 3.0')
            elif self.model in ('X1', 'X2'):
                print(f'The volume of {self.manufacturer} {self.model} is 1.5')
            else:
                print('There is no such manufacturer or model of the car!!!')
        if self.manufacturer == 'Mercedes':
            if self.model in ('C-Class', 'S-Class'):
                print(f'The volume of {self.manufacturer} {self.model} is 2.5')
            elif self.model in ('G-Class', 'E-Class'):
                print(f'The volume of {self.manufacturer} {self.model} is 4.0')
            else:
                print('There is no such manufacturer or model of the car!!!')
        if self.manufacturer not in ('BMW', 'Mercedes'):
            print('There is no such manufacturer or model of the car!!!')


class Fuel(Engine):
    """
    Class for fuel description
    """
    def __init__(self, manufacturer, model, fuel):
        super().__init__(manufacturer, model)
        self.fuel = fuel

    def fuel_consumption(self):
        """
        Function for the displaying fuel consumption of the certain car
        :return: fuel consumption
        """
        if self.fuel == 'Petrol' and self.manufacturer == 'BMW' and self.model in ('X5', 'X6'):
            print(f'The consumption of {self.manufacturer} {self.model} is 8.7L/100km')
        elif self.fuel == 'Diesel' and self.manufacturer == 'BMW' and self.model in ('X5', 'X6'):
            print(f'The consumption of {self.manufacturer} {self.model}'
                  f' with {self.fuel} engine is 7.7L/100km')
        elif self.fuel == 'Petrol' and self.manufacturer == 'BMW' and self.model in ('X1', 'X2'):
            print(f'The consumption of {self.manufacturer} {self.model} is 6.6/100km')
        elif self.fuel == 'Diesel' and self.manufacturer == 'BMW' and self.model in ('X1', 'X2'):
            print(f'The consumption of {self.manufacturer}'
                  f' {self.model} is 7.2/100km')
        elif self.fuel == 'Petrol' and self.manufacturer == 'Mercedes'\
                and self.model in ('C-Class', 'S-Class'):
            print(f'The consumption of {self.manufacturer} {self.model} is 9.0/100km')
        elif self.fuel == 'Diesel' and self.manufacturer == 'Mercedes'\
                and self.model in ('C-Class', 'S-Class'):
            print(f'The consumption of {self.manufacturer}'
                  f' {self.model} is 8.8/100km')
        elif self.fuel == 'Petrol' and self.manufacturer == 'Mercedes'\
                and self.model in ('G-Class', 'E-Class'):
            print(f'The consumption of {self.manufacturer} {self.model} is 10.0/100km')
        elif self.fuel == 'Diesel' and self.manufacturer == 'Mercedes'\
                and self.model in ('G-Class', 'E-Class'):
            print(f'The consumption of {self.manufacturer} {self.model} is 9.5/100km')
        else:
            print('There is no consumption info about such model of the car!!!')


class DriveUnit(CarModel):
    """
    Class for drive unit description
    """
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def wheel_drive(self):
        """
        Function for displaying drive unit of the certain car
        :return: drive unit
        """
        if self.manufacturer == 'BMW' and self.model in ('X6', 'X5'):
            drive_unit = '4WD (wheel drive)'
            print(f'The {self.manufacturer} {self.model} has {drive_unit}')
        elif self.manufacturer == 'BMW' and self.model in ('X1', 'X2'):
            drive_unit = '2WD (wheel drive)'
            print(f'The {self.manufacturer} {self.model} has {drive_unit}')
        elif self.manufacturer == 'Mercedes' and self.model in ('C-Class', 'S-Class'):
            drive_unit = '4WD (wheel drive)'
            print(f'The {self.manufacturer} {self.model} has {drive_unit}')
        elif self.manufacturer == 'Mercedes' and self.model in ('G-Class', 'E-Class'):
            drive_unit = '4WD (wheel drive)'
            print(f'The {self.manufacturer} {self.model} has {drive_unit}')
        else:
            print('There is no info about wheel drive for such model!!!')


class Cars(Fuel, Engine, DriveUnit):
    """
    Class for the car
    """
    def __init__(self, manufacturer, model, fuel):
        super().__init__(manufacturer, model, fuel)


# print(Cars.__mro__)
print('-' * 30, '1st auto', '-' * 30)
auto1 = Cars('BMW', 'X6', 'Diesel')
auto1.car_model()
auto1.engine_volume()
auto1.fuel_consumption()
auto1.wheel_drive()
print('-' * 30, '2nd auto', '-' * 30)
auto2 = Cars('Mercedes', 'C-Class', 'Petrol')
auto2.car_model()
auto2.engine_volume()
auto2.fuel_consumption()
auto2.wheel_drive()
print('-' * 30, '3rd auto', '-' * 30)
auto3 = Cars('Audi', 'B6', 'Petrol')
auto3.car_model()
auto3.engine_volume()
auto3.fuel_consumption()
auto3.wheel_drive()
