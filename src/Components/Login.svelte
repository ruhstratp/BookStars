<script>
    // @ts-nocheck
    import { jwt_token } from "../store";
    import { push } from 'svelte-spa-router';
    let name = "";
    let password = "";
    let loginError = false;

    const sendLoginRequest = async () => {
        let responseData;
        await fetch(`http://127.0.0.1:5000/login`, {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            headers: {
                'Authorization': ('Basic ' + btoa(name + ':' + password))
            }
        }).then((response) => response.json())
        .then((data) => {
            responseData = data;
        }).catch((error) => {
            console.error('Error:', error);
            loginError = true;
        });

        jwt_token.set(responseData.token ?? '');
        push('#/')
    };
</script>

<body class="align">
    <div class="grid align__item">
        <div class="login form">
            <h2 style="color: rgb(243, 221, 126); font-weight: 200">Login</h2>
                <div class="form__field">
                    <div>
                        <div class="my-2">
                            <div>
                                <span>Username: </span>
                            </div>
                            <div>
                                <input
                                    type="username"
                                    placeholder="Enter your username"
                                    on:input={(e) => {
                                        name = e.target.value;
                                    }}
                                />
                            </div>
                        </div>
                    </div>
                    <div class="form__field">
                        <div class="my-2">
                            <div>
                                <span>Password:</span>
                            </div>
                            <div>
                                <input
                                    type="password"
                                    placeholder="Enter your password"
                                    on:input={(e) => {
                                        password = e.target.value;
                                    }}
                                />
                            </div>
                        </div>
                    </div>
                </div>
                {#if loginError}
                    <p class="error-message">
                        Error logging in. Please check your username and
                        password.
                    </p>
                {/if}
                <button class="mt-3" on:click={sendLoginRequest}>Login</button>
                <a class="nav-link" href="#/register">Don't have an account?</a>
        </div>
    </div>
</body>

<style>
    .error-message {
        color: rgb(235, 42, 42); 
    }

    .nav-link:hover{
        font-style: italic;
        font-weight: 300;
        color:rgb(58, 39, 39);
    }

    * {
        box-sizing: border-box;
    }
    body {
        background-color: white;
        color: black;
        font: 300 1rem/1.5 Helvetica Neue, sans-serif;
        margin: 0;
        /* min-height:100%; */
        width: 100%;
        margin: 10px;
        margin-bottom: 20px;
    }

    .align {
        align-items: center;
        display: flex;
        flex-direction: row;
    }

    input {
        border: 0;
        font: inherit;
    }
    input::placeholder {
        color: #7e8ba3;
    }

    .form__field {
        align-content: center;
        margin-bottom: 1rem;
    }
    .form input {
        outline: 0;
        padding: 0.5rem 1rem;
    }
    .form input[type="username"],
    .form input[type="password"] {
        width: 100%;
        margin: 20px 0 20px 0;
    }

    .grid {
        margin: 0 auto;
        max-width: 25rem;
        width: 100%;
    }

    h2 {
        font-size: 2.75rem;
        font-weight: 100;
        margin: 0 0 1rem;
        text-transform: uppercase;
    }

    a {
        color: #7e8ba3;
    }

    .login {
        box-shadow: 0 0 250px rgba(0, 0, 0, 0.438);
        text-align: center;
        padding: 4rem 2rem;
    }
    .login input {
        border: 1px solid #242c37;
        border-radius: 999px;
        background-color: transparent;
        text-align: center;
    }

    button {
        background-image: linear-gradient(
            160deg,
            rgb(243, 228, 160) 0%,
            rgb(234, 200, 50) 100%
        );
        color: #fff;
        margin-bottom: 2rem;
        height: 50px;
        width: 100%;
        border: none;
        border-radius: 50px;
    }
</style>
