package book;

import static org.junit.jupiter.api.Assertions.*;

import java.util.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import book.file.BookFileReader;

class BookTest {
	
	List<String> warAndPeace = BookFileReader.parseFile("src/war_and_peace.txt");
	Book warAndPeaceBook = new Book(warAndPeace);
	
	List<String> siddhartha = BookFileReader.parseFile("src/siddhartha.txt");
	Book siddharthaBook = new Book(siddhartha);
	
	
	@BeforeEach
	void setUp() throws Exception {
		
	}

	@Test
	void testBook() {
		List<String> bookLines = new ArrayList<String>();
		Book book = new Book(bookLines);
		
		//confirm book lines is empty
		assertEquals(0, book.getLines().size());
	}

	@Test
	void testGetTitle() {
		
		assertEquals(warAndPeaceBook.getTitle(),"War and Peace");
		assertEquals(siddharthaBook.getTitle(),"Siddhartha");
	}

	@Test
	void testGetAuthor() {
		
		assertEquals(warAndPeaceBook.getAuthor(),"Leo Tolstoy");
		assertEquals(siddharthaBook.getAuthor(),"Hermann Hesse");
	}

	@Test
	void testGetTotalWordCount() {
		
		List<String> bookLines = new ArrayList<String>();
		Book book = new Book(bookLines);
		
		assertTrue(book.getTotalWordCount() == 0);
		
		bookLines.add("These are some words");
		Book book2 = new Book(bookLines);
		
		assertTrue(book2.getTotalWordCount() == 4);
		
		bookLines.add("These are some more words");
		Book book3 = new Book(bookLines);
		
		assertTrue(book3.getTotalWordCount() == 9);
	}

	@Test
	void testGetUniqueWordCount() {
		
		List<String> bookLines = new ArrayList<String>();
		Book book = new Book(bookLines);
		
		assertTrue(book.getUniqueWordCount() == 0);
		
		bookLines.add("These are some words");
		Book book2 = new Book(bookLines);
		
		assertTrue(book2.getUniqueWordCount() == 4);
		
		bookLines.add("These are some more words");
		Book book3 = new Book(bookLines);
		
		assertTrue(book3.getUniqueWordCount() == 5);
	}

	@Test
	void testGetSpecificWordCount() {
		
		List<String> bookLines = new ArrayList<String>();
		Book book = new Book(bookLines);
		
		assertTrue(book.getSpecificWordCount("are") == 0);
		
		bookLines.add("These are some words");
		Book book2 = new Book(bookLines);
		
		assertTrue(book2.getSpecificWordCount("are") == 1);
		
		bookLines.add("These are some more words");
		Book book3 = new Book(bookLines);
		
		System.out.println(book3.getSpecificWordCount("are"));
		
		assertTrue(book3.getSpecificWordCount("are") == 2);
	}
}