def select_opponents(opps):
    result = []
    for opp in opps:
        if opp[0] < 60 and opp[1] < 600 and opp[2] < 40:
            result.append("Нужный Боец")
        else:
            result.append("Майку Крышка")
    return result


opps = [(66, 674, 38), (88, 450, 78), (59, 599, 32), (59, 600, 33), (60, 800, 43), (88, 555, 38), (55, 585, 38)]
result = select_opponents(opps)
print(result)

l1 = [(66, 674, 38), (88, 450, 78), (59, 599, 32), (59, 600, 33), (60, 800, 43), (88, 555, 38), (55, 585, 38)]
l2 = []
for i in l1:
    if i[0] < 60 and i[1]<600 and i[2]<40:
        l2.append("Нужный Боец")
    else:
        l2.append("Майку Крышка")
print(l2)