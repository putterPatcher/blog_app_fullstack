def verify_admind():fun()
def verify_adminc():fun()
def verify_adminb():fun()
def verify_admina():fun()
verify_admin_iter = iter(
[
verify_admina,verify_adminb,verify_adminc,verify_admind
]
)

import os
processing = True
def __add_function(name, lines: list[str], index_name: int, s: str):
    def next_name(i):
        j = i[len(name):][-1]
        if j != 'Z':
            j = chr(ord(j)+1)
            return i[:-1]+j
        else:
            return i+j
    new_lines = lambda name: ['{}_iter = iter(\n'.format(name), '[\n', '{}a\n'.format(name), ']\n', ')\n\n']
    if index_name != -1:
        line = lines[a:=index_name+2]
        if s:
            line = line[:-1]+","+(func_name:=next_name(s))+"\n"
        else:
            line = line[:-1]+","+(func_name:=next_name(line[:-1]))+"\n"
        lines[a] = line
    else:
        lines = new_lines(name) + lines
        func_name = '{}a'.format(name)
    line = "def {}():fun()\n".format(func_name)
    lines = [line,] + lines
    return lines, func_name;
def totalMiddlewares(n: int, name: str):
    global processing
    processing = True
    try:
        # global processing
        with open('{}/get_functions.py'.format(os.path.dirname(__file__)), 'r') as file:
            lines = file.readlines();
            index_name = -1
            s = None
            try:
                index_name = lines.index("{}_iter = iter(\n".format(name))
                n = n - len(lines_array:=(lines[index_name+2].split(',')))
                if n < 0:
                    processing = False
                    return True
                s = lines_array[-1][:-1]
                del lines_array
            except:
                pass
            for _ in range(n):
                lines, s = __add_function(name, lines, index_name, s)
                if index_name == -1:
                    index_name = lines.index("{}_iter = iter(\n".format(name))
                else:
                    index_name += 1
        print("added {}".format(n));
        def update_lines(lines):
            with open('{}/get_functions.py'.format(os.path.dirname(__file__)), 'w') as file:
                new_lines = ''
                for i in lines:
                    new_lines+=i
                file.write(new_lines)
        update_lines(lines);
        processing = False
        return True;
    except:
        return False;

def check_processing():
    global processing
    return processing
