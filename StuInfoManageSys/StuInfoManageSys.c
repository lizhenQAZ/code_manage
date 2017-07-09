#include "stdio.h"
#include "stdlib.h"
#include "string.h"

/*
    the program is incomplete
*/
struct student{
	int num;
	char name[15];
	char sex[2];
	int age;
	double score[3];
	double sum;
	double ave;
};

typedef struct node
{
	struct student data;
	struct node *next;
}Node,*link;

int menuSel()
{
	int i;
	printf("\n\n\t  ********************************** \n");
	printf("\t|*      1.input record              *|\n");
	printf("\t|*      2.delete record             *|\n");
	printf("\t|*      3.list record               *|\n");
	printf("\t|*      4.search record             *|\n");
	printf("\t|*      5.save record               *|\n");
	printf("\t|*      6.load record               *|\n");
	printf("\t|*      7.quit                      *|\n");
	printf("\t  **********************************l \n");
      do
      {
	     printf("Enter Your Choice:");
		scanf("%d",&i);
      }while(i<0|i>7);
      return i;
}

void input(link l){
	int i;
	Node *p,*q;
	while(1){
		p=(Node*)malloc(sizeof(Node));
		if (!p){
			printf("memory malloc fail\n");
			return;
		}
		printf("input number:");
		scanf("%d",&p->data.num);
		if(p->data.num==0)
			break;
		for (q=l; q->next!=NULL; q=q->next)
		{
			if (q->data.num==p->data.num)
			{
				printf("the number has existed,please input again:");
				scanf("%d",&p->data.num);
			}
		}
		printf("iput name:");
		scanf("%s",p->data.name);
		printf("iput sex:");
		scanf("%s",p->data.sex);
		printf("iput age:");
		scanf("%s",p->data.age);
		printf("iput Chinese Math English score:");
		for (int i = 0; i < 4; i++)
		{
			scanf("%lf",&p->data.score[i]);
		}
		p->data.sum = p->data.score[0] +  p->data.score[1] + p->data.score[2];
		p->data.ave=p->data.sum/3;
		p->next = NULL;
		q->next = p;
		q = p;
	}
}

void del(link l){
	int num;
	Node *p,*q;
	q=l;
	p=q->next;
	printf("please input the student num you want to delete:");
	scanf("%d",&num);
	while(p){
		if (num == p->data.num){
			q->next = p ->next;
			free(p);
			printf("delete successfully!\n");
			break;
		}
		else{
			q = p;
			p = q->next;
		}
	}
	if(p == NULL)
		printf("can not find the student\n");
}

void display(Node *p){
	printf("STUDENT INFO\n");
	printf("number:%d\n",p->data.num );
	printf("name:%s\n",p->data.name);
	printf("sex:%s\n",p->data.sex);
	printf("age:%d\n",p->data.age);
	printf("Chinese:%lf\n",p->data.score[0]);
	printf("Math:%lf\n",p->data.score[1]);
	printf("English:%lf\n",p->data.score[2]);
	printf("Sum:%lf\n",p->data.sum);
	printf("average:%lf\n",p->data.ave);
}

void list(link l){
	Node *p;
	p=l->next;
	if (p == NULL){
		printf("no student record!");
	}
	while(p != NULL){
		display(p);
		p=p->next;
	}
}

int main(int argc, char const *argv[])
{
	link l;
	l=(Node*)malloc(sizeof(Node));
	if(!l){
		printf("\nallocate memory fail!");
		return 1;
	}
	l->next=NULL;
	while(1){
		system("cls");
		switch(menuSel()){
			case 1:
				input(l);
				break;
			case 2:
			     del(l);
			     break;
			case 3:
				list(l);
				break;
/*			case 4:
				search(l);
				break;
			case 5:
				save(l);
				break;
			case 6:
				load(l);
				break;
			case 7:
				exit(0);*/
		}
	}
	return 0;
}