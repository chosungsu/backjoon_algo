package java_version;

import java.util.Scanner;

public class q_10950 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        
        for (int i = 0; i < x; i++) {
            int y = sc.nextInt();
            int z = sc.nextInt();
            System.out.println(y+z);
        }
	}
}
