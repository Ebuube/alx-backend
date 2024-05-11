import kue from 'kue'

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const queue = kue.createQueue();
const queueName = 'push_notification_code_2';

// Set up jobs
jobs.forEach((payload) => {
  const job = queue.create(queueName, payload)
    .save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

  // Listen for job completion
  job.on('complete', function() {
    console.log(`Notification job #${job.id} completed`);
  });

  // Listen for job failure
  job.on('failed', function(error) {
    console.error(`Notification job #${job.id} failed: ${error}`);
  });

  // Listen for job progress
  job.on('progress', function(progress) {
    console.log(`Notification job #${job.id} ${progress}% complete`);
  });
});
