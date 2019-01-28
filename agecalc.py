

print("hi!, \nwelcome to the age claculator.\nsimply enter your year of birth and get to know your age \nand also if u a minor,youth or an adult")

yob = int(input("enter your year of birh: "))
current_year=2019
def calc():
    result=  (current_year-yob) 

    if result<18:
        print("you are a minor dear Sir or Madam")
    elif result>18 and result <36:
        print("you are a youth sir/madam")
    else:
        print("you are an elder sir/madam")
  
    print("you are " + (str(result) )+ "yearsOld")

calc()






