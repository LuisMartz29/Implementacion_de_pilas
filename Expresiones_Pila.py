class Stack: #funciona como una pila usando una lista
    def __init__(self): #se inicializa una lista vacia
        self.items = []

    def push(self, element): #agrega
        self.items.append(element) #usando append

    def pop(self): #elimina y devuelve
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self): #devuelve sin eliminar
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self): #devuelve true si esta vacia
        return len(self.items) == 0

    def size(self): #devuelve el numero de elementos en la pila
        return len(self.items)


#validación de paréntesis balanceados
def balanceparentesis (expression):
    stack = Stack()
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


# Conversión de notación infija a postfija
def infija_postfija(expression):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []

    for char in expression.split():
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        else:  # operador
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedencia.get(char, 0) <= precedencia.get(stack.peek(), 0)):
                output.append(stack.pop())
            stack.push(char)

    while not stack.is_empty(): #vacia la pila al final
        output.append(stack.pop())

    return ' '.join(output)



def main():
    expr1 = "( 3 + 2 ) * ( 8 / 4 )"
    print("Expresión balanceada:", balanceparentesis(expr1))

    expr2 = "3 + 5 * ( 2 - 8 )"
    print("Notación postfija:", infija_postfija(expr2))


if __name__ == "__main__":
    main()