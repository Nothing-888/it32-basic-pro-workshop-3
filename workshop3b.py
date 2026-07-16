print("เป้าหมาย 50,000")

total = 0
i = 0
while total < 50000 :
    i += 1
    shop = int(input(f"ร้านที่ {i} เก็บ : "))
    total += shop
    
    

print("วันนี้เก็บได้ทั้งหมด : ",total)
print(f"เก็บได้ {i} ร้าน")