import sqlite3
import time
import os

print('Łączenie z bazą...')
time.sleep(1)


login = "root"
passwd = "root"

glogin = input( "Podaj login: ")
gpasswd = input("Podaj hasło: ")

#Zdarzenie błędnego logowania
while login != glogin or gpasswd != passwd:
    print("Błędne dane logowania, spróbuj ponownie")
    glogin = input("Podaj login: ")
    gpasswd = input("Podaj hasło: ")

#Widoczność wszystkich baz danych
def search(text):
    print('\n\nDostępne bazy danych:\n-------------------------------------')
    files = set(filter(lambda i: not os.path.isdir(os.path.join("D:\databases",i)), os.listdir("D:\databases")))
    return set(filter(lambda i: i.endswith(text), files))

#Tworzenie baz danych
def createBase():
    name = input('Podaj nazwę bazy którą chcesz stworzyć: ')
    conn = sqlite3.connect(f'D:\databases\{name}.db')
    conn.close()
    print('Baza pomyślnie utworzona')   

#Wyświetlanie wszystkich tabel
def showTables():
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    items = c.fetchall()
    print("\n\nTABELE:\n---------------------------")
    for item in items:
        print(item[0])
    print("\n\n")

#Tworzenie tabel
def createTables():
    nameTable = input('Podaj nazwę tabeli: ')
    HowMany = input('podaj jak dużo chcesz stworzyć kolumn: ')
    nameOne = input('Podaj nazwę pierwszej kolumny: ')
    typeOne = input('Podaj typ danych dla pierwszej kolumny[INT, VARCHAR(), CHAR(), TEXT]: ')
    c.execute(f"CREATE TABLE {nameTable} ({nameOne} {typeOne})")
    IntHowMany = int(HowMany)
    for i in range(IntHowMany-1):
        nameMore = input(f'Podaj nazwę {i+2} kolumny: ')
        typeMore = input(f'Podaj typ danych dla {i+2} kolumny[INT, VARCHAR(), CHAR(), TEXT]: ')
        c.execute(f"ALTER TABLE {nameTable} ADD {nameMore} {typeMore}")

#Wyświetlanie struktury tabeli
def tableStructure():
    inTable = input('Wprowadź nazwę tabeli: ')
    c.execute(f"PRAGMA table_info({inTable})")
    items = c.fetchall()
    print('\nTABELA: ' + inTable.capitalize() + '\n------------------------')
    for item in items:
        print(item[1] + ' ' + "[" + item[2] + "]")
    print('\n')
    conn.commit()

#Dodawanie kolumn do tabeli
def addColumns():
    tableName = input("Podaj nazwę tabeli do której chcesz dodać kolumnę: ")
    columnName = input("Podaj nazwę kolumny: ")
    dataType = input("Podaj typ danych[INT, VARCHAR(), CHAR(), TEXT]: ")
    c.execute(f'ALTER TABLE {tableName} ADD {columnName} {dataType}')

#Usuwanie tabel
def tablesDelete():
    tableDelete = input("Podaj nazwę tabeli którą chcesz usunąć: ")
    c.execute(f'DROP TABLE {tableDelete}')
    print("Tabela została pomyślnie usunięta")

#Usuwanie kolumny z tabeli
def columnsDeletes():
    tableType = input("Podaj nazwę tabeli z której ma być usunięta kolumna: ")
    columnDelete = input("Podaj nazwę kolumny do usunięcia: ")
    c.execute(f'ALTER TABLE {tableType} DROP COLUMN {columnDelete}')

#Dodawanie danych do tabeli
def dataAdd():
    tableAdd = input('Podaj tabelę do której mają być dodane dane: ')
    c.execute(f"PRAGMA table_info({tableAdd})")
    items = c.fetchall()
    print('\nTABELA: ' + tableAdd.capitalize() + '\n------------------------')
    for item in items:
        print(item[1] + ' ' + "[" + item[2] + "]")
    data = input('Teraz mając na zwględzie powyższą kolejość kolumn podaj dane które mają być wprowadzone (oddzielaj dane przecinkiem i pisz je w cudzysłowiu): ')
    c.execute(f'INSERT INTO {tableAdd} VALUES({data})')
    conn.commit()

#Wyświetlanie danych z tabeli
def showData():
    adjust = input("Podaj nazwę tabeli: ")
    print('\nTABELA: ' + adjust.capitalize() + '\n------------------------')
    for row in c.execute(f'SELECT * FROM {adjust}'):
        print(row)
    print("\n\n")

