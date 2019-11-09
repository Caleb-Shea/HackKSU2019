#include <string>
#include <iostream>

// Map generation
class mapClass
{
public:
  int x[5], y[5];
  // Pass grid and border values as pointers to not remove their values
  float grid[x[0]][y[0]], border[x[1]][y[1]];
  bool isExisting[x[2][x[2], isBlocked[x[3]][y[3]];
  int mapClass();
  int mapGen();
};

// Base for obstacles
class obstacleClass
{
public:
  int count;
  string type;
  int hitbox[64][64], center[64][64];;
};

// The tree obstacle
class treeClass: public obstacleClass
{
public:
  int *setHitbox(int hitbox[][], int count, int centerX, int centerY);
};


int *hitboxarr(int arr[][])
{

}
