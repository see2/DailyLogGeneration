require('dotenv').config();
const app = require('./src/app');

const axios = require("axios");

async function fetchTasks(accessToken, completed) {
  const apiUrl = "https://open.feishu.cn/open-apis/task/v1/tasks";
  const headers = {
    Authorization: `Bearer ${accessToken}`,
  };
  const now = new Date();
  const startOfWeek = now.setDate(now.getDate() - now.getDay());
  const startCreateTime = Math.floor(startOfWeek / 1000);
  const params = {
    task_completed: completed,
    start_create_time: startCreateTime,
  };

  try {
    const response = await axios.get(apiUrl, { headers, params });
    return response.data.data.items;
  } catch (error) {
    console.error("Error fetching tasks:", error);
    return [];
  }
}
