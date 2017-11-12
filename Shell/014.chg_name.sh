#!/bin/bash
src_dir=014_files_src
desc_dir=014_files_desc

files=`ls ${src_dir}/`
for file in ${files}
do
    filename=${file%.*}
    echo ${filename}
    src_name=${src_dir}/${file}
    echo ${src_name}
    desc_name=${desc_dir}/${filename}.txt
    echo ${desc_name}
    cat ${src_name} > ${desc_name}
done

