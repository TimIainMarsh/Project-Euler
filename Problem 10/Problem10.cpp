#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(int a){
    for(int i = 2; i <= sqrt(double(a))+1; i++){
        if((a % i)==0) return false;
    }
    return true;
}

int main(){

    long long sum = 2; // NB using int looses precision and gives wrong answer
    for (int i= 3; i < 2000000; i+=2){
        if (is_prime(i)){
            // cout<<i<<endl;
            sum += i;
        }
    }
    cout<<sum<<endl;
}