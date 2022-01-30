package java_version.정렬;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class q_1181 {
    public static void main(String[] args)  {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        String arr[] = new String[n];
        
        for(int i =0;i<arr.length;i++) { 
            arr[i] = in.next();
        }
        
        Arrays.sort(arr,new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) { 
                if(o1.length() == o2.length()) {
                    // 두 문자열의 길이가 같은 경우는
                    return o1.compareTo(o2);
                }			
                else {
                    // 그 외에는 문자열들의 길이로 비교
                    return Integer.compare(o1.length(),o2.length());
                }
            }  
        });
        // 중복을 고려해 출력하기 위해 첫 번째 문자열은 출력
        System.out.println(arr[0]);
        for(int i=1;i<arr.length;i++) {
            if(arr[i-1].equals(arr[i])) continue;
            System.out.println(arr[i]);
        }
      }
}
