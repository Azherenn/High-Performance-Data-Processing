#include <stdlib.h>

double processor(double *arr, size_t size){
    double sum = 0;
    for (size_t i = 0; i < size; i++){
        sum = sum + arr[i];
    }
    double media = sum/size;
    return media;
}