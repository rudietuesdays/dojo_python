# #create array
# arr = [3,5,1,2,7,9,8,13,25,32]
# #print sum
# puts arr.reduce(:+)
# # return array of nums greater than 10
# puts arr.reject {|i| i < 10}

# # create array, shuffle, print names
# arr = ["John", "KB", "Oliver", "Cory", "Matthew", "Christopher"]
# puts arr.shuffle
# # return array with names longer than 5 characters
# puts arr.select {|i| i.length > 5 }

# # create array with whole alphabet
# # shuffle array, display last letter
# alphabet = ("a".."z").to_a.shuffle
# puts alphabet.last
# # display first letter of array -- if vowel, display a message
# puts "#{alphabet.first} is a vowel" if ["a","e","i","o","u"].include? alphabet.first

# # generate array with 10 random nums from 55-100
# # have it be sorted so the smallest number is in the beginning
# arr = 10.times.map { rand(55..100) } .sort
# # display the max and min values in the array
# puts arr.max
# puts arr.min

# create random string that is 5 characters long
str = ""
5.times { str << rand(65..90).chr }
puts str
# generate array with 10 random strings, each 5 characters long
10.times do
    str = ""
    5.times { str << rand(65..90).chr }
    puts str
end
