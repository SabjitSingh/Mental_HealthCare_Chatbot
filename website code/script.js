let chatbotMsgList = ["Hi", "Hey", "Good Morning", "Good Evening", "How can I help you?", "Thank You"];

let chatContainer = document.getElementById("chatContainer");
let userInput = document.getElementById("userInput");
let sendMsgBtn = document.getElementById("sendMsgBtn");

sendMsgBtn.onclick = sendMessage; // Assigning the function to the click event of the button

// Adding event listener for the Enter key press on the input field
userInput.addEventListener("keydown", function(event) {
    if (event.keyCode === 13) {
        sendMessage();
    }
});

function sendMessage() {
    let userEnteredMsg = userInput.value;

    if (userEnteredMsg.trim() === "") return; // Don't send empty messages

    let messageContainer = document.createElement("div");
    messageContainer.classList.add("msg-to-chatbot-container");
    chatContainer.appendChild(messageContainer);

    let userMsgEl = document.createElement("span");
    userMsgEl.textContent = userEnteredMsg;
    userMsgEl.classList.add("msg-to-chatbot");
    messageContainer.appendChild(userMsgEl);

    userInput.value = "";

    getReplayChatbotMsg();
}

function getReplayChatbotMsg() {
    let noOfChatbotMsg = chatbotMsgList.length;

    let chatbotMsg = chatbotMsgList[Math.floor(Math.random() * noOfChatbotMsg)]; // Fixing Math.random() usage

    let messageContainer = document.createElement("div");
    messageContainer.classList.add("msg-from-chatbot-container");
    chatContainer.appendChild(messageContainer);

    let chatbotMsgEl = document.createElement("span");
    chatbotMsgEl.textContent = chatbotMsg;
    chatbotMsgEl.classList.add("msg-from-chatbot");
    messageContainer.appendChild(chatbotMsgEl);
}




//button code
// document.getElementById("userInput").addEventListener("keypress", function(event) {
//     // Check if the key pressed is Enter key
//     if (event.key === "Enter") {
//       // Trigger the process here, for example:
//       getReplayChatbotMsg();
//     }
//   });