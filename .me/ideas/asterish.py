#You can write ugly code if you want.
#You cannot write code by not writing code, even if you want to.
import os, sys
import re


#You are writing this to soothe your soul.
class Asterism:
    """What the symbols mean:
    *: Author wishes to expand on the text enclosed. >>> "*<text>*"? Elaborate:". Input is a child asterism.
   To be expanded...
    """
    symbols = ['*']
    symbToRe = {'*': '\*.+?\*'}
    symbPrompts = {'*' : '{}? Elaborate:'}
    text = ""

    def __init__(self,title=''):
        self.title = title
        self.children = {symbol: [] for symbol in self.symbols} 
    
    def step(self, promptText):
        print(promptText)
        self.text = sys.stdin.readline()
        for symb in self.children:
            self.children[symb] = [item.strip(symb)  for item in re.findall(self.symbToRe[symb],self.text)]
            for childName in self.children[symb]:
                child = Asterism(childName)
                child.step(self.symbPrompts[symb].format(childName))


if __name__=="__main__":
    john = Asterism()
    john.step('What\'s on your mind?')
    print(john.children)

