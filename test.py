import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    file_path = "/Users/AhsanAzim/.talon/talon.log"
    logfile = open(file_path,"r")
    loglines = follow(logfile)
    for line in loglines:
        splitted_line = line.split(" ")
        # print(splitted_line)
        if (len(splitted_line) >= 8) and (splitted_line[7] == "1"):          # filter log properly
            x, y = splitted_line[8], splitted_line[9]
            y = y.strip("\n")                                   # get rid of newline
            x, y = float(x) * 1000, float(y) * 1000         # convert
            print(x, y)
        # print(line)