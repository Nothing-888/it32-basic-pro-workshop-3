print("เป้าหมาย 50,000")

total = 0
i = 1
while total < 50000 :
    shop = int(input(f"ร้านที่ {i} เก็บ : "))
    total += shop
    i += 1
    

print("วันนี้เก็บได้ทั้งหมด : ",total)
print(f"เก็บได้ {i} ร้าน")