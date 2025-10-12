#include<iostream>
using namespace std;

void Maior_MenorNum(float num[]){
    float maior = 0;
    float menor = 0;
    maior = menor = num[1];

    for(int i = 0; i < 3; i++){
        if (num[i] > maior) maior = num[i];
        else menor = num[i];
    }
    cout << "Maior: "<< maior << endl;
    cout << "Mneor: "<< menor;
}

int main(){
    float num[3];
    cout << "De 3 numeros:\n";
    for(int i = 0; i < 3; i ++){
        cin >> num[i];
    }

    Maior_MenorNum(num);

    return 0;
}