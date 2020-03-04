grep OptionGroupName dat.json | awk '{print $2}' | sed 's/"//g' | sed 's/,//g'
