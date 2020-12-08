class Bag:
    def __init__(self, color, content):
        self.color = color
        self.hard_content = content.copy()
        self.content = content
        self.has_gold = None
        self.direct_bags = sum(content.values())
    
    def contains(self, color):
        return color in self.content
    
    def empty(self):
        return self.content == {}
    
    def remove(self, color):
        self.content.pop(color, None)
        return self
    
