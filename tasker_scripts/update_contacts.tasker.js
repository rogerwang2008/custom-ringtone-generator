const files = listFiles("/storage/emulated/0/CustomWechatNotification/Ringtones")

const fileList = files.split("\n")

let contactList = []

fileList.forEach((fileDir) => {
    if (fileDir.indexOf(".mp3") === -1) return
    let split = fileDir.split("/")
    let contactName = split[split.length - 1].split(".")[0]
    contactList.push(contactName)
})

let contactListString = contactList.join("\n")
setGlobal("PreparedWechatContacts", contactListString)

flash(`刷新了铃声列表! 共有 ${contactList.length} 条铃声被定义`)
