Award = Struct.new(:name, :expires_in, :quality) do

    def update_award!
        case name
        when 'Blue First' 
            update_blue_first_award!
        when 'Blue Distinction Plus'
            update_blue_distinction_plus!
        when 'Blue Compare'
            update_blue_compare!
        when 'Blue Star'
            update_blue_star!
        else 
            update_normal_award!
        end
    end

    def update_blue_distinction_plus!
        # blue distinction plus awards are not modified
    end

    def update_blue_star!
        self.expires_in -= 1

        if expires_in > 0    
            self.quality = [0, quality - 2].max
        else
            self.quality = [0, quality - 4].max
        end
    end

    def update_normal_award!
        self.expires_in -= 1 

        if expires_in > 0
            self.quality = [0, quality - 1].max
        else
            self.quality = [0, quality - 2].max
        end
    end

    def update_blue_first_award!
        self.expires_in -= 1 

        if expires_in > 0
            self.quality = [50, quality + 1].min
        else
            self.quality = [50, quality + 2].min
        end
    end

    def update_blue_compare!
        self.expires_in -= 1 

        if expires_in < 0
            self.quality = 0
        elsif expires_in < 5
            self.quality = [50, quality + 3].min
        elsif expires_in < 10
            self.quality = [50, quality + 2].min
        else
            self.quality = [50, quality + 1].min
        end
    end

end