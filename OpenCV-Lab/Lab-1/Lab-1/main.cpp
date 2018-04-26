#include <iostream>  
#include <opencv2/core/core.hpp>  
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace cv;
using namespace std;
int main()
{
	Mat img = imread("../tree.jpg");
	Mat img2 = img.clone();

	if (img.empty())
	{
		cout << "未能正确读取图片" << endl;
		system("pause");
		return -1;
	}
	imshow("input", img);

	int x_offset = -410;
	int y_offset = +100;

	for (int i = 520; i < 810; i++) {
		for (int j = 180; j < 505; j++) {
			if (img.at<Vec3b>(Point(i, j))[0] < 180) {
				for (int k = 0; k < 3; k++) {
						img.at<Vec3b>(Point(i + x_offset, j + y_offset))[k] = img.at<Vec3b>(Point(i, j))[k];
				}
			}
		}
	}
	imshow("result", img);
	waitKey();
	return 0;
}