#include <assert.h>
#include <stdlib.h>

#define ARRAYSIZE(a) (sizeof(a)/sizeof(a[0]))

static void move_last(int* values, const int num_values, const int idx);
static void swap(int* a, int* b);

int main(int argc, const char* argv[])
{
    int values[] = {2, 3, 5, 7, 11, 13, 17, 19};
    move_last(values, ARRAYSIZE(values), 2);

    assert(values[0] == 2);
    assert(values[1] == 3);
    assert(values[2] == 7);
    assert(values[3] == 11);
    assert(values[4] == 13);
    assert(values[5] == 17);
    assert(values[6] == 19);
    assert(values[7] == 5);

    return EXIT_SUCCESS;
}

void move_last(int* values, const int num_values, const int idx)
{
    assert(idx < num_values);

    for (int i = idx; i < (num_values - 1); i++)
    {
        swap(&values[i], &values[i + 1]);
    }
}

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
