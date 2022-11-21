FROM node:12-buster-slim

COPY package.json /app/
WORKDIR /app

ENV NODE_ENV production
ENV FLAG "ITT{...Th4t_1s_Th3_Qu3St10n...}"

RUN yarn

COPY . .

EXPOSE 7006

CMD ["node", "/app/index.js"]

# 7006:7006