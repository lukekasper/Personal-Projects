package battleship;

public class Cruiser extends Ship {
	
	// instantiate static cruiser parameters
	static final int cruiserLength = 3;
	static final String cruiserType  = "cruiser";

	/**
	 * Extension of Ship class constructor.
	 * Sets the length of the cruiser to static value by calling super class constructor.
	 */
	public Cruiser() {
		super(cruiserLength);
	}
	
	/**
	 * Overrides the ship type to return the static value for cruiser.
	 */
	@Override
	public String getShipType() {
		return cruiserType;
	}

}
