const user_id = Math.floor(Math.random() * 10000);

function handleClick() {
    const text = document.getElementById('promptText').value || 'default';
    const bnt = document.getElementById('promptButton');
    
    const date = new Date();
    const time_start = date.toLocaleTimeString();

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
            console.log(res)
            const date = new Date();
            const time_end = date.toLocaleTimeString();
            const html = `
      <tr>
        <td>${user_id}</td>
        <td>${res.task_id}</td>
        <td>${time_start}</td>
        <td>${time_end}</td>
        <td>${res.task_result}</td>
      </tr>`;
            const newRow = document.getElementById('tasks').insertRow(0);
            newRow.innerHTML = html;
            bnt.disabled = false;
        })
}
