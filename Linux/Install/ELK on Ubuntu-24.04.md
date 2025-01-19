## HOW TO INSTALL ELK ON UBUNTU-24.04
```
# Install java
sudo apt install openjdk-17-jdk -y
java -version

# Add the Repo for Elastic stack
sudo wget https://artifacts.elastic.co/GPG-KEY-elasticsearch -O /etc/apt/keyrings/GPG-KEY-elasticsearch.key
echo "deb [signed-by=/etc/apt/keyrings/GPG-KEY-elasticsearch.key] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
sudo apt update

# Install Elasticsearch
sudo apt install elasticsearch -y
sudo systemctl daemon-reload
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
sudo systemctl status elasticsearch

# Configure Elastic
# Uncomment and assign cluster.name, node.name. Set network.host to 0.0.0.0 and xpack.security.enabled to false.
sudo vim /etc/elasticsearch/elasticsearch.yml
sudo systemctl restart elasticsearch
sudo systemctl status elasticsearch
curl -X GET "localhost:9200"

# Install Kibana
sudo apt install kibana -y
sudo systemctl start kibana
sudo systemctl enable kibana
sudo systemctl status kibana
sudo ss -pnltu | grep 5601

# Configure Kibana
sudo vim /etc/kibana/kibana.yml
Uncomment and set server.port to 5601, server.host to 0.0.0.0, elasticsearch.hosts to ["http://localhost:9200"]
sudo systemctl restart kibana
Go to a browser, enter http://server-ip:5601/status, press enter and you should have:
![image](https://github.com/user-attachments/assets/881512cb-38e0-40e4-b678-36994bfb510f)

# Install Logstash
sudo apt install logstash -y
sudo systemctl start logstash
sudo systemctl enable logstash
sudo systemctl status logstash

# Configure Logstash
sudo vim /etc/logstash/conf.d/02-beats-input.conf
# Add the following and save:
input {
  beats {
    port => 5044
  }
}
sudo vim /etc/logstash/conf.d/30-elasticsearch-output.conf
# Add:
output {
  if [@metadata][pipeline] {
     elasticsearch {
     hosts => ["localhost:9200"]
     manage_template => false
     index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
     pipeline => "%{[@metadata][pipeline]}"
     }
  } else {
     elasticsearch {
     hosts => ["localhost:9200"]
     manage_template => false
     index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
     }
  }
}
# Test Logstash conf
sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash -t

# Install Filebeat
sudo systemctl restart logstash
sudo apt install filebeat -y

# Configure Filebeate
sudo vim /etc/filebeat/filebeat.yml
# Comment off the following lines
#output.elasticsearch:
  # Array of hosts to connect to.
  #hosts: ["localhost:9200"]
# Then uncomment the following to get Filebeat to connect to Logstash on port 5044
output.logstash:
  # The Logstash hosts
  hosts: ["localhost:5044"]

sudo filebeat modules enable system
sudo filebeat setup --pipelines --modules system
# Now load index template into Elasticsearch
sudo filebeat setup --index-management -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'
# Create the index pattern and load the dashboards into Kibana.
sudo filebeat setup -E output.logstash.enabled=false -E output.elasticsearch.hosts=['localhost:9200'] -E setup.kibana.host=localhost:5601
sudo systemctl start filebeat
sudo systemctl enable filebeat
sudo systemctl status filebeat


```

## TROUBLESHOOTING

If filebeat fails to start, try:
- Re-enabling the system module:
  ```
  - sudo filebeat modules enable system
  ```
- Edit sudo vim /etc/filebeat/modules.d/system.yml<br/>
  Ensure that the filesets you need are enabled by setting enabled: true for the respective sections:
  ```
  - module: system
    syslog:
      enabled: true
      var.paths: ["/var/log/syslog*"]
    auth:
      enabled: true
      var.paths: ["/var/log/auth.log*"]

  ```
- Test filebeat conf
```
  sudo filebeat test config
```
