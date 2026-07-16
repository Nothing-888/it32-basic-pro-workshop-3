num = int(input("ไปเก็บกี่ร้าน : "))
total = 0

for i in range(1,num) :
    shop = int(input(f"ร้านที่ {i} เก็บ : "))
    total += shop

print("วันนี้เก็บได้ทั้งหมด : ",total)
