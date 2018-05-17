import cv2
import numpy as np
import tensorflow as tf

import scan
from sudo import Sudo
from mnist import model

# 神经网络初始化
x = tf.placeholder("float", [None, 784])
sess = tf.Session()

# 载入训练数据
with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder("float")
    y2, variables = model.convolutional(x, keep_prob)
saver = tf.train.Saver(variables)
saver.restore(sess, "mnist/data/convolutional.ckpt")


# 判断手写数字
def convolutional(input):
    return sess.run(y2, feed_dict={x: input, keep_prob: 1.0}).flatten().tolist()


def main(path, pre):
    img = cv2.imread(path)
    gray = pre
    # 阈值分割
    ret, thresh = cv2.threshold(gray, 200, 255, 1)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    dilated = cv2.dilate(thresh, kernel)

    # 轮廓提取
    image, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 提取八十一个小方格
    boxes = []
    for i in range(len(hierarchy[0])):
        if hierarchy[0][i][3] == 0:
            boxes.append(hierarchy[0][i])

    height, width = img.shape[:2]
    box_h = height / 9
    box_w = width / 9
    number_boxes = []
    # 数独初始化为零阵
    soduko = np.zeros((9, 9), np.int32)

    for j in range(len(boxes)):
        if boxes[j][2] != -1:
            x, y, w, h = cv2.boundingRect(contours[boxes[j][2]])
            if (w < box_w / 3 and h < box_h / 3) or w > 56 or h > 56:
                continue
            number_boxes.append([x, y, w, h])
            # 对提取的数字进行处理
            number_roi = gray[y:y + h, x:x + w]

            # 统一大小
            num = np.zeros((56, 56), dtype=np.uint8)
            num.fill(255)
            num[(56 - h + 1) // 2:(56 + h + 1) // 2, (56 - w + 1) // 2:(56 + w + 1) // 2] = number_roi
            image = np.zeros((1, 784)).astype(np.float32)

            temp = 0
            for i in range(0, 56, 2):
                for k in range(0, 56, 2):
                    total = int(num[i][k]) + int(num[i][k + 1]) + int(num[i + 1][k + 1]) + int(num[i + 1][k])
                    image[0][temp] = (255 - total / 4) / 255.0
                    temp += 1

            result = convolutional(image)
            number = int(result.index(max(result)))

            # 识别结果展示
            cv2.putText(img, str(number), (x + w + 1, y + h - 20), 3, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow("result", img)
            name = "images/recongized_" + path.split("_")[-1]
            cv2.imwrite(name, img)
            cv2.waitKey(30)

            # 求在矩阵中的位置
            soduko[int(y / box_h)][int(x / box_w)] = number

    print("\n生成的数独\n")
    print(soduko)
    print("\n求解后的数独\n")

    # 数独求解
    app = Sudo(soduko)
    try:
        soduko = app.calc()
    except Exception as e:
        raise Exception("数独无解")

    print(soduko)
    print("\n验算：求每行每列的和\n")
    row_sum = map(sum, soduko)
    col_sum = map(sum, zip(*soduko))
    print(list(row_sum))
    print(list(col_sum))

    # 把结果按照位置填入图片中
    for i in range(9):
        for j in range(9):
            x = int((i + 0.25) * box_w)
            y = int((j + 0.5) * box_h)
            cv2.putText(img, str(soduko[j][i]), (x, y), 3, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("result", img)
    name = "images/result_" + path.split("_")[-1]
    cv2.imwrite(name, img)
    cv2.waitKey(5000)


if __name__ == "__main__":
    temp = 'images/3.jpg'
    path, pre = scan.main(temp)
    try:
        main(path, pre)
    except Exception as e:
        print(e)
