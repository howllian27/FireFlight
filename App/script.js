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
    var gender = document.getElementById('new-user-gender').value;
    var age = document.getElementById('new-user-age').value;
    var interests = document.getElementById('new-user-interests').value.toLowerCase().split(',');
    var ageGroupPreference = document.getElementById('new-user-age-group-preference').value;
    var genderPreference = document.getElementById('new-user-gender-preference').value;
    var city = document.getElementById('new-user-city').value;

    fetch('http://127.0.0.1:5000//addUser', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user: userId,
            gender: gender,
            age: age,
            interests: interests,
            ageGroupPreference: ageGroupPreference,
            genderPreference: genderPreference,
            city: city
        })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
}
