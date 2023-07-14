Varieties={
    "Veggie Pizza":450,
    "Pepperoni Pizza":500,
    "MeatPizza":600,
    "Margherita Pizza":690,
    "BBQ Chicken Pizza":750,
    "Hawaiian Pizza":900
}
for key,value in Varieties.items():
    print(key,value)

print("Enter the name of the required item.Enter 'done' to exit.")
price_of_pizza=0
while True:
    key=input("input name: ")
    if key=="done":
        break
    price_of_pizza+=Varieties[key]
    
if price_of_pizza>1500:
    pr_final=price_of_pizza-((10/100)*price_of_pizza)
    print(f"actual price: {price_of_pizza}")
    print(f"total price after 10% discount: {price_of_pizza}")
else:
    print(f"total price: {price_of_pizza}")