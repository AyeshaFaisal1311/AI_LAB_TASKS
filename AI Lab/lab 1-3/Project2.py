
def fizzbuzz(): 
    try:
        start_point=int(input("enter start value of range"))
        end_point=int(input("enter end value of range"))
        div1=int(input("enter 1st divisor(default:3)" or 3))
        div2=int(input("enter 2nd divisor(default:5)" or 5))
        
        if start_point<0 or start_point>end_point:
            print('''start value cann't be less than 0
                   or grater then end value.
                   Using Default Range 1-100''')
            
            start_point,end_point=1,100


    except ValueError:
        print("Invalid input. Please enter valid integer.")
        return
    output = []
    
    for i in range(start_point, end_point+1):
        if i% 5 == 0 and i % 3 == 0:
            output.append("FIZZBUZZ")
        elif i % 3 == 0:
            output.append("FIZZ")
        elif i % 5 == 0:
            output.append("BUZZ")
        else:
            output.append(str(i))
    
    print(output)
    
fizzbuzz()
