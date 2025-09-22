from stack import Stack



class MinStack:
    
    def __init__(self):
        self.main_stack = Stack()
        self.aux_stack = Stack()
        
        
    def get_min(self):
        
        if self.aux_stack.is_empty():
            return None
        
        return self.aux_stack.peek()
        
    def push(self, data):
        
        self.main_stack.push(data)
        
        if self.aux_stack.is_empty() or data <= self.aux_stack.peek():
            self.aux_stack.push(data)
           
        
    def pop(self):
        
        if self.main_stack.is_empty():
            return None
        
        valor_removido = self.main_stack.pop()
        
        if valor_removido == self.aux_stack.peek():
            self.aux_stack.pop()
        
        return valor_removido
    