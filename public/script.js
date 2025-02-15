document.getElementById('profileForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value
    };


    fetch('http://localhost:5000/api/profile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        alert('Profile saved successfully!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while saving the profile.');
    });
});
