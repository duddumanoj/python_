#procedure to convert dictionary to csv file
import csv
col=["id","title","link","description","long_description","alt_titles","brand","tags","entities"]
#d=[ regular basis. Coliform in Ganga water at alarming levels Data collected by SMF’s Ganga Laboratory at Tulsi Ghat here has painted a gloomy picture of the Ganga’s health due to high bacterial pollution. Coliform organisms should be 50MPN (most probable number)/100ml or less in drinking water and 500MPN/100ml in outdoor bathing water, while BOD should be less than 3mg/l. According to SMF data, faecal coliform count rose from 4.5 lakh (upstream at Nagwa) and 5.2 crore (downstream in Varuna) in January 2016 to 3.8 crore (upstream) and 14.4 crore (downstream) in February 2019. “Similarly, BOD level has risen from 46.8-54mg/l to 66-78mg/l during January 2016-February 2019. Besides, the level of dissolved oxygen (DO), which should be 6mg/l or more, has gone down from 2.4mg/l to 1.4mg/l during this period. High presence of coliform bacteria in Ganga water is alarming for human health,” said SMF president and IIT-BHU professor V N Mishra, who is also the mahant of the famous Sankat Mochan temple. “Faecal coliform is present in the gut and faeces of warmblooded animals. Consequently, E coli is considered to be the species of coliform bacteria that is the best indicator of faecal pollution and possible presence of disease-causing pathogens,” said noted environmental scientist and former BHU professor B D Tripathi. A slight improvement was seen in tapping discharge of sewage into the Ganga during this period. 0Comments","brand":"ET","entities":["Prime Minister Narendra Modi","Ganga"]}]
d=[]
c="names.csv"

try:
    with open(c,'w')as cs:
        w=csv.DictWriter(cs,fieldnames=col)
        w.writeheader()
        for da in d:
            w.writerow(da)
except IOError:
    print("i/o error")
