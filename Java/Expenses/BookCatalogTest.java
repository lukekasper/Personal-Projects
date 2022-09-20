package book;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import book.file.BookFileReader;

class BookCatalogTest {
	
	List<String> warAndPeace = BookFileReader.parseFile("src/war_and_peace.txt");
	Book warAndPeaceBook = new Book(warAndPeace);
	
	List<String> siddhartha = BookFileReader.parseFile("src/siddhartha.txt");
	Book siddharthaBook = new Book(siddhartha);
	
	@BeforeEach
	void setUp() throws Exception {
		
	}
	
	@Test
	void testBookCatalog() {
		BookCatalog bookCatalog = new BookCatalog();
		
		//confirm book map is empty
		assertEquals(0, bookCatalog.getBookMap().size());
	}

	@Test
	void testAddBook() {
		
		BookCatalog bookCatalog = new BookCatalog();
		assertEquals(0, bookCatalog.getBookMap().size());
		
		bookCatalog.addBook(warAndPeaceBook);
		assertEquals(1, bookCatalog.getBookMap().size());
		
		bookCatalog.addBook(siddharthaBook);
		assertEquals(2, bookCatalog.getBookMap().size());
	}

	@Test
	void testGetBookByTitle() {
		
		BookCatalog bookCatalog = new BookCatalog();
		bookCatalog.addBook(warAndPeaceBook);
		
		assertTrue(bookCatalog.getBookByTitle("War and Peace") == warAndPeaceBook);
		
		bookCatalog.addBook(siddharthaBook);
		
		assertTrue(bookCatalog.getBookByTitle("Siddhartha") == siddharthaBook);
	}

	@Test
	void testGetBookByAuthor() {
		
		BookCatalog bookCatalog = new BookCatalog();
		bookCatalog.addBook(warAndPeaceBook);
		
		System.out.println(bookCatalog.getBookByAuthor("Leo Tolstoy"));
		
		assertTrue(bookCatalog.getBookByAuthor("Leo Tolstoy") == warAndPeaceBook);
		
		bookCatalog.addBook(siddharthaBook);
		
		assertTrue(bookCatalog.getBookByAuthor("Hermann Hesse") == siddharthaBook);
	}
}
