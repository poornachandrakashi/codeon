#include<stdio.h>
#include<cs50.h>
#include<string.h>
int  main(void){
    int i;
    string names[4]={"poorna","hari","anupama","poorna1"};
    string numbers[4]={"9945530541","8904700354","9481615571","656565555"};
    for(i=0;i<4;i++)
    {
        if(strcmp(names[i],"hari")==0)
        {
            printf("%s\n",numbers[i]);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;

}
