import static org.junit.jupiter.api.Assertions.*;

import java.io.File;
import java.util.ArrayList;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class HangmanTest {

	HangmanTraditional ht;
	@BeforeEach
	void setUp() throws Exception {
		String filePath = new File("").getAbsolutePath();
		filePath = filePath.concat("/src/words_clean.txt");
		this.ht = new HangmanTraditional(filePath);
	}
	
	@Test
	void testGetCurrentWordFamily() {
		int length = ht.getWord().length();
		
		ArrayList<String> currentWordFamily = new ArrayList<String>(ht.getCurrentWordFamily());
		
		for (String word : currentWordFamily) {
			
			assertEquals(word.length(), length);
		}
		
		assertTrue(currentWordFamily.size() > 1);
	}

	@Test
	void testSetCurrentWordFamily() {
		
		ArrayList<String> currentWordFamily = new ArrayList<String>();
		
		currentWordFamily.add("bark");
		currentWordFamily.add("meow");
		currentWordFamily.add("grow");
		currentWordFamily.add("show");
		
		ht.setCurrentWordFamily(currentWordFamily);
		
		assertTrue(currentWordFamily.get(0) == "bark");
		assertTrue(currentWordFamily.get(1) == "meow");
		assertTrue(currentWordFamily.get(2) == "grow");
		assertTrue(currentWordFamily.get(3) == "show");
	}

	@Test
	void testGetWord() {
		
		ht.setWord("dog");
		assertTrue(ht.getWord() == "dog");
		
		ht.setWord("cat");
		assertTrue(ht.getWord() == "cat");
		
		ht.setWord("mouse");
		assertTrue(ht.getWord() == "mouse");
	}

	@Test
	void testSetWord() {
		
		ht.setWord("fat");
		assertTrue(ht.getWord() == "fat");
		
		ht.setWord("thin");
		assertTrue(ht.getWord() == "thin");
		
		ht.setWord("medium");
		assertTrue(ht.getWord() == "medium");
	}

	@Test
	void testSetWrongGuesses() {
		
		ArrayList<Character> guesses = new ArrayList<Character>();
		
		ht.setWrongGuesses('s');
		guesses.add('s');
		
		assertEquals(ht.getWrongGuesses(), guesses);
		
		ht.setWrongGuesses('a');
		guesses.add('a');
		
		assertEquals(ht.getWrongGuesses(), guesses);
		
		ht.setWrongGuesses('t');
		guesses.add('t');
		
		assertEquals(ht.getWrongGuesses(), guesses);
	}

	@Test
	void testSetStatus() {
		
		int length = ht.getstatusLength();
		ht.setStatus(1, 'p');
		
		assertEquals(length,ht.getstatusLength());
		
		ht.setStatus(0, 'a');
		assertTrue(ht.getStatus()[1] == 'p');
		assertTrue(ht.getStatus()[0] == 'a');
	}

	@Test
	void testGetstatusLength() {
		
		assertEquals(ht.getstatusLength(), ht.getWord().length());
		
		ht.setStatus(1, 'g');
		assertEquals(ht.getstatusLength(), ht.getWord().length());
	}

	@Test
	void testDecreasestatusLength() {
		
		int length = ht.getstatusLength();
		ht.decreasestatusLength();
		int length2 = ht.getstatusLength();
		
		assertEquals(length, ht.getWord().length());
		assertTrue(length > length2);
		
		ht.decreasestatusLength();
		assertTrue(length2 > ht.getstatusLength());
	}

	@Test
	void testGetStatus() {
		
		char[] status = ht.getStatus();
		
		for (char c : status) {
			assertTrue(c == '-');
		}
		
		ht.setStatus(1, 'g');
		assertEquals(ht.getStatus()[1],'g');
		
		ht.setStatus(3, 'e');
		assertEquals(ht.getStatus()[3],'e');
		
	}

}
