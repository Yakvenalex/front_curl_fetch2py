let currentTab = 'curl';

function switchTab(tab) {
    currentTab = tab;
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelector(`.tab:nth-child(${tab === 'curl' ? 1 : 2})`).classList.add('active');
    document.getElementById('input').placeholder = `Enter your ${tab} command here...`;
    document.getElementById('input').value = '';
}

function clearInput() {
    document.getElementById('input').value = '';
}

async function convertToPython() {
    const input = document.getElementById('input').value;
    const libraryToggle = document.getElementById('libraryToggle');
    const output = document.getElementById('output');
    const target = libraryToggle.checked ? 'httpx' : 'requests';

    // Ensure the input is a single-line string
    const dataStr = input.replace(/\n/g, ' ').trim();

    try {
        const response = await axios.post('/api', {
            request_type: currentTab,
            target: target,
            data_str: dataStr
        });

        output.innerHTML = `<pre>${response.data.request_string}</pre>
                            <button class="copy-button" onclick="copyToClipboard()">Copy</button>`;
    } catch (error) {
        output.textContent = 'Error: ' + (error.response ? error.response.data.error : error.message);
    }
}

function copyToClipboard() {
    const code = document.querySelector('#output pre').textContent;
    navigator.clipboard.writeText(code).then(() => {
        showCopyAlert();
    }, (err) => {
        console.error('Could not copy text: ', err);
    });
}

function showCopyAlert() {
    const alert = document.getElementById('copyAlert');
    alert.classList.add('show');
    setTimeout(() => {
        alert.classList.remove('show');
    }, 2000);
}

document.getElementById('libraryToggle').addEventListener('change', function () {
    const labels = document.querySelectorAll('.slider-label');
    labels[0].style.fontWeight = this.checked ? 'normal' : 'bold';
    labels[1].style.fontWeight = this.checked ? 'bold' : 'normal';
});