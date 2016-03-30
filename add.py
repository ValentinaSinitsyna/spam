import xlrd
import xlsxwriter

def add(): #начало как и в buy.py
    rb = xlrd.open_workbook('in.xlsx')
    sheet = rb.sheet_by_index(0)
    gid=[]
    name=[]
    price=[]
    count=[]
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        gid.append(row[0])
        name.append(row[1])
        price.append(row[2])
        count.append(row[3])
        
    tab=[gid,name,price,count]
    sell=[]


    print("id\tname\tprice\tcount")
    for i in range(len(tab[0])):
        s=''
        for j in range(4):
            s=s+str(tab[j][i])+"\t"
        print(s)

        
   
    while 1:
        src=input("введите id товара или  end для окончания ввода")
        if src=="end" or src=="END": break
        fid=-1 #ищем введеный id  в таблице товаров
        for i,c in enumerate(tab[0]):   
             if c==src: fid=i

        if fid==-1: #если неизвестный товар, то просим ввести информацию о нем
            tab[1].append(input("введите название"))
            tab[3].append(input("введите количество"))
            tab[2].append(input("введите цену"))
            tab[0].append(src)
        else: #если товар есть в таблице, значит просто спрашиваем сколько добавить
            print(tab[1][int(fid)]," цена:",tab[2][int(fid)]," кол-во:",tab[3][int(fid)])
            cnt=input("введите количество")
            if int(cnt)>0:
                 tab[3][int(fid)]=int(tab[3][int(fid)])+int(cnt);
            else:
                print("поставка не может быть отрицательной")

  
    #потом просто перезаписываем измененную таблицу товаров 
    workbook = xlsxwriter.Workbook('in.xlsx')
    worksheet = workbook.add_worksheet()

    for i in range(len(tab[0])):
        worksheet.write(i, 0, tab[0][i])
        worksheet.write(i, 1, tab[1][i])
        worksheet.write(i, 2, tab[2][i])
        worksheet.write(i, 3, tab[3][i])

    workbook.close()
     
    print('запись поставки товара прошла успешно')



