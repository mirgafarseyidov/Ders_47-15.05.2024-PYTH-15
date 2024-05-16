"""
Salman bəy 
Home Task 
Salam,hərvaxtınız xeyir. 
1) taskınız ilk olaraq bir text faylı yaradıb içərisinə istədiyiniz bir cümlə yazırsınız .
2) daha sonra həmin textin ilk sətrindəki  sözlərin bütün hərflərini böyük hərflərə çeviririk .
3) Ən sonda bu sözləri başqa  bir text faylı yaradıb onun içərisində yazırıq.

"""
# ---------------- Task Method  ----------



with open("esas.txt","w",encoding="UTF-8") as esas:
    esas.write("Bu ilk cümləmizdir esas text filesinde bu ve ikinci cümle olduğu kimi görsenecek second text filesinde ise böyük hərflərlə yazılacaq.\n Bu isə ikinci cümləmizdir second text filesinde böyük hərflərlə görsənəcək ")

with open("second.txt","w",encoding="UTF-8") as second:
    esas=open("esas.txt","r",encoding="UTF-8")
    second.write(esas.readline().upper())
