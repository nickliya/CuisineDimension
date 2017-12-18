select
REFINE_GJ,REFINE_BJ,REFINE_BS,zz_bj,szgj,
((zz_bs*zz_bj)/100+(100-zz_bj))*szgj/100*skill/100
,szgj*zz_bs/100*skill/100
from (select REFINE_GJ,REFINE_BJ,REFINE_BS,skill,bs,
REFINE_GJ*20+100+gj zz_gj,min(REFINE_BJ*180+SL_BJ,1000)/10 zz_bj,(REFINE_BS*500+bs+SL_BS)/10 zz_bs
,(REFINE_GJ*20+100)*MAX_GJ/100 szgj
from equip_refine r,
(select 560 SL_BJ, 1940 SL_BS,574 MAX_GJ,270 skill, 0 bs, 0 gj))