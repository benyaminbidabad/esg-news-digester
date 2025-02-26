from langchain.tools import tool

class CalculatorTools():
    @tool("Make a calculation")
    def calculate(operation):
        """Useful to perform any mathematical calculations
        The input to this tool are mathematical expressions
        2*10 or 5+2"""
        try: 
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"
        
        