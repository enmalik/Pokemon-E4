% fid = fopen('../pokemon_primary_types.txt', 'r');
% pokemonTypes = textscan(fid, '%d%d', 'Delimiter','\t');
% fclose(fid);

fid = fopen('../pokemon_all_types.txt', 'r');
pokemonTypes = textscan(fid, '%d%d%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../Labels/dragon_label.txt', 'r');
dragonLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../Labels/ice_label.txt', 'r');
iceLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../Labels/fighting_label.txt', 'r');
fightingLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../Labels/ghost_label.txt', 'r');
ghostLabels = textscan(fid, '%d', 'Delimiter','\t');
fclose(fid);

fid = fopen('../pokemon_base_stats.txt', 'r');
baseStats = textscan(fid, '%d%d', 'Delimiter','\t');
fclose(fid);

pokemonTypes = [pokemonTypes{:}];
pokemonTypes = double(pokemonTypes(1:251,:));
pokemonTypesVals = pokemonTypes(:,2:end);

size(pokemonTypesVals)

baseStats = [baseStats{:}];
baseStats = double(baseStats(1:251,:));
baseStatsVals = baseStats(:,2);
baseStatsValsNorm = baseStatsVals/max(baseStatsVals);

% testData = horzcat(pokemonTypesVals, baseStatsValsNorm);

size(baseStatsValsNorm)

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

dragonTrain = svmtrain(dragonData(1:200,:), dragonWeightedLabels(1:200), 'showplot', true);
dragonClassify = svmclassify(dragonTrain, dragonData(201:end,:));

iceTrain = svmtrain(iceData(1:200,:), iceWeightedLabels(1:200), 'showplot', true);
iceClassify = svmclassify(iceTrain, iceData);

fightingTrain = svmtrain(fightingData(1:200,:), fightingWeightedLabels(1:200), 'showplot', true);
fightingClassify = svmclassify(fightingTrain, fightingData);

ghostTrain = svmtrain(ghostData(1:200,:), ghostWeightedLabels(1:200), 'showplot', true);
ghostClassify = svmclassify(ghostTrain, ghostData);


dragonResult = dragonWeightedLabels(201:end) == dragonClassify;
iceResult = iceWeightedLabels == iceClassify;
fightingResult = fightingWeightedLabels == fightingClassify;
ghostResult = ghostWeightedLabels == ghostClassify;


