const express = require('express');
const cors = require('cors');
const { getCalendarEvents } = require('./controllers/caldavController');

const app = express();

app.use(cors());

app.get('/calendar/events', getCalendarEvents);

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
