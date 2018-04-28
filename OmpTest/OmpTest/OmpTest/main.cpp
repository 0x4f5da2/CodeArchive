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
			//������ɾ�������
			A[i][j] = rand() % MODVAL;
			B[i][j] = rand() % MODVAL;
		}
	}
}
int main() {
	//�ڲ��е�forѭ���У�����̺߳�
#pragma omp parallel for num_threads(6)
	for (int i = 0; i < 12; i++)
	{
		printf("OpenMP Test, �̱߳��Ϊ: %d\n", omp_get_thread_num());
	}

	double s, e;
	LARGE_INTEGER op, ed;
	init();
	int i, j, k;
	int n = MATSIZE;
	int sum, r;
	init();
    

	//ʹ�ô�ͳ��������������
	QueryPerformanceCounter(&op);//ʹ��WIndowsAPI��������ʱ��
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
	
	//ʹ��OpenMP������������
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