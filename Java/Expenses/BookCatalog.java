package book;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.Map.Entry;

import book.file.BookFileReader;

/**
 * Represents a catalog of books.
 * Code: <insert code>
 * @author <Y6T5R4 ldk44>
 *
 */
public class BookCatalog {

	/**
	 * Internal map for storing books.
	 */
	private Map<String, Book> bookMap;

	/**
	 * Creates a book catalog and initializes the internal map for storing books.
	 */
	public BookCatalog() {
		this.bookMap = new TreeMap<String, Book>();
	}

	/**
	 * Gets internal book map.
	 * @return book map
	 */
	public Map<String, Book> getBookMap() {
		return this.bookMap;
	}

	/**
	 * Adds the given book to the internal map.
	 * Uses book title as key and book itself as value.  If title is null, doesn't add book.
	 * @param book to add
	 */
	public void addBook(Book book) {

		if (book.getTitle() != null) {
			this.getBookMap().put(book.getTitle(), book);
		}
	}

	/**
	 * Gets the book associated with the given title.
	 * Returns null if the book doesn't exist in the catalog.
	 * @param title of book
	 * @return book
	 */
	public Book getBookByTitle(String title) {

		Map<String, Book> map = this.getBookMap();

		if (map.containsKey(title)) {
			return map.get(title);
		}

		else {
			return null;
		}
	}

	/**
	 * Gets the book associated with the given author.
	 * Returns null if the book doesn't exist in the catalog.
	 * @param author of book
	 * @return book
	 */
	public Book getBookByAuthor(String author) {

		Map<String, Book> map = this.getBookMap();

		for (Entry<String, Book> entry : map.entrySet()) {
			
			Book book = entry.getValue();

			String author2 = book.getAuthor();

			if (author == author2) {
				return book;
			}
		}
		return null;
	}

	public static void main(String[] args) {

		//create instance of book catalog
		BookCatalog bookCatalog = new BookCatalog();

		//load book files 
		List<String> warAndPeace = BookFileReader.parseFile("src/war_and_peace.txt");
		List<String> siddhartha = BookFileReader.parseFile("src/siddhartha.txt");

		//create books with lists above
		Book warAndPeaceBook = new Book(warAndPeace);
		Book siddharthaBook = new Book(siddhartha);

		//add books to catalog
		bookCatalog.addBook(warAndPeaceBook);
		bookCatalog.addBook(siddharthaBook); 

		//get titles
		System.out.println("\nGET TITLES");
		String warAndPeaceBookTitle = warAndPeaceBook.getTitle();
		System.out.println(warAndPeaceBookTitle);
		String siddharthaBookTitle = siddharthaBook.getTitle();
		System.out.println(siddharthaBookTitle);

		//get authors
		System.out.println("\nGET AUTHORS");
		String warAndPeaceBookAuthor = warAndPeaceBook.getAuthor();
		System.out.println(warAndPeaceBookAuthor);
		String siddharthaBookAuthor = siddharthaBook.getAuthor();
		System.out.println(siddharthaBookAuthor);

		//get books by title
		System.out.println("\nGET BOOKS BY TITLE");
		System.out.println(bookCatalog.getBookByTitle("War and Peace"));
		System.out.println(bookCatalog.getBookByTitle("Siddhartha"));

		//get books by author
		System.out.println("\nGET BOOKS BY AUTHOR");
		System.out.println(bookCatalog.getBookByAuthor("Leo Tolstoy"));
		System.out.println(bookCatalog.getBookByAuthor("Hermann Hesse"));

		//get total word count
		System.out.println("\nTOTAL WORD COUNTS");
		System.out.println(bookCatalog.getBookByTitle("War and Peace").getTotalWordCount());
		System.out.println(bookCatalog.getBookByTitle("Siddhartha").getTotalWordCount());

		//get unique word count
		System.out.println("\nUNIQUE WORD COUNTS");
		System.out.println(bookCatalog.getBookByTitle("War and Peace").getUniqueWordCount());
		System.out.println(bookCatalog.getBookByTitle("Siddhartha").getUniqueWordCount());

		//get word count for specific word
		System.out.println("\nWORD COUNT FOR SPECIFIC WORDS");
		System.out.println("'love' in War and Peace: " 
				+ bookCatalog.getBookByTitle("War and Peace").getSpecificWordCount("love"));
		System.out.println("'hate' in Siddhartha: " 
				+ bookCatalog.getBookByTitle("Siddhartha").getSpecificWordCount("hate"));

		/*
		 * EXTRA CREDIT BELOW!
		 */

		//get first lines
		//System.out.println("\nFIRST LINES");
		//for (String line : bookCatalog.getBookByAuthor("Leo Tolstoy").getFirstLines()) {
		//	System.out.println(line);
		//}
		//get first 5 lines
		//for (String line : bookCatalog.getBookByAuthor("Hermann Hesse").getFirstLines(5)) {
		//	System.out.println(line);
		//}		
	}
}
