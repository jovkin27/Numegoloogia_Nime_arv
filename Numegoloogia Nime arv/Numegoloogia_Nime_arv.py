from Omamodule import*

nimi = input("Введите ваше имя: ")
nimi_arv = calculate_name_value(nimi, 'table.txt')
nimi_arv=str(nimi_arv)
print(f"Число вашего имени {nimi_arv}")
x=nimi_arvestus(nimi_arv,"Nime_väärtused.txt")
