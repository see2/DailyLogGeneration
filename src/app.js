const express = require('express');
const cors = require('cors');
const { getCalendarEvents } = require('./controllers/caldavController');

const app = express();

app.use(cors());

app.get('/calendar/events', getCalendarEvents);

app.get("/tasks", async (req, res) => {
  const accessToken = process.env.ACCESS_TOKEN;

  try {
    const tasksThisWeek = await fetchTasks(accessToken, undefined);
    const tasksUncompleted = await fetchTasks(accessToken, false);

    res.status(200).json({ tasksThisWeek, tasksUncompleted });
  } catch (error) {
    console.error("Error fetching tasks:", error);
    res.status(500).json({ error: "Failed to fetch tasks" });
  }
});


const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
