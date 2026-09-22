import random

r = random.randint(1, 100)
s = 0
g = 0

def c(i,a):
 if i<1 or i>100:
  print("??? that is not even in range bro")
 elif i<a:
      print("go UP maybe idk")
 elif i>a:
   print("nah lower lower")
 else:
    print("ok u got it i guess")
    print("tries:",s)
    raise SystemExit

while g != r:
 bad = False
 while bad == False:
  try:
    g = int(input("type num 1-100 now: "))
    c(g,r)
    s=s+1
    bad=True
  except:
    print("not a number lol")
    
