#include<iostream>
using namespace std;

int main(){
    const int tam = 31;
    float temperatura[tam], menor_Zero=0, maior_Zero=0;

    cout << "De as temperaturas dos 31 dias do mes:\n";

    for(int i = 0; i < tam; i++){
        cout << "DIA "<<i<<":";
        cin >> temperatura[i];

        if(temperatura[i]<0) menor_Zero++;
        else if(temperatura[i]>0) maior_Zero++;
    }

    cout << "Temperaturas do mes:\n";
    for(int i = 0; i < tam; i++){
        cout << "DIA "<<i<<": "<<temperatura[i]<<endl;
    }

    cout << "quantidade de dias com temperatura < 0: "<<menor_Zero<<endl;
    cout << "quantidade de dias com temperatura > 0: "<<maior_Zero<<endl;

    return 0;
}