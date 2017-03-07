# $i = 0
# $num = 5
# begin
#     puts "inside the loop i = #{$i}"
#     $i += 1
#     # puts "$i is now 3" if $i == 3
#     puts "$i is not 3" unless $i == 3
# end while $i < $num

for i in 0..5
    puts "the value of the local varuable is #{i}"
    puts "i is now 3" if i == 3
end


# a = ["priscilla", "olu", "dojo", "rae", "jake", "nishant"]
# b = [5, 3, 9, 1, 2, 6]
# c = ["dojo", 9]
# d = %w{matz guido choi dojo john}
#
# x = (a+b)-c

# puts x.to_s

# puts a.shuffle.join(', ')

# a.delete "olu"
# puts a
#
# puts "Length of a is #{a.length}"
#
# puts d
