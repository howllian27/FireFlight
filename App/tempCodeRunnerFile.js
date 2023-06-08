function submitForm(event) {
    event.preventDefault();

    var userId = document.getElementById('user-id').value;

    fetch('http://127.0.0.1:5000/match', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user: userId
        })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
}
