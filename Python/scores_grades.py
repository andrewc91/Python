def grades():
    user_input = input()

    if 90 < user_input < 101:
        print "Score:", user_input, "; Your grade is A"
    elif 80 < user_input < 90:
        print "Score:", user_input, "; Your grade is B"
    elif 70 < user_input < 80:
        print "Score:", user_input, "; Your grade is C"
    elif 0 < user_input < 70:
        print "Score:", user_input, "; Your grade is D"
    else:
        print "End of the program. Bye!"

grades()
