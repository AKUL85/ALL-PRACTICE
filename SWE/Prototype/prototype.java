package Prototype;


interface clonable {
     String getCategory();
    
}
class Sheep implements clonable{
    private String name;
    private String category;
    Sheep(String name,String category){
        this.name=name;
        this.category=category;
    }
    public Sheep clone(){
        try {
            return(Sheep)super.clone();
        } catch (CloneNotSupportedException e) {
             throw new RuntimeException(e);
        }
    }// TODO: handle exception
      public String getName() {
        return name;
    }
    public void setName(String name){
        this.name=name;
    }
    public String getCategory(){
        return category;
    }

}


public class prototype {
    public static void main(String[] args) {
        Sheep original=new Sheep("dolly","mountain");
                System.out.println(original.getName());      // Jolly
        System.out.println(original.getCategory());  

        Sheep cloned=original.clone();
        cloned.setName("jolly");
         System.out.println(cloned.getName());        // Dolly
        System.out.println(cloned.getCategory());    // Mountain Sheep

        System.out.println(original.getName()); 
    }
}
