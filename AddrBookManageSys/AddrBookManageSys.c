#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define LEN sizeof(struct addritem)
#define FORMAT "%-10s%-10s%-15s%-25s%-30s%\n"
#define DATA addrinfo[i].name,addrinfo[i].occu,addrinfo[i].tel,addrinfo[i].email,addrinfo[i].address

struct addritem				/*¶¨ÒåÍ¨Ñ¶Â¼½á¹¹Ìå*/
{ 
  char name[10];			/*ÐÕÃû*/
  char occu[10];     			/*Ö°Òµ*/
  char tel[15];  			/*ÊÖ»úºÅ*/
  char email[25];			/*µç×ÓÓÊ¼þ*/
  char address[30];			/*Í¨Ñ¶µØÖ·*/
};

struct addritem addrinfo[100];	/*¶¨Òå½á¹¹ÌåÊý×é*/
void input();					/*Â¼ÈëÍ¨Ñ¶Â¼ÌõÄ¿*/
void search();					/*°´Ãû×Ö²éÕÒÍ¨Ñ¶Â¼ÌõÄ¿*/
void update();					/*ÐÞ¸ÄÍ¨Ñ¶Â¼ÌõÄ¿*/
void del();						/*É¾³ýÍ¨Ñ¶Â¼ÌõÄ¿*/
void display();					/*ÏÔÊ¾Í¨Ñ¶Â¼ÐÅÏ¢*/
void sort();					/*°´Ãû×ÖÅÅÐò*/
void menu();					/*Ö÷²Ëµ¥*/

int main()						/*Ö÷º¯Êý*/
{ int n;
  menu();
  scanf("%d",&n);				/*ÊäÈëÑ¡Ôñ¹¦ÄÜµÄ±àºÅ*/
  while(n)
  { 
	  switch(n)
	  { 
		case 1: input();  break;	
	   case 2: search(); break;
		case 3: update(); break;
		case 4: del();	  break;
		case 5: sort();   break;
		case 6: display();break;
		default:break;
     }
    menu();						/*Ö´ÐÐÍê¹¦ÄÜºóÔÙ´ÎÏÔÊ¾²Ëµ¥½çÃæ*/
    scanf("%d",&n);
  }
  return 0;
}

/*Â¼ÈëÍ¨Ñ¶Â¼ÌõÄ¿*/
void input()					
{ int i,count=0;				/*countÊÇ¼ÇÂ¼µÄÌõÊý*/
  char ch[2];  
  FILE *fp;						/*¶¨ÒåÎÄ¼þÖ¸Õë*/
  if((fp=fopen("data.txt","a+"))==NULL)		/*´ò¿ªÖ¸¶¨ÎÄ¼þ*/
  { 
	  printf("can not open\n");
	  return;
  }
  while(!feof(fp))
  {
	  if(fread(&addrinfo[count],LEN,1,fp)==1)
		  count++;				/*Í³¼Æµ±Ç°¼ÇÂ¼ÌõÊý*/
  }
  fclose(fp);
  if(count==0)
	  printf("No contact record!\n");
  else
  {
     display();			/*µ÷ÓÃdisplayº¯Êý£¬ÏÔÊ¾Ô­ÓÐÐÅÏ¢*/
  }

  if((fp=fopen("data.txt","wb"))==NULL)
  {
	  printf("can not open address list!\n");
	  return;
  }
  for(i=0;i<count;i++)
  {
	  fwrite(&addrinfo[i] ,LEN,1,fp);			/*ÏòÖ¸¶¨µÄ´ÅÅÌÎÄ¼þÐ´ÈëÐÅÏ¢*/
  }

  printf("please input(y/n):");
  scanf("%s",ch);
  while(strcmp(ch,"Y")==0||strcmp(ch,"y")==0)/*ÅÐ¶ÏÊÇ·ñÒªÂ¼ÈëÐÂÐÅÏ¢*/
  {
    printf("name:");
	 scanf("%s",&addrinfo[count].name);		 /*ÊäÈëÐÕÃû*/
    for(i=0;i<count;i++)
	    if(strcmp(addrinfo[i].name,addrinfo[count].name)==0)
	    {
			printf("The name already exists,press any key to continue!");
			fclose(fp);
			return;
	    }
    printf("occupation:");
    scanf("%s",&addrinfo[count].occu);		/*ÊäÈëÁªÏµÈËÖ°Òµ*/
    printf("telephone:");
	 scanf("%s",&addrinfo[count].tel);		/*ÊäÈëÁªÏµÈËÊÖ»úºÅ*/
	 printf("email:");
	 scanf("%s",&addrinfo[count].email);	/*ÊäÈëÁªÏµÈËµç×ÓÓÊ¼þ*/
    printf("address:");
	 scanf("%s",&addrinfo[count].address);	/*ÊäÈëÁªÏµÈËµØÖ·*/
   
    if(fwrite(&addrinfo[count],LEN,1,fp)!=1)/*½«ÐÂÂ¼ÈëµÄÁªÏµÈËÐÅÏ¢Ð´ÈëÖ¸¶¨µÄ´ÅÅÌÎÄ¼þ*/
     {
		 printf("Can not save the record!");
	 }
     else
	 {
		 printf("%s saved!\n",addrinfo[count].name);
		 count++;
	 }
     printf("continue?(y/n):");				/*Ñ¯ÎÊÊÇ·ñ¼ÌÐøÊäÈë*/
     scanf("%s",ch);
  }
  fclose(fp);
  printf("OK!\n");
}

