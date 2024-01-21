<script>
    // @ts-nocheck
    import { onMount } from "svelte";
    import { jwt_token } from "../../store";
    import { chatMessagesMockData } from "../../mockData/mockData";
    import ChatMessage from "./ChatMessage.svelte";

    let jwtToken;
    jwt_token.subscribe((jwt) => (jwtToken = jwt));

    let chatMessage = "";
    $: messages = [];

    const getChat = async () => {
        let responseData = { chat: chatMessagesMockData };
        await fetch(`http://127.0.0.1:5000/chat`, {
            mode: "cors",
            headers: {
                "authorization-token": jwtToken,
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                responseData = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });

        return responseData;
    };

    const sendMessage = async () => {
        if (!chatMessage) {
            return;
        }
        messages = [{
                    userName: 'You just added this!',
                    message: chatMessage
                }, ...messages]
        console.log(messages);
        let responseData = { chat: chatMessagesMockData };
        await fetch(`http://127.0.0.1:5000/chat`, {
            method: "POST",
            mode: "cors",
            headers: {
                "authorization-token": jwtToken,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message: chatMessage,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                responseData = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
            
        return responseData;
    };

    onMount(async () => {
        const chatMessages = await getChat();
        messages = chatMessages.chat;
    });
</script>

<body>
    {#if jwtToken !== ''}
    {#key messages}
    <div class="mx-5 mt-2">
        <textarea placeholder="What's your opinion about this book?"
            on:change={(e) => {
                chatMessage = e.target.value;
            }}
        />
        <button on:click={sendMessage}>Send message</button>
    </div>
        {#each messages as message}
            <ChatMessage
                userName={message.userName}
                message={message.message}
            />
        {/each}
    {/key}
    {/if}
</body>

<style>
    body {
        font-family: Bitter;
        height: 100%;
        margin-bottom: 100px;
    }
    textarea {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 50px;
        margin-bottom: 50px;
        width: 50%;
        height: 150px;
        padding: 12px 20px;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        background-color: #f8f8f8;
        font-size: 16px;
        resize: none;
    }
    textarea::placeholder {
        font-size: 16px;
        font-style: italic;
    }
    button {
        margin-left: 45%;
        margin-bottom: 10px;
        font-size: 15px;
        border-radius: 50px;
        height: 30px;
        width: 150px;
        border: none;
        background-color: rgb(243, 228, 160);
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.466),
            0 1px 2px 0 rgba(0, 0, 0, 0.322);
    }
</style>
