from abc import ABC, abstractmethod


class ABSFabric(ABC):

    @abstractmethod
    def product_name(self):
        ...


class Fabric:

    def fabric_run(self):
        print('Фабрика работает')
        return self

    @staticmethod
    def product_name(product: ABSFabric):
        return product

    @staticmethod
    def get_candy_class():
        return Candy()

    @staticmethod
    def get_chocolate_class():
        return Chocolate()


class Candy(ABSFabric):

    def product_name(self):
        print(f'Конфеты')


class Chocolate(ABSFabric):
    def product_name(self):
        print('Шоколад')


class Cookies(ABSFabric):

    def product_name(self):
        print('Печенье готовы, господа')


class Icecream(ABSFabric):

    def product_name(self):
        print('Мороженое')


def get_instance(instance: ABSFabric):
    return instance.product_name()


get_instance(Icecream())

# CA = Candy()
# CH = Chocolate()
# CO = Cookies()
# I = Icecream()

# Fabric().fabric_run().product_name(CO).product_name()
