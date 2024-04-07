function runSpeedTest() {
    fetch('/run_speedtest') // Assuming your server handles this route
        .then(response => response.text())
        .then(data => {
            document.getElementById('result').innerHTML = data;
        });
}