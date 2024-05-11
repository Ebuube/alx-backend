import createPushNotificationsJobs from './8-jobs.js';
import kue from 'kue';
import { expect } from 'chai';

const queueName = 'push_notification_code_3';
describe('cratePushNotificaionsJobs - Testing', () => {
  let queue;

  beforeEach(() => {
    // Create a Kue queue in test mode
    queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1', db: 3 }, prexif: 'q' });
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit the test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  // Tests
  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });
});
