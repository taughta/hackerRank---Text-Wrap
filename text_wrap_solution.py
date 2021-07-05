import textwrap

my_string = input(str())
max_width = input(int())

assert 0 < int(len(my_string)) < 1000
assert 0 < int(max_width) < int(len(my_string))

def wrap(string, max_width):
    solution = ''

    for i in (textwrap.wrap(string, max_width)):
        solution += i + '\n'

    return solution

if __name__ == '__main__':
    print(wrap(str(my_string), int(max_width)))
