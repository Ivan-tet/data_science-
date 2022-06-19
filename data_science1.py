import csv

zarobki  = ["P_E_ZAR_P1","P_E_ZAR_P2","P_E_ZAR_P3","P_E_ZAR_P4","P_E_ZAR_P5"]
kierunek = ['P_KIERUNEK_NAZWA']
uczelnia = ['P_NAZWA_UCZELNI']
studenci = ['P_N']
studia = ['P_POZIOM_TEKST_PL']

with open('graduates-major-data.csv', encoding='utf-8' ) as file:
    rows = csv.DictReader(file, delimiter=';')

    for row in rows:
         if (row[studenci[0]] > '30'
             and
             row[studia[0]] == 'Studia drugiego stopnia'
             and
             row[kierunek[0]] == row[kierunek[0]]
             and
             row[uczelnia[0]] == row[uczelnia[0]]
             and 
             row[zarobki[0]] > "4000"
             and
             row[zarobki[1]] > "5000"
             and
             row[zarobki[2]] > "60000"
             and
             row[zarobki[3]] > "7000"
             and
             row[zarobki[4]] > "8000"):
             
             print([row[uczelnia[0]],
                    row[kierunek[0]],
                   row[studia[0]],
                   row[studenci[0]],
                   row[zarobki[0]],row[zarobki[1]], row[zarobki[2]], row[zarobki[3]], row[zarobki[4]]], sep = ' ')

keys = "Uczelnia", "Kierunek", "Studia", "Studenci", "Zarobki 1 rok", "Zarobki 2 rok", "Zarobki 3 rok", "Zarobki 4 rok", "Zarobki 5 rok"

lista = [...]

with open ("new_file_1.csv", "w", encoding='utf-8') as  file:
    file_new = csv.writer(file, delimiter=';')
    file_new.writerow(keys)
    for d in lista:
        file_new.writerow(d) 
file.close()
