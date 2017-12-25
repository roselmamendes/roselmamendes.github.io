FROM jekyll/jekyll

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY Gemfile /usr/src/app

COPY Gemfile.lock /usr/src/app

RUN bundle install

COPY . /usr/src/app

EXPOSE 4000
