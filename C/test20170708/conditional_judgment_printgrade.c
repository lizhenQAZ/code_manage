#include "stdio.h"
void max(int A,int B)
{
	printf("%d\n", A>B?A:B);
}

void test1(int score)
{
	if (score>=90)
		printf("excellent\n");
	else if (score>=80)
		printf("general\n");
	else if (score>=60)
		printf("suitable\n");
	else
		printf("unsuitable\n");
}

void test2(int score)
{
	switch (score/10)
	{
		case 10:
		case 9:
			printf("excellent\n");
			break;
		case 8:
		     printf("general\n");
		      break;
		case 7:
		case 6:
		     printf("suitable\n");
		     break;
		case 5:
		case 4:
		case 3:
		case 2:
		case 1:
		case 0:
		     printf("unsuitable\n"); 
		     break;    
	}
}

int main(int argc, char const *argv[])
{
	max(55,78);
	test1(78);
	test2(55);
	return 0;
}