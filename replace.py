import os
from glob import glob

input_folder = 'files'
output_folder = 'processed'

ahk_file_contents = """#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.\n\n"""


# other customized key: q w e a s ; , .

# qingtian
mapping_dict = {"A": "GW", "S": "VQ",
                "Q": "AQ", ",": "ME",
                "W": "GE", "7": "BSGJ",
                ".": "BE", "2": "BD",
                "1": "MG", "3": "CD",
                "5": "DQ", ";": "GQ",
                "4": "AW",
                "8": "BQ",
                "R": "Q", "T": "W",
                "Y": "E", "U": "R",
                "I": "T", "O": "Y",
                "P": "U",

                "D": "A", "F": "S",
                "G": "D", "H": "F",
                "J": "G", "K": "H",
                "L": "J"}

# mapping_dict = {"W": "Q", "E": "W",
#                 "R": "E", "T": "E",
#                 "U": "R", "Y": "R",
#                 "I": "T", "O": "Y",
#                 "P": "U", "G": "F",
#                 "J": "G", "H": "G",
#                 "K": "H", "L": "J"}

replace_dict = {}

count = 0
for k, v in mapping_dict.items():
    if len(v) == 1:
        ahk_file_contents += f"{k.lower()}::{v.lower()}\n"
        replace_dict[f"+{count}-"] = [v, k]
    else:
        send_info_string = ["{" + str(val.lower()) + "}" for val in v]
        send_info_string = ''.join(send_info_string)
        ahk_file_contents += f"""${k.lower()}::
    Send, {send_info_string}
    return\n"""
        replace_dict[f"+{count}-"] = [f'({v})', k]

    count += 1
ahk_file_contents += '`::g'
print(ahk_file_contents)
with open('genshin_music.ahk', 'w') as ahk_file:
    ahk_file.write(ahk_file_contents)

for file_name in glob(os.path.join(input_folder, "*.txt")):
    with open(file_name, 'r') as read_file:
        file_content = read_file.read()

    for replace_id, replace_pair in replace_dict.items():
        file_content = file_content.replace(replace_pair[0], replace_id)

    for replace_id, replace_pair in replace_dict.items():
        file_content = file_content.replace(replace_id, replace_pair[1])

    new_file_name = file_name.split('\\')[-1]
    new_file_name = os.path.join(output_folder, new_file_name)
    with open(new_file_name, "w") as new_file:
        new_file.write(file_content)

