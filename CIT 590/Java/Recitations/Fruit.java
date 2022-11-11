package recitation;

/**
 * Represents fruit.
 * @author tianshi.wang
 */
public abstract class Fruit {
	
    /**
     * The color of the fruit, Notice that the color is another class, you should implement it first.
     */
	protected Color color;
	
	/**
	 * Whether the fruit is seasonal, if so, true. If it's not seasonal, it's false.
	 */
    protected boolean seasonal;
    
    /**
     * The weight of the fruit.
     */
    protected int weight;
	
    /**
	 * The price of the fruit.
	 */
	protected int price;
	
	/**
	 * The fruit name.
	 */
	protected String name;
	
	/**
	 * Abstract Class Fruit with Color color, boolean seasonal.
	 * Notice that Color is a class, you have to implement it first.
	 * @param color of fruit
	 * @param seasonal property of fruit
	 */
    public Fruit(Color color, boolean seasonal) {
        this.color = color;
        this.seasonal = seasonal;
    }
   
    /**
     *  This is an abstract method, see it doesn't have method body, only declaration.
     *  You have to print "Peal the banana" in Banana class and print "Cut the Mango" in Mango Class.
     */
    public abstract void prepare();
    
    /**
     * @return whether fruit is seasonal, if yes return true, else return false
     */
    public boolean isSeasonal() {
        return this.seasonal;
    }
    
    /**
     * @return the weight of the fruit
     */
    public int getWeight(){
    	return this.weight;
    }
    
    /**
     * 
     * @return return the price of the fruit
     */
    public int getPrice() {
    	return this.price;
    }
    
    /**
     * 
     * @return the color of the fruit
     */
    public Color getColor() {
        return this.color;
    }
    
    /**
     * get the name of the fruit
     * @return name of fruit
     */
    public String getName() {
    	return this.name;
    }
    
    /**
     * You can return the int value of total price, use totalPrice = weight * price.
     * @param weight of fruit
     * @param price for fruit
     * @return the total price of the fruit
     */
    private int totalPrice(int weight, int price) {
    	int totalPrice = weight*price;
    	return totalPrice;
    }
    
    /**
     * Print out the total price
     */
    public void printTotalPrice() {
    	System.out.println("The total price for a " + this.getName() +  " is: " + totalPrice(this.weight,this.getPrice()));
    }

    /**
     * Print out the fruit color with the format : Fruit Name + Color.
     */
    public void printColor() {
    	System.out.println(this.getName() + this.getColor());
    }
 
    /**
     * main function
     * In the main function, you have to create two colors first.
     * Then create two instances of Mango Class and Banana Class.
     * Test that the printColor(), printTotalPrice(), prepare() and isSeasonal() functions are correct.
     */
    public static void main(String[] args) {
    	Color color1 = new Color("yellow");
    	Color color2 = new Color("red/orange");
    	
    	Mango mango = new Mango(color2, true, 3, 4);
    	Banana banana = new Banana(color1, false, 2, 2);
    	
    	mango.printColor();
    	banana.printColor();

    	mango.printTotalPrice();
    	banana.printTotalPrice();
    	
    	mango.prepare();
    	banana.prepare();
    	
    	mango.isSeasonal();
    	banana.isSeasonal();
    }
}
