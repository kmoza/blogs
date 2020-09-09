/* cuda kernel device code - cuda sample code
*computes the vector addition of A and B into C. The three vectors have
*the same number of elements*/
__global__ void vectorAdd(float *A, float *B, float *C, int numElements)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < numElements)
    {
        C[i] = A[i] + B[i];
    }
}
