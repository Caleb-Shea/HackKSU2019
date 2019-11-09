#include <boost/python.hpp>

class mapClass
{
private:
  int grid[64][64];
  //
  bool isBlocked[64][64], isOpen[64][64];

public:
  // Gen Mapping
  int genMap(int param1[64][64], int param2, int count1, int count2)
  {

    //checks if bool has been set for certain settings
    if ()
    {
      isBlocked[count1][count2] = true;
    }
    else if (param3 && !param2)
    {
      isOpen[count1][count2] = true;
    }
    else
    {
      isBlocked[count1][count2] = false;
      isOpen[count1][count2] = false;
    }
    if ((isBlocked[count1][count2] == isOpen[count1][count2]) && isBlocked[count1][count2])
    {
      isBlocked[count1][count2] = false;
    }

    if (isBlocked[count1][count2])
    {
      return 1;
    }
    else if (isOpen[count1][count2])
    {
      return 2;
    }
    else
    {
      return 0;
    }

  }
};

class obstacleClass
{
private:

public:

};
