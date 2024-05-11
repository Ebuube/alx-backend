import kue from 'kue'

const blacklist = ['4153518780', '4153518781'];
const queueName = 'push_notification_code_2';
const levelOfConcurrency = 2;
const queue = kue.createQueue({
  concurrency: levelOfConcurrency // Process this number of jobs at a time
});

/**
 * Send notification to these numbers except blacklisted numbers
 * @param {string} phoneNumber - The receipient's contact
 * @param {string} message - Content of the notification
 * @param {function} job - Interface to job
 * @param {function} done - Marks a job as done
 */
function sendNotification(phoneNumber, message, job, done) {
  if (phoneNumber in blacklist) {
    // fail
  }

  // Track progress to 50%
  job.progress(50, 100);

  // Execute job
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete job
  done();
}

// Process jobs in a queue
queue.process(queueName, levelOfConcurrency, function(job, done) {
  // Get job data
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});
