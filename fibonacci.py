

class Fibonacci:
    def __init__(self,stop):
        self.start = 0
        self.stop = stop + 1
        self.step = 1
        self.current_value = self.start - self.step
        if not isinstance(self.stop, int):
            raise ValueError

    def __iter__(self):
        return self

    def __next__(self):
        self.current_value += self.step
        if self.current_value >= self.stop:
            raise StopIteration
        return self.current_value
