package recitation;

/**
 * Represents a mango.
 * Extends fruit.
 * @author tianshi.wang
 *
 */
public class Mango extends Fruit{

	/**
	 * Build constructor using super() function
	 * Create the different Mangos with color, seasonal or not, weight and price
	 * The name of the Mango Class is always a string "Mango", so we don't need a new parameter to be passed in constructor 
	 * @param color for mango
	 * @param seasonal for mango
	 * @param int weight of mango
	 * @param int price for mango
	 */
	public Mango(Color color, boolean seasonal, int weight, int price) {
		super(color,seasonal);
		
		this.weight = weight;
		this.price = price;
	}

	
	/**
	 * Print out "Cut the Mango".
	 */
	@Override
	public void prepare() {
		System.out.print("Cut the Mango");
		System.out.println(" ");
	}
}
