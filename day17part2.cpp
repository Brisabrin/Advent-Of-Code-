#include <stdio.h>
#include <map>
#include <vector>
#include <iostream>
using namespace std;
int l = 26;
vector<vector<int>> v(100);
int ind = -1;

int n = 8;
int m = 8;
// int z = 1;
int account = 0;

int main()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            // cout<<"hello"<<endl ;
            char cc;
            cin >> cc;
            // cin >> arr[i + (l / 2)][j + (l / 2)][(l / 2)];
            if (cc == '#')
            {
                account += 1;
                // cout<< i <<" "<<j <<endl ;
                ind += 1;
                v[ind].push_back(i + (l / 2));
                v[ind].push_back(j + (l / 2));
                v[ind].push_back(l / 2);
                v[ind].push_back(l / 2);
            }
        }
    }

    cout << "hel";

    long long co = 0;

    for (int x = 0; x < l; x++)
    {
        for (int y = 0; y < l; y++)
        {
            for (int z = 0; z < l; z++)
            {
                for (int w = 0; w < l; w++)
                {
                    bool track = true;

                    for (int i = 0; i < account && track; i++)
                    {
                        int cx = v[i][0];
                        int cy = v[i][1];
                        int cz = v[i][2];
                        int cw = v[i][3];

                        if ((abs(cx - x) <= 6) and (abs(cy - y) <= 6) and (abs(cz - z) <= 6) and (abs(cw - w) <= 6))
                        {
                            cout << "gherub4" << endl;
                            co += 1;
                            track = false;
                        }
                    }
                }
            }
        }

        cout << co;
    }
}