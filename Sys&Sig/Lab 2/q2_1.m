t = -5 : 0.01 : 5;
x = zeros(size(t));
for i = 1 : length (t)
    if abs(t(i)) <= 1
        x(i) = 1;
    else
        x(i) = 0;
    end
end

plot(t,x)
