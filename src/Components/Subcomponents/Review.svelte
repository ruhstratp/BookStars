<script>
  // @ts-nocheck
  import { jwt_token } from "../../store";
  import { onMount } from "svelte";
  import Stars from "./Stars.svelte";
  export let review;

  let jwtToken;
  jwt_token.subscribe((jwt) => (jwtToken = jwt));

  let dislikedByUser;
  let likedByUser;

  const appreciateReviewRequest = async (likeOrNot) => {
    let responseData;
    await fetch(`http://127.0.0.1:5000/appreciate_review/${review.id}`, {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      headers: {
        "authorization-token": jwtToken,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        like: likeOrNot,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        responseData = data;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  onMount(() => {
    if (review.dislikedByUser == true) {
      dislikedByUser = true;
    }
    if (review.likedByUser == true) {
      likedByUser = true;
    }
  })
</script>

<body>
  <div class="card">
    <div class="row g-0">
      <!-- <div class="col-md-4">
        <img class="img-fluid rounded-start" src={imageUrl} alt="Book 1" />
      </div> -->
      <!-- <div class="col-md-8"> -->
      <div class="card-body">
        <h3 class="card-title">
          {review.userName}
          <!-- {username} -->
        </h3>
        <p>
          <Stars 
            rating={review.rating}
          />
        </p>
        <p class="card-text">
          {review.text}
        </p>
      </div>
      <div class="like-dislike">
        {#if likedByUser == true}
          <button class="btn like-button is-liked" on:click={async () => {await appreciateReviewRequest(true); likedByUser=true; dislikedByUser=false;}}>
            <i class="fa fa-thumbs-up fa-lg" aria-hidden="true" />
          </button>
        {:else}
          <button class="btn like-button" on:click={async () => {await appreciateReviewRequest(true); likedByUser=true; dislikedByUser=false;}}>
            <i class="fa fa-thumbs-up fa-lg" aria-hidden="true" />
          </button>
        {/if}

        {#if dislikedByUser == true}
          <button class="btn dislike-button is-disliked" on:click={async () => {await appreciateReviewRequest(false); dislikedByUser=true; likedByUser=false;}}>
            <i class="fa fa-thumbs-down fa-lg" aria-hidden="true" />
          </button>
        {:else}
          <button class="btn dislike-button" on:click={async () => {await appreciateReviewRequest(false); dislikedByUser=true; likedByUser=false;}}>
            <i class="fa fa-thumbs-down fa-lg" aria-hidden="true" />
          </button>
        {/if}
      </div>
    </div>
  </div></body
>

<style>
  @import url("https://fonts.googleapis.com/css?family=Poppins:200,400,600|Bitter:400,600italic,600|Playfair+Display:700");
body{
  font-family: Bitter;
}
  .card {
    max-height: 100%;
    width: 800px;
    margin-bottom: 3rem;
    border-radius: 1.5rem;
    padding: 2rem;
    --bg-opacity: 1;
    background-color: #fff;
    background-color: rgba(255, 255, 255, var(--bg-opacity));
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.46), 0 1px 2px 0 rgb(0 0 0 / 6%);
    box-sizing: border-box;
    border: 0 solid;
  }

  .like-dislike {
    text-align: center;
  }
  button {
    cursor: pointer;
    outline: 0;
    outline-color: rgb(3, 3, 3);
  }
.btn{
  background-color: rgba(161, 159, 159, 0.172);
  border-color: rgba(0, 0, 0, 0.394);
  box-shadow: 0 1px 3px 0 rgba(253, 251, 251, 0.46), 0 1px 2px 0 rgba(23, 22, 22, 0.755);
}
  .btn:focus {
    outline: none;
  }

  .is-liked {
    color: rgb(1, 187, 1);
  }

  .is-disliked {
    color: rgb(221, 11, 11);
  }

  .like-button:hover {
    color: rgb(0, 196, 0);
  }

  .dislike-button:hover {
    color: rgb(255, 0, 0);
  }

  .card-text {
    margin-top: 20px;
  }
  .card-title {
    font-style: italic;
    font-weight: bold;
  }

  /* Variables */

  :root {
    --black: rgba(0, 0, 0, 1);
    --white: rgba(255, 255, 255, 1);

    --font-size-s: 20px;
    --font-size-m: 26px;

    --font-family-bitter: "Bitter";
    --font-family-poppins: "Poppins";
  }

</style>

