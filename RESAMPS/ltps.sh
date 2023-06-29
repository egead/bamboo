#!/bin/bash


root_dir="/media/ege/DATA/bamboo/bamboo"

check_ltps_folder() {
    local dir_path="$1"
    local ltps_path="${dir_path}/ltps"
    local files_count=$(find "$ltps_path" -type f | wc -l)
    
    if [[ $files_count -gt 0 ]]; then
        echo "Folder: $dir_path"
    fi
}

traverse_directories() {
    local dir="$1"
    
    for entry in "$dir"/*; do
        if [[ -d "$entry" ]]; then
            local ltps_dir="${entry}/ltps"
            
            if [[ -d "$ltps_dir" ]]; then
                check_ltps_folder "$entry"
            fi
            
         
            traverse_directories "$entry"
        fi
    done
}

traverse_directories "$root_dir"

