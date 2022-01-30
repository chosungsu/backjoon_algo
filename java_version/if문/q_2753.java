package java_version.if문;

import java.util.Scanner;

public class q_2753 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        if (x % 4 == 0 && (x % 400 == 0 || x % 100 != 0)) {
            System.out.println("1");
        } else {
            System.out.println("0");
        }
	}
}
