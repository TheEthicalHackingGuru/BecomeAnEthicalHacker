#include <unistd.h>

int main()
{
   setuid(0);
   execl(“/bin/sh”,”/bin/bash”, NULL);
   return 0;
}
