import random

class Tree:
    events(external) = [A]
    map = []
    tag = 0

    def __init__(self,depth,event):
        self.event = random.choice(events)
        self.cross = random.random()
        self.tag = tag
        
    def generation(self,depth):
        if self.tag == depth:
            return map
        else:
            t = Tree()
            Tree.map.append(self.tag)
            self.tag +=1
            if self.cross > 0.5:
                return generation(self,depth-self.tag)
            else:
                t = Tree() 

        
        return map