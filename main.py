#To get xml transcript of a youtube video:
#http://video.google.com/timedtext?lang=en&v=VIDEO_ID

import xml.etree.ElementTree as ET
tree = ET.parse('transcript.xml')
root = tree.getroot()
output = open("file.srt",'w')
cnt = 1

for x in root.iter('text'):
	temp = 0
	output.write("\n"+str(cnt)+"\n")
	start = float(x.get('start'))
	dur = float(x.get('dur'))
	
	temp = start
	hour = int(temp)//3600
	minute = int(temp)//60 - hour*60
	sec = int(temp) - minute*60
	mill = temp - int(temp)
	output.write(str('%0.2d'%hour)+":"+str(minute)+":"+str(sec)+","+str('%0.3d'%(mill*1000)))
	
	output.write(" --> ")
	
	start += dur
	temp = start
	hour = int(temp)//3600
	minute = int(temp)//60 - hour*60
	sec = int(temp) - minute*60
	mill = temp - int(temp)
	output.write(str('%0.2d'%hour)+":"+str(minute)+":"+str(sec)+","+str('%0.3d'%(mill*1000))+"\n")
	
	text = x.text
	output.write(text+"\n")
	
	cnt+=1
output.close()
