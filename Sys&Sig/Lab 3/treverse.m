% time reverse x(t) -> x(-t)
function [x1,t1]=treverse(x,t)
t1 = fliplr(-t);
x1 = fliplr(x);
plot(t1,x1);
end