class House(object):
    def __init__(self,position):
        self.position = position
        self.color = ["blue","green","red","white","yellow"]
        self.nat = ["american","austr","brit","irish","can"]
        self.job = ["carpenter","lawyer","pilot","plumber","waiter"]
        self.pet = ["cat","doggo","goldfish","hamster","horse"]
        self.hobby = ["chess","fishing","football","sailing","tennis"]

def test():
    for instance in houselist:
        if not "green" in instance.color:
            instance.nat = [x for x in instance.nat if x != "irish"]
        if not "irish" in instance.nat:
            instance.color = [x for x in instance.color if x != "green"]

        if "red" in instance.color:
            if instance.position < len(houselist) - 1:
                if not "white" in houselist[instance.position].color:
                    instance.color = [x for x in instance.color if x != "red"]
            else:
                instance.color = [x for x in instance.color if x != "red"]

        if "white" in instance.color:
            if instance.position == 0:
                instance.color = [x for x in instance.color if x != "white"]

        if "horse" in instance.pet:
            if instance.position >= 0 and if instance.position < len(houselist) -1:
                if not in




        if not ("red" in instance.color and "pilot" in instance.job):
            instance.job = [x for x in instance.job if x != "pilot"]
            instance.color = [x for x in instance.color if x != "red"]

        if not ("american" in instance.nat and "chess" in instance.hobby ):
            instance.hobby = [x for x in instance.hobby if x != "chess"]
            instance.nat = [x for x in instance.nat if x != "american"]

        if not ("can" in instance.nat and "waiter" in instance.job ):
            instance.job = [x for x in instance.job if x != "waiter"]
            instance.nat = [x for x in instance.nat if x != "can"]

        if not ("goldfish" in instance.pet and "football" in instance.hobby ):
            instance.hobby = [x for x in instance.hobby if x != "football"]
            instance.pet = [x for x in instance.pet if x != "goldfish"]

        if not ("blue" in instance.color and "cat" in instance.pet ):
            instance.pet = [x for x in instance.pet if x != "cat"]
            instance.color = [x for x in instance.color if x != "blue"]

        if not ("brit" in instance.nat and "hamster" in instance.pet):
            instance.pet = [x for x in instance.pet if x != "hamster"]
            instance.nat = [x for x in instance.nat if x != "brit"]

        if not ("doggo" in instance.pet and "carpenter" in instance.job):
            instance.pet = [x for x in instance.pet if x != "doggo"]
            instance.job = [x for x in instance.job if x != "carpenter"]


if __name__ == "__main__" :
    houselist = []
    for count in range(0,5):
        x = House(count)
        houselist.append(x)

    houselist[0].nat = ["austr"]
    houselist[3].job = ["lawyer"]

    test()
    for instance in houselist:
        print(vars(instance))
