FROM node:12.22.10

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 -g

COPY package.json .
COPY package-lock.json .
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "dev"]