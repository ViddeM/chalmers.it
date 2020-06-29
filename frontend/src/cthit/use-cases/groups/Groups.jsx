import React, { useEffect } from "react";
import { Heading, Text } from "../../common/styles/Text.styles";
import { Link } from "react-router-dom";
import axios from "axios";

const Groups = () => {
    useEffect(() => {
        axios.get("/api/groups").then(response => console.log(response));
    }, []);

    return (
        <>
            <Heading>Groups</Heading>
            <Text>
                <Link to={"/"}>To home</Link>
            </Text>
        </>
    );
};

export default Groups;
