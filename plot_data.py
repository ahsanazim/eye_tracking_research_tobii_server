import matplotlib.pyplot as plt

if __name__ == "__main__":
    # will plot these
    X = []
    Y = []

    # read data from file 
    sample_num = 2
    data_file = "./data_sample_{}.txt".format(sample_num)
    with open(data_file, "r") as fh: 
        for line in fh: 
            arr = line.split(" ")
            if arr[0] == "*":
                X.append(float(arr[1]))
                Y.append(float(arr[1]))

    # transform data
    Y = list(X)                 # y-axis will actually have X-coords
    X = list(range(len(X)))     # x-axis will have a proxy for time

    # plot
    plt.plot(X,Y)
    plt.xlabel('fixation num')
    plt.ylabel('x coordinate')
    plt.title('x-coord vs fixation num while reading sample #{}'.format(sample_num))
    plt.show()


"""
see
- https://www.digitalocean.com/community/tutorials/how-to-plot-data-in-python-3-using-matplotlib
- https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
"""