package battleship;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class SubmarineTest {
	
	Submarine submarine = new Submarine();

	@Test
	void testGetShipType() {
		
		assertTrue(submarine.getShipType() == Submarine.submarineType);
		
	}

	@Test
	void testSubmarine() {
		
		assertTrue(submarine.getLength() == Submarine.submarineLength);
		
	}

}
