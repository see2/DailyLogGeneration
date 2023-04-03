const caldavService = require('../services/caldavService');

async function getCalendarEvents(req, res) {
  try {
    const events = await caldavService.getCalendarEvents();
    res.status(200).json(events);
  } catch (error) {
    res.status(500).json({ message: 'Error retrieving calendar events', error });
  }
}

module.exports = {
  getCalendarEvents,
};