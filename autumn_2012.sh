#!/bin/bash

long_academic_term_id=`python autumn_2012.py long`
short_academic_term_id=`python autumn_2012.py short`

echo $long_academic_term_id
echo $short_academic_term_id

# FLS
python import_timetable.py -f timetable/unified_docs/2012_2013_osin_fls_1.csv -y 1 -c 6.030401 -i -t $long_academic_term_id
python import_timetable.py -f timetable/unified_docs/2012_2013_osin_fls_2.csv -y 2 -c 6.030401 -i -t $long_academic_term_id
python import_timetable.py -f timetable/unified_docs/2012_2013_osin_fls_3.csv -y 3 -c 6.030401 -i -t $long_academic_term_id
python import_timetable.py -f timetable/unified_docs/2012_2013_osin_fls_4.csv -y 4 -c 6.030401 -i -t $short_academic_term_id
python import_timetable.py -f timetable/unified_docs/2012_2013_osin_fls_5.csv -y 1 -c 7.03040201 -i -t $long_academic_term_id
python import_timetable.py -f timetable/unified_docs/2012_2013_osin_fls_6.csv -y 1 -c 8.03040201 -i -t $long_academic_term_id

