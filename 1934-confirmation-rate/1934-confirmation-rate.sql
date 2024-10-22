# Write your MySQL query statement below
SELECT s.user_id, case 
when s.user_id not in (select user_id from Confirmations) then 0.00
else round(
    (SELECT COUNT(*) FROM Confirmations c WHERE c.user_id = s.user_id AND c.action = 'confirmed') /(SELECT COUNT(*) FROM Confirmations c WHERE c.user_id = s.user_id), 2)
end AS confirmation_rate FROM Signups s;