import java.io.*;
import java.util.*;

public class q_1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        // 1. n, m 읽기
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);

        // 2. HashSet으로 n개의 듣도 못한 사람 명단을 정렬
        HashSet<String> set = new HashSet<>(); 
        for (int i = 0; i < n; i++) {
            set.add(br.readLine());
        }

        // 3. m개의 보도 못한 사람 명단에서 HashSet에 들어있는 명단과 비교
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String tmp = br.readLine();
            if(set.contains(tmp)){
                result.add(tmp);
            }
        }

        // 4. 결과를 정렬
        Collections.sort(result);

        // 5. 최종결과 출력
        System.out.println(result.size());
        for (String s : result) {
            System.out.println(s);
        }
    }
}
