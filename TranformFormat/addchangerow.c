#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(int argc,char *argv[])
{
    int i=0;
    for(i=1;i<argc;i++)
    {
    FILE *fp1=fopen(argv[i],"r");
    char temp[1024]={0};
    strcpy(temp,"win");
    strcat(temp,argv[i]);
    FILE *fp2=fopen(temp,"w+");
    char buf[4096];
    while(1)
    {
        memset(buf,0,sizeof(buf));
        if(fgets(buf,sizeof(buf),fp1)==NULL&&feof(fp1)==1)
        {
            break;   
        }

        //            int i=0;
        //          for(i=0;i<strlen(buf);i++)
        //        {
        //          printf("%d ",buf[i]);
        //    }
        //  getchar();
        buf[strlen(buf)]='\r';
        buf[strlen(buf)]='\n';//必须以/r/n作为每以行的结尾；
        fwrite(buf,1,strlen(buf),fp2);
        //            int i=0;
        //for(i=0;i<strlen(buf);i++)
        // {
        //   printf("%d ",buf[i]);
        //}

    }
    fclose(fp1);
    fclose(fp2);
    }
    return 0;
}
