def arithmetic_arranger(problems, result = False):

    #check for the number of problem
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    
    #split problem in 3 parts
    first_part = []
    second_part = []
    operators = []
    for problem in problems:
        splitted = problem.split()
        first_part.append(splitted[0])
        operators.append(splitted[1])
        second_part.append(splitted[2])

    #check for * and /
    if "*" in operators or "/" in operators:
        return "Error: Operator must be '+' or '-'."

    #check for only digits and no more than 4 digits
    for i in range(len(first_part)):
        if not first_part[i].isdigit() or not second_part[i].isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_part[i]) > 4 or len(second_part[i]) > 4:
            return "Error: Numbers cannot be more than four digits."


    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for i in range(len(first_part)):
        if len(first_part[i]) > len(second_part[i]):
            first_line.append(" "*2 + first_part[i])
        else:
            first_line.append(" "*(len(second_part[i]) - len(first_part[i]) + 2) + first_part[i])

    for i in range(len(second_part)):
        if len(second_part[i]) > len(first_part[i]):
            second_line.append(operators[i] + " " + second_part[i])
        else:
            second_line.append(operators[i] + " "*(len(first_part[i]) - len(second_part[i]) + 1) + second_part[i])

    for i in range(len(first_part)):
        third_line.append("-"*(max(len(first_part[i]), len(second_part[i])) + 2))

    if result:
        for i in range(len(first_part)):
            if operators[i] == "+":
                ans = str(int(first_part[i]) + int(second_part[i]))
            else:
                ans = str(int(first_part[i]) - int(second_part[i]))

            if len(ans) > max(len(first_part[i]), len(second_part[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" "*(max(len(first_part[i]), len(second_part[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    return arranged_problems