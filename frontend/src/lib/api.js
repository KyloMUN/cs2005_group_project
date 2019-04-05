//const apiUrl = process.env.REACT_APP_API_URL;
const apiUrl = 'http://localhost:5000/api';

async function get(endpoint, {token}) {
  const response = await fetch(`${apiUrl}/${endpoint}`, {
    headers: {
      'Authorization': `JWT ${token}`
    },
  });
  if(!response.ok) {
    throw new Error(response);
  }
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
  const json = await response.json();
  if(!response.ok) {
    throw new Error(json);
  }
  return json;
}

export async function login({username, password}) {
  const response = await post('login', {username, password});
  return response;
}

export async function getWhoami({token}) {
  const response = await get('whoami', {token});
  return response;
}
