import kue from 'kue'

// Create a Kue queue
const queue = kue.createQueue();
const queueName = 'push_notification_code';

/**
 * Send notification to each number
 * @param {string} phoneNumber - The receipient's contact
 * @param {string} message - Content of the notification
 * @returns {void}
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process the queue
queue.process(queueName, function(job, done) {
  // Get job data
  const { phoneNumber, message } = job.data;

  // Call sendNotification function
  sendNotification(phoneNumber, message);

  // Mark job as completed
  done();
});
