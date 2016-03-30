import buy as b
import add as a
import inf as i
import delete as d


while 1:
    print(' 1:продажа товара\n 2:поставка товара\n 3:данные по продажам\n 4:удалить\n 0:выход \n')
    c=input("введите номер пункта меню")
    if c=='1': b.buy()
    if c=='2': a.add()
    if c=='3': i.inf()
    if c=='4': d.delete()
    if c=='0': break
