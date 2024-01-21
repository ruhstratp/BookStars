<script>
    import { push } from 'svelte-spa-router';
    export let params = {};
    //aici cautam in baza de date dupa id

    const goHome = () => {
        push('/')
    }
</script>

<div>
    <button on:click={goHome}>Go Home</button>
    <h1>Book id: {params.id}</h1>

</div>

<style>
    
</style>