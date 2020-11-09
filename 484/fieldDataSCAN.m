clc
clear all
%close all

rng('shuffle')

M = 600;
N = 400;
S = N/100;
S = N/S;
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

screen = zeros(M,N);
mat = ones(M,N);
matF = ones(M,N);

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
        
cmap = zeros(6,3);
%Color Selection:
cmap(1,:) = [42 24 8]/100; %Brown
cmap(2,:) = [0 100 0]/100; %Green
cmap(3,:) = [100 0 0]/100; %Red
cmap(4,:) = [0 0 100]/100; %Blue
cmap(5,:) = [100 100 100]/100; %White
cmap(6,:) = [0 0 0]/100; %Black

for m = 1:M
    for n = 1:N
        if (mat(m,n) < screen(m,n))
            matF(m,n) = screen(m,n);
        else
            matF(m,n) = mat(m,n);
        end
    end
end

mat2 = repelem(matF,2,2);
imshow(mat2, cmap)

j = 1;

%Scanning for the Weeds and Detecting as White Dots.
for k = 1:S:N-1
    if(j)
        for i = 1:S:M-1
            screen(i:i+S,k) = 6;
            screen(i:i+S,k+S) = 6;
            screen(i,k:k+S) = 6;
            screen(i+S,k:k+S) = 6;
            for v = k:k+S-1
                for u = i:i+S-1
                    if(mat(u,v) == 3 || mat(u,v) == 4)
                        mat(u:u+4,v:v+4) = 1;
                        for m = 1:M
                            for n = 1:N
                                if (mat(m,n) < screen(m,n))
                                    matF(m,n) = screen(m,n);
                                else
                                    matF(m,n) = mat(m,n);
                                end
                            end
                        end
                        mat2 = repelem(matF,2,2);
                        imshow(mat2, cmap)
                    end
                end
            end
            for m = 1:M
                for n = 1:N
                    if (mat(m,n) < screen(m,n))
                        matF(m,n) = screen(m,n);
                    else
                        matF(m,n) = mat(m,n);
                    end
                end
            end
            mat2 = repelem(matF,2,2);
            imshow(mat2, cmap)
            screen(i:i+S,k) = 1;
            screen(i:i+S,k+S) = 1;
            screen(i,k:k+S) = 1;
            screen(i+S,k:k+S) = 1;
%             if(matF(i,k) == 3 || matF(i,k) == 4)
%                 matF(i:i+4,k:k+4) = 5;
%                 mat2 = repelem(matF,2,2);
%                 imshow(mat2, cmap)
%             end
        end
        j = 0;
    else
        for i = M-S:-S:0
            if i == 0
                i = 1;
            end
            screen(i:i+S,k) = 6;
            screen(i:i+S,k+S) = 6;
            screen(i,k:k+S) = 6;
            screen(i+S,k:k+S) = 6;
            for v = k:k+S-1
                for u = i:i+S-1
                    if(mat(u,v) == 3 || mat(u,v) == 4)
                        mat(u:u+4,v:v+4) = 1;
                        for m = 1:M
                            for n = 1:N
                                if (mat(m,n) < screen(m,n))
                                    matF(m,n) = screen(m,n);
                                else
                                    matF(m,n) = mat(m,n);
                                end
                            end
                        end
                        mat2 = repelem(matF,2,2);
                        imshow(mat2, cmap)
                    end
                end
            end
            for m = 1:M
                for n = 1:N
                    if (mat(m,n) < screen(m,n))
                        matF(m,n) = screen(m,n);
                    else
                        matF(m,n) = mat(m,n);
                    end
                end
            end
            mat2 = repelem(matF,2,2);
            imshow(mat2, cmap)
            screen(i:i+S,k) = 1;
            screen(i:i+S,k+S) = 1;
            screen(i,k:k+S) = 1;
            screen(i+S,k:k+S) = 1;
%             if(matF(i,k) == 3 || matF(i,k) == 4)
%                 matF(i:i+4,k:k+4) = 5;
%                 mat2 = repelem(matF,2,2);
%                 imshow(mat2, cmap)
%             end
        end
        j = 1;
    end
%     while(k <= N)
%         if (matF(i,k) == 3 || matF(i,k) == 4)
%             matF(i:i+4,k:k+4) = 5;
%             mat2 = repelem(matF,2,2);
%             imshow(mat2, cmap)
%         end
%         k = k + 1;
%     end
end


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
