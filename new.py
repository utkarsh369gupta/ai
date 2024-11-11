import pandas as pd
import time
from csv import writer

bdata = pd.read_csv('data.csv')

genres = ['fiction', 'nonfiction', 'science',
          'tech', 'socialism', 'drama', 'unclassified']


def book_suggestion_bot(k):
    print('finding', genres[k-1], 'books for you!!')
    print('.', time.sleep(0.5), '.', time.sleep(0.5), '.')
    time.sleep(1)
    print('top books found !!')
    mask = bdata['Genre'] == genres[k-1]
    metadata = bdata[mask].sort_values(by='rating', ascending=False).head()
    k = 1
    while k != 0:
        if k == 1:
            for i in range(len(metadata)):
                print('book no. ', i+1, '\n', metadata.iloc[i], '\n\n')
                time.sleep(0.8)
        moreinp = input('do you want more books on the genre! [y/n]:-\n')

        if moreinp == 'y':
            k += 5
            metadata = bdata[mask].sort_values(
                by='rating', ascending=False).iloc[k-1:5+k-1]
            for i in range(len(metadata)):
                print('book no. ', i + k, '\n', metadata.iloc[i], '\n\n')
                time.sleep(0.8)
        elif moreinp == 'n':
            k = 0
            print('\n\nenjoy reading!')


print('welcome to BMS!')
z = 0
while z != 1:
    ainp = int(input('\n\n[1] to register yourself as a new member press 1 \n[2] if an existing member enter 2 '
                     ' \nYour input :- '))

    if ainp == 1:
        nname = str(input('Enter your name:-'))
        nphone = str(input('enter your phone number:-'))
        nuid = nname[:3] + nphone[-5:]
        print('registered!! successfully\n directing to main menu..\n\n')
        with open('users.csv', 'a') as f:
            obj = writer(f)
            obj.writerow([nuid, nname, nphone])
            f.close()

    else:
        inp2 = input(
            '[1] To search new book press 1 [2] To navigate to book press 2')
        if inp2 == 1:
            print('select genre:-')
            inp3 = input('[1] fiction'
                         '[2] non fiction'
                         '[3] science'
                         '[4] tech'
                         '[5] socialism'
                         '[6] drama'
                         '[7] unclassified')
            book_suggestion_bot(int(inp3))


