for f in *.pdf;
do 
    convert "$f" "${f%.pdf}.png"
done
 inkscape --without-gui  --file=$f --export-plain-svg=${f%.pdf}.svg

