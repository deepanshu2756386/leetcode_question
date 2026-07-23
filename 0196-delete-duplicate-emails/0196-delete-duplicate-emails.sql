# Write your MySQL query statement below
delete p2  from person  p1
-- select p1.id ,p1.email, p2.email from person  p1  find the dublicate value  
join person p2 
on p1.email = p2.email 
where p1.id < p2.id ; 

