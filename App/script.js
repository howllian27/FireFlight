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

function addUser(event) {
    event.preventDefault();

    var userId = document.getElementById('new-user-id').value;
    var interests = document.getElementById('new-user-interests').value.split(',');
    var ageGroup = document.getElementById('new-user-age-group').value;
    var gender = document.getElementById('new-user-gender').value;
    var city = document.getElementById('new-user-city').value;

    fetch('http://127.0.0.1:5000/addUser', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user: userId,
            interests: interests,
            ageGroup: ageGroup,
            gender: gender,
            city: city
        })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
}
