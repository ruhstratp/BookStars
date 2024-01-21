<script>
    import { listOfBooksMockData } from "../mockData/mockData";
    import BookCard from "./Subcomponents/BookCard.svelte";

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
</script>

<body>
    <div class="row mx-2">
        {#await getBooks() then data}
            {#each data.listOfBooks as book}
                    <div class="col-lg-4 col-md-6 col-xs-12 d-flex align-items-center justify-content-center my-4">
                        <BookCard 
                            book={book}
                        />
                    </div>
            {/each}
        {/await}
    </div>
</body>

<style>
  @import url("https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css");
  @import url("https://fonts.googleapis.com/css?family=Poppins:200,400,600|Bitter:400,600italic,600|Playfair+Display:700");
  body {
    font-family: Bitter;
  }
</style>
