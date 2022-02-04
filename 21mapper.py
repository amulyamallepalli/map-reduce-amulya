#Mallepalli mapper using standard input output
import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 13) : 
    app,category,rating,reviews,size,installs,typeOf,price,contentRating,genres,lastUpdated,currentVer,androidVer = datalist

    # print intermediate key-value pairs to standard output
    print(genres,"\t",installs)