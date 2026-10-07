# Libary system

from datetime import datetime, timedelta
'''MEMBERS
    ↓
name
id
fine
borrowed book + due date

BOOKS
    ↓
name
id
available

TRANSACTION
    ↓
checkout → assign book + due date
return   → calculate overdue fine + make book available
'''

'''

later feats:
    - api take and data base
'''

books = [
  {
  'name' : 'Baby day Out',
  'id' : 123400,
  'here' : True
}, 
  {
  'name' : 'Into the bad lands',
  'id' : 123401,
  'here' : False
}, 
  {
  'name' : 'The Bible',
  'id' : 123402,
  'here' : False
}, 
  {
  'name' : 'Inmates',
  'id' : 123403,
  'here' : True
}, 
  {
  'name' : 'Prison release',
  'id' : 123404,
  'here' : False
}, 
  {
  'name' : 'Walking in wisdom',
  'id' : 123405,
  'here' : True
}, 
       ]
members = [
  {
  'name' : 'Sam',
  'id' : 345930,
  'fine' : 2.00,
  'borrowed' : [
    {
       'name': 'Into the bad lands',
       'id' : 123401,
       'timeStamp': datetime.now(),
       'due': datetime.now() + timedelta(days=3),
            },
    {
       'name': 'The Bible',
       'id' : 123402,
       'timeStamp': datetime.now(),
       'due': datetime.now() + timedelta(days=5),
            },
  ],
}, 
  {
  'name' : 'Kay',
  'id' : 345931,
  'fine' : 3.50,
  'borrowed' : None,
}, 
  {
  'name' : 'Tee',
  'id' : 345932,
  'fine' : 1.00,
  'borrowed' : None,
}, 
  {
  'name' : 'Vee',
  'id' : 345933,
  'fine' : 2.50,
  'borrowed' : [{
       'name': 'Prison release',
       'id' : 123404,
       'timeStamp': datetime.now(),
       'due': datetime.now() + timedelta(weeks=1),
            }],
}, 
  {
  'name' : 'Dee',
  'id' : 345934,
  'fine' : 3.50,
  'borrowed' : None
}, 
  {
  'name' : 'Tim',
  'id' : 345935,
  'fine' :2.50,
  'borrowed' : None
}, 
       ]

def UIL(inp, datatype = str):
    while True:
        try:
            question = datatype(input(inp))

            if datatype == str and not question.strip():
                raise ValueError

            return question


        except ValueError:
            print("Not Valid")

  
def get_menu():
  print('''
=== Welcome to Tim's Library ===
  1. View available books
  2. Check out a book
  3. Return a book
  4. Pay fine
  5. Exit '''   )
  menu_option = UIL('Enter option : ', int)
  while menu_option not in range(1,5):
    print('Not a valid option')
    menu_option = UIL('Enter Menu Option : ', int)
  return menu_option

def get_user_Id() :
        userId = UIL('Enter User ID : ', int)
        # Check User ID validity
        while userId not in [user['id'] for user in members] :
          print('Invalid User Id')
          userId = UIL('Enter user ID : ', int)
        return userId

def get_book_Id():
  bookId = UIL('Enter Book ID : ', int)
  # Check Book ID validity
  while bookId not in [book['id'] for book in books] :
    print('Invalid Book Id')
    bookId = UIL('Enter Book ID : ', int)
  return bookId

      
def update_borrow_rec(userId,bookId) :
  for member in members:
    if member['id'] == userId and member['fine'] <= 5.00:
      for book in books:
        if book['id'] == bookId and book['here'] == True:
            #due date check
              print(f'Lending {book['name']} to {member['name']} ')
              
              # due datee
              timeStamp = datetime.now()
              due_date = timeStamp + timedelta(weeks=3)
              print(f'Due date - {due_date}')
  
              #Update recs
              if member['borrowed'] == None:
                member['borrowed'] = {
                   'name': book['name'],
                   'id' : book['id'],
                   'timeStamp': timeStamp,
                   'due': due_date
                }
              else:
                member['borrowed'].append({
                   'name': book['name'],
                   'id' : book['id'],
                   'timeStamp': timeStamp,
                   'due': due_date
                })
          
              book['here'] = False
              return True
        elif book['here'] == False:
          print('Book unavailable here, check available books')
          break
    elif member['id'] == userId:
              print(f"{member['name']} owes {member['fine']}")
              print('User needs to owe less than £5')
              print('Pay up fine at desk to checkout')
              libsys()

def update_return_rec(userId,bookId):
  for member in members:
    if member['id'] == userId:
      for book in books:
        if book['id'] == bookId and book['here'] == False:
            #due date check
              print(f'Returning {book['name']} from {member['name']}  ')

              # Calc days left / over due and update member fine
              for borrowed in member['borrowed']:
                  if bookId == borrowed['id']:
                    # update fine
                    late_days = -(datetime.now() - borrowed['due']).days
                    fine = late_days * 0.50
                    if fine > 0:
                      print(f'{fine} added to account because you were {late_days} days late')
                      member['fine'] = member['fine'] + fine
                      print(f'{member['name']} total fine is now {member['fine']}')
                    # Update member borrowed rec
                    member['borrowed'].remove(borrowed)
                    book['here'] = True
                    
                  else:
                    print(f"{member['name']} didn't borrow borrow {book['name']}")
                          
              return True
        elif book['here'] == False:
          print('Book already available here, check available books')
          break

  print('feature under dev')
  
  #get bookId and UserId


def returnBook():
  bookId = get_book_Id()
  userId = get_user_Id()
  if update_return_rec(userId,bookId):
        print('Return Complete') 
  else:
    print('Return failed')
  libsys()

def checkout():
  # Get Book
  bookId = get_book_Id()
  userId = get_user_Id()
  if update_borrow_rec(userId,bookId):
        print('Checkout Complete') 
  else:
    print('Checkout failed')
  libsys()


def payFine():
  print('Feat under dev')
      
def libsys():
    # Display Options and request user choice of action
  
  menu_option =  get_menu()

  if menu_option == 1:
    print('\n=== Available Books ===')
    for book in books:
      if book['here'] == True :
        print(f'  {book['id']} - {book['name']}')
    libsys()
  
  elif menu_option == 2:
    print('\n=== Checkout Book ===')
    checkout()
    
  elif menu_option == 3:
    print('\n=== Return a Book ===')
    returnBook()
    
  elif menu_option == 4:
    print("\n=== Pay fine ===")
    payFine()
    
  elif menu_option == 5:
    print("\n=== Thank You for using Tim's Libery ===")
    raise SystemExit()

libsys()