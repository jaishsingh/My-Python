list=list(map(int, (input("Enter the sequence: ").split(" "))))
element_found=False
for element in list:
    if (element%2==0):
        print(f"First user element={element}")
        element_found=True
        break
if(not element_found):
    print("No even element found.")
