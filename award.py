class Award(object):
    def __init__(self, name=None, expires_in=None, quality=None):
        self.name = name
        self.expires_in = expires_in
        self.quality = quality

    def update_award(self):
        if self.name == 'Blue First':
            self.update_blue_first_award()
        elif self.name == 'Blue Distinction Plus':
            self.update_blue_distinction_plus_award()
        elif self.name == 'Blue Compare':
            self.update_blue_compare_award()
        elif self.name == 'Blue Star':
            self.update_blue_star_award()
        else:
            self.update_normal_award()

    def update_blue_star_award(self):
        self.expires_in -= 1

        if self.expires_in > 0    :
            self.quality = max(0, self.quality - 2)
        else:
            self.quality = max(0, self.quality - 4)

    def update_blue_compare_award(self):
        self.expires_in -= 1 

        if self.expires_in < 0:
            self.quality = 0
        elif self.expires_in < 5:
            self.quality = min(50, self.quality + 3)
        elif self.expires_in < 10:
            self.quality = min(50, self.quality + 2)
        else:
            self.quality = min(50, self.quality + 1)

    def update_blue_distinction_plus_award(self):
        # blue distinction plus awards are not modified
        pass

    def update_blue_first_award(self):
        self.expires_in -= 1

        if self.expires_in > 0:
            self.quality = min(50, self.quality + 1)
        else:
            self.quality = min(50, self.quality + 2)

    def update_normal_award(self):
        self.expires_in -= 1

        if self.expires_in > 0:
            self.quality = max(0, self.quality - 1)
        else:
            self.quality = max(0, self.quality - 2)



