from ast import Return


def calculate_name_value(nimi, table_file):
    """
    :param str nimi: Nimi
    :param file tabel.txt: nime arvede fail 
    :rtype: int nime number
    """
    with open('tabel.txt', 'r') as f:
        nimi_arved = {}
        for line in f:
            täht, number = line.strip().split(',')
            nimi_arved[täht] = int(number)

    nimi_arv = 0
    for täht in nimi.lower():
        if täht in nimi_arved:
            nimi_arv += nimi_arved[täht]

    while nimi_arv > 9:
        uus_arv = 0
        for digit in str(nimi_arv):
            uus_arv += int(digit)
        nimi_arv = uus_arv

    return nimi_arv

