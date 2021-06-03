#include <unistd.h>

Int main()
{
   setuid(0);
   execl(“/bin/sh”,”/bin/bash”, NULL);
   Return 0;
}
