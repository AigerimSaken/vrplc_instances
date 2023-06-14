
echo "Tight windows"
for SEED in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
do
    python3.8 generator.py "fifteen/req200j10s$SEED.dat"  --seed $SEED -r 200
    python3.8 generator.py "fifteen/req300j10s$SEED.dat"  --seed $SEED -r 300
    python3.8 generator.py "fifteen/req400j10s$SEED.dat"  --seed $SEED -r 400
    python3.8 generator.py "fifteen/req500j10s$SEED.dat"  --seed $SEED -r 500
    python3.8 generator.py "fifteen/req1000j10s$SEED.dat"  --seed $SEED -r 1000
done

