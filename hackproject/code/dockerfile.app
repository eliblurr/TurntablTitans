# stage 1 - ui build
FROM node:16-alpine AS ui-build

ENV NODE_ENV=production
WORKDIR /app
COPY . /app/
RUN npm install --production
RUN npm run build

# stage 2 - full app build
COPY --from=ui-build app/dist/frontend ./build/frontend