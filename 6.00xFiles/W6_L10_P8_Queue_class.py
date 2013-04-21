class Queue(object):
    """Simulates the FIFO data structure"""

    def __init__(self):
        self.fifo=[]

    def insert(self, number):
        self.fifo.append(number)

    def remove(self):
        try:
            return self.fifo.pop(0)
        except:
            raise ValueError
    
