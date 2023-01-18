# grammar
# E->T+E | T
# T-> F*T | F
# F-> ( E ) | i

def parse(string):
    pointer = 0
    def match(symbol):
        nonlocal pointer
        if pointer < len(string) and string[pointer] == symbol:
            print("Matched", symbol)
            pointer += 1
            return True
        print("Not matched", symbol)
        return False

    def E():
        print("Expanding E")
        if not T(): return False
        if match('+'):
            if not E(): return False
            return True
        return True

    def T():
        print("Expanding T")
        if not F(): return False
        if match('*'):
            if not T(): return False
            return True
        return True

    def F():
        print("Expanding F")
        if match('i'): return True
        if match('('):
            if not E(): return False
            if not match(')'): return False
            return True
        return False
    if E() and pointer == len(string):
        print("Parsed successfully")
        return True
    print("Parsing failed.")
    return False

string = "i+i"
if parse(string):
    print("The string: '" + string + "' is a valid sentence according to the grammar.")
else:
    print("The string: '" + string + "' is not a valid sentence according to the grammar.")
