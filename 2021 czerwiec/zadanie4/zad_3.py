file = open("napisy.txt","r")
data = []
for l in file:
    data.append(list(l.strip()))

napis = ""
# data = []
# data.append( list("HTGKNDXJDKYTKATELARSYMKELFLEKMYSRALETAKTYKDJXDNKGT"))

for indexzestaw, zestaw in enumerate(data):
    czygitzestaw1 = True
    czygitzestaw2 = True
    for index in range(0,25):
        if(data[indexzestaw][index] != data[indexzestaw][48-index]):
            czygitzestaw1=False

        if(data[indexzestaw][index+1] != data[indexzestaw][50-(index+1)]):
            czygitzestaw2=False




    if (czygitzestaw1):
        napis += data[indexzestaw][24]

    if(czygitzestaw2):
        napis += data[indexzestaw][25]


    if(czygitzestaw1):
        print("1")
    if(czygitzestaw2):
        print("2")
print(napis)