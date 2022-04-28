for f in *.tex; do 
    pandoc "$f" -o "${f%.tex}.rst"
done

[WARNING] Could not load include file a161-searcFitProtocol.tex at tutorial_model_building_basic.tex line 231 column 34
[WARNING] Could not load include file a162-asignOrigAndSampling.tex at tutorial_model_building_basic.tex line 232 column 38

