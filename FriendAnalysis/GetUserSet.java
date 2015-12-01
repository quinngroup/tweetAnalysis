import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Set;



public class GetUserSet {
	private static final String DELIMETER = ",";

	public static void main(String[] args) {
		Set<String> friendSet = new HashSet<String> ();
		String fileName = "/home/manish/ResearchWork/RA/Tweet_Friends/Friends/resultOutputImportedFromAws/experiment.txt";
		try{

			//Create object of FileReader
			FileReader inputFile = new FileReader(fileName);

			//Instantiate the BufferedReader Class
			BufferedReader bufferReader = new BufferedReader(inputFile);

			//Variable to hold the one line data
			String line;
			String[] friendArray;
			int counter =0;
			
			// Read file line by line and print on the console
			while ((line = bufferReader.readLine()) != null)   {
				//System.out.println(line);
				// Data format 1100          SimonGire
				if(!line.startsWith("$#$"))
					System.out.println(line.trim());
				else{
					line = line.substring(3, line.length());
					friendArray = line.trim().split(DELIMETER);
					for(String str: friendArray){
						counter++;
						friendSet.add(str);
					}
				}
			}
			for(String temp:friendSet){
				System.out.println(temp);
			}
			System.out.println("Actual"+counter);
			System.out.println("After Reduction"+friendSet.size());
			
			bufferReader.close();
		}
		catch(Exception e){
			System.out.println("Error while reading file line by line:" + e.getMessage());
		}
	}
}
