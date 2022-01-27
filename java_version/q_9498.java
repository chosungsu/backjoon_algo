package java_version;

import java.util.Scanner;
//시험 성적 구하기
public class q_9498 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        if (x >= 90) {
            System.out.println("A");
        } else if (x >= 80 && x < 90) {
            System.out.println("B");
        } else if (x >= 70 && x < 80) {
            System.out.println("C");
        } else if (x >= 60 && x < 70) {
            System.out.println("D");
        } else {
            System.out.println("F");
        }
	}
}
