"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:

    def __str__(self):
        return f"{self.__count}"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Counter, cls).__new__(cls)
            cls.instance.__count = 0
        else:
            cls.instance.__count = Counter.instance.__count
        return cls.instance

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def increment(self):
        self.count += 1
        return self.count
