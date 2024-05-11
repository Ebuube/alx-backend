import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.error('Redis connection error', err);
});

// Test the connection
client.on('connect', () => {
  console.log('Connected to Redis');

  // Sample
  client.set('playBoykey', 'dance and have fun', (err, reply) => {
    if (err) {
      console.error('Error setting value:', err);
    } else {
      console.log('Set value:', reply);
    }
  });
});
