% fid = fopen('../pokemon_primary_types.txt', 'r');
% pokemonTypes = textscan(fid, '%d%d', 'Delimiter','\t');
% fclose(fid);

fid = fopen('../pokemon_all_types.txt', 'r');
pokemonTypes = textscan(fid, '%d%d%d', 'Delimiter','\t');
fclose(fid);

% fid = fopen('../Labels/dragon_label.txt', 'r');
% dragonLabels = textscan(fid, '%d', 'Delimiter','\t');
% fclose(fid);
% 
% fid = fopen('../Labels/ice_label.txt', 'r');
% iceLabels = textscan(fid, '%d', 'Delimiter','\t');
% fclose(fid);
% 
% fid = fopen('../Labels/fighting_label.txt', 'r');
% fightingLabels = textscan(fid, '%d', 'Delimiter','\t');
% fclose(fid);
% 
% fid = fopen('../Labels/ghost_label.txt', 'r');
% ghostLabels = textscan(fid, '%d', 'Delimiter','\t');
% fclose(fid);

fid = fopen('../Labels/dragon_label_408.txt', 'r');
dragonLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../Labels/ice_label_408.txt', 'r');
iceLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../Labels/fighting_label_408.txt', 'r');
fightingLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../Labels/ghost_label_408.txt', 'r');
ghostLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../pokemon_base_stats.txt', 'r');
baseStats = textscan(fid, '%d%d', 'Delimiter','\t');
fclose(fid);

pokemonTypes = [pokemonTypes{:}];
pokemonTypes = double(pokemonTypes(1:408,:));
pokemonTypesVals = pokemonTypes(:,2:end);

% size(pokemonTypesVals)

baseStats = [baseStats{:}];
baseStats = double(baseStats(1:408,:));
baseStatsVals = baseStats(:,2);
baseStatsValsNorm = baseStatsVals/max(baseStatsVals);

% testData = horzcat(pokemonTypesVals, baseStatsValsNorm);

% size(baseStatsValsNorm)

dragonLabels = [dragonLabels{:}];
dragonLabels = double(dragonLabels);
[dragonData, dragonWeightedLabels] = WeightedTypeStatsLabels(pokemonTypesVals, dragonLabels, baseStatsValsNorm);

iceLabels = [iceLabels{:}];
iceLabels = double(iceLabels);
[iceData, iceWeightedLabels] = WeightedTypeStatsLabels(pokemonTypesVals, iceLabels, baseStatsValsNorm);

fightingLabels = [fightingLabels{:}];
fightingLabels = double(fightingLabels);
[fightingData, fightingWeightedLabels] = WeightedTypeStatsLabels(pokemonTypesVals, fightingLabels, baseStatsValsNorm);

ghostLabels = [ghostLabels{:}];
ghostLabels = double(ghostLabels);
[ghostData, ghostWeightedLabels] = WeightedTypeStatsLabels(pokemonTypesVals, ghostLabels, baseStatsValsNorm);

%this is linear kernel
% dragonTrain = svmtrain(dragonData(152:end,1:end-1), dragonWeightedLabels(152:end), 'showplot', true);

%this is just classifying based on types
% dragonTrain = svmtrain(dragonData(152:end,1:end-1), dragonWeightedLabels(152:end), 'showplot', true, 'kernel_function', 'rbf');
% dragonClassify = svmclassify(dragonTrain, dragonData(1:151,1:end-1));

dragonTrain = svmtrain(dragonData(152:end,:), dragonWeightedLabels(152:end), 'showplot', true, 'kernel_function', 'rbf');
dragonClassify = svmclassify(dragonTrain, dragonData(1:151,:));


% iceTrain = svmtrain(iceData(152:end,1:end-1), iceWeightedLabels(152:end), 'showplot', true);
% iceTrain = svmtrain(iceData(152:end,1:end-1), iceWeightedLabels(152:end), 'showplot', true, 'kernel_function', 'rbf');
% iceClassify = svmclassify(iceTrain, iceData(1:151,1:end-1));
iceTrain = svmtrain(iceData(152:end,:), iceWeightedLabels(152:end), 'showplot', true, 'kernel_function', 'rbf');
iceClassify = svmclassify(iceTrain, iceData(1:151,:));


% fightingTrain = svmtrain(fightingData(152:end,1:end-1), fightingWeightedLabels(152:end), 'showplot', true);
% fightingTrain = svmtrain(fightingData(152:end,1:end-1), fightingWeightedLabels(152:end), 'showplot', true,  'kernel_function', 'rbf');
% fightingClassify = svmclassify(fightingTrain, fightingData(1:151,1:end-1));
fightingTrain = svmtrain(fightingData(152:end,:), fightingWeightedLabels(152:end), 'showplot', true,  'kernel_function', 'rbf');
fightingClassify = svmclassify(fightingTrain, fightingData(1:151,:));



% ghostTrain = svmtrain(ghostData(152:end,:), ghostWeightedLabels(152:end), 'showplot', true);
% ghostTrain = svmtrain(ghostData(152:end,1:end-1), ghostWeightedLabels(152:end), 'showplot', true);
% ghostTrain = svmtrain(ghostData(152:end,1:end-1), ghostWeightedLabels(152:end), 'showplot', true, 'kernel_function', 'rbf');
% ghostClassify = svmclassify(ghostTrain, ghostData(1:151,1:end-1));
ghostTrain = svmtrain(ghostData(152:end,:), ghostWeightedLabels(152:end), 'showplot', true, 'kernel_function', 'rbf');
ghostClassify = svmclassify(ghostTrain, ghostData(1:151,:));




dragonResult = dragonWeightedLabels(1:151) == dragonClassify;
dragonAccuracy = sum(dragonResult)/151

iceResult = iceWeightedLabels(1:151) == iceClassify;
iceAccuracy = sum(iceResult)/151

fightingResult = fightingWeightedLabels(1:151) == fightingClassify;
fightingAccuracy = sum(fightingResult)/151

ghostResult = ghostWeightedLabels(1:151) == ghostClassify;
ghostAccuracy = sum(ghostResult)/151

fid = fopen('../results/DragonTrainer.txt','wt');
fprintf(fid,'%0.f\n', find(dragonClassify == 1));
fclose(fid);

fid = fopen('../results/IceTrainer.txt','wt');
fprintf(fid,'%0.f\n', find(iceClassify == 1));
fclose(fid);

fid = fopen('../results/FightingTrainer.txt','wt');
fprintf(fid,'%0.f\n', find(fightingClassify == 1));
fclose(fid);

fid = fopen('../results/GhostTrainer.txt','wt');
fprintf(fid,'%0.f\n', find(ghostClassify == 1));
fclose(fid);
