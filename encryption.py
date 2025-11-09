

def encryption(massage):
    result = ""
    for char in massage:
        match char:
            case " ":
                result += " "
            case 'a':
                result += 'z'
            case 'b':
                result += 'y'
            case 'c':
                result += 'x'
            case 'd':
                result += 'w'
            case 'e':
                result += 'v'
            case 'f':
                result += 'u'
            case 'g':
                result += 't'
            case 'h':
                result += 's'
            case 'i':
                result += 'r'
            case 'j':
                result += 'q'
            case 'k':
                result += 'p'
            case 'l':
                result += 'o'
            case 'm':
                result += 'n'
            case 'n':
                result += 'm'
            case 'o':
                result += 'l'
            case 'p':
                result += 'k'
            case 'q':
                result += 'l'
            case 'r':
                result += 'i'
            case 's':
                result += 'h'
            case 't':
                result += 'g'
            case 'u':
                result += 'f'
            case 'v':
                result += 'e'
            case 'w':
                result += 'd'
            case 'x':
                result += 'c'
            case 'y':
                result += 'b'
            case 'z':
                result += 'a'
            case _:
                result += char
    return result






