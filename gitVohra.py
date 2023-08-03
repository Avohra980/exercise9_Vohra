'''I am working by myself for this exercise. 
I will be creating this script and adding it to the staging area along with comitting it.
'''


def sayingHello(name):
    '''Simple function that makes a greeting with a parameter 'name' and retruns the greeting. '''
    greeting = "Hello " + name
    return greeting

def sayingFarewell(name):
    '''Simple function that makes a farewell message with a parameter 'name' and retruns the farewell. '''
    farewell = "Bye " + name
    return farewell

def main():
    '''The main function where my name will be passed to the 'sayingHello' function and printed with the greeting.'''
    name = "Aziz"
    
    message = sayingHello(name)
    message2 = sayingFarewell(name)
    
    print(message)
    print(message2)

'''Calling main'''
main()
    
    
    