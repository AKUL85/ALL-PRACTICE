abstract class A {
    int i;

    A(int i) {
        this.i = i;
    }

    abstract int m1(int i, int j);
}

class B extends C {
    int j;

    B(int i, int j) {
        super(i, "ABCDE");
        this.j = j;
    }

    String m2(String s) {
        return s + super.s;
    }

    class D {
        int k;

        D(int k) {
            this.k = k;
        }
    }
}

public class TestC {

    static int testCounter = 1;

    static void tester(boolean b) {
        String status = "Failed";
        if (b)
            status = "Passed";
        System.out.printf("Test #%02d %s.%n", testCounter++, status);
    }

    public static void main(String[] args) {
        B b = new B(5, 10);
        tester((b.i + b.j) == 15 && b.s == "ABCDE");
        tester(b.m1(20, 30) == 85 && b.m1(10, 20) == 55);
        tester(b.m2("123").equals("123ABCDE") && b.m2("Start").equals("StartABCDE"));
        tester(b.m2(30).k == 30 && b.m2(50).k == 50);
        A a = new C(15, "WXY");
        tester(a.i == 15 && a.m1(10, 20) == 65);
        C c = (C) a;
        tester(c.s == "WXY" && c.m1(10, 15) == 55);
        tester(c.m1("Ok").equals("**WXY||Ok") && c.m1("789").equals("**WXY||789"));
        tester(c.m3(1.1, 2.3) == 1.7 && c.m3(12.4, 23.6, 12.6) == 16.2);
        tester(c.m3(1.2, 2.3, 3.4, 4.5) == 2.85 && c.m3(2.1) == 2.1);
        tester(c.m2(25).k == 25 && c.m2(72).k == 72);
    }
}
