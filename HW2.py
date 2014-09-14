import math

def resources_vs_time(upgrade_cost_increment, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    ret = []
    total_resource = 5
    resource = 0.0
    for n in range(0, num_upgrade):
        resource = n * math.log(0.5) * resource + 1
        ret.append( (resource, ( (1.0/2.0*n)*(n+1.0) * upgrade_cost_increment)) )
    return ret
#print resources_vs_time(0.5, 20)

#[[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
#print resources_vs_time(1.5, 10)
#[[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]

i1 = 1.0 + (0.5+ 0.5/2) * math.log(1)
i2 = i1 + (0.5+ 0.5/2) #* math.log(1)
i3 = i2 + (0.5+ 0.5/2) #* math.log(2)
print i1, i2, i3
print math.log(2)
