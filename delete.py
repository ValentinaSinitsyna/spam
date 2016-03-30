import xlrd
import xlsxwriter

def delete(): #считывание и вывод информации на экран аналогичен buy.py
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
             if int(c)==int(src): fid=i

        if fid==-1:print("несуществующий id")
        else: #если нашли введенный id, то запарашиваем пароль и удалаем нужные элементы списка
           if input("введите пароль")=='root': 
               tab[0].pop(int(fid))
               tab[1].pop(int(fid))
               tab[2].pop(int(fid))
               print('запись успешно удалена')
           else:
               print("введен неверный пароль")
          
   
    #переписываем измененный файл списка продаж
    workbook = xlsxwriter.Workbook('out.xlsx')
    worksheet = workbook.add_worksheet()

    for i in range(len(tab[0])):
        worksheet.write(i, 0, tab[0][i])
        worksheet.write(i, 1, tab[1][i])
        worksheet.write(i, 2, tab[2][i]) 

    workbook.close()
           
           
   
    



