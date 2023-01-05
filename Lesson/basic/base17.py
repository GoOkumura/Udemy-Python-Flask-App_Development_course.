# all any

if all((True, 10 < 20, True)): # allは全てTrue
    print("allの中の処理")

if any((10 < 20, 10 < 5, "a" == "b")): # anyは１つでもTrue
    print("anyの中の処理")