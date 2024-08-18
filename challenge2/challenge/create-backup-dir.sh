mkdir backup
cd backup

# Create some compressed backup files
for i in {1..10}
do
  tar -czf "Meowazon_Web_Services_backup_$(date -d "-$i days" +%Y-%m-%d).tar.gz" ../good_files
done

# Create some older compressed backup files
for i in {1..5}
do
  tar -czf "Meowazon_Web_Services_backup_$(date -d "-$((i*7)) days" +%Y-%m-%d).tar.gz" ../good_files
done

# Create some even older compressed backup files
for i in {1..3}
do
  tar -czf "Meowazon_Web_Services_backup_$(date -d "-$((i*30)) days" +%Y-%m-%d).tar.gz" ../good_files
done

# List the backup files
tree

