// g++ ./hello.cpp -o hello
// ./hello
#include <iostream>
void MyFunction(std::string input) {
    std::cout << input << "Hello World!\n";
}
int main() {
    MyFunction("Welcome to ");
    return 0;
}
void InsertRow(std::string input) {
    std::cout << input;
}