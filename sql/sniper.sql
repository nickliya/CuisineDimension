SELECT case when sum(SY)=1 then "50-299" when sum(SY)=2 then "300-599" else "600+" end SY,
       case when sum(ML)=1 then "50-299" when sum(ML)=2 then "300-599" else "600+" end ML,
       case when sum(SC)=1 then "50-299" when sum(SC)=2 then "300-599" else "600+" end SC,
       type1,   type2,   type3,   type4,   type5,   type6
  FROM build group by 
         type1,   type2,   type3,   type4,   type5,   type6  having count(id)=1;