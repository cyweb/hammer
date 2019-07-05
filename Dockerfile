FROM alpine:3.10.0

LABEL version="1.0" \
      author="Can Yalçın (http://www.canyalcin.com/)" \
      docker_build="docker build -t cyweb/hammer:1.0 ." \
      docker_run_basic="docker run --rm cyweb/hammer:1.0 -s http://www.example.com"

COPY ["hammer.py", "headers.txt", "/hammer/"]

RUN echo 'Selecting packages to Hammer.' \
  && apk update \
  && apk add --no-cache --virtual .build-deps \
     python3 \
  && echo 'Cleaning cache from APK.' \
  && rm -rf /var/cache/apk/* \
  && echo 'Creating the hammer group.' \
  && addgroup hammer \
  && echo 'Creating the user hammer.' \
  && adduser -G hammer -g "hammer user" -s /bin/sh -D hammer \
  && echo 'Changing the ownership.' \
  && chown -R hammer.hammer /hammer \
  && echo 'Creating a random password for root.' \
  && export RANDOM_PASSWORD=`tr -dc A-Za-z0-9 < /dev/urandom | head -c44` \
  && echo "root:$RANDOM_PASSWORD" | chpasswd \
  && unset RANDOM_PASSWORD \
  && echo 'Locking root account.' \
  && passwd -l root \
  && echo 'Finishing image.'

USER hammer

WORKDIR /hammer

ENTRYPOINT ["python3", "hammer.py"]
