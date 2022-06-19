import csv

words = ['Informatyka','stopnia','25', 'Studia drugiego stopnia']
zarobki  = ["P_E_ZAR_P1","P_E_ZAR_P2","P_E_ZAR_P3","P_E_ZAR_P4","P_E_ZAR_P5"]
kierunek = ['P_KIERUNEK_NAZWA']
studia = ['P_POZIOM_TEKST_PL']
studenci = ['P_N']

with open('graduates-major-data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    for row in rows:
            if (words[0] in row[kierunek[0]]
                and
                words[1] in row[studia[0]]
                and
                words[2] < row[studenci[0]] 
                and
                row[zarobki[0]] and row[zarobki[1]] and row[zarobki[2]] and row[zarobki[3]] and  row[zarobki[4]]):
                
                zwrot_inwestycji_1_oraz_2 = float(row[zarobki[1]].replace(',', '.')) - float(row[zarobki[0]].replace(',', '.'))
                zwrot_inwestycji_2_oraz_3 = float(row[zarobki[2]].replace(',', '.')) - float(row[zarobki[1]].replace(',', '.'))
                zwrot_inwestycji_3_oraz_4 = float(row[zarobki[3]].replace(',', '.')) - float(row[zarobki[2]].replace(',', '.'))
                zwrot_inwestycji_4_oraz_5 = float(row[zarobki[4]].replace(',', '.')) - float(row[zarobki[3]].replace(',', '.'))
                
                point1 = float("{:.2f}".format(zwrot_inwestycji_1_oraz_2))
                point2 = float("{:.2f}".format(zwrot_inwestycji_2_oraz_3))
                point3 = float("{:.2f}".format(zwrot_inwestycji_3_oraz_4))
                point4 = float("{:.2f}".format(zwrot_inwestycji_4_oraz_5))
                                
                print([row[kierunek[0]],
                        row[studia[0]],
                        row[studenci[0]],
                        row[zarobki[0]],
                        row[zarobki[1]],
                        row[zarobki[2]],
                        row[zarobki[3]],
                        row[zarobki[4]],
                        point1, point2,point3,point4], sep="   ")

keys = "Kierunek", "Studia", "Studenci", "Zarobki 1 rok", "Zarobki 2 rok", "Zarobki 3 rok", "Zarobki 4 rok", "Zarobki 5 rok", "progress lub regress między 1 a 2 rokiem", "progress lub regress między 2 a 3 rokiem","progress lub regress między 3 a 4 rokiem","progress lub regress między 4 a 5 rokiem"

lista=[ ... ]
       
with open ("new_file_2.csv", "w", encoding='utf-8') as  file:
    file_new = csv.writer(file, delimiter=';')
    file_new.writerow(keys)
    for d in lista:
        file_new.writerow(d) 
file.close()