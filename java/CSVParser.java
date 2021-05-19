import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class CSVParser {

	ArrayList<Email> linkList = new ArrayList<Email>();

	ArrayList<Email> nodeList = new ArrayList<Email>();

	public CSVParser() {

		String csvFileName = "enron-v1.csv";
		readCVSFile(csvFileName);

		String jsonFileName = "test.json";
		writeJsonFile(jsonFileName);
	}

	public void readCVSFile(String fileName) {

		BufferedReader reader;
		try {
			reader = new BufferedReader(new FileReader(fileName));
			String line = reader.readLine();

			int fistLine = 0;

			while (line != null) {

				if (fistLine == 0) {
					fistLine = 1;
				} else {
					String tokenArray[] = line.split(",");
					Email email = new Email(tokenArray[2], tokenArray[3], tokenArray[5], tokenArray[6], tokenArray[8]);

					addLink(email);
					addNode(tokenArray[2], tokenArray[3]);
					addNode(tokenArray[5], tokenArray[6]);					
				}

				line = reader.readLine();
			}
			reader.close();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void addNode(String emailStr, String jobTitle) {

		boolean exists = false;

		for (int i = 0; i < nodeList.size(); i++) {

			Email tempEmail = nodeList.get(i);

			if (tempEmail.getNodeEmail().equals(emailStr)
					&& tempEmail.getNodeJobtitle().equals(jobTitle)) {
				exists = true;
				break;
			}
		}

		if (!exists) {
			Email email = new Email();
			email.setNodeEmail(emailStr);
			email.setNodeJobtitle(jobTitle);
			nodeList.add(email);
		}
	}	
	
	public void addNodeFrom(Email email) {

		boolean exists = false;

		for (int i = 0; i < nodeList.size(); i++) {

			Email tempEmail = nodeList.get(i);

			if (tempEmail.getNodeEmail().equals(email.getFromEmail())
					&& tempEmail.getNodeJobtitle().equals(email.getFromJobtitle())) {
				exists = true;
				break;
			}
		}

		if (!exists) {
			email.setNodeEmail(email.getFromEmail());
			email.setNodeJobtitle(email.getFromJobtitle());
			nodeList.add(email);
		}
	}

	public void addNodeTo(Email email) {

		boolean exists = false;

		for (int i = 0; i < nodeList.size(); i++) {

			Email tempEmail = nodeList.get(i);

			if (tempEmail.getNodeEmail().equals(email.getToEmail())
					&& tempEmail.getNodeJobtitle().equals(email.getToJobtitle())) {
				exists = true;
				break;
			}
		}

		if (!exists) {
			email.setNodeEmail(email.getToEmail());
			email.setNodeJobtitle(email.getToJobtitle());			
			nodeList.add(email);
		}
	}	
	
	public void addLink(Email email) {

		boolean exists = false;

		for (int i = 0; i < linkList.size(); i++) {

			Email tempEmail = linkList.get(i);

			if (tempEmail.getFromEmail().equals(email.getFromEmail())
					&& tempEmail.getToEmail().equals(email.getToEmail())
					&& tempEmail.getSentiment().equals(email.getSentiment())) {
				exists = true;
				break;
			}
		}

		if (!exists) {
			linkList.add(email);
		}
	}

	public void writeJsonFile(String fileName) {
		try {

			BufferedWriter bw = new BufferedWriter(new FileWriter(new File(fileName), true));

			bw.write("{");
			bw.newLine();

			bw.write("\"nodes\": [");
			bw.newLine();

			for (int i = 0; i < nodeList.size(); i++) {
				Email tempNode = nodeList.get(i);

				bw.write("{\"id\": \"" + tempNode.getNodeEmail() + "\", \"group\": \""
						+ tempNode.getNodeJobtitle() + "\"}");

				if (i != nodeList.size() - 1) {
					bw.write(",");
				}
				bw.newLine();
			}

			bw.write("  ],");
			bw.newLine();

			bw.write("\"links\": [");
			bw.newLine();

			for (int i = 0; i < linkList.size(); i++) {
				Email tempNode = linkList.get(i);

				bw.write("{\"source\": \"" + tempNode.getFromEmail() + "\", \"target\": \"" + tempNode.getToEmail()
						+ "\", \"sentiment\": " + tempNode.getSentiment() + "}");

				if (i != linkList.size() - 1) {
					bw.write(",");
				}
				bw.newLine();
			}

			bw.write("  ]");
			bw.newLine();

			bw.write("}");
			bw.newLine();

			bw.close();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {

		new CSVParser();

	}
}
