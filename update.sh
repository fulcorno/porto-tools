#!/bin/bash

wget -O export_pub.json 'http://porto.polito.it/cgi/search/archive/advanced/export_pub_JSON.js?screen=Search&dataset=archive&_action_export=1&output=JSON&exp=0|1|-date%2Fcreators_name%2Ftitle|archive|-|dipartimenti%3Auserdep%3AANY%3AEQ%3AUSER_D1010|-|eprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive|metadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&n=&cache=2663731'

gzip export_pub.json
