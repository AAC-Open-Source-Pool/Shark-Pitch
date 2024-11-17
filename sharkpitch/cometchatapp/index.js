    let appID = "267103ff5d158249";
    let region = "in";

   CometChat.init(appID, new CometChat.AppSettingsBuilder().subscribePresenceForAllUsers().setRegion(region).build()).then(
     () => {
       console.log("Initialization completed successfully");
     },
     error => {
       console.log("Initialization failed with error:", error);
     }
   );

   function logout(){
        Cometchat.logout.then(
            () => {
                console.log("Logout completed successfully");
                document.getElementById("login-prompt").style.display = "block";
                document.getElementById("chat-window").style.display = "none";
                removeMsgListener()
            },error => {
                console.log("Logout failed with exception:",{error});
            }
        );
   }

   function createUser(){
        let username = document.getElementById('usename').value;
        console.log('usename',username);
        let authKey = "d8975957378a9b6db579ea1b831ca887d33799af";
        var UID = username;
        var name = username;

        var user = new CometChat.User(UID);
        user.setName(name);
        
        CometChat.createUser(user, authKey).then(
            user => {
                logUserIn(user, authKey, UID)
            }, error => {
                console.log("error", error);
                if(error.code == "ERR_UID_ALREADY_EXISTS"){
                    logUserIn(user, authKey, UID)
                }
            }
        )
   }

   function logUserIn(user){
    CometChat.createUser(UID, authKey).then(
        user => {
         console.log("Login successful:", {user});
         document.getElementById("login-prompt").style.display = "none";
         document.getElementById("chat-window").style.display = "block";
         document.getElementById("your-username").innerHTML = user.name;
         createMsgListener()
        }, error => {
         console.log("Login failed with exception", {error});
        });
   }

   function createMsgListener(){
        let listenerID = "GLOBAL_LISTENER_ID";

        CometChat.addMessageListener(
            listenerID,
            new CometChat.messageListener({
                onTextMessageRecieved: textMessage => {
                    document.getElementById('messages').innerHTML += '<div class="message">${textMessage.sender.name}: ${textMessage.text}</div>';
                    console.log("Text message recieved successfully", textMessage);
                },
                onMediaMessageRecieved: mediaMessage => {
                    console.log("Media message recieved successfully", mediaMessage);
                },
                onCustomMessageRecieved: customMessage => {
                    console.log("Custom message recieved successfully", customMessage);
                }
            })
        );
   }

   function removeMsgListener(){
    let listenerID = "GLOBAL_LISTENER_ID";

    CometChat.addMessageListener(
        listenerID,
    );
}

function sendMessage(msg){
    let recieverID = "GLOBAL";
    let messageText = document.getElementById('message').value;
    let recieverType = CometChat.RECIEVER_TYPE.GROUP;
    let textMessage = new CometChat.TextMessage(recieverID, messageText, recieverType);

    CometChat.sendMessage(textMessage).then(
        message => {
            console.log("Message sent successfully:", message);
        }, error => {
            console.log("Message sending failed with error:", error);
        }
    );
}