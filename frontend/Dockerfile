
# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /frontend

# install and cache app dependencies
COPY package.json /frontend/
RUN yarn install --silent
RUN yarn install react-scripts@3.0.1 -g --silent

# start app
CMD ["yarn", "start"]
