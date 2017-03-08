import re
PoeLogPath = "C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs\Client.txt"


class Functions:

    def GetLogLines():
        countln=0
        with open(PoeLogPath,'rb') as f:
            for line in f:
                countln+=1

        return countln

    def ReadScpecificLine(intLine):
        f = open(PoeLogPath,"r", encoding='UTF8')
        lines = f.readlines()
        gg = intLine
        return lines[gg+1]

    def SubmitRegex(Logstring):
        Logstring = re.sub('\n', '', Logstring)
        Logstring = re.sub(r'.*?@From', '@From', Logstring)
        return Logstring

    def msgTrimmer(Logstring):
        Logstring = re.sub('\n', '', Logstring)
        Logstring = re.sub(r'.*?@From ', '', Logstring)
        Logstring = re.sub(r': .*', '', Logstring)
        return Logstring

#        stringtoTrim = stringtoTrim.split(':', 1)[0]
#print(Functions.GetLogLines())
#print(Functions.ReadScpecificLine(Functions.GetLogLines()))
