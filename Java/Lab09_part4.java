package Java;


class A { int i; static int j;
    // Non-static nested class: Inner
    class B {
        void m() {
            System.out.println("B.m()"+i);
            System.out.println("B.m()"+j);
        }
        static void m2() {
            System.out.println("B.m(i)"+j);
            // System.out.println("B.m(i)"+i); //error: non-static variable i cannot be referenced from a static context
        }
    }
    void m() { B.m2(); B b = new B(); b.m(); }
    static class C {
        void m() {
            System.out.println("C.m()"+j);
            // System.out.println("C.m()"+i); // error: non-static variable i cannot be referenced from a static context
        }
        static void m2() {
            // System.out.println("C.m(i)"+i);
            System.out.println("C.m(i)"+j);
        }
    }
    void m2() {
        C.m2(); //C.m();
        C c = new C(); c.m();
    }
}
// class B{}
public class Lab09_part4 {
    public static void main(String[] args) {
        A a = new A(); // a.m();
        // B b;  // error: cannot find symbol
        // A.B b = new B();// error: cannot find symbol
        // A.B b = new A.B();// error: an enclosing instance that contains A.B is required
        // A.B b = new a.B(); // error: package a does not exist
        // A.B.m2();
        // A.B b = a.new B(); b.m();
        a.m2();
        // C c; // error: cannot find symbol
        A.C.m2();
        A.C c;
        // c = a.new C(); // error: qualified new of static class
        // c = A.new C(); // error: qualified new of static class
        c = new A.C(); c.m();
    }
}