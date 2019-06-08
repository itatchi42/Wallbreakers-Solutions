class MyHashSet:

    def __init__(self):
        self.set = []
    #Naive approach:
    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.set
        
    #optimized boolean array solution
    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key]