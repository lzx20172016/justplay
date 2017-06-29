#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//本程序用于将目录中的.c、.cpp、.h文件每行的末尾都添上\r\n字符,
//从而可以在windows上用txt文件打开阅读
//命令:./a.out *.c;./a.out *.h;./a.out *.cpp;./a.out a.c

int transformwin(char *tempbuf)
{

    
    FILE *fp1=fopen(tempbuf,"r");
    char temp[1024]={0};
    strcpy(temp,"win");
    strcat(temp,tempbuf);
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
    return 0;
}

int main(int argc,char *argv[])
{

    int i=0;

    for(i=1;i<argc;i++)
    {
        if((strcmp(argv[i],"*.c")==0)||(strcmp(argv[i],"*.cpp"))||(strcmp(argv[i],"*.h"))||(strcmp(argv[i],"*.hpp")))
        {
            char buf[1024];
            memset(buf,0, sizeof(buf));

            char cmd[1024];
            memset(cmd,0,sizeof(cmd));
            strcpy(cmd,"ls ");
            strcat(cmd,argv[i]);
            FILE* fp = popen(cmd, "r");
            //int ret = fread(buf, 1, sizeof(buf), fp);
            // buf[ret-1] = 0;
            while(1)
            {
                memset(buf,0,sizeof(buf));
                if((fgets(buf,sizeof(buf),fp)==NULL)&&(feof(fp)==1))
                    break;
                 printf("buf=%s",buf);
                 buf[strlen(buf)-1]=0;
                transformwin(buf);
            }
            fclose(fp);
        }
        else
        {
            transformwin(argv[i]);
        }
    }
    return 0;
}
