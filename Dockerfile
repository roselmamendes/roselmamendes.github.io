FROM jekyll/jekyll

COPY Gemfile /srv/jekyll

RUN bundle update
RUN bundle install

COPY . /srv/jekyll

EXPOSE 4000