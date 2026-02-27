
class President{
    public static President instance;
    President(){
        System.out.println("president created");
    }
    
        public static President getInstance(){
            if(instance==null){
                instance=new President();
            }
            return instance;
        }
        
    
}

public class Singleton {
    public static void main(String[] args) {
        
    

        President a = President.getInstance();
        President b = President.getInstance();

        System.out.println(a == b);   
    

    }
}
