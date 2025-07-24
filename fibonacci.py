

class Fibonacci:
    def __init__(self,stop,step=1):
        self.start = 1
        self.stop = stop
        self.step = step
        self.current_value = 1 - step
        if not isinstance(self.stop, int):
            raise ValueError

    def __iter__(self):
        return self

    def __next__(self):
        self.current_value += self.step
        if self.current_value >= self.stop:
            raise StopIteration
        return self.current_value
