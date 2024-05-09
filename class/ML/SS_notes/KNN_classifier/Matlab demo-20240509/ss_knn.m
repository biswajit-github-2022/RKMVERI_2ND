
%{
-----------------------------------------------------------------------------
k-NN Demo(Maximum SIX class)
-----------------------------------------------------------------------------
AUTHOR: Soumitra Samanta (soumitramath39@gmail.com)
-----------------------------------------------------------------------------
%}

clear;close all; clc;

xb=[-50 50];
yb=[-50 50];
ClassIDs=[1 2 3 4 5 6];
plotstr='rbygwmc';
plot_decision_doundary = 1;

figure;clf;
[tr_feat_mat,tr_label] = ss_get_2d_datapoints(xb, yb, ClassIDs);%Training data
if(~isempty(tr_feat_mat))
    if(length(unique(tr_label)) > 1)
        
        but = 0;
        while (but~=27)
            
            [ts_feat_mat,ts_label]=ss_get_testdata(tr_feat_mat,tr_label, 1, xb, yb);%Test data
            
            T = dist(tr_feat_mat,ts_feat_mat');% Find distances
            [B,IX] = sort(T);
            
            K = input('Enter the value of K(>0) = ');
            if(K > size(tr_feat_mat, 1))
                fprintf('ERROR: K must be <= number training data points\n');
                K = input('Enter the value of K(>0 and < number training data points) = ');
            end
            %%%%Plot the distances%%%%%%%%%%%
            
            figure;hold on;
            xlim(xb);
            ylim(yb);
            ss_invertfig;
            
            plot(ts_feat_mat(1,1), ts_feat_mat(1,2),[plotstr(ts_label),'*'],'MarkerSize',10);
            
            for i = 1:length(tr_label)
                plot(tr_feat_mat(i,1), tr_feat_mat(i,2),[plotstr(tr_label(i)),'*'],'MarkerSize',10);
            end
            
            for i = 1:length(tr_label)
                %         x1 = vertcat(ts_feat_mat(1, 1),tr_feat_mat(i,1));
                %         y1 = vertcat(ts_feat_mat(1,2), tr_feat_mat(i,2));
                %         plot(x1,y1);
                ss_draw_line(ts_feat_mat, tr_feat_mat(i,:));
            end
            hold off;
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            
            %%%%%%%%%%%%%%Classify the point%%%%%%%%%%%%%
            while(K)
                
%                 ts_predict_label = knnclassify(ts_feat_mat, tr_feat_mat, tr_label, K);
                
                Knn_model = fitcknn(tr_feat_mat, tr_label,'NumNeighbors', K);
                ts_predict_label = predict(Knn_model, ts_feat_mat);
                
                figure;
                hold on;
                xlim(xb);
                ylim(yb);
                ss_invertfig;
                
                for i = 1:length(tr_label)
                    plot(tr_feat_mat(i,1), tr_feat_mat(i,2),[plotstr(tr_label(i)),'*'],'MarkerSize',10);
                end
                
                plot(ts_feat_mat(1,1), ts_feat_mat(1,2),[plotstr(ts_predict_label),'*'],'MarkerSize',10);
                
                NNP = tr_feat_mat(IX(1:K),:);
                NNP_LABL = tr_label(IX(1:K));
                for i = 1:K
                    %             x1 = vertcat(ts_feat_mat(1, 1),NNP(i,1));
                    %             y1 = vertcat(ts_feat_mat(1,2), NNP(i,2));
                    %             plot(x1,y1);
                    ss_draw_line(ts_feat_mat, NNP(i,:), plotstr(NNP_LABL(i)));
                end
                
                %%%%%%Plot decision boundary%%%%%%%
                if plot_decision_doundary
                    unique_tr_label = unique(tr_label);
                    plotstr_new = '';
                    for i = 1:numel(unique_tr_label)
                        plotstr_new = strcat(plotstr_new, plotstr(unique_tr_label(i)));
                    end
                    figure;
                    [xxb, yyb] = meshgrid(xb(1):0.5:xb(2), yb:0.5:yb(2));
                    xxyyb = [xxb(:), yyb(:)];
                    xxyyb_predict_label = predict(Knn_model, xxyyb);
                    gscatter(xxb(:), yyb(:), xxyyb_predict_label, plotstr_new);
                    hold on;
                    gscatter(tr_feat_mat(:, 1), tr_feat_mat(:, 2), tr_label, plotstr_new);
                    title('Decision boundary');
                end
                %%%%%%
                
                K = input('Enter another value of K for chacking or type 0 for other point ');
                if(K > size(tr_feat_mat, 1))
                    fprintf('ERROR: K must be <= number training data points\n');
                    K = input('Enter the value of K(>0 and < number training data points) = ');
                end
                hold off;
            end
            but = input('Press enter to exit or any key for other point classification');
        end
    else
        fprintf('ERROR: Input elements all are in same class\n');
    end
else
    fprintf('No input has given\n');
end



