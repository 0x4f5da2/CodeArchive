/*
*
* This file is part of the open-source SeetaFace engine, which includes three modules:
* SeetaFace Detection, SeetaFace Alignment, and SeetaFace Identification.
*
* This file is part of the SeetaFace Identification module, containing codes implementing the
* face identification method described in the following paper:
*
*
*   VIPLFaceNet: An Open Source Deep Face Recognition SDK,
*   Xin Liu, Meina Kan, Wanglong Wu, Shiguang Shan, Xilin Chen.
*   In Frontiers of Computer Science.
*
*
* Copyright (C) 2016, Visual Information Processing and Learning (VIPL) group,
* Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.
*
* The codes are mainly developed by Jie Zhang(a Ph.D supervised by Prof. Shiguang Shan)
*
* As an open-source face recognition engine: you can redistribute SeetaFace source codes
* and/or modify it under the terms of the BSD 2-Clause License.
*
* You should have received a copy of the BSD 2-Clause License along with the software.
* If not, see < https://opensource.org/licenses/BSD-2-Clause>.
*
* Contact Info: you can send an email to SeetaFace@vipl.ict.ac.cn for any problems.
*
* Note: the above information must be kept whenever or wherever the codes are used.
*
*/

#include<iostream>
using namespace std;

#ifdef _WIN32
#pragma once
#include <opencv2/core/version.hpp>

#define CV_VERSION_ID CVAUX_STR(CV_MAJOR_VERSION) CVAUX_STR(CV_MINOR_VERSION) \
  CVAUX_STR(CV_SUBMINOR_VERSION)

#ifdef _DEBUG
#define cvLIB(name) "opencv_" name CV_VERSION_ID "d"
#else
#define cvLIB(name) "opencv_" name CV_VERSION_ID
#endif //_DEBUG

#pragma comment( lib, cvLIB("core") )
#pragma comment( lib, cvLIB("imgproc") )
#pragma comment( lib, cvLIB("highgui") )

#endif //_WIN32

#if defined(__unix__) || defined(__APPLE__)

#ifndef fopen_s

#define fopen_s(pFile,filename,mode) ((*(pFile))=fopen((filename),(mode)))==NULL

#endif //fopen_s

#endif //__unix

#include <opencv/cv.h>
#include <opencv/highgui.h>
#include "face_identification.h"
#include "recognizer.h"
#include "face_detection.h"
#include "face_alignment.h"

#include "math_functions.h"

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstdlib>

using namespace seeta;

#define TEST(major, minor) major##_##minor##_Tester()
#define EXPECT_NE(a, b) if ((a) == (b)) std::cout << "ERROR: "
#define EXPECT_EQ(a, b) if ((a) != (b)) std::cout << "ERROR: "

std::string DATA_DIR = "D:/VSPROJ/Detection/";
std::string MODEL_DIR = "D:/SeetaFaceEngine-master/FaceIdentification/model/";



int main(int argc, char* argv[]) {
	// Initialize face detection model
	seeta::FaceDetection detector("D:/SeetaFaceEngine-master/FaceDetection/model/seeta_fd_frontal_v1.0.bin");
	detector.SetMinFaceSize(40);
	detector.SetScoreThresh(2.f);
	detector.SetImagePyramidScaleFactor(0.8f);
	detector.SetWindowStep(4, 4);

	// Initialize face alignment model 
	seeta::FaceAlignment point_detector("D:/SeetaFaceEngine-master/FaceAlignment/model/seeta_fa_v1.1.bin");

	// Initialize face Identification model 
	FaceIdentification face_recognizer((MODEL_DIR + "seeta_fr_v1.0.bin").c_str());
	std::string test_dir = DATA_DIR;

	std::ifstream ifs;
	ifs.open(test_dir + "datalist.txt", std::ifstream::in);
	std::string img_name;
	std::string best_file;
	std::vector<string> filename_str;
	std::vector<bool> if_face_detected;
	std::vector<float*> img_vec;
	while (ifs >> img_name) {  //预先处理，加块运算
		filename_str.push_back(img_name);
		cv::Mat img_color = cv::imread(test_dir + "data/" + img_name, CV_LOAD_IMAGE_COLOR);
		cv::Mat img_gray;
		cv::cvtColor(img_color, img_gray, CV_BGR2GRAY);
		
		ImageData img_data_color(img_color.cols, img_color.rows, img_color.channels());
		img_data_color.data = img_color.data;

		ImageData img_data_gray(img_gray.cols, img_gray.rows, img_gray.channels());
		img_data_gray.data = img_gray.data;

		std::vector<seeta::FaceInfo> face_info = detector.Detect(img_data_gray);
		int32_t face_num = static_cast<int32_t>(face_info.size());
		if (face_num == 0) {
			if_face_detected.push_back(false);
			std::cout << "face not found in" << img_name << std::endl;
			img_vec.push_back(NULL);
			continue;
		}
		else {
			if_face_detected.push_back(true);
		}
		seeta:FacialLandmark facial_landmark[5];
		point_detector.PointDetectLandmarks(img_data_gray, face_info[0], facial_landmark);
		float* face_vec = new float[2048];
		face_recognizer.ExtractFeatureWithCrop(img_data_color, facial_landmark, face_vec);
		std::cout << img_name << " done" << std::endl;

		img_vec.push_back(face_vec);

	}

	std::cout << "data loaded" << endl;
	std::ofstream ofs;
	ofs.open("./outdata.txt");
	for (int i = 0; i < img_vec.size(); i++) {  //计算相似值
		for (int j = i + 1; j < img_vec.size(); j++) {
			if (if_face_detected[i] && if_face_detected[j]) {
				float simi = face_recognizer.CalcSimilarity(img_vec[i], img_vec[j]);
				ofs << i << " " << j << " " << simi << " " << filename_str[i] << " " << filename_str[j] << std::endl;
			}
			else {
				ofs << i << " " << j << " " << 0 << " " << filename_str[i] << " " << filename_str[j] << std::endl;
			}
		}
		std::cout << "done " << i << std::endl;
	}
	system("pause");
	return 0;
}






//#include <opencv2/highgui/highgui.hpp>  
//
//#include <opencv2/imgproc/imgproc.hpp>  
//
//#include <opencv2/core/core.hpp>  
//
//using namespace cv;
//
//
//
//int main()
//
//{
//
//	VideoCapture cap(0);
//
//	Mat frame;
//
//	while (1)
//
//	{
//
//		cap >> frame;
//
//		imshow("µ÷ÓÃÉãÏñÍ·", frame);
//
//		waitKey(30);
//
//	}
//
//	return 0;
//
//}
