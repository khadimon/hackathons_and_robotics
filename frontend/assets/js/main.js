/*
	Dopetrope by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

document.addEventListener('DOMContentLoaded', () => {
  console.log('JavaScript is working!');
  openTab('employer'); // Default tab
});

function openTab(tabName) {
  const tabContents = document.querySelectorAll('.tab-content');
  tabContents.forEach(tabContent => {
    tabContent.classList.remove('active');
  });

  const activeTab = document.getElementById(tabName);
  if (activeTab) {
    activeTab.classList.add('active');
  }
}

function searchApplicants() {
  // Implement search logic here
  console.log('Searching applicants...');
}

function submitApplication() {
  // Implement application submission logic here
  console.log('Submitting application...');
}