package battleship;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class CruiserTest {

	Cruiser cruiser = new Cruiser();

	@Test
	void testGetShipType() {
		
		assertTrue(cruiser.getShipType() == Cruiser.cruiserType);
	}

	@Test
	void testBattleship() {
		
		assertEquals(cruiser.getLength(),Cruiser.cruiserLength);
	}

}
