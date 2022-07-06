package java_version.기본수학2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class q_1358 {
    public static double getDistance(
        int x1, int y1, int x2, int y2
    ) {
        return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int x_start = Integer.parseInt(st.nextToken());
        int y_start = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        int x_end = x_start + w;
        int y_end = y_start + h;

        int r = h/2, y_half = y_start + r;
        int x, y, cnt = 0;
        for (int i = 0; i < p; ++i) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            if (x_start <= x && x <= x_end && y_start <= y && y <= y_end ||
                getDistance(x, y, x_start, y_half) <= r ||
                getDistance(x, y, x_end, y_half) <= r
            ) {
                cnt++;
            }
        }
        br.close();
        System.out.println(cnt);

    }
}
