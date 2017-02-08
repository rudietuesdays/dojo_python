# stars part i
def draw_stars(list):
    for num in list:
        stars = ''
        for i in range (0, num):
            stars += '*'
        print stars
x = [4, 6, 1, 3, 5, 7, 25]
y = [1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9]
# draw_stars(y)

# part ii
def draw_obj(list):
    for obj in list:
        i = 0
        if (type(obj) == int):
            stars = ''
            for i in range (0, obj):
                stars += '*'
            print stars
        elif (type(obj) == str):
            string = ''
            for i in range (0, len(obj)):
                string += obj[0].lower()
            print string
        i += 1

z = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
a = [1,2,3,"HELLO","Meeeeeeee","You",10]

draw_obj(a)
