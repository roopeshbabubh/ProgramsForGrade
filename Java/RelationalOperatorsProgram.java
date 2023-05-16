package CodeInJava;

import java.util.Scanner;

public class RelationalOperatorsProgram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the First number: ");
        int num1 = sc.nextInt();
        System.out.println("Enter the Second number: ");
        int num2 = sc.nextInt();

        // Equal
        boolean equal = num1 == num2;
        System.out.println("Equal: " + equal);

        // Not Equal
        boolean notEqual = num1 != num2;
        System.out.println("Not Equal: " + notEqual);

        // Greater Than
        boolean greaterThan = num1 > num2;
        System.out.println("num1 is Greater Than num2: " + greaterThan);

        // Less Than
        boolean lesserThan = num1 < num2;
        System.out.println("num1 is Less Than num2: " + lesserThan);
    }
}
