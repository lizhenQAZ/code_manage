#include"stdio.h"
int main(int argc,char* argv[]) {
	long benefit = 0;
	long bonus = 0;
	printf("please enter the value of benefit:");
	scanf("%ld",&benefit);
	if (100000>=benefit){
		bonus = benefit*0.1;
	}
	else if (100000 < benefit && 200000 >= benefit) {
		bonus = 100000 * 0.1 + (benefit - 100000)*0.075;
	}
	else if (200000 < benefit && 400000 >= benefit) {
		bonus = 100000 * 0.1 + (200000 - 100000)*0.075 + (benefit - 200000)*0.05;
	}
	else if (400000 < benefit && 600000 >= benefit){
		bonus = 100000 * 0.1 + (200000 - 100000)*0.075 + (400000 - 200000)*0.05 + (benefit - 400000)*0.03;
	}
	else if (600000 < benefit && 1000000 >= benefit){
		bonus = 100000 * 0.1 + (200000 - 100000)*0.075 + (400000 - 200000)*0.05 + (600000 - 400000)*0.03 + (benefit - 600000)*0.015;
	}
	else{
		bonus = 100000 * 0.1 + (200000 - 100000)*0.075 + (400000 - 200000)*0.05 + (600000 - 400000)*0.03 + (1000000 - 600000)*0.015 + (benefit - 1000000)*0.01;
	}
	printf("final bonus is %ld.",bonus);
}