import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


def isSamePerson(a, b):
    return ((int)(a / 7)) == ((int)(b / 7))


if __name__ == "__main__":
    data = []
    with open("./outdata.txt") as f:
        for line in f.readlines():
            ele = line.split()[0:3]
            ele = map(lambda x: eval(x), ele)
            data.append(list(ele))
    diff = []
    same = []
    for each in data:
        if isSamePerson(each[0], each[1]):
            same.append(each[2])
        else:
            diff.append(each[2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    bi = 18
    ax.hist(same, bins=bi, normed=True, alpha=0.8, label="Same person")
    ax.hist(diff, bins=bi, normed=True, alpha=0.8, label="Different person")
    ax.set_ylabel('Probability density')
    ax.set_xlabel('Similarity(The higher the more similar)')
    ax.set_title('Histogram of Similarity')
    plt.legend()
    plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(same, bins=bi, normed=True, alpha=0.8, label="Same person")
    ax.hist(diff, bins=bi, normed=True, alpha=0.8, label="Different person")
    ax.set_ylabel('Probability density')
    ax.set_xlabel('Similarity(The higher the more similar)')
    ax.set_title('Histogram of Similarity')
    x1 = np.linspace(min(diff), max(diff), 1000)
    normal = mlab.normpdf(x1, np.mean(diff), np.std(diff))
    line1, = plt.plot(x1, normal, 'r-', linewidth=2)
    kde = mlab.GaussianKDE(diff)
    x2 = np.linspace(min(diff), max(diff), 1000)
    line2, = plt.plot(x2, kde(x2), 'g-', linewidth=2)
    plt.legend([line1, line2], ['normal', 'gussiankde'], )
    x3 = np.linspace(min(same), max(same), 1000)
    normal = mlab.normpdf(x3, np.mean(same), np.std(same))
    line3, = plt.plot(x3, normal, 'r-', linewidth=2)
    kde = mlab.GaussianKDE(same)
    x4 = np.linspace(min(same), max(same), 1000)
    line4, = plt.plot(x4, kde(x4), 'g-', linewidth=2)
    plt.legend([line1, line2], ['normal', 'gussiankde'], loc="best")
    plt.show()

    dataAll = same + diff
    dataLabel = [1 for _ in same] + [0 for _ in diff]
    dataAll = np.mat([dataAll, dataLabel])
    dataAll = dataAll.transpose()
    dataAll = np.ndarray.tolist(dataAll)
    dataAll = sorted(dataAll, key=lambda p: p[0])
    ran = [each[0] for each in dataAll]
    ran.append(-1)
    rocX = []
    rocY = []
    sameNum = len(same)
    diffNum = len(diff)
    sameCnt = 0
    diffCnt = 0
    for each in dataAll:
        if each[1] > 0.5:
            sameCnt += 1
        else:
            diffCnt += 1
        rocX.append((diffNum - diffCnt) / diffNum)
        rocY.append((sameNum - sameCnt) / sameNum)
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    for i in range(len(rocX) - 1):
        ax2.plot([rocX[i], rocX[i + 1]], [rocY[i], rocY[i + 1]], c='r')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve of SeetaFace Face Verification")
    plt.show()
