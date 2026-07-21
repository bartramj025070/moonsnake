##########################################################################################################
#      |\      _,,,---,,_
#ZZZzz /,`.-'`'    -.  ;-;;,_
#     |,4-  ) )-,_. ,\ (  `'-'
#     '---''(_/--'  `-'\_)
##########################################################################################################

##########################################################################################################
## @name: CLI.py
## @desc: Command Line Interface for moonsnake
## @author: bartramj025070 <- that's me! =]
## @created: 20/07/26
## @last-edited: 20/07/26
##########################################################################################################

import Lexer as lexer
import sys
args = sys.argv

def run():
    return True

def runFile(filePath):
    with open(filePath, 'r') as file:
        run(file.read())
    
def runPrompt():
    while True:
        inputResult = input('> ')
        if inputResult.strip() == '':
            break
        run(inputResult)

if len(args) > 1:
    print("Usage: nap [script]")
    exit(64)
elif len(args) == 1:
    runFile(args[0])
else:
    runPrompt()