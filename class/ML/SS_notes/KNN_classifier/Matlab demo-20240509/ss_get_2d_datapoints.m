function [datapoints, classlabels] = ss_get_2d_datapoints(xbounds,ybounds,classvals)
hold on;
xlim(xbounds);
ylim(ybounds);
title('Press class number and Enter to finish the  point ploating or Esc to quit');
but=0;datapoints=[];classlabels=[];
plotstr='rbygwmc';
ss_invertfig;
while (but~=27)
    [x,y,but]=ginput(1);
    c=double(but)-double('0');
    if (ismember(c,classvals))
        classlabels(end+1)=c;
        datapoints(:,end+1)=[x;y];
        plot(x,y,[plotstr(c),'*'],'MarkerSize',10);
    end
end
classlabels=classlabels';
datapoints = datapoints';
hold off;
end
