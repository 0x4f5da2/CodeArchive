#include<Windows.h>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<time.h>
#include<omp.h>
#define MATSIZE 1500
#define MODVAL 1007
int A[MATSIZE][MATSIZE];
int B[MATSIZE][MATSIZE];
int C[MATSIZE][MATSIZE];
void init() {
	memset(C, 0, sizeof(C));
	srand((unsigned)time(NULL));
	for (int i = 0; i < MATSIZE; i++) {
		for (int j = 0; j < MATSIZE; j++) {
			//随机生成矩阵数据
			A[i][j] = rand() % MODVAL;
			B[i][j] = rand() % MODVAL;
		}
	}
}
int main() {
	//在并行的for循环中，输出线程号
#pragma omp parallel for num_threads(6)
	for (int i = 0; i < 12; i++)
	{
		printf("OpenMP Test, 线程编号为: %d\n", omp_get_thread_num());
	}

	double s, e;
	LARGE_INTEGER op, ed;
	init();
	int i, j, k;
	int n = MATSIZE;
	int sum, r;
	init();
    

	//使用传统方法计算矩阵相乘
	QueryPerformanceCounter(&op);//使用WIndowsAPI计算运行时间
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			sum = 0;
			for (k = 0; k < n; k++) {
				sum += A[i][k] * B[k][j];
			}
			C[i][j] += sum;
		}
	}
	QueryPerformanceCounter(&ed);
	std::cout << ed.QuadPart - op.QuadPart << std::endl;
	
	//使用OpenMP来计算矩阵相乘
	memset(C, 0, sizeof(C));
	QueryPerformanceCounter(&op);
#pragma omp parallel for 
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			sum = 0;
			for (k = 0; k < n; k++) {
				sum += A[i][k] * B[k][j];
			}
			C[i][j] += sum;
		}
	}
	QueryPerformanceCounter(&ed);
	std::cout << ed.QuadPart - op.QuadPart << std::endl;

	system("pause");
	return 0;
}