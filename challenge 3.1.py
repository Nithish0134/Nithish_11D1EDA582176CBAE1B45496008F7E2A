def linear_search_product(products, target_product):
    indices = []
    
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    
    return indices

products = ["Apple", "Banana", "Orange", "Apple", "Mango", "Apple"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print("Indices of", target_product, ":", result)