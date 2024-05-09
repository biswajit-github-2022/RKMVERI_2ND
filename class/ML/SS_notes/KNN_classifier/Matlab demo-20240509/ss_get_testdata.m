function [datapoints classlabels]=ss_get_testdata(X, y, N, xbounds, ybounds)
if( nargin < 3)
    N = 1;
end
if( nargin < 4)
    xbounds = [-50 50];
    ybounds = [-50 50];
end
title('Draw the test point');
classvals = [1 2 3 4 5 6 7];
hold on;
xlim(xbounds);
ylim(ybounds);
datapoints=[];
classlabels=[];
plotstr='rbygwmc';
ss_invertfig;
for i = 1:length(y)
    plot(X(i,1),X(i,2),[plotstr(y(i)),'*'],'MarkerSize',10);
end
for i = 1:N
    [x,y,but]=ginput(1);
    c=double(but)-double('0');
    if (ismember(c,classvals))
        classlabels(end+1)=c;
        datapoints(:,end+1)=[x;y];
        %             plot(x,y,[plotstr(c),'*'],'MarkerSize',10);
        plot(x, y, 'x', ...
            'MarkerEdgeColor',plotstr(c), ...
            'MarkerSize', 10, 'LineWidth', 3);
    end
end
classlabels = classlabels';
datapoints = datapoints';

hold off;
end
