import java.io.FileNotFoundException;

public class lesson_2 {

// Задание 2

    public static void task2() {
    try {
        int d = 0;
        int[] intArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int catchedRes1 = intArray[8] / d;
        System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
        System.out.println("Catching exception: " + e);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Catching exception: " + e);
        }
    }


// Задание 3

    public static void task3() {
    try {
        int a = 90;
        int b = 3;
        System.out.println(a / b);
        printSum(23, 234);
        int[] abc = {1, 2};
        abc[3] = 9;
    } catch (NullPointerException ex) {
        System.out.println("Указатель не может указывать на null!");
    } catch (IndexOutOfBoundsException ex) {
    System.out.println("Массив выходит за пределы своего размера!");
    } catch (Throwable ex) {
    System.out.println("Что-то пошло не так...");
    }
}
    public static void printSum(Integer a, Integer b) throws FileNotFoundException {
    System.out.println(a + b);
    }

    public static void main(String[] args) throws Exception {
        task2();
        task3();
    }
}

