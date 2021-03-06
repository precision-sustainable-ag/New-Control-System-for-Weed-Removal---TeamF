clc
clear all
%close all

rng('shuffle')

M = 500;
N = 200;
Rmax = 2;%maximum red weeds
Bmax = 3;%maximum blue weeds
Rdensity = 90;
Bdensity = 260;

R = randi(Rdensity+Rmax,1,M)-Rdensity; 
B = randi(Bdensity+Bmax,1,M)-Bdensity;

for m = 1:M
        if R(m) < 0
            R(m) = 0;
        end
        if B(m) < 0
            B(m) = 0;
        end
end

mat = ones(M,N);

%RED WEEDS
for m = 1:M
    p = randperm(N,R(m));
    mat(m:m+4,p:p+4) = 3;
end

%BLUE WEEDS
for m = 1:M
    p = randperm(N,B(m));
    mat(m:m+4,p:p+4) = 4;
end

%CROP
for n = 50:100:N
    for m = 20:40:M
        mat(m:m+10,n:n+10) = 2;
    end
end
        
cmap = zeros(4,3);
cmap(1,:) = [42 24 8]/100;
cmap(2,:) = [0 100 0]/100;
cmap(3,:) = [100 0 0]/100;
cmap(4,:) = [0 0 100]/100;

mat2 = repelem(mat,2,2);
imshow(mat2, cmap)



% for n = 1:N
%     
%     while sum(mat(:,n)) < C
%         for ni = (n+1):N
%             if sum(mat(:,ni)) > C
%                 x = find(mat(:,ni));
%                 while 1
%                     xi = randperm(length(x), 1);
%                     if mat(x(xi),n) == 0
%                         mat(x(xi),n) = 1;
%                         mat(x(xi),ni) = 0;
%                         break
%                     end
%                 end
%                 break
%             end
%         end
%     end
%    
%     
%     while sum(mat(:,n)) > C
%         x = find(mat(:,n));
%         for ni = (n+1):N
%             if sum(mat(:,ni)) < C
%                 while 1
%                     xi = randperm(length(x), 1);
%                     if mat(x(xi),ni) == 0
%                         mat(x(xi),ni) = 1;
%                         mat(x(xi),n) = 0;
%                         break
%                     end
%                 end
%                 break
%             end
%         end
%     end
% end



