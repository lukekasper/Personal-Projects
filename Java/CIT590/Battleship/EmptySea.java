package battleship;

public class EmptySea extends Ship {
	
	// instantiate static battleship parameters
	static final int emptyLength = 1;
	static final String emptyType = "empty";
	
	/**
	 * Extension of Ship class constructor.
	 * Sets the length of the empty sea to static value by calling super class constructor.
	 */
	public EmptySea() {
		super(emptyLength);
	}
	
	@Override
	/**
	 * Overridden shootAt method.
	 * @return false to indicate a miss
	 */
	boolean shootAt(int row, int column) {
		return false;
	}

	@Override
	/**
	 * Overridden isSunk method.
	 * @return false to indicate no ship is sunk.
	 */
	boolean isSunk() {
		return false;
	}
	
	@Override
	/**
	 * Overridden toString method for printing the ocean.
	 * @return "-" to indicate a miss.
	 */
	public String toString() {
		return "-";
	}
	
	@Override
	/**
	 * Overrides the ship type to return the static value for empty sea.
	 */
	public String getShipType() {
		return emptyType;
	}
}
