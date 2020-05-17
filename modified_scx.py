import copy

def m_scx(p1x, p2x, city_listx, distance_matrix):
    p1 = []
    p2 = []
    city_list = []
    for i in range(len(city_listx)):
        p1.append(tuple([p1x[i].lat, p1x[i].lon]))
        p2.append(tuple([p2x[i].lat, p2x[i].lon]))
        city_list.append(tuple([city_listx[i].lat, city_listx[i].lon]))

    child = []
    copy_city_list = copy.deepcopy(city_list)

    i = 0
    while i < len(city_list):
        pointer = copy_city_list[0]

        if i == 0:
            child.append(pointer)
            copy_city_list.pop(0)
            i += 1
        
        temp = child[-1]
        
        temp1_index = p1.index(temp)
        temp2_index = p2.index(temp)

        for i1 in range(temp1_index, len(city_list)):
            flag1 = 0
            flag2 = 0
            if p1[i1] not in child:
                dis_p1 = distance_matrix[city_list.index(child[-1])][city_list.index(p1[i1])]
                break
        else:
            for i_p1 in range(len(copy_city_list)):
                if copy_city_list[i_p1] not in child:
                    dis_p1 = distance_matrix[city_list.index(child[-1])][city_list.index(copy_city_list[i_p1])]
                    flag1 = 1
                    break
        
        for i2 in range(temp2_index, len(city_list)):
            if p2[i2] not in child:
                dis_p2 = distance_matrix[city_list.index(child[-1])][city_list.index(p2[i2])]
                break
        else:
            for i_p2 in range(len(copy_city_list)):
                if copy_city_list[i_p2] not in child:
                    dis_p2 = distance_matrix[city_list.index(child[-1])][city_list.index(copy_city_list[i_p2])]
                    flag2 = 1
                    break
        
        if dis_p1 <= dis_p2:
            if flag1 == 1:
                child.append(copy_city_list[i_p1])
                i += 1
            else:
                child.append(p1[i1])
                i += 1
        else:
            if flag2 == 1:
                child.append(copy_city_list[i_p2])
                i += 1
            else:
                child.append(p2[i2])
                i += 1
    
    print(child)
    
    return child