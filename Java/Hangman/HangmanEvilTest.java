import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class HangmanEvilTest {

	HangmanEvil he = new HangmanEvil("/users/lukekasper/downloads/words.txt");

	@Test
	void testHangmanEvil() {

	}

	@Test
	void testGuessLetter() {
		String alphabet = "abcdefghijklmnop";
		
		he.guessLetter('z');
		
		int size1 = he.getCurrentWordFamily().size();

		for (int i = 0; i < alphabet.length(); i++) {
			he.guessLetter(alphabet.charAt(i));
		}
		
		int size2 = he.getCurrentWordFamily().size();
		
		assertTrue(size1 > size2);
	}
}