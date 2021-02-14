counterQuick=0
counterInsertion=0
def insertionSort(arr, begin,end):
    for x in range(begin+1, end):
        curr = arr[x]
        y = x-1
        while y >= 0 and curr < arr[y]:
            global counterInsertion
            counterInsertion= counterInsertion+1
            arr[y+1] = arr[y]
            y-=1
        arr[y+1] = curr

def swap(arr, first,second):
    global counterQuick
    counterQuick=counterQuick+1
    tmp = arr[first]
    arr[first] = arr[second]
    arr[second] = tmp 
def Quick(arr, smallp, bigp):
    if smallp<bigp:
            leftside = smallp
            rightside = bigp
            pivot = arr[smallp]
            while(leftside < rightside):
                if arr[leftside] < pivot:
                    leftside+=1
                    continue
                if arr[rightside] > pivot:
                    rightside-=1
                    continue
                swap(arr,leftside,rightside)
                leftside+=1
            
            pivot = leftside
            Quick(arr,smallp, pivot-1)
            Quick(arr,pivot+1, bigp)
def main():
    arr = [2122, 4210, 6571, 3376, 4929, 7587, 2504, 3574, 3446, 944, 4932, 9007, 4305, 9753, 3213, 3318, 1563, 2193, 5903, 6464, 7476, 5293, 3146, 2398, 1968, 6529, 1277, 9746, 5808, 5645, 1443, 4174, 147, 4048, 7887, 7306, 3580, 1415, 7981, 3861, 72, 8557, 7498, 91, 650, 3569, 1751, 6918, 824, 2921, 6718, 4366, 6459, 102, 8835, 427, 4295, 7265, 7467, 4336, 1435, 3157, 58, 6250, 7190, 9564, 2454, 1114, 9794, 7699, 9302, 2704, 723, 534, 5353, 9191, 9985, 934, 5562, 6265, 8201, 3108, 4297, 2437, 2258, 778, 669, 3234, 8584, 7157, 2099, 4690, 8863, 3468, 8608, 6355, 5517, 2103, 4802, 5355, 5038, 1425, 7908, 1965, 6941, 8845, 460, 5826, 4282, 8301, 5202, 4432, 5611, 1501, 506, 8729, 6773, 6719, 6406, 2009, 7517, 1074, 9154, 1145, 9176, 6955, 4103, 4847, 2906, 1617, 7761, 866, 4681, 2207, 5929, 2412, 614, 708, 387, 3137, 1530, 5200, 804, 8197, 1670, 2231, 7243, 877, 8268, 4326, 908, 1598, 3757, 6072, 4810, 3923, 8259, 9850, 5989, 2656, 9943, 7976, 3495, 9669, 4498, 9001, 6417, 2256, 4065, 4382, 6378, 9814, 7952, 8294, 5313, 3762, 2171, 5403, 5207, 7632, 8704, 94, 2218, 9645, 8987, 8911, 2292, 7304, 2637, 5972, 3529, 9887, 75, 6216, 5838, 2718, 8768, 8322, 9169, 9620, 1080, 4631, 4952, 260, 7717, 1797, 1199, 1275, 7236, 988, 3833, 7970, 190, 7829, 8066, 8701, 1192, 1046, 8250, 9574, 4591, 6669, 8938, 6591, 9025, 9667, 4958, 3052, 2233, 6988, 7059, 7696, 3364, 3291, 2286, 2109, 5283, 4970, 7914, 7923, 4226, 3487, 9860, 1487, 6944, 4308, 7321, 854, 990, 3635, 187, 8417, 9, 4938, 5287, 2542, 9708, 7019, 32, 2595, 5044, 2841, 1741, 8307, 9437, 1872, 4565, 9798, 2651, 3818, 3425, 1970, 9204, 5865, 9744, 9285, 9033, 6141, 6405, 5199, 749, 4005, 7370, 9763, 4789, 5091, 544, 5925, 3749, 95, 7099, 5931, 8387, 215, 3097, 5494, 3851, 1233, 5007, 2783, 150, 8020, 8598, 2947, 994, 4695, 1096, 6460, 34, 5584, 9617, 9835, 9163, 4415, 6363, 5785, 2709, 9485, 5980, 4787, 1614, 761, 8615, 9672, 7670, 4144, 2733, 5841, 2694, 40, 2698, 9693, 4161, 3516, 2018, 2004, 6219, 692, 2615, 5322, 9840, 9450, 7136, 2514, 7929, 8038, 891, 9225, 459, 2212, 7674, 1349, 3001, 1183, 2425, 6409, 2414, 2354, 7329, 8780, 5644, 2719, 9223, 8619, 9138, 5744, 4409, 9592, 8804, 8389, 3552, 7534, 1560, 3785, 1361, 8847, 8638, 9956, 4640, 9723, 1783, 5970, 2731, 1926, 7697, 1912, 6847, 1377, 1153, 2621, 4718, 3278, 2249, 9599, 1025, 5921, 4146, 7584, 1891, 1290, 6867, 9580, 1638, 1457, 6621, 2440, 5279, 5943, 1180, 8193, 2204, 3726, 9306, 6768, 9830, 1057, 7177, 4860, 4801, 1, 9793, 498, 5302, 8774, 391, 4189, 6535, 3441, 9401, 7620, 4645, 3641, 1052, 5615, 4275, 2634, 4520, 6102, 7283, 8628, 8650, 9438, 8261, 7653, 1209, 8055, 1673, 5455, 9930, 4519, 5371, 5763, 4783, 6366, 3585, 7226, 5331, 5152, 8255, 6303, 6840, 9081, 3090, 8994, 4706, 8079, 4312, 8080, 6457, 1227, 9209, 6884, 5180, 785, 4273, 8196, 5082, 319, 5764, 3218, 9687, 9738, 2995, 3662, 1805, 3784, 4852, 748, 6627, 7418, 8881, 1806, 3306, 8935, 4957, 7503, 2375, 4703, 1613, 3624, 2382, 5244, 797, 6196, 1866, 3589, 9297, 2456, 6030, 2474, 2970, 1126, 7118, 1929, 6203, 880, 6407, 4478, 1832, 7328, 5503, 1615, 9295, 3530, 6643, 5885, 7070, 348, 8091, 6276, 3210, 3416, 4994, 966, 8180, 8362, 6933, 481, 762, 5427, 5818, 2852, 8873, 8694, 4030, 6418, 7866, 8970, 2238, 2944, 3961, 5140, 7856, 3519, 868, 3694, 6588, 406, 538, 5411, 9731, 29, 1546, 9424, 4112, 8416, 443, 3551, 2320, 7279, 7434, 3431, 9686, 1407, 9670, 8072, 3605, 2587, 7215, 881, 8501, 6618, 3215, 4818, 1324, 5920, 2689, 7472, 4906, 6812, 9077, 4708, 6249, 6609, 5400, 2241, 503, 4021, 1967, 5368, 982, 9997, 8256, 5397, 7380, 5667, 164, 4430, 7033, 2162, 7854, 587, 2496, 9178, 6856, 3764, 5437, 3804, 8880, 5543, 5848, 6520, 8613, 8618, 9616, 5389, 3688, 7361, 3082, 3607, 554, 3962, 6846, 1885, 8398, 2519, 3483, 9782, 786, 6766, 9371, 6160, 1599, 5942, 6681, 5392, 5402, 6680, 3573, 9066, 4534, 3695, 4232, 4176, 355, 7176, 8564, 8140, 6698, 5917, 3266, 1974, 1911, 9771, 6839, 3948, 2670, 6111, 4947, 3868, 3435, 8309, 3442, 1981, 4165, 4611, 1202, 3050, 7138, 6201, 683, 4034, 1225, 7057, 9511, 245, 9441, 6394, 7428, 6712, 3367, 3781, 8506, 7271, 9024, 6548, 3722, 6908, 656, 600, 3982, 2405, 2094, 1759, 6415, 6044, 7892, 7919, 4269, 7124, 2364, 8813, 2543, 2693, 2862, 9941, 2674, 2524, 3382, 247, 2035, 5065, 1724, 1737, 3602, 5157, 9208, 4661, 6781, 2080, 4086, 9029, 6759, 2577, 4160, 4907, 2835, 7827, 8547, 6822, 9107, 8128, 276, 3890, 2720, 8451, 2314, 252, 3351, 9601, 1490, 4905, 262, 8665, 1384, 2119, 6978, 6794, 6475, 2517, 3162, 7935, 5521, 1902, 2189, 925, 7246, 5616, 77, 452, 7174, 1637, 5805, 731, 7402, 5383, 3707, 4227, 5610, 3410, 5428, 8709, 5822, 5308, 7818, 8834, 8156, 5078, 3622, 2993, 8757, 7552, 940, 1790, 7112, 5304, 1081, 3267, 9213, 2570, 9607, 4531, 3040, 7205, 4025, 7106, 4471, 9951, 1076, 2071, 975, 2743, 1829, 8236, 6434, 4225, 6351, 9823, 2589, 492, 8848, 9395, 1850, 8851, 5442, 5864, 4883, 978, 8078, 2399, 7216, 9984, 3568, 2424, 4546, 6632, 1574, 526, 1558, 2232, 2374, 6268, 830, 4514, 4246, 640, 7707, 5432, 8011, 6021, 629, 2421, 1479, 8214, 7085, 5553, 720, 1532, 103, 5043, 7089, 9454, 9608, 6774, 9362, 5539, 8238, 1852, 2737, 6002, 2344, 3742, 9037, 411, 4517, 46, 8093, 6357, 4060, 8374, 5034, 1102, 1881, 9545, 1620, 2574, 1750, 6842, 3449, 1720, 1851, 1554, 8753, 4941, 495, 4895, 8248, 2410, 7204, 5209, 7496, 179, 4513, 7030, 431, 4717, 9175, 4338, 7675, 9396, 1932, 7454, 6326, 384, 8917, 4395, 5571, 57, 9730, 6308, 1518, 7200, 2818, 7005, 5976, 8666, 6174, 6218, 8803, 5816, 6678, 2825, 4000, 6956, 9356, 7974, 9085, 9766, 5905, 5264, 2248, 7597, 7577, 3307, 5280, 5020, 1167, 3241, 4501, 9276, 9260, 1198, 455, 2341, 3734, 4182, 9935, 4672, 19, 2507, 9010, 4637, 9994, 9192, 5100, 2872, 8315, 9103, 1084, 3838, 3443, 2525, 5035, 892, 7485, 870, 5240, 6943, 4641, 9489, 7038, 7088, 7501, 3642, 5759, 1043, 3801, 4398, 1294, 2342, 1619, 3512, 5751, 7624, 5430, 7158, 570, 7562, 3882, 1365]
    arr1=[None]*len(arr)
    arr2=[None]*len(arr)
    for i in range(0, len(arr)):    
        arr1[i] = arr[i]
        arr2[i] = arr[i]  
    Quick(arr1,0,len(arr1)-1)
    insertionSort(arr2,0,len(arr2)-1)
    print("NUmber of swaps for 1000 input")
    print("for quickSort: "+str(counterQuick))
    print("for insertionSort: "+str(counterInsertion))
    
main()