#include <iostream>

int main()
{
    // INFO: Variables
    char op;
    double num1;
    double num2;
    double result;

    // INFO: Inputs
    std::cout << "What is the operator (+, -, *, /): ";
    std::cin >> op;

    std::cout << "What is number 1: ";
    std::cin >> num1;

    std::cout << "What is number 2: ";
    std::cin >> num2;

    // INFO: Calculation
    switch (op)
    {
    case '+':
        result = num1 + num2;
        break;
    case '-':
        result = num1 - num2;
        break;
    case '*':
        result = num1 * num2;
        break;
    case '/':
        result = num1 / num2;
        break;
    }

    // INFO: Output
    std::cout << num1 << ' ' << op << ' ' << num2 << " = " << result << "\n";
}
