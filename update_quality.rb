require 'award'

def update_quality(awards)
  awards.each do |award|
    case award.name
    when 'Blue First' 
      update_blue_first_award!(award)
    when 'Blue Distinction Plus'
      update_blue_distinction_plus!(award)
    when 'Blue Compare'
      update_blue_compare!(award)
    when 'Blue Star'
      update_blue_star!(award)
    else 
      update_normal_award!(award)
    end
  end
end

def update_blue_distinction_plus!(award)
  # blue distinction plus awards are not modified
end

def update_blue_star!(award)
  award.expires_in -= 1

  if award.expires_in > 0    
    award.quality = [0, award.quality - 2].max
  else
    award.quality = [0, award.quality - 4].max
  end
end

def update_normal_award!(award)
  award.expires_in -= 1 

  if award.expires_in > 0
    award.quality = [0, award.quality - 1].max
  else
    award.quality = [0, award.quality - 2].max
  end
end

def update_blue_first_award!(award)
  award.expires_in -= 1 

  if award.expires_in > 0
    award.quality = [50, award.quality + 1].min
  else
    award.quality = [50, award.quality + 2].min
  end
end

def update_blue_compare!(award)
  award.expires_in -= 1 

  if award.expires_in < 0
    award.quality = 0
  elsif award.expires_in < 5
    award.quality = [50, award.quality + 3].min
  elsif award.expires_in < 10
    award.quality = [50, award.quality + 2].min
  else
    award.quality = [50, award.quality + 1].min
  end
end