#finding the birhday out of 7 days in a week.
print("Welcome!")
import datetime
print("Enter your birthday in the format like YYYY/MM/DD\n(as an example 1998/03/06)")
x=input()
x=str(x)
y=int(x[:4])
if int(x[5])==0:
    m=int(x[6])
else:
    m=int(x[5:7])
if int(x[8])==0:
    d=int(x[9])
else:
    d=int(x[8:])
p=datetime.datetime(y,m,d)
print("Congrats!you born on {}.".format(p.strftime("%A")))
