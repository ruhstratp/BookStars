<script>
// @ts-nocheck
  import { push } from "svelte-spa-router";

  import { topReviewsMockData, listOfBooksMockData } from "../mockData/mockData";
  import { onMount } from 'svelte';
  let carouselBookIndex = 0;
  let booksArray = [];
  const getTopReviews = async () => {
      let responseData = {topReviews: topReviewsMockData};
      await fetch(`http://127.0.0.1:5000/top_reviews`, {
          mode: 'cors',
      }).then((response) => response.json())
      .then((data) => {
          responseData = data;
      }).catch((error) => {
          console.error('Error:', error);
      });

      return responseData;
  };

  const getBooks = async () => {
        let responseData = {listOfBooks: listOfBooksMockData};
        await fetch(`http://127.0.0.1:5000/books`, {
            mode: 'cors',
        }).then((response) => response.json())
        .then((data) => {
            responseData = data;
        }).catch((error) => {
            console.error('Error:', error);
        });

        return responseData;
    };

  const showNextBook = () => {
    if (carouselBookIndex === booksArray.length - 1) {
      carouselBookIndex = 0;
      return;
    }
    carouselBookIndex ++;
  }

  const showPreviousBook = () => {
    if (carouselBookIndex === 0) {
      carouselBookIndex = booksArray.length - 1;
      return;
    }
    carouselBookIndex --;
  }

  const goToBookPage = (pageId) => {
    push(`#/book_details/${pageId}`)
  }

  onMount(async () => {
    const allBooks = await getBooks();
    booksArray = allBooks.listOfBooks;
  })
</script>

