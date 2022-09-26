package battleship;

public class Submarine extends Ship {
	
	static final int submarineLength = 1;
	static final String submarineType  = "submarine";

	public Submarine() {
		super(submarineLength);
	}

	@Override
	public String getShipType() {
		return submarineType;
	}

}
