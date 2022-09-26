package battleship;

import static org.junit.jupiter.api.Assertions.*;
import java.util.Random;

import org.junit.jupiter.api.Test;

class OceanTest {

	Ocean ocean = new Ocean();
	Battleship battleship = new Battleship();
	Cruiser cruiser = new Cruiser();
	Submarine submarine = new Submarine();
	Destroyer destroyer = new Destroyer();

	@Test
	void testOcean() {

		assertTrue(ocean.getShotsFired() == 0);
		assertTrue(ocean.getHitCount() == 0);
		assertTrue(ocean.getShipsSunk() == 0);

		Ship[][] ships = ocean.getShipArray();

		Random r = new Random();
		int row = r.nextInt(10);
		int col = r.nextInt(10);

		assertEquals(ships[row][col].getShipType(), "empty");
	}

	@Test
	void testPlaceAllShipsRandomly() {
		
		ocean.placeAllShipsRandomly();
		
		int count1 = 0;
		int count2 = 0;
		int count3 = 0;
		int count4 = 0;
		
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				Ship[][] ships = ocean.getShipArray();
				String type = ships[i][j].getShipType();
				
				if (type == "submarine") count1++;
				else if (type == "destroyer") count2++;
				else if (type == "cruiser") count3++;
				else if (type == "battleship") count4++;
			}
		}
		
		assertEquals(count1, 4);
		assertEquals(count2/Destroyer.destroyerLength, 3);
		assertEquals(count3/Cruiser.cruiserLength, 2);
		assertEquals(count4/Battleship.battleshipLength, 1);
	}

	@Test
	void testGetShipArray() {

		Ship[][] ships = ocean.getShipArray();

		assertTrue(ships[3][4].getShipType() == "empty");

		battleship.placeShipAt(3, 4, true, ocean);
		ships = ocean.getShipArray();

		assertTrue(ships[3][4] == battleship);

		cruiser.placeShipAt(5, 6, false, ocean);
		ships = ocean.getShipArray();

		assertTrue(ships[3][4] == battleship);
		assertTrue(ships[4][6] == cruiser);
	}

	@Test
	void testIsOccupied() {

		battleship.placeShipAt(3, 4, true, ocean);
		cruiser.placeShipAt(5, 6, false, ocean);

		assertTrue(ocean.isOccupied(3,4));
		assertTrue(ocean.isOccupied(4,6));
		assertFalse(ocean.isOccupied(0,0));
	}

	@Test
	void testShootAt() {

		battleship.placeShipAt(3, 4, true, ocean);

		boolean flag = ocean.shootAt(3,2);

		assertTrue(flag);
		assertEquals(ocean.getShotsFired(),1);
		assertEquals(ocean.getHitCount(),1);
		assertEquals(ocean.getShipsSunk(),0);

		boolean flag2 = ocean.shootAt(1,0);

		assertFalse(flag2);
		assertEquals(ocean.getShotsFired(),2);
		assertEquals(ocean.getHitCount(),1);

		submarine.placeShipAt(9, 9, true, ocean);

		ocean.shootAt(9, 9);

		assertEquals(ocean.getShotsFired(),3);
		assertEquals(ocean.getHitCount(),2);
		assertEquals(ocean.getShipsSunk(),1);

	}

	@Test
	void testGetShotsFired() {

		assertEquals(ocean.getShotsFired(),0);

		ocean.shootAt(3,2);
		assertEquals(ocean.getShotsFired(),1);

		ocean.shootAt(9,1);
		assertEquals(ocean.getShotsFired(),2);

		ocean.shootAt(9,1);
		assertEquals(ocean.getShotsFired(),3);
	}

	@Test
	void testGetHitCount() {

		battleship.placeShipAt(3, 4, true, ocean);

		assertEquals(ocean.getHitCount(),0);
		ocean.shootAt(3,2);
		assertEquals(ocean.getHitCount(),1);
		ocean.shootAt(9,1);
		assertEquals(ocean.getHitCount(),1);
	}

	@Test
	void testGetShipsSunk() {

		destroyer.placeShipAt(3, 4, true, ocean);
		submarine.placeShipAt(9, 9, true, ocean);

		assertEquals(ocean.getShipsSunk(),0);
		ocean.shootAt(3,4);
		assertEquals(ocean.getShipsSunk(),0);
		ocean.shootAt(9,9);
		assertEquals(ocean.getShipsSunk(),1);
		ocean.shootAt(3,3);
		assertEquals(ocean.getShipsSunk(),2);
	}

	@Test
	void testIsGameOver() {

		for (int i = 0; i < 9; i++) {
			Submarine submarine1 = new Submarine();
			submarine1.placeShipAt(9, i, true, ocean);
			ocean.shootAt(9,i);
		}

		assertEquals(ocean.getShipsSunk(),9);
		assertFalse(ocean.isGameOver());

		submarine.placeShipAt(9, 9, true, ocean);
		ocean.shootAt(9,9);
		assertEquals(ocean.getShipsSunk(),10);
		assertTrue(ocean.isGameOver());
	}
}
