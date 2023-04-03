const caldavClient = require('../utils/caldavClient');

function isToday(eventDate) {
  const today = new Date();
  return (
    eventDate.getDate() === today.getDate() &&
    eventDate.getMonth() === today.getMonth() &&
    eventDate.getFullYear() === today.getFullYear()
  );
}

async function getCalendarEvents() {
  const calendars = await caldavClient.listCalendars();
  const events = [];

  for (const calendar of calendars) {
    const calendarEvents = await caldavClient.listEvents(calendar);
    const todayEvents = calendarEvents.filter((event) => {
      const eventStartDate = new Date(event.start);
      return isToday(eventStartDate);
    });

    events.push(...todayEvents);
  }

  return events;
}

module.exports = {
  getCalendarEvents,
};
