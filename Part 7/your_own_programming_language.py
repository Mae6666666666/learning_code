import string
from functools import partial
# make variables that contain coditions, adding, subtracting, diving, multiplyimg, if statements,

program1 = ["PRINT","MOV", "ADD", "SUB", "MUL", "DIV", "JUMP", "IF", "END"]
PRINT = lambda x: print(x)

ADD = lambda x, y: print(x + y)
SUB = lambda x, y: print(x - y)
MUL = lambda x, y: print(x * y)



def run_program():
    PRINT("Program started")
    ADD(5, 2)
    SUB(5, 2)
    MUL(5, 2)
run_program()

# import fast.api as fastapi
# app = fastapi.FastAPI()
# @app.get("/")
# async def root():