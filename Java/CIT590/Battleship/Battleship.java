package battleship;

public class Battleship extends Ship {
	
	// instantiate static battleship parameters
	static final int battleshipLength = 4;
	static final String battleshipType  = "battleship";

	/**
	 * Extension of Ship class constructor.
	 * Sets the length of the battleship to static value by calling super class constructor.
	 */
	public Battleship() {
		super(battleshipLength);
	}

	@Override
	/**
	 * Overrides the ship type to return the static value for battleship.
	 */
	public String getShipType() {
		return battleshipType;
	}

}
