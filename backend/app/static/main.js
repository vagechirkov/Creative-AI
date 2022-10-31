function handleClick() {
    const text = document.getElementById('promptText').value || 'default';
    const bnt = document.getElementById('promptButton');

    // Disable the button to prevent multiple clicks
    bnt.disabled = true;


    fetch(`/generate/${text}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then(res => {
            console.log(res)
            const date = new Date();
            const time = date.toLocaleTimeString();
            const html = `
      <tr>
        <td>${res.task_id}</td>
        <td>${time}</td>
        <td>${res.task_result}</td>
      </tr>`;
            const newRow = document.getElementById('tasks').insertRow(0);
            newRow.innerHTML = html;
            bnt.disabled = false;
        })
}
