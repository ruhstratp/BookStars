<script>
    export let userName;
    export let message;
</script>

<body>
    <div class="message-card mx-5 my-4 p-3">
        <p style="font-weight: bold;">{userName}</p>
        &nbsp;
        <p style="font-size: medium;">{message}</p>
    </div>
</body>

<style>
    .message-card {
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.466), 0 1px 2px 0 rgba(0, 0, 0, 0.322);
    }
</style>