import React from "react";
import { Heading, Text } from "../../common/styles/Text.styles";
import { Link } from "react-router-dom";

const Home = () => {
    return (
        <>
            <Heading>Teknologsektionen Informationsteknik</Heading>
            <Text>
                <Link to={"/groups"}>To groups</Link>
            </Text>
        </>
    );
};

export default Home;
