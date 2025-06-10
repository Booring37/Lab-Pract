n = -5 : 1 : 5;
x = zeros(size(n));
for i = 1 : length (n)
    if n(i)>=0
        x(i) = 1;
    end
end

stem(n,x)
xlabel('Number');
ylabel('X1');