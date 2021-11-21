"""
The program for collecting flower bucket and searching by params
"""


class Flowers:
    """
    CLass for setting and initiating variables
    """
    flower_list = {'roza':
                       {'price': 2.5, 'length': 50, 'lifetime': 7, 'color': 'red', 'freshness': 1},
                   'tulip':
                       {'price': 3, 'length': 30, 'lifetime': 5, 'color': 'yellow', 'freshness': 3},
                   'chrysanthemum':
                       {'price': 1.5, 'length': 40, 'lifetime': 6, 'color': 'pink', 'freshness': 2},
                   'chamomile':
                       {'price': 1.0, 'length': 25, 'lifetime': 10, 'color': 'white', 'freshness': 1.5},
                   'carnation':
                       {'price': 2.7, 'length': 55, 'lifetime': 9, 'color': 'burgundy', 'freshness': 2}}

    def __init__(self, flower):
        self.flower = flower
        self.price = Flowers.flower_list[flower]['price']
        self.length = Flowers.flower_list[flower]['length']
        self.lifetime = Flowers.flower_list[flower]['lifetime']
        self.color = Flowers.flower_list[flower]['color']
        self.freshness = Flowers.flower_list[flower]['freshness']
        self.end_bucket = []
        self.non_in_list = []
        self.price_for_collection = []
        self.lifetimes = []
        self.dict_bucket_with_params = {}
        self.sorted_by_params = {}
        self.list_for_search = []

    def collect_bucket(self, *args):
        """
        The func for collecting bucket
        :param args: param for adding flowers
        :return: end bucket
        """
        start_bucket = []
        for i in args:
            start_bucket.append(i)
        for each_flower in start_bucket:
            if each_flower in list(Flowers.flower_list.keys()):
                self.end_bucket.append(each_flower)
            else:
                self.non_in_list.append(each_flower)

        if len(self.non_in_list) != 0:
            print(f'There is no such flower(s) in the list like:'
                  f' {", ".join(set(self.non_in_list))}')
        else:
            print(f'The bucket contain the following flowers:'
                  f' {", ".join(set(self.end_bucket))}')
        return self.end_bucket

    def bucket_price(self):
        """
        Func for receiving bucket price
        :return: bucket price
        """
        for each_flower in self.end_bucket:
            self.price_for_collection.append(Flowers.flower_list[each_flower]['price'])
        print(f'The whole price for the bucket is: {sum(self.price_for_collection)} BLR')

    def died_time(self):
        """
        The func for calculating flower life time
        :return: life time
        """
        for each_flower in self.end_bucket:
            self.lifetimes.append(Flowers.flower_list[each_flower]['lifetime'])
        print(f'The average bucket lifetime is {round(((sum(self.lifetimes)) / (len(self.lifetimes))), 2)} day(s)')

    def sorting_in_bucket(self, sort_parameter):
        """
        The func for sorting bucket
        :param sort_parameter: parameter for sorting
        :return: sorting bucket by params
        """
        if sort_parameter == 'price':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['price']
        elif sort_parameter == 'length':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['length']
        elif sort_parameter == 'lifetime':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['lifetime']
        elif sort_parameter == 'freshness':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['freshness']
        elif sort_parameter == 'color':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['color']
        self.sorted_by_params = {}
        sorted_keys = sorted(self.dict_bucket_with_params, key=self.dict_bucket_with_params.get)
        for each_key in sorted_keys:
            self.sorted_by_params[each_key] = self.dict_bucket_with_params[each_key]
        if sort_parameter not in ('length', 'lifetime', 'freshness', 'color', 'price'):
            print('There is no such parameter for sorting!')
        else:
            print(f'Sorting by {sort_parameter}:'.upper())
        for i in self.sorted_by_params:
            if sort_parameter == 'price':
                print(f'{i} --> {self.sorted_by_params[i]} BLR')
            elif sort_parameter == 'length':
                print(f'{i} --> {self.sorted_by_params[i]} CM')
            elif sort_parameter == 'lifetime':
                print(f'{i} --> {self.sorted_by_params[i]} day(s)')
            elif sort_parameter == 'freshness':
                print(f'{i} --> {self.sorted_by_params[i]} day(s)')
            elif sort_parameter == 'color':
                print(f'{i} --> {self.sorted_by_params[i]} color')
        return self.sorted_by_params

    def searching_in_bucket_by_params(self, parameter, value):
        """
        The func for the searching by params in bucket
        :param parameter: parameter for searching
        :param value: parameter value for searching
        :return: parameter for flower in bucket
        """
        self.list_for_search = []
        if parameter == 'price':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['price']
        elif parameter == 'length':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['length']
        elif parameter == 'lifetime':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['lifetime']
        elif parameter == 'freshness':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['freshness']
        elif parameter == 'color':
            for each_flower in self.end_bucket:
                self.dict_bucket_with_params[each_flower] = Flowers.flower_list[each_flower]['color']
        spisok = self.dict_bucket_with_params
        for param in spisok:
            self.list_for_search.append(spisok[param])
        if parameter == 'price' and value in self.list_for_search:
            print(f'The {value} BLR is a {parameter.lower()}'
                  f' for flower {(list(spisok.keys())[list(spisok.values()).index(value)])}')
        elif parameter == 'length' and int(value) in self.list_for_search:
            print(f'The {value} CM is a {parameter.lower()}'
                  f' for flower {(list(spisok.keys())[list(spisok.values()).index(int(value))])}')
        elif parameter == 'lifetime' and int(value) in self.list_for_search:
            print(f'The {value} day(s) is {parameter.lower()}'
                  f' for flower {(list(spisok.keys())[list(spisok.values()).index(int(value))])}')
        elif parameter == 'color' and value in self.list_for_search:
            print(f'The {value} is a {parameter.lower()}'
                  f' of flower {(list(spisok.keys())[list(spisok.values()).index(value)])}')
        elif parameter == 'freshness' and int(value) in self.list_for_search:
            print(f'The {value} day(s) is a {parameter.lower()}'
                  f' for flower {(list(spisok.keys())[list(spisok.values()).index(int(value))])}')

    def is_there_flower(self, flower):
        """
        The func for checking is flower in the bucket
        :param flower: flower
        :return: In or not flower in bucket
        """
        if flower in self.end_bucket:
            print(f'The {flower} in your bucket')
        else:
            print(f'There is no {flower} in your bucket')


