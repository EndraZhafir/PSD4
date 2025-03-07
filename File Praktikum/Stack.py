class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

start = Stack()
jumlahinput = int(input("Masukkan input angka: "))

for i in range(jumlahinput):
    huruf = input(f"Masukkan huruf/kata ke-{str(i+1)}: ")
    start.push(huruf)

print('Hasil kebalikannya:')
for j in range(jumlahinput):
    hasil = start.peek()
    start.pop()
    print(hasil, end=' ')

