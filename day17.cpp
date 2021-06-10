#include <stdio.h>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

int l = 26;

char arr[50][50][50];
char cop[50][50][50];

// vector<vector<int>> v;
int ind = 0;
bool check_bool(int x, int y, int z)
{

    return (x >= 0 and x < l) and (y >= 0 and y < l) and (z >= 0 and z < l);
};

void copy_content()
{

    for (int x = 0; x < l; x++)
    {

        for (int y = 0; y < l; y++)
        {
            for (int z = 0; z < l; z++)
            {

                arr[x][y][z] = cop[x][y][z];
                // cout << cop[x][y][z] << endl;
            }
        }
    }
};

int n = 8;
int m = 8;
// int z = 1;

int cy[] = {};
int cz[] = {};

int main()
{

    for (int x = 0; x < l; x++)
    {

        for (int y = 0; y < l; y++)
        {
            for (int z = 0; z < l; z++)
            {

                arr[x][y][z] = '.';
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            char cc;
            // cin >> cc;
            cin >> arr[i + (l / 2)][j + (l / 2)][(l / 2)];
            // if (cc == '#')
            // {
            //     v[ind].push_back(i + (l / 2));
            //     v[ind].push_back(j + (l / 2));
            //     v[ind].push_back(l / 2);
            //     v[ind].push_back(l / 2);
            // }
        }
    }

    for (int k = 0; k < 6; k++)
    {
        for (int x = 0; x < l; x++)
        {

            for (int y = 0; y < l; y++)
            {

                for (int z = 0; z < l; z++)
                {
                    int active = 0;
                    int counts = 0;

                    for (int cx = -1; cx <= 1; cx++)
                    {
                        for (int cy = -1; cy <= 1; cy++)
                        {
                            for (int cz = -1; cz <= 1; cz++)
                            {

                                int nx = cx + x;
                                int ny = cy + y;
                                int nz = cz + z;

                                if (!(cx == 0 and cy == 0 and cz == 0))
                                    counts += 1;

                                if ((cx == 0 and cy == 0 and cz == 0) || !check_bool(nx, ny, nz))
                                    continue;

                                if (arr[nx][ny][nz] == '#')
                                    active += 1;
                            }
                        }
                    }

                    // cout << "counts" << counts << endl;

                    if (arr[x][y][z] == '#' and !(active == 2 or active == 3))
                    {
                        cop[x][y][z] = '.';
                        // cout << x << ' ' << y << ' ' << z << endl;
                    }

                    else if (arr[x][y][z] == '.' and active == 3)
                    {
                        cop[x][y][z] = '#';
                        // cout << x << ' ' << y << ' ' << z << endl;
                        // cout << x << " " << y << " " << z << endl;
                    }

                    else
                        cop[x][y][z] = arr[x][y][z];
                }
            }
        }

        copy_content();
    }

    int co = 0;

    for (int x = 0; x < l; x++)
    {

        for (int y = 0; y < l; y++)
        {
            for (int z = 0; z < l; z++)
            {

                if (arr[x][y][z] == '#')
                {
                    co += 1;

                    cout << x << ' ' << y << ' ' << z << endl;
                }
            }
        }
    }

    cout << endl
         << co;
}