#include <math.h>

#ifdef _WIN32
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT
#endif

DLL_EXPORT double calcular_media(double* array, int tamanho){
    double soma = 0.0;
    for(int i = 0; i < tamanho; i++){
        soma += array[i];
    }
    return soma / tamanho; 
}

DLL_EXPORT double calcular_total(double* array, int tamanho){
    double total = 0.0; 
    for(int i = 0; i < tamanho; i++){
        total += array[i];
    }
    return total; 
}

// 3. Encontra o maior valor
DLL_EXPORT double maior_venda(double* array, int tamanho){
    double maior = array[0];
    for(int i = 0; i < tamanho; i++){
        if(array[i] > maior){
            maior = array[i];
        }
    }
    return maior;
}

DLL_EXPORT double menor_venda(double* array, int tamanho){
    double menor = array[0];
    for(int i = 0; i < tamanho; i++){
        if(array[i] < menor){
            menor = array[i];
        }
    }
    return menor;
}    

DLL_EXPORT double variancia(double* array, int tamanho){
    double media = calcular_media(array, tamanho);
    double soma_dos_quadrados = 0.0;

    for(int i = 0; i < tamanho; i++){
        soma_dos_quadrados += pow(array[i] - media, 2);
    }
    return soma_dos_quadrados / tamanho;
}


DLL_EXPORT double desvio_padrao(double* array, int tamanho){
    double var = variancia(array, tamanho);
    return sqrt(var);
}

DLL_EXPORT int vendas_premium(double* array, int tamanho, double valor_minimo){ 
    int cont = 0; 
    for(int i = 0; i < tamanho; i++){
        if(array[i] >= valor_minimo){
            cont++; 
        }
    }
    return cont;
}