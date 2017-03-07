a = (3..20)
b = [1,5,2,7,4,9,3]

puts "The class of a is #{a.class}"
puts "The class of b is #{b.class}"

puts a.include?(10)
puts a.include?(1)

puts "The last number in the range is " + a.last.to_s
puts "The last number in the array is " + b.last.to_s

puts b.max
puts b.min
