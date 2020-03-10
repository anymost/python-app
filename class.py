class Dog:
    # 类属性
    name = 'dog'

    def __init__(self, name):
        # 实例属性
        self.name = name

    def print_name(self):
        print(self.name)


class GoodDog(Dog):
    dog_type = 'good'

    def __init__(self, name, age):
        super().__init__(name)
        self.name = "jack"
        self.age = age

    @classmethod
    # 类方法
    def say_dog_type(cls):
        print(cls.dog_type)

    @staticmethod
    # 静态方法
    def say_class_name():
        print('hello')

    def print_age(self):
        print(self.age)


goodDog = GoodDog("puppy", 20)
goodDog.print_name()
goodDog.print_age()
goodDog.say_dog_type()
