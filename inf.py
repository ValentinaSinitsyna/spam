import xlrd
import xlsxwriter

def inf(): #аналогичным образом что и в buy.py считываем информацию из файла, только теперь из таблицы продаж
    rb = xlrd.open_workbook('out.xlsx')
    sheet = rb.sheet_by_index(0)
    gid=[]
    ssum=[]
    desc=[] 
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        gid.append(int(row[0]))
        ssum.append(row[1])
        desc.append(row[2]) 
        
    tab=[gid,ssum,desc]
     

    #вывод информации из считанный таблицы
    print("id\tsum")
    for i in range(len(tab[0])):
        s=''
        for j in range(2):
            s=s+str(tab[j][i])+"\t"
        print(s)

        
   
    while 1:
        src=input("введите id продажи или  end для окончания ввода")
        if src=="end" or src=="END": break
        fid=-1
        for i,c in enumerate(tab[0]):   
             if int(c)==int(src): fid=i #ищем введенный id

        if fid==-1:print("несуществующий id")
        else: #выводим информацию
            print("id:",tab[0][int(fid)],"; сумма:",tab[1][int(fid)],";описание:",tab[2][int(fid)])
            

   
    print('запись поставки товара прошла успешно')



