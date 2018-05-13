FROM jekyll/jekyll

COPY Gemfile /srv/jekyll

COPY Gemfile.lock /srv/jekyll

RUN bundle install

COPY . /srv/jekyll

EXPOSE 4000