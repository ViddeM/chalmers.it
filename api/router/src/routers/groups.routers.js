const axios = require("axios");

module.exports = getGroupsRouter = router => {
    router.get("/groups", (req, res) => {
        console.log(req.session.user);
        axios
            .get("http://groups:8080/groups", {
                headers: {
                    user:
                        req.session.user != null
                            ? JSON.stringify(req.session.user)
                            : null
                }
            })
            .then(response => {
                res.status(200).send(response.data);
            })
            .catch(error => {
                res.status(500).send("nope");
                console.log(error);
            });
    });
    return router;
};
