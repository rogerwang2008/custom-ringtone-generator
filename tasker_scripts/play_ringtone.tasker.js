const preparedContacts = global("PreparedWechatContacts").split("\n");


for (const contact of preparedContacts) {
    if (!not_title.startsWith(contact)) continue;
    musicPlay(`/storage/emulated/0/CustomWechatNotification/Ringtones/${contact}.mp3`, 0, false, "notification", true);
    exit();
}
