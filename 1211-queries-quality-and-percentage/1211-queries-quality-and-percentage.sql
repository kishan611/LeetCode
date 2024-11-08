# Write your MySQL query statement below
select q.query_name,round(AVG(q.rating/q.position),2) as quality, round(((select count(*) from queries where query_name=q.query_name and rating<3)/(select count(*) from queries where query_name=q.query_name)*100),2) as poor_query_percentage from queries q where q.query_name is not null group by q.query_name;