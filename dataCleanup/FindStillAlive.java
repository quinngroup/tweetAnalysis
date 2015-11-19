/*
@author ranjanmanish
this java source code takes a list of user screen names and validate if user
still exhist in twitter db and creates a seperate set for those
*/
import java.net.URL;
import java.io.*;
import java.util.*;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import javax.net.ssl.HttpsURLConnection;


class FindStillAlive{
  public static void main(String[] args) throws Exception {
    final String dir = System.getProperty("user.dir");
    System.out.println("current dir = " + dir);
    String fileName = "/home/manish/fall2015/RA/DrunkTweetAnalysis/uniqSet100.txt";
    String URL = "https://twitter.com/users/username_available?username="

    try{

          //Create object of FileReader
          FileReader inputFile = new FileReader(fileName);

          //Instantiate the BufferedReader Class
          BufferedReader bufferReader = new BufferedReader(inputFile);

          //Variable to hold the one line data
          String line;
		
	  HttpURLConnectionExample http = new HttpURLConnectionExample();
	  
	   
          // Read file line by line and print on the console
          while ((line = bufferReader.readLine()) != null)   {
            //System.out.println(line);
            System.out.println(line);
	    reqUrl = URL + line
	   
          }
          //Close the buffer reader
          bufferReader.close();
       }catch(Exception e){
          System.out.println("Error while reading file line by line:" + e.getMessage());
       }
  }
}
