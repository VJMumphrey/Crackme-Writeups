#include <iostream>

/* luna(unsigned long long) */

bool luna(unsigned long long param_1)

{
  unsigned long addv;
  int state;
  int ret;
  unsigned long long i;
  
  ret = 0;

  // this reduces it down to a number between [0,10]
  // only 10 returns true or 1
  for (i = param_1; i != 0; i = i / 100) {
    addv = (i / 10) / 10;
    state = ((int)(i / 10) + ((int)(addv << 2) + (int)addv) * -2) * 2;
    if (9 < state) {
      state = state + -9;
    }
    ret = ret + (int)i + ((int)(i / 10 << 2) + (int)(i / 10)) * -2 + state;
  }

  // the param needs to be a multiple of 10
  std::cout << ret << std::endl;
  return ret % 10 == 0;
}

int main (int argc, char** argv) {

    unsigned long long param;
    bool ret;

    // the value has to be <= 999999
    // this is a good starting point
    param = 999999;

    while (ret != true) {
        ret = luna(param);

        if (ret == true) {
            std::cout << param << "\n";
            break;
        }
        param++;
    }

    return 0;
}
