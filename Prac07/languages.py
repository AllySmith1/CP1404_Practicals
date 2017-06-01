from Prac07.programminglanguage import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", True, 1991)

languages = [ruby, python, vb]

print(python)
print()


print('The dynamically typed languages are:')
for i in range(len(languages)):
    if languages[i].typing == "Dynamic":
        print(languages[i].name)
