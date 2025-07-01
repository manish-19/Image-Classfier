FROM node:22.12 as build
WORKDIR /app
COPY . .
RUN npm install -g @angular/cli
RUN npm install
RUN npm run build --configuration frontend-tmp

FROM nginx:alpine
COPY --from=build /app/dist/frontend-tmp /usr/share/nginx/html
