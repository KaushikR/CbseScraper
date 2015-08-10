%% To do analysis on the downloaded marks.
% 
setList = {
    '16'
    '26'
    '36'
    '46'
    '56'
    '58'
    '66'
    '76'
    '91'
    '96'
    };
format = '.mat'
dataSetInd = 4;
fileName = strcat(setList(dataSetInd, format));
load('36.mat');

subindex = 4;
subject = 'PHYSICS';
allmarks = [];
for c = 1:5
    y = marks36(:,subindex);
    ind = strcmp(y,subject);
    ind = find (ind);
    mathMarks = marks36(ind,subindex+1);
    mathm = cell2mat(mathMarks);
    NaNInd = find(isnan(mathm));
    mathm(NaNInd) = 0;
    subindex = subindex + 6;
    %     fprintf('%d\n',c);
    if ischar(allmarks)
        allmarks = str2num(allmarks);
    end
    allmarks = [allmarks; mathm];
    
end
h = histogram(allmarks,25);
tbl = tabulate(allmarks)
marksMedian = median(allmarks)
marksMan = mean(allmarks)
marksStdDev = std(allmarks)

