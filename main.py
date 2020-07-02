
class Stack:

    def __init__(self, brackets):
        self.string = brackets
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def checking_balance(unity):
    
    """ 
    To check the balance of required elements use the function provided 

    """

    brackets_open = ['[', '(', '{']
    brackets_closed = [']', ')', '}']

    result = '\nThe unity under verification is balanced.'

    for symbol in unity:

        if symbol in brackets_open:
            unity_to_check.push(brackets_open.index(symbol))
        
        elif symbol in brackets_closed:
            if not unity_to_check.is_empty() and unity_to_check.peek() == brackets_closed.index(symbol):
                unity_to_check.pop()
            else:
                result = '\nThe unity under verification is NOT balanced.'

    if not unity_to_check.is_empty():

        result = '\nThe unity under verification is NOT balanced.'

    return result


if __name__ == '__main__':

    unity_to_check = Stack(input("\nEnter any unity of brackets you would like to verify, e.g.'[[{())}]]':"))

    # unity_to_check = Stack('(((([{}]))))')
    # unity_to_check = Stack('[([])((([[[]]])))]{()}')
    # unity_to_check = Stack('{{[()]}}')
    # unity_to_check = Stack('}{}')
    # unity_to_check = Stack('{{[(])]}}')
    # unity_to_check = Stack('[[{())}]]')

    print(checking_balance(unity_to_check.string))

