#include "opencv2/opencv.hpp"
#include "iostream"
using namespace cv;
using namespace std;

int main()
{
	Mat image = imread("../elephant.jpg");
	if (image.empty()) {
		cout << "fail to read image" << endl;
		return 0;
	}
	int s_row = 150, e_row = 650;
	int rcol[8][2] = {
		{ 506,577 },
		{ 61,164 },
		{ 797,901 },
		{ 259,380 },
		{ 588,680 },
		{ 392,489 },
		{ 695,800 },
		{ 168,249 }
	};
	int col = 0;
	for (int i = 0; i < 8; i++) {
		col += rcol[i][1] - rcol[i][0];
	}

	Mat result = Mat(e_row - s_row + 10, col + 10, CV_8UC3);
	
	int col_offset = 0;
	for (int i = 0; i < 8; i++) {
		Mat roi = image(Range(s_row, e_row), Range(rcol[i][0], rcol[i][1]));
		cout << e_row - s_row << " " << col_offset << " " << rcol[i][1] - rcol[i][0] << endl;
		Mat dst = result(Range(0, e_row - s_row), Range(col_offset, col_offset + rcol[i][1] - rcol[i][0]));
		roi.copyTo(dst);
		col_offset += rcol[i][1] - rcol[i][0];
	}

	imshow("result", result);
	waitKey();

	return 0;
}