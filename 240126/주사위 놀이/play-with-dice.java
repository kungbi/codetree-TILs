import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] counter = new int[7];

        for(int i = 0; i < 10; i++){
            counter[sc.nextInt()]++;
        }

        for(int i = 1; i < 7; i++){
            System.out.printf("%d - %d\n", i, counter[i]);
        }

    }
}