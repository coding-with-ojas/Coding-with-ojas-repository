#include <iostream>
#include <cmath>

int main() {
    // Declarations
    double base;
    double perpendicular;
    double hypotenuse;
    // Input
    std::cout << "What is the base of the triangle: ";
    std::cin >> base;
    std::cout << "What is the perpendicular of the triangle: ";
    std::cin >> perpendicular;
    // Calculation
    hypotenuse = sqrt(
                      pow(base, 2) 
                      + 
                      pow(perpendicular, 2)
                     );
    // Output
    std::cout << "The hypotenuse of the triangle is " << hypotenuse;

    return 0;
}