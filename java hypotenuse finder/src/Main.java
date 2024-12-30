import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        // Declaration
        Scanner scanner = new Scanner(System.in);
        double base;
        double perpendicular;
        double hypotenuse;
        // Input
        System.out.print("What is the base of the triangle: ");
        base = scanner.nextDouble();
        System.out.print("What is the perpendicular of the triangle: ");
        perpendicular = scanner.nextDouble();
        // Calculation
        hypotenuse = Math.sqrt(
                               Math.pow(base, 2)
                                       +
                               Math.pow(perpendicular, 2)
                              );
        //Output
        System.out.println("The hypotenuse of the triangle is " + hypotenuse);
        scanner.close();

    }
}
