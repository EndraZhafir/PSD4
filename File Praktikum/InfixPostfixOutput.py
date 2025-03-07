class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

def pangkat(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(ekspresi):
    stack = Stack()
    postfix = []
    for char in ekspresi:
        if char.isalnum(): 
            postfix.append(char)
        elif char == '(':  
            stack.push(char)
        elif char == ')': 
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  
        else: 
            while (not stack.is_empty() and pangkat(char) <= pangkat(stack.peek())):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)  

def hasil_postfix(ekspresi):
    stack = []

    def operator(op, b, a):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '^':
            return a ** b  
        else:
            raise ValueError(f"Bukan suatu operator: {op}")

    digit = ekspresi.split()

    for i in digit:
        if i.isdigit():
            stack.append(int(i)) 
        else: 
            b = stack.pop()  
            a = stack.pop()
            hasil = operator(i, b, a) 
            stack.append(hasil) 

    return stack.pop()  

ekspresi = input("Inputkan ekspresi matematika infix (satu digit per operand): ")

ekspresi_postfix = infix_to_postfix(ekspresi.replace(' ', '')) 
print("Ekspresi matematika Infix: ", ekspresi)
print("Ekspresi matematika postfix: ", ekspresi_postfix)

hasil = hasil_postfix(ekspresi_postfix)
print(f"Hasil perhitungan ekspresi matematika postfix '{ekspresi_postfix}' adalah: {hasil}")