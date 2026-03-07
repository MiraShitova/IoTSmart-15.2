BACKUP_DIR="../backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

mkdir -p $BACKUP_DIR

echo "--- Starting Backup $TIMESTAMP ---"

docker exec influxdb influx backup $BACKUP_DIR/influx_$TIMESTAMP

tar -czvf $BACKUP_DIR/openhab_conf_$TIMESTAMP.tar.gz ../conf/

find $BACKUP_DIR -type d -mtime +7 -exec rm -rf {} \;
find $BACKUP_DIR -type f -mtime +7 -delete

echo "--- Backup Done! Saved to $BACKUP_DIR ---"