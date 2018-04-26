#include<iostream>
#include<cstdlib>
#include<cstdio>
#include"omp.h"

using namespace std;

int main()
{
#pragma omp parallel for num_threads(6)
    for (int i = 0; i < 12; i++)
    {
        printf("OpenMP Test, 线程编号为: %d\n", omp_get_thread_num());
    }
}