/*ÏÔÊ¾ÁªÏµÈËÐÅÏ¢*/
void display()
 { FILE *fp;
   int i,count=0;
   fp=fopen("data.txt","rb");
   while(!feof(fp))
   {
   if(fread(&addrinfo[count] ,LEN,1,fp)==1) 
      count++;
   }  
   fclose(fp);
   printf("name    occupation  telephone      email                      address\t\n");
   for(i=0;i<count;i++)
   { 
	   printf(FORMAT,DATA);					/*½«ÐÅÏ¢°´Ö¸¶¨¸ñÊ½´òÓ¡*/
   }
}
 
void menu()									/*×Ô¶¨Òåº¯ÊýÊµÏÖ²Ëµ¥¹¦ÄÜ*/
{
  printf("\n\n\n\n\n");
  printf("\t\t|---------------------CONTACT-------------------|\n");
  printf("\t\t|\t 0. exit                                |\n");
  printf("\t\t|\t 1. input record                        |\n");
  printf("\t\t|\t 2. search record                       |\n");
  printf("\t\t|\t 3. update record                       |\n");
  printf("\t\t|\t 4. delete record                       |\n");
  printf("\t\t|\t 5. sort                                |\n");
  printf("\t\t|\t 6. display                             |\n");
  printf("\t\t|-----------------------------------------------|\n\n");
  printf("\t\t\tchoose(0-6):");
}

/*×Ô¶¨ÒåÅÅÐòº¯Êý °´ÐÕÃûÊ××ÖÄ¸ÅÅÐò*/
void sort()						
{ FILE *fp;
  struct addritem t;
  int i=0,j=0,count=0;l
  if((fp=fopen("data.txt","r+"))==NULL)
  { 
	   printf("can not open!\n");
      return;
  }
  while(!feof(fp)) 
  if(fread(&addrinfo[count] ,LEN,1,fp)==1) 
	  count++;
  fclose(fp);
  if(count==0) 
  {
	  printf("no record!\n");
	  return;
  }
  for(i=0;i<count-1;i++)
      for(j=i+1;j<count;j++)		/*Ë«ÖØÑ­»·ÊµÏÖÐÕÃû±È½Ï²¢½»»»*/
	  if(strcmp(addrinfo[i].name,addrinfo[j].name)>0)
        { 
			  t=addrinfo[i];
			  addrinfo[i]=addrinfo[j];
			  addrinfo[j]=t;
		  }
	  if((fp=fopen("data.txt","wb"))==NULL)
       { printf("can not open\n");return;}
  for(i=0;i<count;i++)				/*½«ÖØÐÂÅÅºÃÐòµÄÄÚÈÝÖØÐÂÐ´ÈëÖ¸¶¨µÄ´ÅÅÌÎÄ¼þÖÐ*/
      if(fwrite(&addrinfo[i] ,LEN,1,fp)!=1)
      { 
        printf("%s can not save!\n"); 
      }
  fclose(fp);
  printf("save successfully\n");
}

