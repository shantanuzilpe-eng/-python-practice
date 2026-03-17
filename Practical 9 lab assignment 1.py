import java.util.Scanner;

class Employee {
    String name;
    int age;
    double salary;
    String address;

    void getData(Scanner sc) {
        System.out.print("Enter Name: ");
        name = sc.nextLine();
        System.out.print("Enter Age: ");
        age = sc.nextInt();
        System.out.print("Enter Salary: ");
        salary = sc.nextDouble();
        sc.nextLine(); // buffer clear
        System.out.print("Enter Address: ");
        address = sc.nextLine();
    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Salary: " + salary);
        System.out.println("Address: " + address);
    }
}

class Manager extends Employee {
    void showManager() {
        System.out.println("---- Manager Details ----");
        display();
    }
}

public class Main1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Manager[] m = new Manager[10];

        for (int i = 0; i < 10; i++) {
            System.out.println("\nEnter details of Manager " + (i + 1));
            m[i] = new Manager();
            m[i].getData(sc);
        }

        System.out.println("\n=== Managers Information ===");
        for (int i = 0; i < 10; i++) {
            m[i].showManager();
        }
    }
}
