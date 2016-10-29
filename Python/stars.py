x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars():
    for i in range(len(x)):
        x[i] *= "*"
        print x[i]

draw_stars()


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars2(arr):
    for i in arr:
        if type(i) is int:
            i = i * "*"
            print i
        elif type(i) is str:
            first = i[0].lower()
            print (first * len(i))

draw_stars2(x)
