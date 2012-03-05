#!/bin/bash

if [ ! -f timetable_jan/settings_local.py ]
then
    echo "Copying timetable_jan/settings_local.sample to timetable_jan/settings_local.py"
    cp timetable_jan/settings_local.sample timetable_jan/settings_local.py
fi

source /Users/gsnewmark/Projects/python/virtEnv/dj/bin/activate

export PIP_DOWNLOAD_CACHE=/tmp/

pip install -r requirements.txt

if [ -f timetable_jan/db.sqlite ]
then
    echo "Backing up existing sqlite DB to timetable_jan/db.sqlite.backup"
    mv timetable_jan/db.sqlite timetable_jan/db.sqlite.backup
fi

python manage.py syncdb --noinput
python manage.py migrate university --noinput


# FCSS
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_cs_1.csv -y 1 -c 6.050103 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_cs_2.csv -y 2 -c 6.050103 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_cs_3.csv -y 3 -c 6.050103 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_cs_4.csv -y 4 -c 6.050103 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_math_1.csv -y 1 -c 6.040301 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_math_2.csv -y 2 -c 6.040301 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_math_3.csv -y 3 -c 6.040301 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_math_4.csv -y 4 -c 6.040301 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_cs_5.csv -y 1 -c 7.05010101 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_iust_1.csv -y 1 -c 8.05010101 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_ispr_1.csv -y 1 -c 8.04030302 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_pzas_1.csv -y 1 -c 8.05010203 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_iust_2.csv -y 2 -c 8.05010101 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_ispr_2.csv -y 2 -c 8.04030302 -i
python import_timetable.py -f timetable_jan/unified_docs/2011_2012_vesna_pzas_2.csv -y 2 -c 8.05010203 -i

# foreign courses
python add_courses.py -f 6.050103 -y 1 -t 6.040301 -z 1 -n "Англійська мова"
python add_courses.py -f 6.050103 -y 1 -t 6.040301 -z 1 -n "Екологія"
python add_courses.py -f 6.050103 -y 2 -t 6.040301 -z 2 -n "Англійська мова"
python add_courses.py -f 6.050103 -y 2 -t 6.040301 -z 2 -n "Об’єктно-орієнтоване програмування"
python add_courses.py -f 6.050103 -y 2 -t 6.040301 -z 2 -n "Історія України"
python add_courses.py -f 6.050103 -y 2 -t 6.040301 -z 2 -n "Українська мова (за професійним спрямуванням)"
python add_courses.py -f 7.05010101 -y 1 -t 8.05010101 -z 2 -n "Цивільний захист"
python add_courses.py -f 7.05010101 -y 1 -t 8.04030302 -z 2 -n "Цивільний захист"
python add_courses.py -f 7.05010101 -y 1 -t 8.05010203 -z 2 -n "Цивільний захист"
python add_courses.py -f 8.05010101 -y 1 -t 7.05010101 -z 1 -n "Інформаційні системи та структури даних"
python add_courses.py -f 8.05010101 -y 1 -t 7.05010101 -z 1 -n "Побудова масштабованих мереж"
python add_courses.py -f 8.05010101 -y 1 -t 7.05010101 -z 1 -n "Розподілені операційні системи"
python add_courses.py -f 8.05010101 -y 1 -t 8.04030302 -z 1 -n "Англійська мова"
python add_courses.py -f 8.05010101 -y 1 -t 8.04030302 -z 1 -n "Інформаційні системи та структури даних"
python add_courses.py -f 8.05010101 -y 1 -t 8.05010203 -z 1 -n "Англійська мова"
python add_courses.py -f 8.05010101 -y 2 -t 8.04030302 -z 2 -n "Декларативне програмування та розробка баз знань"

