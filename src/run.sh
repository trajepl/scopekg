echo 'index...' > ../result_data/ret_10w
python index.py ../origin_data/line_10w >> ../result_data/ret_10w
echo 'create test data...' >> ../result_data/ret_10w
python tdata.py ../origin_data/line_10w >> ../result_data/ret_10w
# python line.py ../origin_data/line_10w >> ../result_data/ret_10w
echo 'four query...' >> ../result_data/ret_10w
python matrix.py ../origin_data/line_10w >> ../result_data/ret_10w
echo 'line...
39377
query_head runtime: 433.7482051849365
465715770
query_rel runtime: 491.8028426170349
17968
query_hr runtime: 430.867244720459
553
query_htr runtime: 351.9649705886841
run runtime: 1708.3899157047272
' >> ../result_data/ret_10w

echo 'index...' > ../result_data/ret_100w
python index.py ../origin_data/line_100w >> ../result_data/ret_100w
echo 'create test data...' >> ../result_data/ret_100w
python tdata.py ../origin_data/line_100w >> ../result_data/ret_100w
# python line.py ../origin_data/line_10w >> ../result_data/ret_10w
echo 'four query...' >> ../result_data/ret_100w
python matrix.py ../origin_data/line_100w >> ../result_data/ret_100w

echo 'index...' > ../result_data/ret_1kw
python index.py ../origin_data/line_1kw >> ../result_data/ret_1kw
echo 'create test data...' >> ../result_data/ret_1kw
python tdata.py ../origin_data/line_1kw >> ../result_data/ret_1kw
# python line.py ../origin_data/line_10w >> ../result_data/ret_10w
echo 'four query...' >> ../result_data/ret_1kw
python matrix.py ../origin_data/line_1kw >> ../result_data/ret_1kw
