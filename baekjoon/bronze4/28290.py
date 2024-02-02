di = {
    "fdsajkl;" : "in-out",
    "jkl;fdsa" : "in-out",
    "asdf;lkj" : "out-in",
    ";lkjasdf" : "out-in",
    "asdfjkl;" : "stairs",
    ";lkjfdsa" : "reverse",
}

# s = str(input())

# for i in di.keys():
#     if s == i:
#         print(di[i])
#     else:
#         print("molu")

s = input()

if s == "fdsajkl;" or s == "jkl;fdsa":
    print("in-out")
elif s == "asdf;lkj" or s == ";lkjasdf":
    print("out-in")
elif s == "asdfjkl;":
    print("stairs")
elif s == ";lkjfdsa":
    print("reverse")
else:
    print("molu")
