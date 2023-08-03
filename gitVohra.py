'''I am working by myself for this exercise. 
I will be creating this script and adding it to the staging area along with comitting it.
'''


def sayingHello(name):
    '''Simple function that makes a greeting with a parameter 'name' and retruns the greeting. '''
    greeting = "Hello " + name
    return greeting


def main():
    '''The main function where my name will be passed to the 'sayingHello' function and printed with the greeting.'''
    name = "Aziz"
    
    message = sayingHello(name)
    
    print(message)

'''Calling main'''
main()
    
    
    