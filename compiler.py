import re

RESERVED = {"SET", "ADD", "SUB", "MUL", "DIV", "PRINT"}

symbol_table = {}
generated_code = []



def is_number(token):
    return token.isdigit()


def is_valid_identifier(name):
    return name.isalpha() and name not in RESERVED


def semantic_error(line, msg):
    print(f"Erro semântico na linha {line}: {msg}")
    exit()
    
#processo de analise de linhas(sint e semant)

def process_line(line, line_number):

    tokens = line.strip().split()

    if not tokens:
        return

    command = tokens[0]


    if command == "SET":

        if len(tokens) != 3:
            semantic_error(line_number, "estrutura inválida para SET")

        name = tokens[1]
        value = tokens[2]

        # valida 
        if not is_valid_identifier(name):
            semantic_error(line_number,
                           f"nome de variável inválido '{name}'")

        if not is_number(value):
            semantic_error(line_number,
                           "SET aceita apenas número")

        # adiciona
        symbol_table[name] = int(value)

        generated_code.append(f"{name} = {value}")

    elif command in {"ADD", "SUB", "MUL", "DIV"}:

        if len(tokens) != 3:
            semantic_error(line_number,
                           f"estrutura inválida para {command}")

        op1, op2 = tokens[1], tokens[2]

        def validate_operand(op):
            if is_number(op):
                return op
            if op not in symbol_table:
                semantic_error(line_number,
                               f"variável '{op}' não declarada")
            return op

        op1 = validate_operand(op1)
        op2 = validate_operand(op2)

        operator_map = {
            "ADD": "+",
            "SUB": "-",
            "MUL": "*",
            "DIV": "/"
        }

        python_op = operator_map[command]

        generated_code.append(f"print({op1} {python_op} {op2})")

    elif command == "PRINT":

        if len(tokens) != 2:
            semantic_error(line_number,
                           "estrutura inválida para PRINT")

        var = tokens[1]

        if var not in symbol_table:
            semantic_error(line_number,
                           f"variável '{var}' não declarada")

        generated_code.append(f"print({var})")

    else:
        semantic_error(line_number,
                       f"comando desconhecido '{command}'")

#compilador aqui

def compile_file(input_file, output_file):

    with open(input_file, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        process_line(line, i)

    with open(output_file, "w") as f:
        for code in generated_code:
            f.write(code + "\n")

    print("Compilação concluída com sucesso!")


#execucao do codigo na main
if __name__ == "__main__":
    compile_file("entrada.calc", "saida.py")