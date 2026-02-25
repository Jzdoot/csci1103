def driving_cost(mpg, dpg, miles):
    return (miles / mpg) * dpg

if __name__ == "__main__":
    milesPerGallon = float(input())
    dollarsPerGallon = float(input())
    # output for 10 miles
    print(f"{driving_cost(milesPerGallon, dollarsPerGallon, 10):.2f}")
    # output for 50 miles
    print(f"{driving_cost(milesPerGallon, dollarsPerGallon, 50):.2f}")
    # output for 400 miles
    print(f"{driving_cost(milesPerGallon, dollarsPerGallon, 400):.2f}")
