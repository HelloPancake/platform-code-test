def update_quality(awards):
    for award in awards:
        if award.name == 'Blue First':
            update_blue_first_award(award)
        elif award.name == 'Blue Distinction Plus':
            update_blue_distinction_plus_award(award)
        elif award.name == 'Blue Compare':
            update_blue_compare_award(award)
        elif award.name == 'Blue Star':
            update_blue_star_award(award)
        else:
            update_normal_award(award)

def update_blue_star_award(award):
    award.expires_in -= 1

    if award.expires_in > 0    :
        award.quality = max(0, award.quality - 2)
    else:
        award.quality = max(0, award.quality - 4)

def update_blue_compare_award(award):
    award.expires_in -= 1 

    if award.expires_in < 0:
        award.quality = 0
    elif award.expires_in < 5:
        award.quality = min(50, award.quality + 3)
    elif award.expires_in < 10:
        award.quality = min(50, award.quality + 2)
    else:
        award.quality = min(50, award.quality + 1)

def update_blue_distinction_plus_award(award):
    # blue distinction plus awards are not modified
    pass

def update_blue_first_award(award):
    award.expires_in -= 1

    if award.expires_in > 0:
        award.quality = min(50, award.quality + 1)
    else:
        award.quality = min(50, award.quality + 2)

def update_normal_award(award):
    award.expires_in -= 1

    if award.expires_in > 0:
        award.quality = max(0, award.quality - 1)
    else:
        award.quality = max(0, award.quality - 2)


