import static org.junit.jupiter.api.Assertions.*;

import java.io.File;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class HangmanTraditionalTest {
	
	HangmanTraditional ht;
	@BeforeEach
	void setUp() throws Exception {
		String filePath = new File("").getAbsolutePath();
		filePath = filePath.concat("/src/words_clean.txt");
		this.ht = new HangmanTraditional(filePath);
	}

	@Test
	void testGuessLetter() {
		
		String word = this.ht.getWord();
		char[] status = new char[word.length()];
		for(int ix=0;ix<status.length;ix++) {
			status[ix] = '-';
		}
		for (int ix = 0;ix<word.length();ix++) {
			char c = word.charAt(ix);
			for(int jx=ix;jx<word.length();jx++) {
				if (word.charAt(jx)==c) {
					status[jx] = c;
				}
			}
			this.ht.guessLetter(c);
			assertArrayEquals(status, this.ht.getStatus());
		}
	}

}
