#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE* file = fopen("tmp.txt","w");
	char* model[3] = {"sir","sirs","sis"};
	char* upmodel[3] = {"SIR","SIRS","SIS"};
	for(int i=0; i<3; i++)
	{
		for(int j=1; j<=10; j++)
		{
			fprintf(file,"\\begin{figure}\n\\includegraphics[scale=0.8]{%sp07r1i%ds3}\n\\caption[%s p=0.7,r=1,i=%d,init infected=3]{%s Model with p=0.7 r=1 i=%d initial infected=3 simulation using Snap.py}\n\\end{figure}\n",model[i],j,upmodel[i],j,upmodel[i],j);
		}
		fprintf(file,"\\begin{figure}\n\\includegraphics[scale=0.8]{%sp07r1i%ds3}\n\\caption[%s p=0.7,r=1,i=%d,init infected=3]{%s Model with p=0.7 r=1 i=%d initial infected=3 simulation using Snap.py}\n\\end{figure}\n",model[i],20,upmodel[i],20,upmodel[i],20);
	}
	fclose(file);
	return 0;
}
