function openTab(tabName) {
    var i, tabcontent, tabbuttons;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tabbuttons = document.getElementsByClassName("tab-button");
    for (i = 0; i < tabbuttons.length; i++) {
        tabbuttons[i].className = tabbuttons[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}

function searchApplicants() {
    const jobDescription = document.getElementById('job-description').value;
    fetch('/api/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ jobDescription })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('applicant-results');
        resultsDiv.innerHTML = '<h3>Top 10 Applicants:</h3>';
        data.forEach(applicant => {
            const applicantDiv = document.createElement('div');
            applicantDiv.innerHTML = `
                <p>Name: ${applicant.name}</p>
                <p>LinkedIn: <a href="${applicant.linkedin}" target="_blank">${applicant.linkedin}</a></p>
                <p>Skills: ${applicant.skills.join(', ')}</p>
                <p>Experience: ${applicant.experience} years</p>
            `;
            resultsDiv.appendChild(applicantDiv);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function submitApplication() {
    // Placeholder function to simulate submitting an application
    alert('Application submitted!');
}

// Set default tab
document.addEventListener('DOMContentLoaded', function() {
    openTab('employer');
});
