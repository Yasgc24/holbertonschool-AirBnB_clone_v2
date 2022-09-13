# Redo the task #0 but by using Puppet
exec { '/usr/bin/env apt -y update' : }
-> exec { '/usr/bin/env apt -y install nginx' : }
-> exec { '/usr/bin/env service nginx start' : }
-> exec { '/usr/bin/env mkdir -p /data/web_static/shared/' : }
-> exec { '/usr/bin/env mkdir -p /data/web_static/releases/test/' : }
-> exec { '/usr/bin/env echo "Test for puppet" > /data/web_static/releases/test/index.html' : }
-> exec { '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current' : }
-> exec { '/usr/bin/env sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default' : }
-> exec { '/usr/bin/env service nginx restart' : }
-> exec { '/usr/bin/env chown -R ubuntu:ubuntu /data/' : }
