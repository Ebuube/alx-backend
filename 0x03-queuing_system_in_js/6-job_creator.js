import kue from 'kue'

// Create a Kue queue
const queue = kue.createQueue();
const queueName = 'push_notification_code';

// Define payload
const payload = {
  phoneNumber: '+2347040369093',
  message: 'Hello man, how are you doing?'
};

// Set up a job
const job = queue.create(queueName, payload)
  .save(function(err) {
    if (!err)  {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
