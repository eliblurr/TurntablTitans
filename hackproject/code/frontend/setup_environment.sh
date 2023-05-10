#!/bin/bash
# pass in api url from shell
# ./setup_environ.sh -c url
# -c is required

while getopts ":c:" opt; do
  case $opt in
    c) cmd="$OPTARG";;
  esac
done

if [ -z "$cmd" ]
then
  echo '-c is required, add api url'
else
  echo 'url accepted'
  export API_BASE_URL=${cmd}
  echo "apiUrl->$API_BASE_URL"
  tmp=$(mktemp)
  jq '."/api/v1".target = env.API_BASE_URL' ./proxy.conf.json > "$tmp" && mv "$tmp" ./proxy.conf.json
fi && exit 1
