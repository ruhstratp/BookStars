<script>
// @ts-nocheck
    import { jwt_token } from "../store";
    import BookOfTheWeekChat from "./Subcomponents/BookOfTheWeekChat.svelte";

    import CountdownTimer from "./Subcomponents/CountdownTimer.svelte";

    let jwtToken;
    jwt_token.subscribe(jwt => jwtToken = jwt);

    const getBookOfTheWeekInfo = async () => {
        let responseData = {bookData: {
		bookId: 2,
		name: "How to win friends and influence people",
		sendMessage: false,
		time: 1673820000.0
	}};
        await fetch(`http://127.0.0.1:5000/book_of_the_week`, {
            mode: 'cors',
            headers: {
                    'authorization-token': jwtToken,
                    'Content-Type': 'application/json'
                },
        }).then((response) => response.json())
        .then((data) => {
            responseData = data;
        }).catch((error) => {
            console.error('Error:', error);
        });
console.log(responseData);
        return responseData;
    }
</script>

<body>
    {#await getBookOfTheWeekInfo() then data}
        <div class="d-flex flex-align-center justify-content-center my-5">
            <div class="countdown-timer">
                    <CountdownTimer
                        endTime={data.bookData.time}
                    />
            </div>
        </div>
        <div class="d-flex flex-align-center justify-content-center mt-5 wait-for-book">
            The book of this week is &nbsp;"<a class="book-title" href="#/book_details/{data.bookData.bookId}">{data.bookData.name}</a>".
            {#if data.bookData.sendMessage === false}
                    Read it and chat about it when the timer ends!
            {/if}
        </div>
        <!-- {#if data.bookData.sendMessage === true} -->
            <div>
                <BookOfTheWeekChat/>
            </div>
        <!-- {/if} -->
    {/await}
</body>

<style>
    .countdown-timer {
        width: 50%;
    }

    .wait-for-book {
        font-size: 18px;
        font-family: Bitter;
    }

    .book-title {
        color: rgb(207, 194, 137);
        text-decoration: none;
    }
</style>