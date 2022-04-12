# extracts 10 colors from our beautiful image below, created an rbg tuple for
# each of our colors, and adds them to "tupled_list"
import colorgram

colors = colorgram.extract('7external-content.duckduckgo.com.jpg', 10)

main_list=[]

for each in colors:
    X= each.rgb
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    temp_list = [x1, x2, x3]
    main_list.append(temp_list)

tupled_list= [tuple(each) for each in main_list]
