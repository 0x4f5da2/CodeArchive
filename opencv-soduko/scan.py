from transform import four_point_transform
import cv2
import sys


def main(path):
    image = cv2.imread(path)
    ratio = image.shape[0] / 1000.0
    orig = image.copy()
    image = cv2.resize(image, (int(image.shape[1] / ratio), 1000), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("processing", image)
    cv2.waitKey(500)

    # 将图片转换为灰阶图片并进行高斯模糊，然后使用Canny算子查找边缘
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edged = cv2.Canny(gray, 75, 200)

    cv2.imshow("processing", edged)
    cv2.waitKey(500)

    # 寻找最大的五个边界
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts[1], key=cv2.contourArea, reverse=True)[:5]

    screenCnt = None
    # 遍历边界，
    for c in cnts:
        # 轮廓近似
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # 如果轮廓有4条边，则认为是我们要找的
        if len(approx) == 4:
            screenCnt = approx
            break
    if screenCnt is None:
        print("没有找到目标")
        sys.exit(-1)
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("processing", image)
    cv2.waitKey(500)

    # 将图片拉直并二值化
    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    warped = cv2.threshold(warped, 0, 255, cv2.THRESH_OTSU)[1]

    # 展示最终效果
    result = cv2.resize(warped, (650, 650), interpolation=cv2.INTER_AREA)
    cv2.imshow("processing", result)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    # 存储图片供后续步骤使用
    name = "images/scanned_" + path.split("/")[-1]
    cv2.imwrite(name, result)
    return (name, result)


if __name__ == "__main__":
    main("666_original.png")
