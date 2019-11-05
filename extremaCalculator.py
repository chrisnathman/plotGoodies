
def findAllExtrema(data):
    minIndexList = []
    maxIndexList = []

    i = 1
    length = len(data)
    while i < length - 1:
        if (data[i] < data [i - 1] and data[i] < data[i + 1]):
            minIndexList.append(i)

        elif (data[i] > data[i -1] and data[i] > data[i + 1]):
            maxIndexList.append(i)

        i+=1

    extremaIndexList = [minIndexList, maxIndexList]
    return extremaIndexList
