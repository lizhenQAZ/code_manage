#include "stdio.h"

struct People
{
	int age;
	const char *name;	
};

int main(int argc, char const *argv[])
{
	struct People p;
	p.age=25;
	p.name="xiaoli";
	printf("age=%d\n",p.age);

	struct People p1=p;
	p.age=30;
	printf("age=%d\n",p1.age);

	return 0;
}