#import all content in File.py
import File
print File.filePath #variable in the py is also imported
File.readSampleFile()


#import only one function
from File import readSampleFile
#File.filePath won't be available here
readSampleFile()


