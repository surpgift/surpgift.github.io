function createRandomEmoji() {
    const emojis = ['🐯', '🐻']; // Add more emoji symbols as needed
    const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
    return randomEmoji;
}

function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.className = 'snowflakes';
    snowflake.style.left = `${Math.random() * window.innerWidth}px`;
    snowflake.style.animationDuration = `${3 + Math.random() * 3}s`;

    const randomEmoji = createRandomEmoji();
    snowflake.innerText = randomEmoji;

    document.querySelector('.snowfall-container').appendChild(snowflake);

    snowflake.addEventListener('animationiteration', () => {
        document.querySelector('.snowfall-container').removeChild(snowflake);
    });
}

setInterval(createSnowflake, 100);
