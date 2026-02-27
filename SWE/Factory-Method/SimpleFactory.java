 interface Door {
    int getHeight();
    int getWidth();
    
}
class WoodenDoor implements Door{
    private int height;
    private int width;
    WoodenDoor(int height,int width){
        this.height=height;
        this.width=width;
    }
    public int getHeight(){
        return height;
    }
    public int getWidth(){
        return width;
    }
}
class DoorFactory{
    public static Door makeDoor(int height,int width){
        return new WoodenDoor(height, width);
    }
}
public class SimpleFactory{
    public static void main(String[] args) {
        Door door=DoorFactory.makeDoor(80,30);

        System.out.println("Height: " + door.getHeight());
        System.out.println("Width: " + door.getWidth());
    }
    
}
