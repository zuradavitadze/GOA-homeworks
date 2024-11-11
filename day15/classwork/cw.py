giorgi_list = ["vaja", "daviti", "daviti2", True, 12]
res = ""

for item in giorgi_list:
    res += str(item) + " "

print(res.strip())  # ზედმეტი სივრცის მოსაშორებლად


result = " ".join(str(item) for item in giorgi_list)
print(result)