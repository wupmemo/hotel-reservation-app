FROM node

WORKDIR ./
COPY package.json ./src

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]