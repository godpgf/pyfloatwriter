//
// Created by EDY on 2022/12/21.
//

#include <iostream>
using namespace std;
#include "libwriter_api.h"

extern "C"
{

DLLEXPORT void writeFloat(const float* feature, int elementSize, char* path){
    cout<<path<<endl;
    FILE*  fp1 = fopen(path, "wb");
    fwrite(feature, sizeof(float ), elementSize, fp1);
    fclose(fp1);
}

DLLEXPORT void writeInt(const int* feature, int elementSize, char* path){
    cout<<path<<endl;
    FILE*  fp1 = fopen(path, "wb");
    fwrite(feature, sizeof(int ), elementSize, fp1);
    fclose(fp1);
}

}