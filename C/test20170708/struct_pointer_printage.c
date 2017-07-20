#include "stdio.h"
#include "stdlib.h"

struct People
{
	int age;
};

int main(int argc, const char *argv[])
{
	/* code */
	struct People *p;
	p=(People *)malloc(sizeof(struct People));
	p->age=10;
	printf("%d\n",p->age);

	struct People * p1=p;
	p->age=15;
	printf("%d\n",p1->age);
	free(p);

	return 0;
}