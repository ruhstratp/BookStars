<script>
    export let rating;
</script>

<body>
    {#each Array(rating) as _, index (index)}
        <span class="fa fa-star checked"></span>
    {/each}
    {#each Array(5-rating) as _, index (index)}
        <span class="fa fa-star"></span>
    {/each}
</body>

<style>
    .checked {
    color: rgb(245, 206, 35);
    }
</style>