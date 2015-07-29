import ParseStateAndCapitals

def  main():
    text_input = raw_input('yeh batao ki tumhara naam kya hai? \n')
    print 'Hello ' + str(text_input) + ' !!!'
    random_state = ParseStateAndCapitals.get_random_state()
    state_capital = ParseStateAndCapitals.get_state_capital(random_state)
    capital_input = raw_input('Achha yeh to batao ki ' + random_state + ' ki Capital kya hai ? \n')
    if capital_input == state_capital:
        print'Sahi Jawaab'
    else:
        print 'Galat Jawab'
        print  random_state + ' ki Capital ' + state_capital  + ' hai.'




if __name__ == '__main__':
    main()