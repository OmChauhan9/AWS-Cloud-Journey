async function fetchUserData() {
  const userId = document.getElementById('userId').value.trim();
  const userDetails = document.getElementById('userDetails');
  const status = document.getElementById('status');

  userDetails.style.display = 'none';
  userDetails.innerHTML = '';
  status.textContent = '';

  if (!userId) {
    status.textContent = 'Please enter a User ID.';
    return;
  }

  status.textContent = 'Fetching user data…';

  try {
    const response = await fetch(
      `https://ox4123bzzc.execute-api.us-east-1.amazonaws.com/prod/users?userId=${encodeURIComponent(userId)}`
    );
    const data = await response.json();

    if (!response.ok) {
      status.textContent = 'User not found.';
      return;
    }

    status.textContent = 'Success';
    userDetails.style.display = 'block';
    userDetails.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  } catch (error) {
    console.error(error);
    status.textContent = 'Failed to reach the API.';
  }
}
