def solution(my_string):
    data = ['a', 'e', 'i', 'o', 'u']
    
    my_string_list = list(my_string)
    for i in my_string_list:
        if i in data:
            my_string = my_string.replace(i, '')

    return my_string;