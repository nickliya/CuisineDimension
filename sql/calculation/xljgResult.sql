select
REFINE_GJ,REFINE_BJ,REFINE_BS,substr("  "||zz_bj,-3),szgj,
szgj*((zz_bs*zz_bj)+(100-zz_bj)*100)*skill/1000000
,szgj*zz_bs*skill/10000
from (select REFINE_GJ,REFINE_BJ,REFINE_BS,skill,bs,
REFINE_GJ*20+100+gj zz_gj,min(REFINE_BJ*180+SL_BJ,1000)/10 zz_bj,(REFINE_BS*500+bs+SL_BS)/10 zz_bs
,(REFINE_GJ*20+100)*MAX_GJ/100 szgj
from (select * from equip_refine r where refine_hp = %s) ,
(select %s SL_BJ, %s SL_BS, %s MAX_GJ, %s skill, 0 bs, 0 gj))