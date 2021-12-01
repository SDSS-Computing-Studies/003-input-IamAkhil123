#! python3

txt = input("enter name")

txt2 = input("enter email address")

x = txt.strip() + (",")
y = txt2.strip() + (".")

print("Your name is " + x + " and your email is " + y)
