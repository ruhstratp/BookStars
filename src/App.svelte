<script>
  import svelteLogo from "./assets/svelte.svg";

  import NavBar from "./Components/NavBar.svelte";
  import Router from "svelte-spa-router";
  import Home from "./Components/Home.svelte";
  import NotFound from "./Components/NotFound.svelte";
  import AllBooks from "./Components/AllBooks.svelte";
  import Footer from "./Components/Footer.svelte";
  import Book from "./Components/Book.svelte"
  import Login from "./Components/Login.svelte";
  import Register from "./Components/Register.svelte";
  import MyReviews from "./Components/MyReviews.svelte";
    import BookOfTheWeek from "./Components/BookOfTheWeek.svelte";

  const routes = {
    "/": Home,
    "/all_books": AllBooks,
    "/book_details/:id": Book,
    "/login": Login,
    "/register": Register,
    "/my_reviews": MyReviews,
    "/book_of_the_week": BookOfTheWeek,
    
    "*": NotFound,
  };
</script>

<main>
  <NavBar />
  <div class="page-container">
    <Router {routes} />
  </div>
  <Footer />
</main>

<style>
  main {
    min-height: 100vh;
    padding: 0;
    margin: 0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  .page-container {
    margin-top: 100px;
  }

</style>
