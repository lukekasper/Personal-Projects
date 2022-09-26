package battleship;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class BattleshipTest {
	
	Battleship battleship = new Battleship();

	@Test
	void testGetShipType() {
		
		assertTrue(battleship.getShipType() == Battleship.battleshipType);
	}

	@Test
	void testBattleship() {
		
		assertEquals(battleship.getLength(),Battleship.battleshipLength);
	}

}
