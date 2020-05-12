import random

session_name = ''
session_id = ''

members = {
    '007': 'admin',
}

members_record = {
    '007': 'settled'
}

books = {
    '1': 'Da Vinci Code',
    '2': 'Angels and Demons',
    '3': 'Fifty Shades of Grey'
}

books_status = {
    '1': 'available',
    '2': 'available',
    '3': 'available',
}


def id_issue():
    Id = random.randint(1001, 1999)
    if Id in members:
        id_issue()
    else:
        return Id


def to_borrow_a_book():
    print('List of Books with their S.no')
    print(books)
    book_no = input('Enter the S.no of the book which you want to borrow:')
    if book_no in books:
        if books_status[book_no] == 'available':
            if members_record[session_id] == 'settled':
                books_status[book_no] = 'unavailable'
                members_record[session_id] = 'pending'
                print('Book Issued')
            else:
                print("We can't issue you a book sir. You already have one book to return.")
        else:
            print('Sorry Sir! The book is currently unavailable')
    else:
        print('WRONG S.No')


def to_return_a_book():
    print('List of Books with their S.no')
    print(books)
    book_no = input('Which book do you want to return?')

    if book_no in books:
        if books_status[book_no] == 'unavailable':
            if members_record[session_id] == 'pending':
                books_status[book_no] = 'available'
                members_record[session_id] = 'settled'
                print('Book Returned')
            else:
                print("You must have mistaken sir. All your accounts are settled")
        else:
            print("There is some mistake. Please check the book's serial number again")
    else:
        print('WRONG S.No')


def to_entry_a_new_book():
    if session_id == '007' and session_name == 'admin':
        print('Howdy, ' + session_name)
        book_no = input('Enter the S.no of the Book:')
        book_name = input('Enter the name of the Book:')
        if book_no in books:
            print('This serial no is already available and can not be assigned to any other book')
        else:
            books[book_no] = book_name
            books_status[book_no] = 'available'

    else:
        print("You don't have access to this area")


print('Welcome to "World of Wisdom"')
user_status = input('Do you have your membership card?(yes/no)')

choice = '0'

if user_status == 'yes':
    mem_id = input('Enter your member id:')
    mem_name = input('Enter your name:')
    if mem_id in members:
        if mem_name == members[mem_id]:
            print('Welcome ' + mem_name)
            session_id = mem_id
            session_name = mem_name
        else:
            print('Wrong Username')
            choice = '4'
    else:
        print('Wrong ID or username')
        choice = '4'


elif user_status == 'no':
    print('We need some details to issue you a membership card.')
    name = input('Tell me your name:')
    Id = str(id_issue())
    members[Id] = name
    members_record[Id] = 'settled'
    print('Your card is issued with ' + name + ' as your name and ' + Id + ' as your Id.')
    session_name = name
    session_id = Id

else:
    print('Wrong Input')
    choice = '4'

while choice != '4':
    print('So, what do you want to do now?')
    print('Press "1" to BORROW a book')
    print('Press "2" to RETURN a book')
    print('Press "3" to ENTER a new book')
    print('Press "4" to LEAVE the "World of Wisdom"')
    choice = input()
    if choice == '1':
        to_borrow_a_book()
    elif choice == '2':
        to_return_a_book()
    elif choice == '3':
        to_entry_a_new_book()
    elif choice == '4':
        print('Goodbye, ' + session_name)
    else:
        print('WRONG INPUT. Try again!')
