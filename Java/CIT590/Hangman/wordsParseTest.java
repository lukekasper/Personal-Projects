import static org.junit.jupiter.api.Assertions.*;

import java.util.regex.Pattern;

import org.junit.jupiter.api.Test;

class wordsParseTest {

	wordsParse w = new wordsParse("/users/lukekasper/downloads/words_clean.txt");

	@Test
	void testWordsParse() {
		
	}

	@Test
	void testReadParse() {

		w.readParse();
		String[] words = w.getWords();

		for (String word : words) {

			assertTrue(word == word.toLowerCase());

			Pattern p = Pattern.compile("[a-z]");
			assertTrue(p.matcher(word).find());

		}
	}

	@Test
	void testGetRandomWord() {

		w.readParse();
		String word = w.getRandomWord();

		Pattern p = Pattern.compile("[a-z]");
		assertTrue(p.matcher(word).find());

		String word2 = w.getRandomWord();

		assertFalse(word == word2);
		assertTrue(p.matcher(word2).find());
	}

	@Test
	void testGetWords() {

		w.readParse();
		String[] words = w.getWords();

		for (String word : words) {

			assertTrue(word == word.toLowerCase());

			Pattern p = Pattern.compile("[a-z]");
			assertTrue(p.matcher(word).find());

		}
	}

}
