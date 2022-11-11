package battleship;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ShipTest {
	
	Ocean ocean = new Ocean();
	Ship ship = new Battleship();
	Ship ship2 = new Cruiser();
	Ship ship3 = new Destroyer();
	Ship ship4 = new Submarine();
	Ship ship5 = new EmptySea();
	
	@Test
	void testShip() {
		
		assertEquals(ship.getLength(), Battleship.battleshipLength);
		assertEquals(ship.getHit().length, Battleship.battleshipLength);	
	}

	@Test
	void testGetBowRow() {
		
		ship.placeShipAt(3, 4, true, ocean);
		assertTrue(ship.getBowRow() == 3);
		
		Ship ship2 = new Cruiser();
		ship2.placeShipAt(9, 9, true, ocean);
		assertTrue(ship2.getBowRow() == 9);
	}

	@Test
	void testSetBowRow() {
		
		ship.setBowRow(5);
		assertTrue(ship.getBowRow() == 5);
		
		ship.setBowRow(9);
		assertTrue(ship.getBowRow() == 9);
		
		ship2.placeShipAt(2, 9, true, ocean);
		ship2.setBowRow(8);
		assertTrue(ship2.getBowRow() == 8);
	}

	@Test
	void testGetBowColumn() {
		
		ship.placeShipAt(3, 4, true, ocean);
		assertTrue(ship.getBowColumn() == 4);
		
		ship2.placeShipAt(9, 8, true, ocean);
		assertTrue(ship2.getBowColumn() == 8);
	}

	@Test
	void testSetBowColumn() {
		
		ship.setBowColumn(5);
		assertTrue(ship.getBowColumn() == 5);
		
		ship.setBowColumn(9);
		assertTrue(ship.getBowColumn() == 9);
		
		ship2.placeShipAt(2, 8, false, ocean);
		ship2.setBowColumn(7);
		assertTrue(ship2.getBowColumn() == 7);
	}

	@Test
	void testGetLength() {
		
		assertEquals(ship.getLength(), Battleship.battleshipLength);
		assertEquals(ship2.getLength(), Cruiser.cruiserLength);
	}

	@Test
	void testIsHorizontal() {
		
		ship.placeShipAt(3, 4, false, ocean);
		assertFalse(ship.isHorizontal());
		
		ship.placeShipAt(3, 4, true, ocean);
		assertTrue(ship.isHorizontal());
	}

	@Test
	void testSetHorizontal() {
		
		ship.setHorizontal(false);
		assertFalse(ship.isHorizontal());
		
		ship.setHorizontal(true);
		assertTrue(ship.isHorizontal());
		
		ship.placeShipAt(8, 9, true, ocean);
		ship.setHorizontal(false);
		assertFalse(ship.isHorizontal());
	}

	@Test
	void testGetHit() {
		
		boolean[] hits = ship.getHit();
		
		for (int i = 0; i < ship.getLength(); i++) {
			assertFalse(hits[i]);
		}
		
		ship.placeShipAt(3, 4, true, ocean);
		ship.shootAt(3,4);
		
		assertTrue(hits[0]);
		assertFalse(hits[1]);
		
		ship.shootAt(3,3);
		
		assertTrue(hits[1]);
		assertEquals(hits[2],false);
	}

	@Test
	void testGetShipType() {
		
		assertTrue(ship.getShipType() == "battleship");
		assertEquals(ship2.getShipType(), "cruiser");
		assertTrue(ship3.getShipType() == "destroyer");
		assertEquals(ship4.getShipType(), "submarine");
		assertTrue(ship5.getShipType() == "empty");
	}

	@Test
	void testOkToPlaceShipAt() {
		
		assertTrue(ship.okToPlaceShipAt(5, 5, true, ocean));
		assertFalse(ship.okToPlaceShipAt(2, 2, false, ocean));
		
		ship4.placeShipAt(5, 5, true, ocean);
		assertFalse(ship.okToPlaceShipAt(5, 4, true, ocean));
		assertTrue(ship.okToPlaceShipAt(5, 3, false, ocean));
		
		ship5.placeShipAt(9, 9, true, ocean);
		assertTrue(ship.okToPlaceShipAt(9, 9, false, ocean));
	}
	
	@Test
	void testJudgeOccupied() {
		
		ship4.placeShipAt(5, 5, true, ocean);
		assertTrue(ship4.judgeOccupied(ship4.getBowColumn() + 1, ship4.getBowColumn() - 1, ship4.getBowRow() - 1, ship4.getBowRow() + 1, ocean));
		assertFalse(ship4.judgeOccupied(9, 7, 7, 9, ocean));
		assertTrue(ship4.judgeOccupied(6, 4, 3, 5, ocean));
	}

	@Test
	void testPlaceShipAt() {
		
		ship.placeShipAt(3, 4, false, ocean);
		assertTrue(ship.getBowColumn() == 4);
		assertEquals(ship.getBowRow(),3);
		assertFalse(ship.isHorizontal());
		
		Ship[][] ships = ocean.getShipArray();
		
		assertTrue(ships[0][4].getShipType() == "battleship");
		assertEquals(ships[0][3].getShipType(),"empty");
	}

	@Test
	void testShootAt() {
		
		ship.placeShipAt(3, 4, false, ocean);
		
		assertFalse(ship.shootAt(8, 8));
		
		boolean[] hits = ship.getHit();
		
		for (int i = 0; i < ship.getLength(); i++) {
			assertFalse(hits[i]);
		}
		
		assertTrue(ship.shootAt(0, 4));
		assertTrue(hits[ship.getLength()-1]);
		
		assertTrue(ship.shootAt(1, 4));
		assertTrue(ship.shootAt(2, 4));
		assertTrue(ship.shootAt(2, 4));  // second shot at same location still returns a hit
		assertTrue(ship.shootAt(3, 4));  // ship is now sunk
		assertFalse(ship.shootAt(3, 4)); // second shot at now sunk location does not return a hit
	}

	@Test
	void testIsSunk() {
		
		assertFalse(ship3.isSunk());
		ship3.placeShipAt(3, 3, true, ocean);
		ship3.shootAt(3,3);
		
		assertFalse(ship3.isSunk());
		ship3.shootAt(3,2);
		assertTrue(ship3.isSunk());
		
		ship4.placeShipAt(9, 9, true, ocean);
		assertFalse(ship4.isSunk());
		ship4.shootAt(9,9);
		assertTrue(ship4.isSunk());
	}

	@Test
	void testToString() {
		
		ship3.placeShipAt(4, 4, false, ocean);
		assertEquals(ship3.toString(),"x");
		ship3.shootAt(4,4);
		assertEquals(ship3.toString(),"x");
		ship3.shootAt(3, 4);
		assertEquals(ship3.toString(),"s");
	}
}
