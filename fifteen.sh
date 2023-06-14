
echo "Tight windows"
for SEED in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
do
    python3.8 generator.py "fifteen/req60j10s$SEED.dat"  --seed $SEED -r 50
    python3.8 generator.py "fifteen/req80j10s$SEED.dat"  --seed $SEED -r 80
    python3.8 generator.py "fifteen/req100j10s$SEED.dat"  --seed $SEED -r 100
    python3.8 generator.py "fifteen/req120j10s$SEED.dat"  --seed $SEED -r 120
    python3.8 generator.py "fifteen/req150j10s$SEED.dat"  --seed $SEED -r 150
done

