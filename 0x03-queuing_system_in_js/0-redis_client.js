import redis from 'redis';
import dotenv from 'dotenv';


// Load environmental vairables from .env file
dotenv.config();

const client = redis.createClient(process.env.REDIS_URL);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
