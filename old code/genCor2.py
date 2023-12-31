import numpy as np
import matplotlib.pyplot as plt

def grabdata(crv_file): #when calling files, make sure to specify r'filepath'
    with open(crv_file, 'r') as fid1:
        header = [next(fid1) for _ in range(8)]
        ptsline = header[5]
        pts = int(ptsline.split('=')[1])
        data_lines = list(fid1)
        # data_lines.remove('endcurve')

    out = [tuple(map(float, line.split())) for line in data_lines]
    out = np.array(out, dtype='float')
    x = out[:,0]
    y = out[:,1]
    return x,y




# def grabdata(crv_file): #when calling files, make sure to specify r'filepath'
#     fid1 = open(crv_file, 'r')
#     # header = [next(fid1) for _ in range(8)]
#     # ptsline = header[5]
#     # pts = int(ptsline.split('=')[1])
#     data_lines = list(fid1)
#     # data_lines.remove('endcurve\n')

#     out = [tuple(map(float, line.split(","))) for line in data_lines]
#     out = np.array(out, dtype='float')
#     x = out[:,0]
#     y = out[:,1]
#     return x,y

[x, y] = grabdata("Hybrid III/NBDLHeadLag.crv")
[a, b] = grabdata
# [ex, ey] = grabdata("corridors/NBDLHeadLagCorridor.crv")

plt.plot(x, y)
plt.show()

# roundVal = 0.01
# x = [getRoundedThreshold(v, roundVal) for v in x]
# ex = [getRoundedThreshold(v, roundVal) for v in ex]


# if corridorType == "tension":
#     ip = [0, 100, 200, 300]
#     xaxis = "Displacement (mm)"
#     yaxis = "Force (N)"
#     title = "Tension"
        

# elif corridorType == "compression":
#     ip = [0, 100, 200, 300]
#     xaxis = "Displacement (mm)"
#     yaxis = "Force (N)"
#     title = "Compression"


# xPartition = [0] * len(ip)
# yPartition = [0] * len(ip)

# for i in range(len(ip)-1):
#     xPartition[i]=(x[ip[i]:ip[i+1]])
#     yPartition[i]=(y[ip[i]:ip[i+1]])
#     plt.plot(xPartition[i], yPartition[i])

# # Cutting the ex data

# maxX = max(x)
# nex = []
# ney = []

# for i in range(len(ex)):
#     if ex[i] > maxX:
#         break
#     nex.append(ex[i])
#     ney.append(ey[i])

# # How many points of e is within corridor

# totalPoints = len(nex)
# count = 0

# for i in range(len(nex)):
#     # What is the index of this value in x?
#     value = nex[i]
#     myIndexLow = list(xPartition[1]).index(value)
#     myIndexHigh = list(yPartition[0]).index(value)

#     if (yPartition[1][myIndexLow] <= value <= yPartition[0][myIndexHigh]):
#         count += 1


# print(count)
# print(totalPoints)
# print(float(count)/totalPoints)


# plt.plot(nex, ney)
# plt.show()

