import re

# solve parameter is a default param
def arithmetic_arranger(problems, solve = False):
    # taking in this
    # arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

    # outputing this
    #    32     3801       45      123
    # + 698    -   2    +  43    +  49
    # -----    -----    -----    -----

    # observations
    # 1. needs to output multiple lines per problem 
    # 2. must count number of characters needed to create a line
    # 3. split up first number from +/- and second number

    # string format example
    # "   32    3801       45      123\n+ 698    -   2    +  43    +  49\n-----    -----    -----    -----"

    if(len(problems) > 5):
      return "Error: Too many problems."
  
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""

    for problem in problems:
      # if there's any spaces numbers period or +- operators
      if(re.search("[^\s0-9.+-]", problem)):
        if(re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
    
      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]

      if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
        return "Error: Numbers cannot be more than four digits."

      sum = ""
      if(operator == "+"):
        sum = str(int(firstNumber) + int(secondNumber))
      elif(operator == "-"):
        sum = str(int(firstNumber) - int(secondNumber))

      length = max(len(firstNumber), len(secondNumber)) + 2
      top = str(firstNumber).rjust(length)
      bottom = operator + str(secondNumber).rjust(length - 1)
      line = ""
      res = str(sum).rjust(length)
      for s in range(length):
        line += "-"

      if problem != problems[-1]:
        first += top + '    '
        second += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else:
        first += top
        second += bottom
        lines += line
        sumx += res

    if solve:
      string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
      string = first + "\n" + second + "\n" + lines
    return string