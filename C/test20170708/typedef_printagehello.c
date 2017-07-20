#include "stdio.h"
typedef struct
{
	int age;
}People;

void sayhello()
{
	printf("hello c!\n");
}

typedef void (*Func)();

int main(int argc, char const *argv[])
{
	People p;
	p.age=10;
	printf("%d\n",p.age);
	Func f = sayhello;
	f();
	return 0;
}
