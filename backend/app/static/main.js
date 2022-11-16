const user_id = Math.floor(Math.random() * 10000);

function handleClick() {
    const text = document.getElementById('promptText').value || 'default';
    const bnt = document.getElementById('promptButton');

    // Disable the button to prevent multiple clicks
    bnt.disabled = true;

    const img = document.getElementById('resultImage');
    // loading icon
    img.src = 'https://i.pinimg.com/originals/2b/02/15/2b02159fee58d573c079ad5212d56b63.gif';

    fetch(`/generate/${user_id}`, {
        method: 'POST',
        body: JSON.stringify({
            requestId: user_id.toString(),
            prompt: text,
            num_images: 1,
        }),
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then(res => {
            console.log(res);
            // add new image url
            const img = document.getElementById('resultImage');
            img.src = res['images'][0]['url'];
            bnt.disabled = false;
        })
}
