### print 1-255 ###
# for i in 1..255
#     puts i
# end
### OR ...
puts 1.upto(255) { |i| print i, "\n" }

### print odd nums 1-255 ###
puts (1..255).reject { |i| i % 2 == 0 }

### print sum ###
i = 1
sum = 0
while i < 256
    sum += i
    puts "new number: #{i}; sum: #{sum}"
    i += 1
end

### iterate array ###
# arr = [1,3,5,7,9,13]
# arr.each do |i|
#     puts i
# end
### OR....
# puts arr = %w(1,3,5,7,9,13)

### find max ###
# def find_max(arr)
#     puts "The maximum number is #{arr.max}"
# end
#
# find_max([-1,5,21,0,0,0,-24])

### get average ###
# def average(arr)
#     sum = 0
#     arr.each do |i|
#         sum += i
#     end
#     average = sum / arr.length
#     return average
# end
#
# puts average([2,10,3])

### array with odd nums ###
# y = Array.new
# for i in 1..255
#     unless i%2 == 0
#         y.push(i)
#     end
# end
# puts y

### greater than y ###
# def greater_than(y, arr)
#     count = 0
#     for i in 0...arr.length
#         unless arr[i] < y
#             count += 1
#         end
#     end
#     return count
# end
#
# puts greater_than(3, [1, 3, 5, 7])

### square vals ###
# x =  [1, 5, 10, -2]
# puts x.collect { |i| i*i }

### eliminate negative nums ###
# x =  [1, -5, 5, 10, -2, -3]
# puts x.map {|i| i<0 ? 0:i }

### max, min, avg ###
# x =  [1, 5, 10, -2]
# def max_min_avg(arr)
#     max = arr.max
#     min = arr.min
#     sum = 0
#     arr.each do |i|
#         sum += i
#     end
#     avg = sum / arr.length
#     return Hash["max", max, "min", min, "avg", avg]
# end
#
# puts max_min_avg(x)

### shifting vals in arr ###
# x = [1, 5, 10, 7, -2]
# def shifting(arr)
#     arr.shift
#     arr.push(0)
#     return arr
# end
# puts shifting(x)

### num to str ###
# x = [-1, -3, 2]
# puts x.collect { |i| i < 0 ? "Dojo" : i }
