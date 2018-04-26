#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <sys/times.h>
#include <omp.h>
#include "clock.h"



#define MATSIZE 1000
#define MODVAL 1007

int A[MATSIZE][MATSIZE];
int B[MATSIZE][MATSIZE];
int C[MATSIZE][MATSIZE];

static unsigned cyc_hi = 0;
static unsigned cyc_lo = 0;

void access_counter(unsigned *hi, unsigned *lo)
{
  /* Get cycle counter */
  asm("rdtsc; movl %%edx,%0; movl %%eax,%1" 
      : "=r" (*hi), "=r" (*lo)
      : /* No input */ 
      : "%edx", "%eax");
}

void start_counter()
{
  access_counter(&cyc_hi, &cyc_lo);
}

double get_counter()
{
  unsigned ncyc_hi, ncyc_lo;
  unsigned hi, lo, borrow;
  double result;
  /* Get cycle counter */
  access_counter(&ncyc_hi, &ncyc_lo);
  /* Do double precision subtraction */
  lo = ncyc_lo - cyc_lo;
  borrow = lo > ncyc_lo;
  hi = ncyc_hi - cyc_hi - borrow;
  result = (double) hi * (1 << 30) * 4 + lo;
  if (result < 0) {
    fprintf(stderr, "Error: Cycle counter returning negative value: %.0f\n", result);
  }
  return result;
}

void init(){
    memset(C, 0, sizeof(C));
    srand((unsigned)time(NULL));
    for(int i=0; i < MATSIZE; i++){
        for(int j=0; j < MATSIZE; j++){
            A[i][j] = rand() % MODVAL;
            B[i][j] = rand() % MODVAL;
        }
    }
}

int main(){
    double start, end;
    int i,j,k;
    int n = MATSIZE;
    int sum,r;
    init();

    start = get_counter();
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            sum = 0;
            for(k = 0; k < n; k++){
                sum += A[i][k] * B[k][j];
            }
            C[i][j] += sum;
        }
    }
    end = get_counter();
    printf("%lf\n", end - start);

    start = get_counter();
    for(i = 0; i < n; i++){
        #pragma  omp parallel for num_threads(4)
        for(j = 0; j < n; j++){
            sum = 0;
            for(k = 0; k < n; k++){
                sum += A[i][k] * B[k][j];
            }
            C[i][j] += sum;
        }
    }
    end = get_counter();
    printf("%lf\n", end - start);

    memset(C, 0, sizeof(C));
    start = get_counter();
    for(k = 0; k < n; k++){
        for(i = 0; i < n; i++){
            r = A[i][k];
            for(j = 0; j < n; j++){
                C[i][j] += r * B[k][j];
            }
        }
    }
    end = get_counter();
    printf("%lf\n", end - start);

    memset(C, 0, sizeof(C));
    start = get_counter();
    for(k = 0; k < n; k++){
        for(i = 0; i < n; i++){
            r = A[i][k];
            #pragma  omp parallel for num_threads(4)
            for(j = 0; j < n; j++){
                C[i][j] += r * B[k][j];
            }
        }
    }
    end = get_counter();
    printf("%lf\n", end - start);

    return 0;
}