/*×Ô¶¨ÒåÉ¾³ýº¯Êý*/
void del()
{
	FILE *fp;
	int i,j,count=0;
	char ch[2];
	char name[15];
	if((fp=fopen("data.txt","r+"))==NULL)
	{
		printf("can not open\n");return;}
		while( !feof(fp) )  
			if(fread(&addrinfo[count],LEN,1,fp)==1) count++;
			fclose(fp);
		if(count==0) 
		{
			printf("no record!\n");
			return;
		}
  		display();
		printf("please input the name:");
		scanf("%s",&name);
		for(i=0;i<count;i++)
		{
			if(strcmp(name,addrinfo[i].name)==0)
			{
				printf("find the contact,del?(y/n)");
				scanf("%s",ch);
				if(strcmp(ch,"Y")==0||strcmp(ch,"y")==0)/*ÅÐ¶ÏÊÇ·ñÒª½øÐÐÉ¾³ý*/
				for(j=i;j<count;j++)
				addrinfo[j]=addrinfo[j+1];/*½«ºóÒ»¸ö¼ÇÂ¼ÒÆµ½Ç°Ò»¸ö¼ÇÂ¼µÄÎ»ÖÃ*/
				count--;/*¼ÇÂ¼µÄ×Ü¸öÊý¼õ1*/
				if((fp=fopen("data.txt","wb"))==NULL)
				{ printf("can not open\n");return;}
				for(j=0;j<count;j++)/*½«¸ü¸ÄºóµÄ¼ÇÂ¼ÖØÐÂÐ´ÈëÖ¸¶¨µÄ´ÅÅÌÎÄ¼þÖÐ*/
				if(fwrite(&addrinfo[j] ,LEN,1,fp)!=1)
				{ 
           printf("can not save!\n");
           }
				fclose(fp);
				printf("del successfully!\n");
				return;
			}
		}
		printf("Ã»ÓÐÕÒµ½ÒªÉ¾³ýµÄÁªÏµÈË£¡\n");
}

/*×Ô¶¨Òå²éÕÒº¯Êý*/
void search()
{ FILE *fp;
  int i,count=0;
  char ch[2],name[15];
  if((fp=fopen("data.txt","rb"))==NULL)
     { 
      printf("can not open\n");
	   return;
     }
  while(!feof(fp))  
  if(fread(&addrinfo[count],LEN,1,fp)==1) 
     count++;
  fclose(fp);
  if(count==0) {
      printf("no record!\n");return;
      }
	   printf("please input the name:");
		scanf("%s",name);
		for(i=0;i<count;i++)
			if(strcmp(name,addrinfo[i].name)==0)
     { 
      printf("find the contact,display?(y/n)");
		 scanf("%s",ch);
      if(strcmp(ch,"Y")==0||strcmp(ch,"y")==0) 
      {
	      printf("name    occupation  telephone      email                      address\t\n");
         printf(FORMAT,DATA);/*½«²éÕÒ³öµÄ½á¹û°´Ö¸¶¨¸ñÊ½Êä³ö*/
	   } 
	      break;
     }   
  if(i==count) 
    printf("can not find the contact!\n");/*Î´ÕÒµ½Òª²éÕÒµÄÐÅÏ¢*/
}


/*×Ô¶¨ÒåÐÞ¸Äº¯Êý*/
void update()
{ 
  FILE *fp;
  int i,j,count=0;
  char name[30];
  if((fp=fopen("data.txt","r+"))==NULL)
     { 
      printf("can not open\n");
      return;
     }
  while(!feof(fp))  
     if(fread(&addrinfo[count],LEN,1,fp)==1) 
        count++;
  if(count==0) 
  {
	printf("no record!\n");
	fclose(fp);
	return;
  }
  display();
  printf("please input the name of the contact which you want to update!\n");
  printf("update name:");
  scanf("%s",&name);
  for(i=0;i<count;i++)
  {
	if(strcmp(name,addrinfo[i].name)==0)
	{
	  printf("find the contact!you can update!\n");
	  printf("name:");
	  scanf("%s",addrinfo[i].name);/*ÊäÈëÃû×Ö*/
     printf("occuption:");
	  scanf("%s",&addrinfo[i].occu);/*ÊäÈëÖ°Òµ*/
     printf("telephone:");
	  scanf("%s",&addrinfo[i].tel);/*ÊäÈëµç»°ºÅÂë*/
     printf("email:");
	  scanf("%s",&addrinfo[i].email);/*ÊäÈëµç×ÓÓÊÏä*/
	  printf("address:");
	  scanf("%s",&addrinfo[i].address);
	  printf("update successful!");
	  if((fp=fopen("data.txt","wb"))==NULL)
     { printf("can not open\n");return;}
	  for(j=0;j<count;j++)/*½«ÐÂÐÞ¸ÄµÄÐÅÏ¢Ð´ÈëÖ¸¶¨µÄ´ÅÅÌÎÄ¼þÖÐ*/
	  if(fwrite(&addrinfo[j] ,LEN,1,fp)!=1)
       { printf("can not save!");}
	fclose(fp);
	return;
	}	 
  }
	printf("Ã»ÓÐÕÒµ½Æ¥ÅäÐÅÏ¢£¡\n");
 }