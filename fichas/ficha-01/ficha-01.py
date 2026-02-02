import doctest
import math


def break_seconds(secs):
    """
    Break the given number of seconds into days, hours, minutes and remaining seconds.

    >>> break_seconds(10)
    (0, 0, 0, 10)

    >>> break_seconds(3620)
    (0, 1, 0, 20)

    >>> break_seconds(17492173)
    (202, 10, 56, 13)
    """

    # number of days
    days = secs // (60 * 60 * 24)
    secs = secs % (60 * 60 * 24)
    # number of hours
    hours = secs // (60 * 60)
    secs = secs % (60 * 60)
    # number of minutes
    minutes = secs // 60
    # number of seconds
    secs = secs % 60

    return (days, hours, minutes, secs)


doctest.run_docstring_examples(break_seconds, globals())


def reverse_number(number):
    """
    Reverse the given integer number using ONLY arithmetic operations.

    >>> reverse_number(12345)
    54321

    >>> reverse_number(758148293)
    392841857

    >>> reverse_number(1)
    1

    >>> reverse_number(12321)
    12321
    """

    n = int(math.log10(number))
    # or create loop to know how what is the log10(number)
    out = 0
    for i in range(n, -1, -1):
        temp = number % 10
        number = number // 10
        out += temp * 10**i

    # out = 0
    # while number > 0:
    #   out *= 10
    #   temp = number % 10
    #   number = number // 10
    #   out += temp

    return out


doctest.run_docstring_examples(reverse_number, globals())


def reverse_str(s):
    """
    Reverse the given string WITHOUT using any auxiliary methods or functions.

    >>> reverse_str("Hello World")
    'dlroW olleH'

    >>> reverse_str("Erised stra ehru oyt ube cafru oyt on wohsi")
    'ishow no tyo urfac ebu tyo urhe arts desirE'

    >>> reverse_str("siht ekil dnuos I dna mra eht ma I")
    'I am the arm and I sound like this'

    >>> reverse_str("?")
    '?'
    """

    out = ""
    for c in s:
        out = c + out

    return out
    # return s[::-1]


doctest.run_docstring_examples(reverse_str, globals())


def camel_case(s):
    """
    Convert the given string into camel case: remove all non-alphabetic
    characters, and only characters after a non-alphabetic characters are
    ppercase, except the first.

    >>> camel_case("simple_case_of_camel_case")
    'simpleCaseOfCamelCase'

    >>> camel_case("ALL YOUR BASE ARE BELONG TO US")
    'allYourBaseAreBelongToUs'

    >>> camel_case("well&%/this%$#escalated q(u)i-c kly")
    'wellThisEscalatedQUICKly'
    """

    out = ""
    prev = False
    for c in s:
        if not c.isalpha():
            prev = True
        else:
            if prev:
                c = c.upper()
                prev = False
            else:
                c = c.lower()
            out += c

    return out


doctest.run_docstring_examples(camel_case, globals())


def caesar_cipher(shift, text):
    """
    Shift each character in the given text according to the given value. You can
    assume only lower case characters. Leave other characters unchanged.

    >>> caesar_cipher(5, "hello")
    'mjqqt'

    >>> caesar_cipher(3, "keep it quiet...")
    'nhhs lw txlhw...'

    >>> caesar_cipher(50, "x marks the spot")
    'x marks the spot'
    """

    out = ""
    for c in text:
        if c.islower():
            idx = ((ord(c) - ord("a")) + shift) % (ord("z") - ord("a"))
            c = chr(idx + ord("a"))
        out += c

    return out


doctest.run_docstring_examples(caesar_cipher, globals())


def quadratic_formula(a, b, c):
    """
    Implement the quadratic formula to solve ax² + bx + c = 0. Result should be a tuple with 0, 1 or 2 elements.

    >>> quadratic_formula(1, -5, 6)
    (3.0, 2.0)

    >>> quadratic_formula(2, -7, 3)
    (3.0, 0.5)

    >>> quadratic_formula(2, -8, 8)
    (2.0,)

    >>> quadratic_formula(10, 20, 30)
    ()
    """

    temp = b**2 - 4 * a * c
    if temp == 0:
        return (-b / (2 * a),)
    elif temp < 0:
        return ()
    else:
        return ((-b + math.sqrt(temp)) / (2 * a), (-b - math.sqrt(temp)) / (2 * a))


doctest.run_docstring_examples(quadratic_formula, globals())


