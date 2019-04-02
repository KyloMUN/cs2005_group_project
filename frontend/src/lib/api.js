//const apiUrl = process.env.REACT_APP_API_URL;
const apiUrl = 'http://localhost:5000';

async function get(endpoint, {token}) {
  const response = await fetch(`${apiUrl}/${endpoint}`, {
    headers: {
      'Authorization': `JWT ${token}`
    },
  });
  return await response.json();
}

async function post(endpoint, data, {token} = {}) {
  const response = await fetch(`${apiUrl}/${endpoint}`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  return await response.json();
}

export async function login({username, password}) {
  const response = await post('login', {username, password});
  console.log(response);
  return response;
}
