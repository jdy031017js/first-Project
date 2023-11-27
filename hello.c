#include <stdio.h>


int main()
{
  char a[100]="";
  char b[100]="";
  
  printf("문자열을 입력하시오 : ");
  gets_s(a,sizeof a);
  
  int k =0;
  for(int i=0; a[i]!=0; i++)
    {
  if('A'>=a[i]&&a[i]>='z')
      { a[i]=b[k];
      k++;
      } 
    }

  b[k+1]='\0';
  printf("%s",b);
  
  
  return 0;
} 
