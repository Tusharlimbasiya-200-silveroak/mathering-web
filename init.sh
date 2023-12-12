
file="./.secret_key"
if [ -f "$file" ]
then
    echo "Using an existing SECRET_KEY..."
else
    echo "Generating a new SECRET_KEY..."
    echo `date +%s|sha256sum|base64|head -c 50` > "$file"
fi

python3 manage.py makemigrations mgw_back
python3 manage.py migrate

# https://docs.docker.com/config/containers/multi-service_container/
supervisord -c /app/supervisord.conf
