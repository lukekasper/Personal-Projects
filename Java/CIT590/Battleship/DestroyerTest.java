package battleship;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class DestroyerTest {

	Destroyer destroyer = new Destroyer();

	@Test
	void testGetShipType() {
		
		assertTrue(destroyer.getShipType() == Destroyer.destroyerType);
	}

	@Test
	void testBattleship() {
		
		assertEquals(destroyer.getLength(), Destroyer.destroyerLength);
	}

}
