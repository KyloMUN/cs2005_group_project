//const apiUrl = process.env.REACT_APP_API_URL;
const apiUrl = 'http://localhost:5000';

const api = {
  async get(endpoint) {
    try {
      const response = await fetch(`${apiUrl}/${endpoint}`);
      return await response.json();
    } catch (err) {
      console.error(err);
      return {};
    }
  },

  async post(endpoint, data) {
    try {
      const response = await fetch(`${apiUrl}/${endpoint}`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      return await response.json();
    } catch (err) {
      console.error(err);
      return {};
    }
  },
};

export default api;