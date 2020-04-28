print("Developed by Cameron Industries, All Rights Reserved. ")
print("Do not distribute without written permission from Cameron Industries.")
mode_select = input("Press P for Pool Volume, Press C for Soda Can Day, Press S for Softballs in the Gym Day")
mode_select = mode_select.upper()
if mode_select == "P":
    pool_length = float(input("Pool Length"))
    pool_width = float(input("Pool Width"))
    pool_depth = float(input("Pool Depth"))
    stairs_width = float(input("Stairs Width"))
    stairs_length = float(input("Stairs Length"))
    stairs_depth = float(input("Stairs Depth at Highest Stair"))
    stairs_amount = float(input("Number of Stairs"))
    main_pool_volume = pool_length * pool_width * pool_depth
    stair_volume = stairs_width * stairs_depth * stairs_length
    stairs_volume = stair_volume * stairs_amount
    total_volume = main_pool_volume + stairs_volume
    print(total_volume)
