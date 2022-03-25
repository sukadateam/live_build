#include <iostream>
extern "C" void MyFunction(std::string input) {
    std::cout << input << "Hello World!\n";
}
extern "C" int main() {
    MyFunction("Welcome to ");
}
extern "C" void InsertRow(std::string input) {
    std::cout << input;
}
//Compile as a shared library: ----
//g++ -c -o library.o hello.cpp
//g++ -shared -o libfoo.so library.o