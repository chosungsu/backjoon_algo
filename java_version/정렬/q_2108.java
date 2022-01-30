package java_version.정렬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class q_2108 {
    public static void main(String[] args) throws IOException {        
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<Integer>();
        int [] arr =new int[n];
        int [] check =new int[8001];
        int max=0;
        int sum = 0;
        //산술평균
        for(int i=0;i<n;i++) {
            arr[i]=Integer.parseInt(br.readLine());
            sum+=arr[i];
            check[arr[i] + 4000]++;
        }
        System.out.println((int)Math.round((double)sum/n));
        //중앙값
        Arrays.sort(arr);
        System.out.println(arr[n/2]);
        //최빈값
        for (int j = 0; j < check.length; j++) {
            max = Math.max(max, check[j]);
        }
        for (int j = 0; j < check.length; j++) {
            if (check[j] == max) {
                list.add(j - 4000);
            }
        }
        System.out.println(list.size() > 1 ? list.get(1) : list.get(0));
        //범위
        System.out.println(arr[n-1]-arr[0]);
              
    }
}
