tmp=$(mktemp)
jq '."/api/v1".target = env.API_BASE_URL' ./proxy.conf.json > "$tmp" && mv "$tmp" ./proxy.conf.json
# npm run build