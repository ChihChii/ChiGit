#include <iostream>
#include <cstdlib>
#include <string>
#include <iomanip>

using namespace std;

int main(void)
{
    string v[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    string line = {"********************************"};
    cout << line << endl;
    int len = sizeof(v) / sizeof(v[0]);

    for (int i = 0; i < len; i++)
    {
        cout << setw(4) << v[i];
    }
    cout << endl;
    for (int i = 1; i <= 31; i++)
    {
        cout << setw(4) << i;
        if (i % 7 == 0)
        {
            cout << endl;
        }
    }

    cout << endl
         << line << endl;

    return 0;
}