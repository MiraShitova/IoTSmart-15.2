#!/bin/bash
# Відновлення з архіву
BACKUP_PATH=$1

if [ -z "$BACKUP_PATH" ]; then
    echo "Usage: ./restore.sh <path_to_backup_folder>"
    exit 1
fi

echo "--- Restoring from $BACKUP_PATH ---"
docker exec -i influxdb influx restore $BACKUP_PATH
echo "--- Restore Finished ---"