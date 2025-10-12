#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    const int tam = 10;
    int numeros[tam];

    cout << "De dez numeros:";
    for (int i = 0; i < tam; i ++){
        cin >> numeros[i];
        cout << "\n";
    }

    sort(numeros, numeros + tam);
    cout << "Numeros em orde crescente: ";
    for (int i = 0; i < tam; i ++){
        cout << numeros[i]<< ";";
    }

    cout <<"\n\n";

    sort(numeros, numeros+tam, greater<int>());
    cout << "Numeros em orde decrescente: ";
    for (int i = 0; i < tam; i ++){
        cout << numeros[i]<< ";";
    }

}
