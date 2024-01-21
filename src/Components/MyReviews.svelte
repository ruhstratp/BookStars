<script>
    // @ts-nocheck
    import { jwt_token } from "../store";
    import { bookMockData, reviewsMockData, myReviewMockData } from '../mockData/mockData';
    import MyReview from "./Subcomponents/MyReview.svelte";

    let jwtToken;
    jwt_token.subscribe(jwt => jwtToken = jwt);
    
    const getMyReviewsData = async () => {
        let responseData = {
            myReviews: [
                myReviewMockData
            ]
        };
        await fetch(`http://127.0.0.1:5000/get_my_reviews`, {
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
    
    {#await getMyReviewsData() then data}
        {#each data.myReviews as review}
            <MyReview
                myReview={review}
            />
        {/each}
    {/await}
    
</body>

<style>
    
</style>
