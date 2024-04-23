# Write your MySQL query statement below
select weather.id from weather join weather w where 
datediff(weather.recordDate,w.recordDate)=1 and weather.temperature>w.temperature;