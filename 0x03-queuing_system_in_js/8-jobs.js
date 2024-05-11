const queueName = 'push_notification_code_3';

/**
 * Create a push notifications for jobs
 * @param {Array} jobs - The jobs to process
 * @param {object} queue - The queue to create jobs in
 * returns {void}
 */
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((payload) => {
    const job = queue.create(queueName, payload)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    // Listen for job completion
    job.on('complete', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Listen for job failure
    job.on('failed', (error) => {
      console.error(`Notification job #${job.id} failed: ${error}`);
    });

    // Listen for job progress
    job.on('progress', (progress) => {
      console.log(`Notification job #${job.id} ${porgress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
