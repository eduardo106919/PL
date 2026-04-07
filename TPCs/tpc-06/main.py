import ply.lex as lex
import sys

tokens = ("INT", "LEAF")

t_INT = r"\d+"
t_LEAF = r"x"
t_ignore = " \t\n"


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lookahead = None

lexer = lex.lex()


def next_token():
    tok = lexer.token()
    global lookahead
    if tok:
        lookahead = (tok.type, tok.value)
    else:
        lookahead = ("$", None)


def recognize_terminal(expected):
    tok_type, tok_value = lookahead
    if tok_type == expected:
        next_token()
        return tok_value
    else:
        raise ValueError("Expected token type:", expected, "but got:", tok_type)


def recognize_tree():
    tok_type, _ = lookahead
    if tok_type == "INT":
        recognize_terminal("INT")
        left_depth = recognize_tree()
        right_depth = recognize_tree()
        return 1 + max(left_depth, right_depth)
    elif tok_type == "LEAF":
        recognize_terminal("LEAF")
        return 1
    else:
        raise ValueError("Expected token type: INT or LEAF, but got:", tok_type)


def calculate_depth(data: str) -> int:
    lexer.input(data)
    next_token()
    return recognize_tree()


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python main.py <filename>")
        exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            content = file.read()

        depth = calculate_depth(content)
        print(f"Tree depth: {depth}")

    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
