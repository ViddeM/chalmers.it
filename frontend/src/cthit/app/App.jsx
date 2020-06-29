import React from "react";
import { Route, Switch } from "react-router-dom";
import Groups from "../use-cases/groups";
import Home from "../use-cases/home";
import { useGamma } from "@cthit/react-digit-components";

const App = () => {
    const [loading] = useGamma();

    if (loading) {
        return <div>loading...</div>;
    }

    return (
        <Switch>
            <Route path={"/groups"} component={Groups} />
            <Route path={"/"} component={Home} />
        </Switch>
    );
};
export default App;
