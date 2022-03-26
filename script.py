# A python script that takes in user input as float value >=2.5
# make calculation and print the resulf in a list and find the max number from the list
# number of entries must be either 5 or 7 times



def max_num(): #defining a function max_num

        f= ('enter a Decimal number: ') # sentence to display asking user to input a decimal number
        print(f)
        r = [] # an empty list

       # specifying the number of enteries
        while len(r) < 7:   
        
            try:
                 f = float(input('enter a number: ')) # taking user input
                 print(f)


            # error to display for wrong enter
            except:
                print('value must be a figure') 
                continue

            # calculation part
            if f >= 2.5:
                x = (f * 10) - 15
                r.append(x)
                r = sorted(r)
                print(r)
                print("The maximum number in the list is", (max(r)))
            else:
                print('Number must be greater than 2.5')
            
            
            if len(r) == 5: # condition for user to end operation at len 5
                x = ''.lower
                y = ''.lower


                # asking user to quit the operation at len 5
                while x !='q':

                    print('type q to stop operation or\nenter y two time  to continue')
                    x = input('')
                    if x == 'q':
                        print('The maximum number in the list is', (max(r)))
                        return
                    y = input('')
                    if y=='y':
                        

                        break
                   
  

            
max_num()
    