class Element():
    def __init__(self, obj):
        self.obj = obj
        self.num_comparations = 0

    def __repr__(self):
        return str(self.obj)

    def __str__(self):
        return str(self.obj)

    def __gt__(self, other):
        self.num_comparations += 1

        return self.obj > other.obj
    
    def __lt__(self, other):
        self.num_comparations += 1
        
        return self.obj < other.obj

    def __eq__(self, other):
        self.num_comparations += 1

        return self.obj == other.obj

    def __le__(self, other):
        self.num_comparations += 1

        return self.obj <= other.obj
    
    def __ge__(self, other):
        self.num_comparations += 1

        return self.obj >= other.obj