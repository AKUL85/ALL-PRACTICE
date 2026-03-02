package Adapter;

interface Lion {
    void roar();
}
class AfricanLion implements Lion {
    public void roar() {
        System.out.println("African Lion Roars!");
    }
}

class AsiaLion implements Lion {
    public void roar() {
        System.out.println("Asia Lion Roars!");
    }
}
class Hunter {
    public void hunt(Lion lion) {
        lion.roar();
        System.out.println("Hunter hunts the lion!");
    }
}
class WildDog {
    public void bark() {
        System.out.println("Wild Dog Barks!");
    }
}
class WildDogAdapter implements Lion {

    private WildDog dog;

    public WildDogAdapter(WildDog dog) {
        this.dog = dog;
    }

    public void roar() {
        dog.bark();   // Convert roar() into bark()
    }
}
public class adapter {
    public static void main(String[] args) {
        
    }
}
