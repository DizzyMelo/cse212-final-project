class Plate:

    def __str__(self) -> str:
        return '--_______--'

class StackOfPlates:
    stack = []

    def add(self, amount = 1):
        if amount == 1:
            self.stack.append(Plate())
        else:
            '''
            Implement the code that handles two other situations.
            First: if amount is 0
            Second: If amount is greater than 1
            '''
            while amount > 0:
                self.stack.append(Plate())
                amount -= 1

    def remove(self, amount = 1):
        if amount == 1:
            self.stack.pop()
        else:
            '''
            Implement the code that handles two other situations.
            First: if amount is 0
            Second: If amount is greater than 1
            '''
            while amount > 0:
                self.stack.append(Plate())
                amount -= 1

    def displayStack(self):
        '''
        Implement some code that prints a message if the stack is empty
        '''
        if len(self.stack):
            print('Stack is empty')
        else:
            stackOfPlates = f'{str(Plate())}\n' * len(self.stack)
            print(stackOfPlates)
    
    def displayAmount(self):
        '''
        Implement some code that display the number of plates in the stack
        '''
        print(f"The stack {len(self.stack)} plates")
