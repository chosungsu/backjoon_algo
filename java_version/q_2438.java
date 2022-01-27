package java_version;

import java.util.Scanner;

//별찍기-1
//예시
//* 
//**
//***
//****
public class q_2438 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
	}
}
