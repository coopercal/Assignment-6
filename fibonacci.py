

class Fibonacci:
    def __init__(self,stop):
        self.start = 0
        self.stop = stop + 1
        self.step = 0
        self.previous_value = 0
        self.current_value = 1
        self.combined = 0
        if not isinstance(self.stop, int):
            raise ValueError

    def __iter__(self):
        return self

    def __next__(self):
        x = self.previous_value
        self.combined = self.previous_value + self.current_value
        self.previous_value = self.current_value
        self.current_value = self.combined
        self.step += 1
        if self.step > self.stop:
            raise StopIteration
        return x