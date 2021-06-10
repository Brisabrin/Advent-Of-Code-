#include <stdio.h>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

int l = 26;

vector<vector<int>> v;
int ind = 0;

int n = 8;
int m = 8;
// int z = 1;

int main()
{

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            char cc;
            cin >> cc;
            // cin >> arr[i + (l / 2)][j + (l / 2)][(l / 2)];
            if (cc == '#')
            {
                v[ind].push_back(i + (l / 2));
                v[ind].push_back(j + (l / 2));
                v[ind].push_back(l / 2);
                v[ind].push_back(l / 2);
            }
        }
    }

    int co = 0;

    for (int k = 0; k < 6; k++)
    {
        for (int x = 0; x < l; x++)
        {

            for (int y = 0; y < l; y++)
            {

                for (int z = 0; z < l; z++)
                {

                    for (int w = 0; w < l; w++)
                    {

                        for (int i = 0; i < v.size(); i++)
                        {

                            int cx = v[i][0];
                            int cy = v[i][1];
                            int cz = v[i][2];
                            int cw = v[i][3];

                            if ((abs(cx - x) <= 6) and (abs(cy - y) <= 6) and (abs(cz - z) <= 6) and (abs(cw - w) <= 6))
                                co += 1;
                        }
                    }
                }
            }
        }

        cout << co;
    }
}