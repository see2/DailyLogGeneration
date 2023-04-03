const dav = require('dav');
const url = require('url');

const { CALDAV_URL, CALDAV_EMAIL, CALDAV_PASSWORD } = process.env;

const caldavClient = new dav.Client(
  new dav.transport.OAuth2(new dav.Credentials({ username: CALDAV_EMAIL, password: CALDAV_PASSWORD })),
  {
    baseUrl: url.resolve(CALDAV_URL, '/remote.php/dav'),
    sandbox: new dav.Sandbox(),
  }
);

module.exports = caldavClient;