<body>
  <div class="home-page screen">
    <img
      class="pexels-bg"
      src="\src\img\pexels-cottonbro-4861347-1@1x.png"
      alt="pexels-cottonbro-4861347 1"
    />
    <h1 class="the-place-where-you valign-text-middle">
      The place where you don't only find new books, but also new opinions ...
    </h1>
    <h1 class="title-explore">Explore all books</h1>
    <!-- <h1 class="title-reviews">Recent Reviews</h1> -->
    <div class="overlap-group7">
      <div class="categories">

        <div class="rectangle-4652" />
        <div class="biographies-memories bitter-semi-bold-storm-dust-16px">
          Biographies &amp; Memories
        </div>
        <div class="rectangle-4653" />
        <div class="business-management bitter-semi-bold-storm-dust-16px">
          Business &amp; Management
        </div>
        <div class="rectangle-4654" />
        <div class="memoir-autobiography bitter-semi-bold-storm-dust-16px">
          Memoir &amp; Autobiography
        </div>
        <div class="rectangle-4655" />
        <div class="graphic-novels-comics bitter-semi-bold-storm-dust-16px">
          Graphic novels &amp; Comics
        </div>
        <div class="rectangle-4656" />
        <div class="science-nature bitter-semi-bold-storm-dust-16px">
          Science &amp;<br />Nature
        </div>
      </div>
      {#await getTopReviews() then data}
        <div class="component-frame">
          <div class="f">
            <div class="f-item"> 
              <!-- <div class="overlap-group"> -->
                <!-- <div class="rectangle-170" /> -->
              <!-- </div> -->
            </div> 
            <div class="f-item">
              <div class="overlap-group1">
                <div class="card-name">{data.topReviews[0].userName}</div>
              </div>
            </div>
            <div class="f-item">
              <div class="overlap-group2">
                <div class="card-name">{data.topReviews[1].userName}</div>
              </div>
            </div>
            <div class="f-item">
              <div class="overlap-group3">
                <div class="card-name">{data.topReviews[2].userName}</div>
              </div>
            </div>
          </div>
        </div>
        <img
          class="recent-reviews"
          src="\src\img\recent-reviews@1x.jpg"
          alt="Recent Reviews"
        />
        {#await getBooks() then data}
          <button
            on:click={showPreviousBook}
            ><img
              class="left-3"
              src="\src\img\left-3@1x.jpg"
              alt="left 3"
            /></button
          >
        <button
          on:click={showNextBook}
          ><img
            class="left-4"
            src="\src\img\left-4@1x.jpg"
            alt="left 4"
          /></button>
        <!-- svelte-ignore a11y-img-redundant-alt -->
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <img on:click={goToBookPage(data.listOfBooks[carouselBookIndex].id)} class="image-47 pointer-on-hover" src={data.listOfBooks[carouselBookIndex].imageUrl} alt="image 47" />
        {/await}
        <p class="text-card1 poppins-normal-shark-20px">
          {data.topReviews[0].text}
        </p>
        <p class="text-card2 poppins-normal-shark-20px">
          {data.topReviews[1].text}
        </p>
        <p class="text-card3 poppins-normal-shark-20px">
          {data.topReviews[2].text}
        </p>
        <img class="rating-2" src="\src\img\rating@2x.png" alt="Rating" /><img
          class="rating-3"
          src="\src\img\rating@2x.png"
          alt="Rating"
        /><img class="rating-4" src="\src\img\rating-2@2x.png" alt="Rating" />
      {/await}
    </div>
  </div>
</body>

<style>
  @import url("https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css");
  @import url("https://fonts.googleapis.com/css?family=Poppins:200,400,600|Bitter:400,600italic,600|Playfair+Display:700");

  .pointer-on-hover:hover {
    cursor: pointer;
  }

  .title-explore {
    font-family: var(--font-family-bitter);
    color: black;
    font-weight: bolder;
    font-size: 35px;
    margin-left: -800px;
  }
/* 
  .title-reviews {
    font-family: var(--font-family-bitter);
    color: black;
    font-weight: bolder;
    font-size: 35px;
    margin-left: -900px;
    margin-left: -800px;
  } */
  .home-page {
    align-items: center;
    background-color: var(--white);
    border: 1px none;
    display: flex;
    flex-direction: column;
    /* gap: 101px; */
    height: 2400px;
    overflow: hidden;
    width: 100%;
    height: 100%;
  }
  .pexels-bg {
    width: 100%;
    margin-bottom: 50px;
  }

  * {
    box-sizing: border-box;
  }

  body {
    padding: 0;
    margin: 0;
    height: 100%;
  }

  .the-place-where-you {
    color: var(--white);
    font-family: var(--font-family-bitter);
    font-size: var(--font-size-xl);
    font-style: italic;
    font-weight: 600;
    height: 290px;
    left: 200px;
    letter-spacing: 3.12px;
    line-height: normal;
    position: absolute;
    text-align: center;
    text-shadow: 0px 4px 4px #00000040;
    top: 350px;
    width: 965px;
  }
  .overlap-group7 {
    height: 1700px;
    position: relative;
    width: 2171px;
  }

  .recent-reviews {
    height: 28px;
    left: 534px;
    position: absolute;
    top: 1000px;
    width: 290px;
  }

  /* .explore-all-books {
    height: 36px;
    margin-left: 530px;
    margin-top: 650px;
    width: 320px;
  } */

  .left-4 {
    height: 71px;
    left: 1539px;
    object-fit: cover;
    position: absolute;
    top: 500px;
    width: 81px;
  }

  .image-47 {
    box-shadow: 0 1px 20px 0 rgba(216, 212, 212, 0.817), 0 1px 10px 0 rgba(0, 0, 0, 0.749);
    border-radius: 5px;
    height: auto;
    left: 928px;
    object-fit: cover;
    position: absolute;
    top: 320px;
    width: 318px;
  }

  .memoir-autobiography {
    left: 1292px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 127px;
    width: 127px;
  }
  .science-nature {
    left: 800px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 127px;
    width: 127px;
  }
  .biographies-memories {
    left: 554px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 127px;
    width: 127px;
  }

  .graphic-novels-comics {
    left: 1046px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 127px;
    width: 127px;
  }
 

  .rating-3 {
    height: 28px;
    left: 1460px;
    position: absolute;
    top: 1200px;
    width: 166px;
  }

  .rectangle-4655 {
    background-color: rgba(243, 228, 160, 0.59);
    border: 1px solid;
    border-color: black;
    border-radius: 10px;
    height: 89px;
    left: 1010px;
    position: absolute;
    top: 100px;
    width: 199px;
  }

  .left-3 {
    cursor: pointer;
    height: 71px;
    left: 556px;
    object-fit: cover;
    position: absolute;
    top: 500px;
    width: 85px;
  }

  .component-frame {
    align-items: flex-end;
    border: 1px none;
    display: flex;
    height: 450px;
    left: 0;
    min-width: 2171px;
    position: absolute;
    top: 1100px;
  }

  .f {
    align-items: flex-start;
    border: 1px none;
    display: flex;
    gap: 50px;
    margin-bottom: -8.96px;
    width: fit-content;
  }

  .f-item {
    border: 1px none;
    height: 459.29px;
    min-width: 400px;
  }

  .overlap-group3 {
    align-items: flex-start;
    background-color: var(--concrete);
    border-radius: 43px;
    box-shadow: 20px 20px 50px #d2d2d2, -20px -20px 50px #ffffff;
    display: flex;
    height: 400px;
    min-width: 400px;
    padding: 80.7px 102px;
    position: relative;
    top: 59px;
  }
  .overlap-group1 {
    align-items: flex-start;
    background-color: var(--concrete);
    border-radius: 43px;
    box-shadow: 20px 20px 50px #d2d2d2, -20px -20px 50px #ffffff;
    display: flex;
    height: 400px;
    min-width: 400px;
    padding: 80.7px 102px;
    position: relative;
    top: 59px;
  }

  .overlap-group2 {
    align-items: flex-start;
    background-color: var(--concrete);
    border-radius: 43px;
    box-shadow: 20px 20px 50px #d2d2d2, -20px -20px 50px #ffffff;
    display: flex;
    height: 400px;
    min-width: 400px;
    padding: 80.7px 102px;
    position: relative;
    top: 59px;
  }

  .card-name {
    color: var(--shark);
    font-family: var(--font-family-playfair_display);
    font-size: var(--font-size-l);
    font-weight: 700;
    letter-spacing: 0;
    line-height: normal;
    text-align: center;
    width: 180px;
    margin-top: 15px;
  }


  .text-card3 {
    font-family: Poppins;
    left: 1410px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 1300px;
    width: 271px;
  }

  .rectangle-4652 {
    background-color: rgba(243, 228, 160, 0.59);
    border: 1px solid;
    border-color: black;
    border-radius: 10px;
    height: 89px;
    left: 518px;
    position: absolute;
    top: 100px;
    width: 199px;
  }

  .rectangle-4656 {
    background-color: rgba(243, 228, 160, 0.59);
    border: 1px solid;
    border-color: black;
    border-radius: 10px;
    height: 89px;
    left: 764px;
    position: absolute;
    top: 100px;
    width: 199px;
  }

  .rectangle-4653 {
    background-color: rgba(243, 228, 160, 0.59);
    border: 1px solid;
    border-color: black;
    border-radius: 10px;
    height: 89px;
    left: 1502px;
    position: absolute;
    top: 100px;
    width: 199px;
  }
  .rectangle-4654 {
    background-color: rgba(243, 228, 160, 0.59);
    border: 1px solid;
    border-color: black;
    border-radius: 10px;
    height: 89px;
    left: 1256px;
    position: absolute;
    top: 100px;
    width: 199px;
  }

  .rating-4 {
    height: 28px;
    left: 1010px;
    position: absolute;
    top: 1200px;
    width: 166px;
  }

  .text-card2{
    font-family: Poppins;
    left: 510px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 1300px;
    width: 271px;
  }

  .text-card1 {
    font-family: Poppins;
    left: 960px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 1300px;
    width: 271px;
  }

  .business-management {
    left: 1538px;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    top: 127px;
    width: 127px;
  }

  .rating-2 {
    height: 28px;
    left: 560px;
    position: absolute;
    top: 1200px;
    width: 166px;
  }

  .categories {
    width: 100px;
    position: absolute;
    left: 0%;
    color: black;
  }

  /* variabile */

  :root {
    --black: rgba(0, 0, 0, 1);
    --white: rgba(255, 255, 255, 1);

    --font-size-s: 20px;
    --font-size-m: 26px;

    --font-family-bitter: "Bitter";
    --font-family-poppins: "Poppins";
  }


</style>

