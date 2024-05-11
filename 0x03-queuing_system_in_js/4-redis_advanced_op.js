import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Task 4: Create Hash -> Store the values using HSET
const schools = 'HolbertonSchools';
const locations = {
  'Portland': 50, 'Seattle': 80, 'New York': 20, 'Bogota': 20,
  'Cali': 40, 'Paris': 2};

Object.entries(locations).forEach(([name, population]) => {
  // console.log(`I am -> ${key}: ${value}`);
  client.hset(schools, name, population, redis.print);
});


client.hgetall(schools, (err, reply) => {
  if (reply) {
    console.log(reply);
  }
});
