Implementación de pilas

- Implementar desde cero una clase personalizada de Pila (Stack) en Python y aplicarla en un sistema de manejo de expresiones matemáticas, validando la correcta agrupación de paréntesis y convirtiendo expresiones infijas a postfijas.

Crear una clase "Stack" sin utilizar estructuras predefinidas (list, deque, queue.LifoQueue).


Funciones requeridas en la Pila:

- "push(element)": Agregar un elemento a la pila.
- "pop()": Eliminar y devolver el elemento superior.
- "peek()": Devolver el elemento superior sin eliminarlo.
- "is_empty()": Retornar True si la pila está vacía.
- "size()": Retornar el número de elementos en la pila.

Aplicación práctica:

Validación de expresiones matemáticas:

Escribir una función que verifique si una expresión matemática tiene los paréntesis balanceados.

- Ejemplo de entrada válida: (3 + 2) * (8 / 4).
- Ejemplo de entrada no válida: ((3 + 2) * (8 / 4.

Conversión de notación infija a postfija:
Escribir un algoritmo que convierta una expresión en notación infija a notación postfija usando una pila.
- Entrada: 3 + 5 * ( 2 - 8 ).
- Salida esperada: 3 5 2 8 - * +.
