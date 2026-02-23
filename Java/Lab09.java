package Java;

class AStatic { static int i = 10;
    static { System.out.println("A:Static Block B1.");}
    { System.out.println("A:Normal Block B2.");}
    static { System.out.println("A:Static Block B3.");}     
    static void m() {
        System.out.println("A:static m()");
    }  
}

class Lab09 {
    static {System.out.println("Lab09:Static Block.");}
    public static void main(String[] args) {
        System.out.println("Main starts");
        AStatic a = new AStatic(); 
        new AStatic();
        System.out.println("A.i="+AStatic.i);
        System.out.println("A.i="+AStatic.i);
        AStatic.m();
        System.out.println("Main ends");
    }
}