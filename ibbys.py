import smtplib
import datetime
day = datetime.date.today().strftime("%A")
server = smtplib.SMTP_SSL('smtp.gmail.com:465')

server.login("ibbysreminder@gmail.com","IbbysReminderPassword")

from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText

msg=MIMEMultipart()
fromaddr = "ibbysreminder@gmail.com"
toaddr = "tejas.shekhar@wustl.edu"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject']="Ibby's Menu"

if day == "Sunday":
	day = 0
elif day == "Monday":
	day = 1
elif day == "Tuesday":
	day = 2
elif day == "Wednesday":
	day = 3
elif day == "Thursday":
	day = 4
elif day == "Friday":
	day = 5
elif day == "Saturday":
	day = 6
else:
	raise Exception("Something has gone terribly wrong!")
	
month = datetime.date.today().strftime("%B")
daynum = int(datetime.date.today().strftime("%d"))
dayfin = daynum-day

html = """\
<html>
	<head></head>
	<body>
		<h4>For the Week of %s %d - %d </h4>
			<p>
				<a href="http://diningservices.wustl.edu/ibbys/menu/lunch/">This Week\'s Menu</a>
			</p>
	</body>
</html>
""" % (month,dayfin,dayfin+6)

msg.attach(MIMEText(html,'html'))
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
