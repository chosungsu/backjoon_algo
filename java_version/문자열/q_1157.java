package java_version.문자열;

import java.util.*;
//대소문자 문제
//가장 많이 사용된 알파벳 찾기
public class q_1157 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        //arr : 알파벳 배열
        int[] arr = new int[26];
        String a = in.next().toUpperCase();

        int max = -1;
        char st = '?';
        for (int i = 0; i < a.length(); i++) {
            arr[a.charAt(i) - 65]++;
            if (max < arr[a.charAt(i) - 65]) {
                max = arr[a.charAt(i) - 65];
                st = a.charAt(i);
            } else if (max == arr[a.charAt(i) - 65]) {
                st = '?';
            }
        }
        System.out.println(st);
        
	}
}