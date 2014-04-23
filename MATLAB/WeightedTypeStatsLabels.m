function [data, updatedLabels] = WeightedTypeStatsLabels(types, typeLabels, stats)
    
    typeWeight = 0.7;
    statsWeight = 0.3;
    
    threshold = 0.9;
    
    noPokemon = size(types,1);
    
    updatedLabels = zeros(noPokemon,1);
    
    for index = 1 : noPokemon
%         index
        if typeLabels(index,1) == -1
            typeBase = 0;
        elseif typeLabels(index,1) == 1
            typeBase = 1;
        end
        
%         score = typeLabels(index,1)*typeWeight + stats(index,1)*statsWeight;
        score = typeBase*typeWeight + stats(index,1)*statsWeight;
        
%         score
        if score >= threshold
            updatedLabels(index,1) = 1;
        else
            updatedLabels(index,1) = -1;
        end
    end
    
    data = horzcat(types, stats);
    
end