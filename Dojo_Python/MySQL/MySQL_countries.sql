-- 1
SELECT name, language, percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY languages.percentage desc;

-- 2
SELECT countries.name, COUNT(cities.id) as cities_num
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY cities_num desc;

-- 3
SELECT cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id 
WHERE countries.name = 'Mexico' and cities.population > 500000
ORDER BY cities.population DESC;

-- 4
SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages on countries.id = languages.country_id
WHERE languages.percentage >= 89
GROUP BY languages.percentage desc;

-- 5
SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 and population > 100000;

-- 6
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;

-- 7
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities on countries.id = cities.country_id
WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;

-- 8
SELECT region, COUNT(*) as countries
FROM countries
GROUP BY region desc;


