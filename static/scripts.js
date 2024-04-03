function startProcessing() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];

    if (file) {
        var formData = new FormData();
        formData.append('video', file);

        fetch('/process_video', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error occurred during processing.');
            }
        })
        .then(data => {
            document.getElementById('status').textContent = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('status').textContent = 'Error occurred during processing.';
        });
    } else {
        alert('Please select a video file.');
    }
}


