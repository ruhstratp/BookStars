<script>
    // @ts-ignore
    import { push } from 'svelte-spa-router';
    export let book;

    const viewBookDetailsPage = () => {
        push(`#/book_details/${book.id}`);
    }
</script>

<div>
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="book-card" on:click={viewBookDetailsPage}>
        <p>
            <span class="bolded">Title:</span> &nbsp;"{book.name}"
        </p>
        <p>
            <span class="bolded">Author:</span> &nbsp;{book.author}
        </p>
        <div class="d-flex align-items-center justify-content-center">
            <img class="book-image" src={book.imageUrl} alt="Book"/>
        </div>
    </div>
</div>

<style>
    .bolded{
        color: rgba(0, 0, 0, 0.629);
        font-weight: bold;
    }
    p{
        font-weight: 400;
        text-align: center;
        margin: 10px 0 18px 0;
    }
    .book-card {
        margin-bottom: 30px ;
        padding: 10px;
        width: 300px;
        height: 450px;
        border-radius: 8px;
        border-style: solid;
        border-width: 1px;
        border-color: rgba(0, 0, 0, 0.212);
        background: linear-gradient(180deg, #fbfbfb, rgba(249, 176, 29, 0.4) 230%);
        color: black;
    }

    .book-card:hover {
        cursor: pointer;
        filter: drop-shadow(0 0 0.5em #752f0049);
    }

    .book-image {
        border-radius: 5px;
        max-height: 300px;
        max-width: 300px;
    }
</style>