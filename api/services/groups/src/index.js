//Redis setup
const { getRedisClient } = require("./setup/redis.setup");
const redisClient = getRedisClient();

//Express setup
const { app, createRouter } = require("./setup/server.setup");

//Middlewares
const gammaUserParser = require("./middlewares/gamma-user-parser.middleware");
app.use(gammaUserParser);

const initRouters = require("./routers");
initRouters(app, createRouter);
