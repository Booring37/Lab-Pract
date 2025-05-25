range=5;
step=1;
t=-range:step:range;  
y=(size(t)); 

for i=1:length(t);
    if t(i)<=0;
        y(i)=0;
    else;
        y(i)=1;
    end;
end;

stem(t, y)
title('Unit Step Function')
xlabel('t')
ylabel('u(t)')

