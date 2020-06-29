const unprotectedRouters = router => {
    router.get("/groups", (req, res) => {
        res.status(200).send(
            "Hej " + (req.gammaUser != null ? req.gammaUser.nick : " noone")
        );
    });
    return router;
};

const initRouters = (app, createRouter) => {
    app.use("/", unprotectedRouters(createRouter()));
};

module.exports = initRouters;
