# 자바 언어에서의 핵심 코드 정리

## 초반 입력값 읽기 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    # 방법1
    Scanner in = new Scanner(System.in);
    int x = in.nextInt();
    # 방법2
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    int x = Integer.parseInt(st.nextToken());
  }
}
```

## 배열 문제의 핵심 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Arrays.sort(arr);
  }
}
```
