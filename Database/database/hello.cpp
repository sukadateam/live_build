#include <iostream>
using namespace std;
//Translate inputs into an opposite value
extern "C" int not_gateInt(int input) {
    if ( input == 1 ) {
        return 0;
    }
    else if ( input == 0 ) {
        return 1;
    }
    else {
        return 2;
    }
}
//Method Failed as python uses True instead of true.
extern "C" bool not_gateBool(bool input) {
    if ( input == false ) {
        return true;
    }
    else if ( input == false) {
        return false;
    }
    else {
        return false;
    }
}
//Compile as a shared library: ----
//g++ -c -o library.o hello.cpp
//g++ -shared -o libfoo.so library.o