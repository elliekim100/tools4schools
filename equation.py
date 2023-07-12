import csv

with open("products.csv", "r") as file:
    csv_reader=csv.reader(file)
#Basic information
    maxPrice = 0.0
    minPrice = 25.0
    maxInventory = 0
    minInventory = 50
    minDemand = 1
    maxDemand = 3
    priceWeight = 0.33
    inventoryWeight = 0.33
    demandWeight = 0.33
    next(csv_reader)
    for row in csv_reader: 
    #Price, Inventory, and Demand Values based on input
        inventory = float(input("What is the inventory of this product?"))
        price = float(row[2])
        demand = float(input("What is the demand of the product (1 being low, 3 being high)?"))

        #Normalized Values (reversed from regular normalization)
        normalizedPrice = 1 - (price - minPrice)/(maxPrice - minPrice)
        print("Normalized Price: " + str(normalizedPrice))
        normalizedInventory = 1 -(inventory - minInventory)/(maxInventory - minInventory)
        print("Normalized Inventory: " + str(normalizedInventory))
        normalizedDemand = (demand - minDemand) / (maxDemand - minDemand)
        print("Normalized Demand: " + str(normalizedDemand))

        #Final value calculation - scaled from 1 - 20 points
        value = priceWeight * normalizedPrice + inventoryWeight * normalizedInventory + demandWeight * normalizedDemand
        print("Value: " + str(value))
        finalValue = round(value * 24 + 1)
        print("Final Value: "+ str(finalValue))
file.close()