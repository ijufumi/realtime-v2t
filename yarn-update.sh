#!/bin/bash
##
## This script is for updating all libraries to the latest automatically.
##

function getListName {
  declare key=$1
  declare localDepList
  localDepList=$(cat package.json | jq $key | jq 'keys')
  localDepList=$(echo $localDepList | sed -E 's/[,"]//g' | sed -E 's/\[//g' | sed -E 's/\]//g')
  echo -n $localDepList
}

rm -f yarn.lock

depList=$(getListName '.dependencies')
yarn -W add $depList

depList=$(getListName '.devDependencies')
yarn -W -D add $depList

if [ -e package-lock.json ]; then
  npm i
fi