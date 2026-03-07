#!/bin/bash
# Автоматичний бекап для Міри
BACKUP_DIR="../backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

mkdir -p $BACKUP_DIR

echo "--- Starting Backup $TIMESTAMP ---"

# 1. Бекап InfluxDB (структура та дані)
docker exec influxdb influx backup $BACKUP_DIR/influx_$TIMESTAMP

# 2. Бекап конфігурацій OpenHAB
tar -czvf $BACKUP_DIR/openhab_conf_$TIMESTAMP.tar.gz ../conf/

# 3. Ротація: видаляємо бекапи старіші за 7 днів
find $BACKUP_DIR -type d -mtime +7 -exec rm -rf {} \;
find $BACKUP_DIR -type f -mtime +7 -delete

echo "--- Backup Done! Saved to $BACKUP_DIR ---"