<script>
    import { onMount } from "svelte";

    export let endTime;

    let daysRemaining = 0;
    let hoursRemaining = 0;
    let minutesRemaining = 0;
    let secondsRemaining = 0;
    const countDown = () => {
        const targetTimestamp = endTime;
        let currentTimestamp = Math.floor(Date.now() / 1000);
        let secondsLeft = targetTimestamp - currentTimestamp;

        let days = Math.floor(secondsLeft / 86400);
        secondsLeft = secondsLeft % 86400;

        let hours = Math.floor(secondsLeft / 3600);
        secondsLeft = secondsLeft % 3600;

        let minutes = Math.floor(secondsLeft / 60);
        secondsLeft = secondsLeft % 60;

        daysRemaining = days;
        hoursRemaining = hours;
        minutesRemaining = minutes;
        secondsRemaining = secondsLeft;
    };

    onMount(() => {
        setInterval(countDown, 1000);
    });
</script>

<body>
    <div class="countdown-timer-box">
        <div class="bloc-time days">
            <span>Days</span>
            <div class="figure days">
                <p class="mt-2 day">{daysRemaining}</p>
            </div>
        </div>
        <div class="bloc-time hours">
            <span>Hours</span>
            <div class="figure hours">
                <p class="mt-2 hour">{hoursRemaining}</p>
            </div>
        </div>
        <div class="bloc-time minutes">
            <span>Minutes</span>
            <div class="figure minutes">
                <p class="mt-2 minute">{minutesRemaining}</p>
            </div>
        </div>
        <div class="bloc-time seconds">
            <span>Seconds</span>
            <div class="figure seconds">
                <p class="mt-2 second">{secondsRemaining}</p>
            </div>
        </div>
    </div>
</body>

<style>
    span {
        display: block;
        margin-bottom: 15px;
        font: normal 0.94em "Lato";
        color: #1a1a1ac5;
        font-weight: bolder;
        text-transform: uppercase;
    }
    .countdown-timer-box {
        font-size: 24px;
        font-weight: 600;
        margin-left: 10%;
    }
    .countdown-timer-box .bloc-time {
        float: left;
        margin-right: 45px;
        text-align: center;
    }
    .countdown-timer-box .bloc-time:last-child {
        margin-right: 0;
    }
    .countdown-timer-box .figure {
        position: relative;
        float: left;
        height: 100px;
        width: 100px;
        margin-right: 10px;
        background-color: #f2f1edb3;
        border-radius: 8px;
        -moz-box-shadow: 0 3px 4px 0 rgba(0, 0, 0, 0.2),
            inset 2px 4px 0 0 rgba(255, 255, 255, 0.08);
        -webkit-box-shadow: 0 3px 4px 0 rgba(0, 0, 0, 0.2),
            inset 2px 4px 0 0 rgba(255, 255, 255, 0.08);
        box-shadow: 0 3px 4px 0 rgba(0, 0, 0, 0.2),
            inset 2px 4px 0 0 rgba(255, 255, 255, 0.08);
    }
    .day{
        padding-top: 30%;
    }
    .hour{
        padding-top: 30%;
    }
    .hour{
        padding-top: 30%;
    }
    .minute{
        padding-top: 30%;
    }
    .second{
        padding-top: 30%;
    }
</style>
