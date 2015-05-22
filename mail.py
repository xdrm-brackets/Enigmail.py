# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendMail(pFrom, pPass, pTo, pSubject, pMessage):
	pMsg = MIMEMultipart();
	pMsg['From'] = pFrom;
	pMsg['To'] = pTo;
	pMsg['Subject'] = pSubject;

	pMsg.attach( MIMEText(pMessage.encode('utf-8')) );

	srv = smtplib.SMTP('smtp.gmail.com', 587);
	srv.ehlo();
	srv.starttls();
	srv.ehlo();
	srv.login(pFrom, pPass);

	srv.sendmail( pFrom, pTo, pMsg.as_string() );
	srv.quit();

	print "[*] Mail envoye !";