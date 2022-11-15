const user_id = Math.floor(Math.random() * 10000);

function handleClick() {
    const text = document.getElementById('promptText').value || 'default';
    const bnt = document.getElementById('promptButton');

    // Disable the button to prevent multiple clicks
    bnt.disabled = true;

    fetch(`/generate/${user_id}/${text}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then(res => {
            console.log(res);
            // add new image url
            const img = document.getElementById('resultImage');
            img.src = res.task_result;
            bnt.disabled = false;
        })
}
