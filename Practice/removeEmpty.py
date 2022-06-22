str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
s_list = []
for i in str_list:
    if i == "":
        pass
    elif i == None:
        pass
    else:
        s_list.append(i)
print(s_list)
  