#Usuwanie wierszy z tabeli
def deleteRows():
    rowDeleteTable = input('Podaj tabelę z której chcesz usunąć wiersz: ')
    columnN = input('Podaj nazwę kolumny w której znajduje się item: ')
    rowDelete = input('Podaj element z wiersza kótry pozwoli na usuniącie wierszy powiązanych z tym elementem: ')
    c.execute(f'DELETE FROM {rowDeleteTable} WHERE {columnN}={rowDelete}')
    conn.commit()

#Usuwanie baz danych
def deleteDatabases():
    baseName = input('Podaj nazwę bazy którą chcesz usunąć: ')
    try:
        os.remove(f"D:\databases\{baseName}.db")
        print(f"Usunięto bazę danych o nazwie {baseName}")
    except:
        print("Baza danych o takiej nazwie nie istnieje, podawaj nazwy bez rozszerzeń lub sprawdź czy baza jest na liście")

#Import bazy danych
def baseImport():
    importPath = input('Podaj ścieżkę do pliku z bazą: ')
    try:
        os.replace(importPath,'D:\databases')
    except:
        print("Błąd importowania bazy, plik nie istnieje lub podano niepoprawną ścieżkę")

#Zmiana lub dodanie rekordu
def updateItem():
    updateRow = input('Podaj nazwę tabeli dla której chcesz wykonać update:')
    updateWhere = input('Podaj nazwe kolumny której wartość znajduje się w tym samym wierszu co updatowana komórka: ')
    updateWherer = input('Podaj wartosc komorki dla znajdującej się w tym samym wierszu: ')
    updateSet = input('Podaj wiersz dla którego robisz update: ')
    updateSeter = input('Podaj nową wartość komórki: ')
    c.execute(f'UPDATE {updateRow} SET {updateSet}={updateSeter} WHERE {updateWhere}={updateWherer}')
    print('\n\nKomórka pomyślnie przyjęła nową wartość\n\n')
    conn.commit()

#Główna obsługa MENU
while login == glogin and gpasswd == passwd:
    print("\n###### Witaj w programie do baz danych, poniżej znajduje się lista dostępnych operacji ######\n")
    print("Autorem programu jest Artur Jóźwiak")
    print('Dostępne opcje: \n-----------------------------------------\n|1.Zobacz dostępne bazy danych danych\t|\n|2.Utwórz nową bazę danych\t\t|\n|3.Wejdź do konkretnej bazy danych\t|\n|4.Usuń konkretną bazę danych.\t\t|\n|5.Importuj bazę danych.\t\t|\n|6.Zakończ działanie programu\t\t|\n-----------------------------------------')
    choose = input('Twój wybór[1/2/3/4/5/6]: ')
    match choose:
        case '1':
            os.system('cls')
            print('\n'.join(search('.db')))
            print('\n\n')
        case '2':
            createBase()
        case '3':
            baseconnect = input('Wprowadź nazwę bazy z którą chcesz się połączyć: ')
            os.system('cls')
            conn = sqlite3.connect(f'D:\databases\{baseconnect}.db')
            c = conn.cursor()
            print('Połączyłeś się z bazą danych o nazwie ' + baseconnect + '\n\n')
            while True:
                print('Wybierz operację której chcesz dokonać: ')
                print('---------------------------------------\n1.Wyświetl wszystkie tabele\n2.Utwórz nową tabele\n3.Wyświetl strukturę tabeli\n4.Dodaj nowe kolumny do tabeli\n5.Usuń konkretną tabele\n6.Usunięcie konkretnej kolumny\n7.Dodawanie danych do bazy\n8.Wyświetl dane z tabeli\n9.Usuń wiersz z tabeli\n10.Edytowanie komórki\n11.Wyjdź z bazy\n---------------------------------------')
                choose_table = input(f'[{baseconnect}]Twój wybór[1/2/3/4/5/6/7/8/9/10/11]: ')
                match choose_table:
                    case '1':
                        showTables()
                    case '2':
                        createTables()
                    case '3':
                        tableStructure()
                    case '4':
                        addColumns()
                    case '5':
                        tablesDelete()
                    case '6':
                        columnsDeletes()
                    case '7':
                        dataAdd()
                    case '8':
                        showData()
                    case '9':
                        deleteRows()
                    case '10':
                        updateItem()
                    case '11':
                        print('\n\nZamykanie połączenia z bazą...\n\n')
                        conn.commit()
                        conn.close()
                        os.system('cls')
                        break
                    case _:
                        print('\n\nZły wybór, proszę podać wartość ponownie\n\n')
        case '4':
            deleteDatabases()
        case '5':
            baseImport()
        case '6':
            print('\n\nZamykanie połączenia z programem...\n')
            os.system('cls')
            break
        case _:
            print('\n\nZły wybór, proszę wpisać ponownie\n\n')