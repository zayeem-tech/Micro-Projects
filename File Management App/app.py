import os
import time

def create_file(filename):
    try:
        with open(filename, 'x'):
            print(f'File Name {filename}: Create successfully1')
    except FileExistsError:
        print(f'File name {filename} already exists!')
    except Exception as E:
        print('An error occurred!')

def view_all_files():
    files= os.listdir()
    if not files:
        print('No file found.')
    else:
        print('Files in directory.')
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully.')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error has occured during deletion of {filename}')
    
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f'Content of \'{filename}\' :\n{content} ')
    except FileNotFoundError:
        print(f'{filename} does not exist.')
    except Exception as e:
        print('An error has occured.')

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter data to add: ')
            f.write('\n'+content+'\n')
            print(f'Content add to {filename} successfully.')
    except FileNotFoundError:
        print(f'{filename} does not exist.')
    except Exception as e:
        print('An error has occured.')

def main():
    while True:
        time.sleep(2)
        print('\nFILE MANAGEMENT APP:')
        print('1- Create file')
        print('2- View all files')
        print('3- Delete file')
        print('4- Read file')
        print('5- Edit file')
        print('6- Exit app')
        choice = int(input('What would you like to do? '))
        match choice:
            case 1:
                filename = input('Enter file name: ')
                create_file(filename)
            case 2:
                view_all_files()
            case 3:
                filename = input('Enter file name: ')
                delete_file(filename)
            case 4:
                filename = input('Enter file name: ')
                read_file(filename)
            case 5:
                filename = input('Enter file name: ')
                edit_file(filename)
            case 6:
                break


main()