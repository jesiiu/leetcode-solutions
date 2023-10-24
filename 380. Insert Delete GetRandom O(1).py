# 380. Insert Delete GetRandom O(1)

class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        l = list(self.set)
        random_index = random.randint(0, len(l) - 1)
        return l[random_index]
