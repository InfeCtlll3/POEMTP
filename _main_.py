from poegrep import Functions
from smtpMailer import SmtpFunc
import re
import os

mailFrom = "YOURGMAILHERE@gmail.com"
mailFromPass = "YOURPASSWORDHERE"
mailTo = "ADDRESSYOUWANTTORECEIVE@anymail.com"

oldLogEntry = Functions.GetLogLines()
msgArray = []
SendEmail = False
parseString = ''
antispam = []
os.system('cls' if os.name=='nt' else 'clear')
print("Welcome to POEMTP. Any bugs or suggestions e-mail them to: contato.carmando@gmail.com")
while 1==1:
    if (oldLogEntry != Functions.GetLogLines()):
        countr = 1
        lineToRead = (Functions.GetLogLines() - oldLogEntry)
        toRead = ''
        print("Old Log Lines: " + str(oldLogEntry))
        print("New Log Lines: " + str(Functions.GetLogLines()))
        print("Reading: " + str(lineToRead) + " line(s)")

        for i in range(lineToRead):
            print("Reading line: " + str(oldLogEntry+countr))
            try:
                    toRead = Functions.ReadScpecificLine(oldLogEntry+countr)
            except:
                    errorlevel = 1
            print("Reading: " + toRead)

            print(' ')
            print(Functions.msgTrimmer(toRead))

            if any(re.findall(r'@From', toRead, re.IGNORECASE))and any(re.findall(r'wtb|buy|Hi, I would like to buy', toRead, re.IGNORECASE)):
            
                SendEmail = True
                print("Found a Match!; " + toRead)
                msgArray.append(Functions.SubmitRegex(toRead))
                print("String: " + toRead + " has been appended to the array.")

            countr+=1
        oldLogEntry = Functions.GetLogLines()

    if (SendEmail):
        parseString = ''
        print("Sending E-mail... \n")
        SendEmail = False
        #oldLogEntry = Functions.GetLogLines()
        for j in msgArray:
            parseString = parseString+j+' \n'
        msgArray = []
        print("\n Sending : " + parseString)
        SmtpFunc.SmtpSend(mailFrom, mailTo, mailFromPass, parseString)
        SendEmail = False
        print("\n\n\n\n\n\n\n\n\n")
