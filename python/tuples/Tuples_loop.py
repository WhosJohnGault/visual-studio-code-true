#this program loops through all elements of a tuple
dimensions=(200,300,350,500)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(600,700)                #we cannot modify individual values but we can redefine the entire tuple
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)
