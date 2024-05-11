// A publisher to channel
import redis from 'redis';

const publisher = redis.createClient();
const channelName = 'holberton school channel';

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Publish a message to the channel
 * @param message The message to publish
 * @param time The time to wait before sending message
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish(channelName, message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
