import xlrd
import xlsxwriter

def buy():
    rb = xlrd.open_workbook('in.xlsx')
    sheet = rb.sheet_by_index(0)
    gid=[] #id 
    name=[]
    price=[]
    count=[]
    for rownum in range(sheet.nrows): #считываем данные из файла в списки
        row = sheet.row_values(rownum)
        gid.append(row[0])
        name.append(row[1])
        price.append(row[2])
        count.append(row[3])
        
    tab=[gid,name,price,count] #объеденяем их в один двумерный
    sell=[] #список, где будет формироваться запись в продажи

    #вывод на экран списка товаров
    print("id\tname\tprice\tcount")
    for i in range(len(tab[0])):
        s=''
        for j in range(4):
            s=s+str(tab[j][i])+"\t"
        print(s)

        
    ssum=0; #сумма продажи
    gds=''; #описание продажи
    while 1:
        src=input("введите id или название товара или end для окончания ввода")
        if src=="end" or src=="END": break
        fid=-1 #адрес нужного товара в таблице
        for i,c in enumerate( tab[0] if src.isdigit() else tab[1] ):   
             if c==src: fid=i
        if fid==-1: print("несуществующий товар")
        else:
            print(tab[1][int(fid)]," цена:",tab[2][int(fid)]," кол-во:",tab[3][int(fid)])
            cnt=input("введите количество")
            if int(cnt)<=int(tab[3][int(fid)]): #если товара достаточно 
                ssum+=int(cnt)*int(tab[2][int(fid)])  #добавляем стоимость в сумму продажи  
                gds=gds+" "+tab[1][int(fid)]+" x"+cnt+";" #и описание 
                tab[3][int(fid)]=int(tab[3][int(fid)])-int(cnt); #и вычитаем нужное количество из  исходной таблицы
            else:
                print("на складе недостаточно товара")

    print(ssum,gds)

    #теперь переписываем файлы с новыми данными
    rc = xlrd.open_workbook('out.xlsx') #продажи
    sheet1 = rc.sheet_by_index(0)
    idd=[] #id
    sm=[] #сумма продажи
    desc=[] #описание

    #формируем список из файла продаж *по-хорошему это нужно вынести в отдельную функцию, а то в каждом файле по повтору 
    for rownum in range(sheet1.nrows):
        row = sheet1.row_values(rownum)
        idd.append(row[0])
        sm.append(row[1])
        desc.append(row[2])
    
    sell=[idd,sm,desc] 

    sell[0].append(len(sell[0])+1)  #добавляем новую запись в список продаж, id формируем как равный номеру записи
    sell[1].append(ssum)
    sell[2].append(gds)


    workbook = xlsxwriter.Workbook('out.xlsx') #открываем файл для записи
    worksheet = workbook.add_worksheet()
    

    for i in range(len(sell[0])):   #и записываем новую таблицу в него *и да, снова надо бы вынести все это в  отдельную функцию*
        worksheet.write(i, 0, sell[0][i])
        worksheet.write(i, 1, sell[1][i])
        worksheet.write(i, 2, sell[2][i])

    workbook.close()


    #повторяем операцию с фалом товаров, записывая туда с учетом купленных товаров
    workbook = xlsxwriter.Workbook('in.xlsx')
    worksheet = workbook.add_worksheet()

    for i in range(len(tab[0])):
        worksheet.write(i, 0, tab[0][i])
        worksheet.write(i, 1, tab[1][i])
        worksheet.write(i, 2, tab[2][i])
        worksheet.write(i, 3, tab[3][i])

    workbook.close()
     
    print('запись продажи успешно добавлена')



