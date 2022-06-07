FROM NODE:lts
WORKDIR /app
COPY /src/package*.json /app/
RUN npm install --quiet

COPY /src/ /app/

EXPOSE 8080

CMD [ "node","server.js" ]