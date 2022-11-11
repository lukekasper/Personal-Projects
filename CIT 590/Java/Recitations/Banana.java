package recitation;

/**
 * Represents a banana.
 * Extends fruit.
 * @author tianshi.wang
 *
 */
public class Banana extends Fruit{
	
	/**
	 * Build constructor using super() function.
	 * Create the different Bananas with color, seasonal or not, weight and price.
	 * The name of the Banana Class is always a string "Banana", so we don't need a new parameter to be passed in constructor. 
	 * @param color of banana
	 * @param seasonal for banana
	 * @param int weight for bananas
	 * @param int price for business
	 */
	public Banana(Color color, boolean seasonal, int weight, int price) {
		super(color,seasonal);
		
		this.weight = weight;
		this.price = price;
	}
	
	/**
	 * Print out "Peal the Banana".
	 */
	@Override
	public void prepare() {
		System.out.println("Peal the Banana");
		System.out.println(" ");
	}
}
