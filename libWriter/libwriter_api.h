//
// Created by EDY on 2022/12/21.
//

#ifndef LIBWRITER_LIBWRITER_API_H
#define LIBWRITER_LIBWRITER_API_H


#ifndef WIN32 // or something like that...
#define DLLEXPORT
#else
#define DLLEXPORT __declspec(dllexport)
#endif

extern "C"
{
DLLEXPORT void writeFloat(const float* feature, int elementSize, char* path);
DLLEXPORT void writeInt(const int* feature, int elementSize, char* path);
}

#endif //LIBWRITER_LIBWRITER_API_H
