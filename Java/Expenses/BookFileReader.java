package book.file;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Manages the loading of book files.
 * @author lbrandon
 *
 */
public class BookFileReader {

	/**
	 * Loads the given filename and adds each line to a list.
	 * Ignores lines with only whitespace.
	 * @param fileName to load
	 * @return list of lines from the file
	 */
	public static List<String> parseFile(String fileName) {
		// TODO Implement method
		// Hint: Load and read each line in the file.
		// If a line is made up entirely of whitespace, ignore it.

		File file = new File(fileName);
		List<String> lines = new ArrayList<String>();
		FileReader fileReader = null;
		BufferedReader bufferedReader = null;

		try {
			fileReader = new FileReader(file);
			bufferedReader = new BufferedReader(fileReader);

			String line = "";

			while ((line = bufferedReader.readLine()) != null) {
				line = line.strip();
				if (!line.isEmpty()) {
					lines.add(line);
				}
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		finally {
			try {
				fileReader.close();
				bufferedReader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		return lines;
	}
}