package java_version.기본수학1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class q_1193 {
    public static void main(String[] args) throws IOException { 
        // BufferedReader, StringBuffer 선언 및 N 입력 
        BufferedReader br = new BufferedReader(
            new InputStreamReader(
            System.in)
        ); 
        StringBuffer sb = new StringBuffer(); 
        int N = Integer.parseInt(br.readLine()); 
        // 갯수를 구할 Count 
        int count = 1; 
        // 반복문을 사용 N이 Count보다 작아지면 반복문 종료 
        while(N > count) { 
            N -= count++; 
        } // 짝 수인 경우 
        if(count % 2 == 0) { 
            // N이 분자, count+1-N 분모 
            sb.append(N).append("/").append(count+1 - N); 
            // 홀 수인 경우 
        }else { 
            // count+1-N 분자, N이 분모 
            sb.append(count+1 - N).append("/").append(N); 
        } // 결과 출력 
        System.out.print(sb.toString()); 
    }
}