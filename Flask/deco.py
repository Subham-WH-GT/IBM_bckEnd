#Creating user-defined decorators:

#Defining a Decorator--
def jsonify_decorator(function):
    def modify_output():
        return {'output':function()}
    
    return modify_output

# Lets use the decorator--
@jsonify_decorator
def hello():
    return 'Hello Subham!'

@jsonify_decorator
def add():
    num1=int(input("Enter First number: "))
    num2=int(input("Enter second number: "))

    return num1+num2

print(hello())
print(add())