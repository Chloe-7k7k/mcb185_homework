gunzip -c dictionary.gz | grep "r" | grep -v -E "[^zonicar]+" | grep -E ".{4,}"
