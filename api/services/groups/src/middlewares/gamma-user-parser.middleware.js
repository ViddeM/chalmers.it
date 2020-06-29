module.exports = (req, res, next) => {
    console.log("hej");
    console.log(req.headers);
    var userObj = req.headers.user;
    req.gammaUser = userObj != null ? JSON.parse(userObj) : null;
    next();
};
