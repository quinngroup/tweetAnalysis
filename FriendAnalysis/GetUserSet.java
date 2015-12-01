import java.io.BufferedReader;
import java.io.FileReader;


public class GetUserSet {
public static void main(String[] args) {
	String fileName = "/home/manish/ResearchWork/RA/Tweet_Friends/Friends/resultOutputImportedFromAws/experiment.txt";
	try{
		
		//Create object of FileReader
		FileReader inputFile = new FileReader(fileName);

		//Instantiate the BufferedReader Class
		BufferedReader bufferReader = new BufferedReader(inputFile);

		//Variable to hold the one line data
		String line;
		
		// Read file line by line and print on the console
		while ((line = bufferReader.readLine()) != null)   {
			//System.out.println(line);
			// Data format 1100          SimonGire
                        if(!line.startsWith("$#$"))
			    System.out.println(line.trim());
                        else{
                            line = line.substring(3, line.length());
			    System.out.println(line.trim());
                        }
		}
		bufferReader.close();
	}
	catch(Exception e){
		System.out.println("Error while reading file line by line:" + e.getMessage());
	}
}
}
