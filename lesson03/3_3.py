def my_func(arg_1, arg_2, arg_3):
    my_tuple = arg_1, arg_2, arg_3
    result = sum(my_tuple) - min(my_tuple)
    print(result)

my_func(300, 30, 3)