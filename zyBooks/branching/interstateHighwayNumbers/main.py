highway = int(input())
direction = "east/west" if highway % 2 == 0 else "north/south"

if 1 <= highway <= 99:
    print(f"I-{highway} is primary, going {direction}.")
elif (100 < highway < 1000) and (highway % 100 != 0):
    print(f"I-{highway} is auxiliary, serving I-{highway%100}, "
          f"going {direction}.")
else:
    print(f"{highway} is not a valid interstate highway number.")
