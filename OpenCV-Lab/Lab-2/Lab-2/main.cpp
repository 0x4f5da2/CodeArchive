#include <iostream>  
#include <vector>
#include <opencv2/core/core.hpp>  
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace std;
using namespace cv;

int main()
{
	Mat image = imread("../animals.jpg");
	Mat image_gray = imread("../animals.jpg", CV_LOAD_IMAGE_GRAYSCALE);
	if (image.empty())
	{
		cout << "error" << endl;
		system("pause");
		return -1;
	}

	Mat thresholded;
	threshold(image_gray, thresholded, 60, 255, THRESH_BINARY_INV);

	Mat result;
	Mat element5(5, 5, CV_8U, Scalar(1));
	morphologyEx(thresholded, result, MORPH_CLOSE, element5);

	vector<vector<Point>>contours;
	findContours(result, contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE);

	int cmin = 100;
	int cmax = 1000;
	vector<vector<Point>>::const_iterator itc = contours.begin();
	while (itc != contours.end()) {
		if (itc->size() < cmin || itc->size() > cmax)
			itc = contours.erase(itc);
		else
			++itc;
	}

	drawContours(image, contours, -1, Scalar(0, 255, 0), 2);

	itc = contours.begin();
	while (itc != contours.end()) {
		Moments mom = moments(Mat(*itc));
		circle(image, Point(mom.m10 / mom.m00, mom.m01 / mom.m00), 2, Scalar(0, 255, 255), 2);
		Rect rect = boundingRect(*itc);
		rectangle(image, rect, Scalar(0, 0, 255), 2);
		itc++;
	}

	imshow("result", image);
	waitKey(0);
	return 0;
}