package java_version;

import java.util.Scanner;

public class q_10430 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int z = sc.nextInt();

        System.out.println((x + y)% z);
        System.out.println(((x%z + y%z))% z);
        System.out.println((x * y)% z);
        System.out.println(((x%z * y%z))% z);
	}
}
