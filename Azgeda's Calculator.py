reply = 1
while reply < 2:
    class Calc(object):
        def __init__(self, a, b):
            
            self.value1 = a
            self.value2 = b
        def addition(self):
            return self.value1 + self.value2
        
        def multiply(self):
            return self.value1 * self.value2
        
        def division(self):
            return self.value1 / self.value2
        
        def subtraction(self):
            return self.value1 - self.value2
        print("  ")
        print("Welcome to Azgeda's Calculator. ")
        print("  ")
        print("Please select the calculation you want to perform.")
        print("  ")
        print("Addition(1), Multiply(2), Division(3), Subtraction(4) ")
        print("  ")
        

    selection = input("Selection: ")

    v1 = int(input("Please enter first value. "))
    v2 = int(input("Please enter second value. "))

    c1 = Calc(v1,v2)
    
    if selection == "1":
        add_result = c1.addition()
        print("  ")
        print("Result: {}".format(add_result))
        print("  ")
    elif selection == "2":
        multiply_result = c1.multiply()
        print("  ")
        print("Result: {}".format(multiply_result))
        print("  ")
    elif selection == "3":
        division_result = c1.division()
        print("  ")
        print("Result: {}".format(division_result))
        print("  ")
    elif selection == "4":
        subtraction_result = c1.subtraction()
        print("  ")
        print("Result: {}".format(subtraction_result))
        print("  ")
    else:
        print("Error there is no proper selection. ")
        

    dongu = input("Would you like to make a new calculation ? (yes or no) ")
    if dongu == "yes":
        reply = 1
    else:
        reply = 2



