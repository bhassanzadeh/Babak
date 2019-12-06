import numpy
import matplotlib.pylab as plt
import pandas as pd
import sys
from mpl_toolkits.mplot3d import Axes3D

# Number of data points
N = 100


def getRand():
    return numpy.random.uniform(-1, 1)


def getY(x1Val, m1, x2Val, m2, b):
    # Get position on our 45 degree straight line
    lineY = m1 * x1Val + m2 * x2Val + b

    std_dev = 0.2

    # Offset the generated data using a normal distribution to give it some noise
    y = numpy.random.normal(lineY, std_dev)

    return y


def plotData(currentData, delay):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(currentData["x1"], currentData["x2"], currentData["yp"], marker="o")
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('yp')
    plt.show()


def createData(m1, m2, b):
    # Initialize an empty dictionary to hold our data
    dataDict = {"x1": [], "x2": [], "yp": []}

    # Create N datapoints
    for i in range(N):
        x1 = getRand()
        x2 = getRand()
        y = getY(x1, m1, x2, m2, b)

        dataDict['x1'].append(x1)
        dataDict['x2'].append(x2)
        dataDict['yp'].append(y)

    data = pd.DataFrame(dataDict)
    return data


line_gradient1 = .5  # 45 degree line 1
line_gradient2 = .5  # 45 degree line 2
intercept = 0  # passing through the origin
input_data = createData(line_gradient1, line_gradient2, intercept)

print(input_data)

# Save generated data to a JSON file (CSV probably would have made better sense)
input_data.to_json("linear_data_2D.txt")

plotData(input_data, 1)