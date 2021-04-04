list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']

x = list(filter(str.isdigit, list_of_strings))
y = type(filter(str.isdigit, list_of_strings))
print(type(x[0]))