def change(amount):
    """
    Break down the given amount of cents in the smallest number of 200, 100, 50,
    20, 10, 5, 2, 1 cent coins.  Note: this is not a knapsack problem, you can be
    greedy.

    >>> change(350)
    [(200, 1), (100, 1), (50, 1)]

    >>> change(200)
    [(200, 1)]

    >>> change(1998)
    [(200, 9), (100, 1), (50, 1), (20, 2), (5, 1), (2, 1), (1, 1)]

    >>> change(0)
    []
    """

    out = []
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    for coin in coins:
        if amount >= coin:
            out.append((coin, amount // coin))
            amount %= coin

    return out


doctest.run_docstring_examples(change, globals())


def path(grid, instructions):
    """
    You are given a rectangular grid and a set of instructions (U, D, L, R).
    Determine the path traversed when starting at position (0,0) and following the
     instructions. If it goes outside the grid, return None.

    >>> path(("###","#?#","###"),["D","R"])
    '##?'

    >>> path(("🌱💣🌱💣","🌱🌱🪙💣","🌱💣🪙🌱"),["D", "R", "R", "D", "U", "D", "U"])
    '🌱🌱🌱🪙🪙🪙🪙🪙'

    >>> path(("SUDH","OSJF","SOSI"), ["D", "R", "L", "D"])
    'SOSOS'

    >>> path(("SUDH","OSJF","SOSI"), ["D", "L", "L", "D"])

    """

    x, y = 0, 0
    out = grid[y][x]

    for i in instructions:
        if i == "U":
            y -= 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1
        else:
            x += 1

        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            return None
        else:
            out += grid[y][x]

    return out


doctest.run_docstring_examples(path, globals())


def vigenere_cipher(key, text):
    """
    Swap each character in the given text according to the given key dictionary.
    If a character is not in the key, use a ?.

    >>> vigenere_cipher({"a" : "x", "b" : "y", "c" : "h", "e" : "m", "l" : "f", "o" : "b"}, "hello")
    '?mffb'

    >>> vigenere_cipher({}, "what?")
    '?????'

    >>> vigenere_cipher({"a" : "x", "m" : "s", "p" : "h", "s" : "m", " " : " ", "o" : "b", "r" : "w", "k" : "v", "t" : "a", "e" : "b", "h" : "w"}, "x marks the spot")
    '? sxwvm awb mhba'
    """

    out = ""
    for x in text:
        out += key.get(x, "?")

    return out


doctest.run_docstring_examples(vigenere_cipher, globals())


def swap_dictionary(d):
    """
    Swap the keys/values of the given dictionary. Since values may be repeated, the new dictionary will have a list of keys as values.

    >>> swap_dictionary({"a" : "b", "b" : "c", "c" : "d", "d" : "e", "e" : "f", "f" : "b"})
    {'b': ['a', 'f'], 'c': ['b'], 'd': ['c'], 'e': ['d'], 'f': ['e']}

    >>> swap_dictionary({"Jan": "Winter", "Fev": "Winter", "Mar": "Spring", "Apr": "Spring", "Dec": "Winter", "Jul" : "Summer"})
    {'Winter': ['Jan', 'Fev', 'Dec'], 'Spring': ['Mar', 'Apr'], 'Summer': ['Jul']}

    >>> swap_dictionary({"Arya": "Stark", "Sansa": "Stark", "Jon": "Stark", "Cersei": "Lannister", "Jaime": "Lannister", "Tyrion": "Lannister"})
    {'Stark': ['Arya', 'Sansa', 'Jon'], 'Lannister': ['Cersei', 'Jaime', 'Tyrion']}
    """

    out = {}
    for k, v in d.items():
        if v in out:
            out[v].append(k)
        else:
            out[v] = [k]

    return out


doctest.run_docstring_examples(swap_dictionary, globals())


def iso_strings(s1, s2):
    """
    Two strings are isomorphic if there is each character in one corresponds
    exactly to a character in the other. Determine if two strings are isomorphic,
    and return that correspondence if that is the case. Otherwise, return None.

    >>> iso_strings("CABAC","WXYXW")
    {'C': 'W', 'A': 'X', 'B': 'Y'}

    >>> iso_strings("HAL9000","XZY7999")
    {'H': 'X', 'A': 'Z', 'L': 'Y', '9': '7', '0': '9'}

    >>> iso_strings("HELLO","JELLO")
    {'H': 'J', 'E': 'E', 'L': 'L', 'O': 'O'}

    >>> iso_strings("HELLO","HELMO")

    """

    if not (len(s1) is len(s2)):
        return None

    out = {}
    for i, c in enumerate(s1):
        if c in out:
            if not (out[c] is s2[i]):
                return None
        else:
            out[c] = s2[i]

    return out


doctest.run_docstring_examples(iso_strings, globals())


def relational_composition(r1, r2):
    """
    Implement relational composition between two binary relations. A and B are
    related by composition the composition R.S if R relates A to some C that is
    related to B vy S. Consider relations to be sets of pairs.

    >>> relational_composition({("A","C")}, {("C","B")})
    {('A', 'B')}

    >>> relational_composition({("A","C"),("B","C")}, {("C","B"),("C","X")})
    {('A', 'B'), ('B', 'B'), ('A', 'X'), ('B', 'X')}

    >>> relational_composition({("A","C"),("B","Y")}, {("C","B"),("Y","X")})
    {('A', 'B'), ('B', 'X')}

    >>> relational_composition({("A","C"),("B","C")}, {("B","C")})
    set()
    """

    out = set()
    for a, b in r1:
        for c, d in r2:
            if b == c:
                out.add((a, d))

    return out


doctest.run_docstring_examples(relational_composition, globals())


def flatten(nested):
    """
    Flatten a nested list into a flat list.

    >>> flatten([[1,2],[3,4]])
    [1, 2, 3, 4]

    >>> flatten([1,2,3])
    [1, 2, 3]

    >>> flatten([[2,4,5,[3,5],[2,4]],[2,4,[9,6]],7])
    [2, 4, 5, 3, 5, 2, 4, 2, 4, 9, 6, 7]
    """

    out = []
    for v in nested:
        if isinstance(v, list):
            out.extend(flatten(v))
        else:
            out.append(v)

    return out


doctest.run_docstring_examples(flatten, globals())


def max_path(tree):
    """
    Assume a binary tree defined as nested pairs, until leaves represented by
    None. Calculate the path that gives the maximum sum of values.

    >>> max_path((10,(30,None,None),(50,None,None)))
    [10, 50]

    >>> max_path((10,(30,(40,None,None),None),(50,None,None)))
    [10, 30, 40]

    >>> max_path((10,(30,(40,None,None),None),(50,(44,None,None),(76,None,None))))
    [10, 50, 76]

    >>> max_path((10,None,None))
    [10]
    """

    if tree is None:
        return []

    left = max_path(tree[1])
    right = max_path(tree[2])

    if sum(left) > sum(right):
        out = left
    else:
        out = right

    out.insert(0, tree[0])

    return out


doctest.run_docstring_examples(max_path, globals())


def get_first_last(names):
    return names[0] + " " + names[-1]


def passing_students(students):
    """
    Filter the students that have a passing grade (average >= 10) and return their
    first and last name. Try to use the functional programming style.

    >>> passing_students([("Harry James Potter", (7, 12, 3)),("Hermione Jean Granger", (4, 19, 8)),("Ronald Bilius Weasley", (11, 2, 17))])
    ['Hermione Granger', 'Ronald Weasley']

    >>> passing_students([("Luke Skywalker of Tatooine", (5, 14, 9)), ("Leia Organa of Alderaan", (6, 3, 20)), ("Anakin Skywalker of Tatooine", (13, 7, 1))])
    []

    >>> passing_students([("Peter Benjamin Parker", (9, 4, 12)), ("Diana Prince of Themyscira", (15, 8, 6)), ("Clark Joseph Kent", (2, 17, 11))])
    ['Clark Kent']
    """

    return [
        get_first_last(n.split()) for n, gs in students if (sum(gs) / len(gs)) >= 10
    ]


doctest.run_docstring_examples(passing_students, globals())


def polyalphabetic_cypher(shift, text):
    """
    Implement a polyalphabetic substitution cypher that receives the shift as an
    arbitrary function that, given an index position and a character, returns
    another character.

    >>> polyalphabetic_cypher(lambda i,j: chr(ord(j)+i), "hello world")
    'hfnos%}vzun'

    >>> polyalphabetic_cypher(lambda i,j: chr((ord(j)*2*i)%24+ord("A")), "hello world")
    'AKAAAIMSAAI'

    >>> polyalphabetic_cypher(lambda i,j: j, "hello world")
    'hello world'
    """

    l = [shift(i, c) for i, c in enumerate(text)]
    return "".join(l)


doctest.run_docstring_examples(polyalphabetic_cypher, globals())


def num_students():
    """
    Read file "alunos.csv" and count the number of students.

    >>> num_students()
    100
    """

    with open("material/alunos.csv") as alunos_file:
        lines = alunos_file.readlines()
        return len(lines) - 1


doctest.run_docstring_examples(num_students, globals())


def process_students():
    """
    Read file "alunos.csv" and process the data into a dictionary from student
    ids to a tuple contained the rest of the information.

    >>> process_students()["a1"]
    ('Aysha Melanie Gilberto', 'LEI', (12, 8, 19, 8))

    >>> process_students()["a14"]
    ('Kaylla Pessego', 'LCC', (10, 14, 17, 15))

    >>> process_students()["a31"]
    ('Eva Manuel Caio', 'ENGFIS', (12, 16, 20, 16))
    """

    with open("material/alunos.csv") as alunos_file:
        lines = alunos_file.readlines()

        out = {}
        lines.pop(0)
        for l in lines:
            l = l.rstrip("\n")
            data = l.split(",")
            out[data[0].strip('"')] = (
                data[1].strip('"'),
                data[2].strip('"'),
                tuple([int(c) for c in data[3:]]),
            )

        return out


doctest.run_docstring_examples(process_students, globals())


def best_average():
    """
    Finds the students with best average in alunos.csv.

    >>> best_average()
    'a80'
    """
    alunos = process_students()

    return max(alunos, key=lambda k: sum(alunos[k][2]) / len(alunos[k][2]))


doctest.run_docstring_examples(best_average, globals())


def good_average():
    """
    Find all students with average higher than 15 in alunos.csv.

    >>> len(good_average())
    30
    """

    return [k for k, v in process_students().items() if (sum(v[2]) / len(v[2])) > 15]


doctest.run_docstring_examples(good_average, globals())
