package battleship;

public class Destroyer extends Ship {

	// instantiate static destroyer parameters
	static final int destroyerLength = 2;
	static final String destroyerType  = "destroyer";
	
	/**
	 * Extension of Ship class constructor.
	 * Sets the length of the destroyer to static value by calling super class constructor.
	 */
	public Destroyer() {
		super(destroyerLength);
	}

	@Override
	/**
	 * Overrides the ship type to return the static value for destroyer.
	 */
	public String getShipType() {
		return destroyerType;
	}

}
