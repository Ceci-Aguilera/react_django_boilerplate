FROM node:14.19-alpine3.15 as BUILDER

WORKDIR /usr/src/app

RUN apk update && apk add tzdata
ENV TZ America/New_York
ENV PATH /usr/app/node_modules/.bin:$PATH
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apk update && apk add vim

COPY package.json package-lock.json ./

RUN npm install --silent
RUN npm install react-scripts -g --silent

COPY . .

ARG API_SERVER

ENV REACT_APP_API_SERVER=${API_SERVER}
RUN REACT_APP_API_SERVER=${API_SERVER} \
  npm run build




FROM node:14.19-alpine3.15

WORKDIR /usr/src/app

RUN npm install -g serve

COPY --from=BUILDER /usr/src/app/build ./build