package battleship;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class EmptySeaTest {

	EmptySea empty = new EmptySea();
	
	@Test
	void testGetShipType() {
		
		assertTrue(empty.getShipType() == EmptySea.emptyType);
	}

	@Test
	void testShootAt() {
		
		Random r = new Random();
		int row = r.nextInt(10);
		int col = r.nextInt(10);
		
		assertTrue(empty.shootAt(row, col) == false);
	}

	@Test
	void testIsSunk() {
		
		assertFalse(empty.isSunk() == true);
	}

	@Test
	void testToString() {
		
		assertTrue(empty.toString() == "-");
	}

	@Test
	void testEmptySea() {
		
		assertEquals(empty.getLength(), EmptySea.emptyLength);
		
	}

}
