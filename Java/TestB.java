interface A {
    interface D {
        int j = 20;

        int m1(int j);
    }
    int j = 10;

    default String m2(String s) {
        return s.replace('a', 'd');
    }
    int m3(int j);


}

public class TestB {

    static int testCounter = 1;

    static void tester(boolean b) {
        String status = "Failed";
        if (b)
            status = "Passed";
        System.out.printf("Test #%02d %s.%n", testCounter++, status);
    }

    public static void main(String[] args) {
        B b = new B(5);
        tester((b.j + A.j + A.D.j) == 35);
        A.D d = b;
        tester(d.m1(15) == 40 && d.m1(5) == 30);
        b.j += 10;
        tester(b.m1(15) == 50 && b.m1(5) == 40);
        A a = b;
        tester(a.m2("abaabd").equals("bbbbbd"));
        tester(a.m2("dabcddaa").equals("dbbcddbb"));
        tester(a.m3(5) == 30 && a.m3(15) == 40);
        tester(b.m3(5, 10) == 50 && b.m3(15, 10) == 60);
        b.j += 10;
        tester(a.m3(15) == 50);
        tester(b.m3(15, 10) == 70);
        tester(new B(A.j).m3(10, 10) == 50);

    }
}
