#include "stdio.h"
#include "string.h"
int main(int argc, char const *argv[])
{
	char buf[100];
	memset(buf,0,100);
	sprintf(buf,"hello %f %d %s",96.5,24,"lizhen");
	printf("%s\n",buf);
	return 0;
}