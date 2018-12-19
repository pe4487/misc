FILE=$1
cat $FILE | awk '{total += $2}; END {print total}'

z=0
for i in `cat $FILE | cut -d' ' -f2`; do
  z=$((z + i))
done
echo $z
