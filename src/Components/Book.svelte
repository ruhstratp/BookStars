<script>
    // @ts-nocheck
        import { jwt_token } from "../store";
        import Reviews from './Reviews.svelte';
        import { bookMockData, reviewsMockData } from '../mockData/mockData';
        import AddReview from './AddReview.svelte';
    import Stars from "./Subcomponents/Stars.svelte";
    import { raf } from "svelte/internal";
    
        export let params = {};
    
        let jwtToken;
        jwt_token.subscribe(jwt => jwtToken = jwt);
        
        const getBookData = async () => {
            let responseData = {
                bookData: bookMockData,
                reviews: reviewsMockData
            };
            await fetch(`http://127.0.0.1:5000/book/${params.id}`, {
                mode: 'cors',
                headers: {
                    'authorization-token': jwtToken,
                    'Content-Type': 'application/json'
                },
            }).then((response) => response.json())
            .then((data) => {
                if (data.message != 'a valid token is missing') {
                    responseData = data;
                }
            }).catch((error) => {
                console.error('Error:', error);
            });

            return responseData;
        }
    </script>
<body>
    {#await getBookData() then data}
        <div class="d-flex align-items-center justify-content-center">
            <div id="book-page">
                <div>
                    <h1 class="book-title mt-5 text-center">
                        "{data.bookData.name}"
                    </h1>

                    <div class="book-details">
                        <!-- svelte-ignore a11y-img-redundant-alt -->
                        <img
                            class="book-picture"
                            src={data.bookData.imageUrl}
                            alt="Picture of Book"
                        />
                    </div>
                    <div
                        class="d-flex align-items-center justify-content-center"
                    >
                        <Stars rating={Math.floor(data.bookData.rating)} />
                    </div>
                    <div
                        class="d-flex align-items-center justify-content-center"
                    >
                        <div
                            class="pub-date-1876-page valign-text-middle bitter-light-black-20px"
                        >
                            <div class="row mt-2">
                                <div class="col-sm-4 bitter-light-black-20px">
                                    Pub Date:
                                    <span class="bitter-normal-black-20px">
                                        {data.bookData.publishYear}
                                    </span>
                                </div>
                                <div class="col-sm-4 bitter-light-black-20px">
                                    Page Count:
                                    <span class="bitter-normal-black-20px">
                                        {data.bookData.pageCount}
                                    </span>
                                </div>
                                <div class="bitter-light-black-20px col-sm-4">
                                    Publisher:
                                    <span class="bitter-normal-black-20px">
                                        {data.bookData.publisher}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <p
                        class="description valign-text-middle bitter-normal-black-20px"
                    >
                        {data.bookData.description}
                    </p>
                </div>
                <div class="sppb-divider sppb-divider-border " />
                {#if data.bookData.userHasWrittenReview === false}
                    <div class="my-5">
                        <AddReview bookId={data.bookData.id} />
                    </div>
                {/if}
                <div>
                    <Reviews
                        imageUrl={data.bookData.imageUrl}
                        reviews={data.reviews}
                    />
                </div>
            </div>
        </div>
    {/await}
</body>

<style>
    @import url("https://fonts.googleapis.com/css?family=Poppins:200,400,600|Bitter:400,600italic,600|Playfair+Display:700");
    @import url("https://fonts.googleapis.com/css?family=Poppins:200,400,600|Bitter:400,600italic,300,500,400italic,600|Playfair+Display:700");

    .sppb-divider {
        display: inline-block;
        width: 100%;
        margin-top: 10px;
        margin-bottom: 10px;
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: rgba(51, 45, 36, 0.1);
    }

    .description {
        align-self: center;
        height: 224px;
        letter-spacing: 1.7px;
        line-height: 35px;
        margin-left: 108px;
        margin-top: 59px;
        text-align: center;
        width: 1083px;
    }

    .valign-text-middle {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    #book-page {
        align-items: center;
        background-color: var(--white);
        border: 1px none;
        display: flex;
        flex-direction: column;
        height: 2609px;
        overflow: hidden;
        width: 1365px;
    }

    /* .book-title {
        font-family: Bitter;
        font-size: 40px;
        font-weight: bolder;
    } */

    .book-title {
        position: relative;
        padding: 0;
        margin: 0 0 50px 0;
        font-family: Bitter;
        font-weight: 300;
        text-align: center;
        text-transform: uppercase;
        font-size: 40px;
        letter-spacing: 1px;
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        grid-template-rows: 16px 0;
        grid-gap: 22px;
    }

    .book-title:after,
    .book-title:before {
        content: " ";
        display: block;
        border-bottom: 2px solid rgb(243, 228, 160);
        background-color: transparent;

    }

    /* .overlap-group5 {
        align-items: flex-start;
        background-color: rgb(243, 228, 160);
        display: flex; 
        height: 111px;
        margin-right: -3.97px;
        margin-top: 50px;
        min-width: 1373px;
        padding: 38.6px 85.4px;
        width: 100%;
    } */

    /* .the-adventures-of-tom-sawyer {
        height: 33px;
        margin-right: 83.03px;
        width: 553px;
    } */

    .book-picture {
        height: auto;
        display: block;
        margin: 30px auto 30px auto;
        object-fit: cover;
        border-radius: 8px;
        /* transform: rotate(-0.65deg); */
        width: 513px;
    }

    .rating {
        height: 37px;
        width: 210px;
    }

    @import url("https://fonts.googleapis.com/css?family=Poppins:200,400,600|Bitter:400,300,600italic,600|Playfair+Display:700");

    .pub-date-1876-page {
        height: 8px;
        letter-spacing: 1.3px;
        line-height: normal;
        margin-top: 46px;
        text-align: center;
        width: 1083px;
    }

    .valign-text-middle {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
