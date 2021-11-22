#include<stdio.h>
#include<stdlib.h>

int main(){
    char algarismos[10] = {'0','1','2','3','4','5','6','7','8','9'};
    int contados[10] = {0,0,0,0,0,0,0,0,0,0};
    
    //int tamanho = sizeof(contados)/sizeof(contados[0]);
    
    int intervalo[2], i,j,k;
    
    for(i=0;i<2;i++){
    	scanf("%d",&intervalo[i]);
	}

    while(intervalo[0] != 0 && intervalo[1] != 0){

		for(i=intervalo[0];i<=intervalo[1];i++){
			char numero[50];
			sprintf(numero, "%d", i);
			int tam = 0;
			while(numero[tam] != '\0'){
				tam++;
			}
			for(k = 0; k<tam;k++){
				for (j = 0; j < 10; j++){
					if(numero[k] == algarismos[j]){
						contados[j] += 1;
						break;
					}
				}	
			}
		}
		
		for(i = 0; i<10; i++){
			if(i != 9){
				printf("%d ",contados[i]);	
			}else{
				printf("%d\n",contados[i]);
			}
			contados[i] = 0;
		}
		
		for(i=0;i<2;i++){
    		scanf("%d",&intervalo[i]);
		}
	}
}
