def enter_num():
    print('Enter an integer')
    choice = input('>>')
    try:
        print (int(choice))
    except:
        print( 'Error: try again')
        enter_num()
enter_num()


