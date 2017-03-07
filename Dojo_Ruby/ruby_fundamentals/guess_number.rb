def guess_number guess
    number = 25
    if guess == 25
        return "You got it right!"
    elsif guess > number
        return "Too high"
    else
        return "Too low"
    end
end

puts guess_number 25
