package Java;

class A {
    void m() {System.out.println("m()");}
    // void m(int i) {System.out.println("m(i)");}
    // void m(int abc) {System.out.println("m(abc)");}
    // int m(int i) {return 10;} //error: method m(int) is already defined in class A
    // void m(byte b) {System.out.println("m(b)");}
    // void m(long i) {System.out.println("m(l)");}
    void m(double d) {System.out.println("m(d)");}
    // void m(float f) {System.out.println("m(f)");}
    void m(String s) {System.out.println("m(s)");}
    void m(int i, long l) {
        System.out.println("m(i,l)");
    }
    void m(int i, byte b) {
        System.out.println("m(i,b)");
    }
    
}
class Lab08_part3 {
    public static void main(String[] args) {
        A a = new A(); a.m(); a.m(256);
        // a.m(10); //error: incompatible types: possible lossy conversSystem.outn from int to byte
        a.m((byte)10); a.m(10l);
        a.m(10,10l); 
        a.m(10,10); a.m(10,(byte)10);
    }    
}