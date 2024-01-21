<script>
  // @ts-ignore
  import { push } from 'svelte-spa-router';
  import { jwt_token } from "../store";

  let userHasJwtToken = false;
  jwt_token.subscribe(val => {
    if (val === '') {
      userHasJwtToken = false;
    }
    else {
      userHasJwtToken = true;
    }
  });

  const goToLoginPage = () => {
    push('#/login');
  }

  const goToMyReviewsPage = () => {
    push('#/my_reviews');
  }

  const logout = () => {
    jwt_token.set('');
  }
</script>

<body>
  <header>
    <div class="flex-row">
      <img class="logo" src="\src\img\logo@1x.jpg" alt="logo" />
      <h1 style="font-size:3.3vw;font-weight:bold">BookStars</h1>

      <nav>
        <div class="overlap-group8">
          <div class="searchBar">
            <input
              type="text"
              class="searchTerm"
              placeholder="Search book..."
            />
          </div>
          <ul class="navbar">
            <li class="nav-item"><a class="nav-link" href="#/">Home</a></li>
            <li class="nav-item">
              <a class="nav-link" href="#/all_books">Books</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#/book_of_the_week">Forum</a>
            </li>
            {#if userHasJwtToken}
              <li>
                <a class="nav-link" href="#/my_reviews">My Reviews</a>
              </li>
            {/if}
            <li>
              {#if !userHasJwtToken}
                <button type="submit" class="btn btn-link btn-logout" on:click={goToLoginPage}
                  >Login</button
                >
              {:else}
                <button type="submit" class="btn btn-link btn-logout" on:click={logout}
                  >Logout</button
                >
              {/if}
            </li>
          </ul>
        </div>
      </nav>
    </div>
  </header>
</body>

<style>
  @import url("https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css");
  @import url("https://fonts.googleapis.com/css?family=Poppins:200,400,600|Bitter:400,600italic,600|Playfair+Display:700");
  .flex-row {
    background-color: white;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 90px;
    display: flex;
    align-items: center;
    box-shadow: 0 0 10px 0 black;
    margin-bottom:-10px;
    z-index: 2;
    width: 100%;
    
  }
  body {
    font-family: Bitter;
  }


  header {
    background-color: white;
    position: top;
    top: 0;
    left: 0;
    right: 0;
    height: auto;
    display: flex;
    align-items: center;
  }

  header * {
    display: inline;
  }

  header li {
    margin: 20px;
  }

  header li a {
    color: black;
    text-decoration: none;
    margin-right: -30px;
  }


  .overlap-group8 {
    /* background-color: beige; */
    border-radius: 30px;
    display: flex;
    height: 90px;
    justify-content: flex-start;
    margin-left: 30%;
    width: 900px;
    /* min-width: 700px; */
    padding: 31px 20px;
  }
  .btn {
    color: black;
  }
  .btn:hover {
    font-weight: bold;
    color: rgb(95, 48, 0);
  }
  .searchTerm {
    width: 100%;
    border-right: none;
    padding: 5px;
    /* height: 20px; */
    outline: none;
  }

  .searchTerm:focus {
    color: rgb(95, 48, 0);
  }

  .searchTerm:hover {
    font-style: italic;
  }

  .searchBar input[type="text"] {
    background: none;
    float: left;
    padding: 6 6 6 0;
    border: none;
    margin-top: none;
    margin-right: 6px;
    font-size: 17px;
    /* width: 250px; */
  }

  .nav-link {
    color: black;
  }

  .nav-link:hover {
    font-weight: bold;
    font-style: italic;
  }

  .navbar {
    margin-bottom: 50px;
    background: white;
    width: 700px;
    padding-left: 30px;
    padding-top: 0 !important;
  }

  .searchBar {
    /* width: 100%; */
    position: relative;
    display: flex;
    outline: auto;
    outline-color: rgb(243, 228, 160);
    border-radius: 30px;
    height: 55px;
    /* min-width: 200px; */
    padding: 20px 58px;
    margin: -10px 0 0 10px;
  }

  .logo {
    margin-left: 20px;
    height: 85px;
    margin-bottom: 5px;
    object-fit: cover;
    width: 78px;
  }

  @media screen and (max-width: 600px) {
    .navbar a,
    .searchBar input[type="text"] {
      float: none;
      display: block;
      text-align: left;
      width: 100%;
      margin: 0;
      padding: 14px;
    }
    .searchBar input[type="text"] {
      border: 1px solid #ccc;
    }
  }
</style>
