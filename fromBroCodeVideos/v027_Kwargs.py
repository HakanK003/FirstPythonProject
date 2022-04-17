# **kwargs =   parameter that will pack all arguments into a dictionary
#                       useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):  # we can use another name but, ** must
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="H", middle="K", last="3")
