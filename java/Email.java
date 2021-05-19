
public class Email {

	private String fromEmail;
	private String fromJobtitle;
	private String toEmail;
	private String toJobtitle;	
	private String sentiment;		
	
	private String nodeEmail;
	private String nodeJobtitle;	
	
	public Email() {
		
	}

	public Email(String fromEmail, String fromJobtitle, String toEmail, String toJobtitle, String sentiment) {
		super();
		this.fromEmail = fromEmail;
		this.fromJobtitle = fromJobtitle;
		this.toEmail = toEmail;
		this.toJobtitle = toJobtitle;
		this.sentiment = sentiment;
	}

	public String getFromEmail() {
		return fromEmail;
	}

	public void setFromEmail(String fromEmail) {
		this.fromEmail = fromEmail;
	}

	public String getFromJobtitle() {
		return fromJobtitle;
	}

	public void setFromJobtitle(String fromJobtitle) {
		this.fromJobtitle = fromJobtitle;
	}

	public String getToEmail() {
		return toEmail;
	}

	public void setToEmail(String toEmail) {
		this.toEmail = toEmail;
	}

	public String getToJobtitle() {
		return toJobtitle;
	}

	public void setToJobtitle(String toJobtitle) {
		this.toJobtitle = toJobtitle;
	}

	public String getSentiment() {
		return sentiment;
	}

	public void setSentiment(String sentiment) {
		this.sentiment = sentiment;
	}

	
	public String getNodeEmail() {
		return nodeEmail;
	}

	public void setNodeEmail(String nodeEmail) {
		this.nodeEmail = nodeEmail;
	}

	public String getNodeJobtitle() {
		return nodeJobtitle;
	}

	public void setNodeJobtitle(String nodeJobtitle) {
		this.nodeJobtitle = nodeJobtitle;
	}

	@Override
	public String toString() {
		return "Email [fromEmail=" + fromEmail + ", fromJobtitle=" + fromJobtitle + ", toEmail=" + toEmail
				+ ", toJobtitle=" + toJobtitle + ", sentiment=" + sentiment + "]";
	}
}
