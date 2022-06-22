import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class q_14425 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N, M을 읽기
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        // HashMap에 N줄만큼의 문자열을 담기
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            map.put(br.readLine(), 1);
        }
        // N이하에서 M줄까지의 문자열을 읽음과 동시에
        // HashMap에 담긴 문자열과 비교하여 cnt 증가시킴
        int cnt = 0;
        for (int i = 0; i < M; i++) {
            String str = br.readLine();
            if (map.get(str) != null) {
                cnt++;
            }
        }
        // 최종결과 출력
        bw.write(cnt + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}