class FlowerDescription(Flowers):
    """
    Class for flower description
    """
    def flower_price(self):
        """
        Func for displaying flower price
        :return: flower price
        """
        print(f'The {self.flower} price is {self.price} BLR')

    def flower_name(self):
        """
        Func for displaying flower name
        :return: flower name
        """
        print(f'The {self.flower} is {self.flower}')

    def flower_length(self):
        """
        Func for displaying flower length
        :return: flower length
        """
        print(f'The {self.flower} length is {self.length} cm')

    def flower_lifetime(self):
        """
        Func for displaying flower lifetime
        :return: flower lifetime
        """
        print(f'The {self.flower} lifetime is {self.lifetime} day')

    def flower_color(self):
        """
        Func for displaying flower color
        :return: flower color
        """
        print(f'The {self.flower} color is {self.color}')

    def flower_freshness(self):
        """
        Func for displaying flower freshness
        :return: flower freshness
        """
        print(f'The {self.flower} freshness is {self.freshness} day')


print('-' * 25, 'Flower Description', '-' * 25)
# class exemplar
flower_description = FlowerDescription('ROZA'.lower())
# flower description, in this case 'length'
flower_description.flower_length()
# flower description, in this case 'price'
flower_description.flower_price()
# flower description, in this case 'freshness'
flower_description.flower_freshness()
# flower description, in this case 'color'
flower_description.flower_color()
# flower description, in this case 'lifetime'
flower_description.flower_lifetime()
print('-' * 25, 'Flower bucket', '-' * 25)
#
flowers = Flowers('roza')
# collect bucket
flowers.collect_bucket('tulip', 'roza', 'chamomile', 'carnation')
# bucket price
flowers.bucket_price()
# flower died time
flowers.died_time()
# sorting by params: color, price, lifetime, length, freshness
print('-' * 25, 'Sorting by params: price, color, freshness, lifetime, length', '-' * 25)
flowers.sorting_in_bucket('LifeTime'.lower())

# searching flower by params
print('-' * 20, 'Searching flower by params: price, color, freshness, lifetime, length', '-' * 20)
flowers.searching_in_bucket_by_params('PRICE'.lower(), 3)
flowers.searching_in_bucket_by_params('freshness'.lower(), 2)
flowers.searching_in_bucket_by_params('color'.lower(), 'white')
flowers.searching_in_bucket_by_params('length'.lower(), 50)
flowers.searching_in_bucket_by_params('lifetime'.lower(), 7)
# checking if flower in your bucket
print('-' * 20, 'Checking out, if the flower in your bucket?', '-' * 20)
flowers.is_there_flower('Tulip'.lower())
