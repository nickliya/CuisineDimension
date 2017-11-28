select 
食油,魔力,食材,replace(主食,'0/0/0/0/0/0/0','') '主食',replace(主菜,'0/0/0/0/0/0/0','') '主菜',replace(副菜,'0/0/0/0/0/0/0','') '副菜',replace(甜点,'0/0/0/0/0/0/0','') '甜点' ,replace(头盘,'0/0/0/0/0/0/0','') '头盘',replace(汤饮,'0/0/0/0/0/0/0','') '汤饮'
from (select case when b0.level1 = 1 then '50-299' when b0.level1 =2 then '300-599' else '600+' end '食油',
case when b0.level2 = 1 then '50-299' when b0.level2 =2 then '300-599' else '600+' end '魔力',
case when b0.level3 = 1 then '50-299' when b0.level3 =2 then '300-599' else '600+' end '食材',
b0.weight1||'/'||b1.weight1||'/'||b2.weight1||'/'||b3.weight1||'/'||b4.weight1||'/'||b5.weight1||'/'||b6.weight1 '主食',
b0.weight2||'/'||b1.weight2||'/'||b2.weight2||'/'||b3.weight2||'/'||b4.weight2||'/'||b5.weight2||'/'||b6.weight2 '主菜',
b0.weight3||'/'||b1.weight3||'/'||b2.weight3||'/'||b3.weight3||'/'||b4.weight3||'/'||b5.weight3||'/'||b6.weight3 '副菜',
b0.weight4||'/'||b1.weight4||'/'||b2.weight4||'/'||b3.weight4||'/'||b4.weight4||'/'||b5.weight4||'/'||b6.weight4 '甜点' ,
b0.weight5||'/'||b1.weight5||'/'||b2.weight5||'/'||b3.weight5||'/'||b4.weight5||'/'||b5.weight5||'/'||b6.weight5 '头盘',
b0.weight6||'/'||b1.weight6||'/'||b2.weight6||'/'||b3.weight6||'/'||b4.weight6||'/'||b5.weight6||'/'||b6.weight6 '汤饮'

from
(select t.* from build_pro t where t.no =0) b0,
(select t.* from build_pro t where t.no =1) b1,
(select t.* from build_pro t where t.no =2) b2,
(select t.* from build_pro t where t.no =3) b3,
(select t.* from build_pro t where t.no =4) b4,
(select t.* from build_pro t where t.no =5) b5,
(select t.* from build_pro t where t.no =6) b6
where 1=1
and b0.id = b1.id 
and b0.id = b2.id 
and b0.id = b3.id 
and b0.id = b4.id 
and b0.id = b5.id 
and b0.id = b6.id ) t