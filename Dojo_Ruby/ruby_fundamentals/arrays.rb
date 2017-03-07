
a = ["koala", "dog", "cat", "snake", "panda"]

# .at or .fetch
puts a.at 2
puts a.fetch 1

# .delete
puts a.delete "snake"
puts a

# .reverse
puts a.reverse

# .length
puts a.length

# .sort
puts a.sort

# .slice
puts a.slice 2...4

# .shuffle
puts a.shuffle

# .join
puts a.join('-')

# .insert
puts a.insert 2, "buffalo", "cow"

# .values_at
puts a.values_at 0..2, 4

b = %w{cat dog bear}; puts b.values_at(1,2).join(' and ') #=> "dog and bear"
