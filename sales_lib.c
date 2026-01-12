#include <math.h>

double calcular_media(double* array, int tamanho){

double soma = 0.0;

for(int i = 0; i < tamanho; i++){
    soma += array[i];

    }
    
    return soma / tamanho; 
}

double calcular_total(double* array, int tamanho){

double total = 0.0; 

for(int i = 0; i < tamanho; i++){
    total += array[i];

    }

    return total; 
}

double maior_venda(double* array, int tamanho){
    double maior = array[0];

    for(int i = 0; i < tamanho; i++){
        if(array[i] > maior){
            maior = array[i];
            //printf("Maior venda realizada: %f\n", maior);
            }
        }
        return maior;
    }

double menor_venda(double* array, int tamanho){
    double menor = array[0];

    for(int i = 0; i < tamanho; i++){
        if(array[i] < menor){
            menor = array[i];
            //printf("Menor venda realizada: %f\n", menor);
            }
        }
        return menor;
    }    

double variancia(double* array, int tamanho){

    double media = calcular_media(array, tamanho);
    double soma_dos_quadrados = 0.0;

    for(int i = 0; i < tamanho; i++){
        soma_dos_quadrados += pow(array[i] - media, 2);
    }

    return soma_dos_quadrados / tamanho;

}

double desvio_padrao(double* array, int tamanho){
    double var = variancia(array, tamanho);
    return sqrt(var);

}

int vendas_premium(double* array, int tamanho, double valor_minimo){ 
    int cont = 0; 

    for(int i = 0; i < tamanho; i++){
        if(array[i] >= valor_minimo){
            cont++; 
        }
    }
    
    return cont;

}