# Bash Script By Matthieu Riegler - http://matthieu.riegler.fr
# Licence CC-BY 0 
#
# This script takes an iMessage account input and takes a backup of its
# into txt files. It also saves its pictures that are cached locally.

# Parameter is a iMessage account (email or phone number i.e. +33616.... )
if [ $# -lt 1 ]; then
    echo "Enter a iMessage account (email of phone number i.e +33616.....) "
fi
login="$1"

# Retrieve the text messages 

sqlite3 chat.db "
select is_from_me,text from message where handle_id=(
select handle_id from chat_handle_join where chat_id=(
select ROWID from chat where guid='iMessage;-;$1')
)" | sed 's/1\|/me: /g;s/0\|/buddy: /g' > MessageBackup.txt


# Retrieve the attached stored in the local cache

sqlite3 chat.db "
select filename from attachment where rowid in (
select attachment_id from message_attachment_join where message_id in (
select rowid from message where cache_has_attachments=1 and handle_id=(
select handle_id from chat_handle_join where chat_id=(
select ROWID from chat where guid='iMessage;-;$1')
)))" | cut -c 2- | awk -v home=$HOME '{print home $0}' | tr '\n' '\0' | xargs -0 -t -I fname cp fname .
