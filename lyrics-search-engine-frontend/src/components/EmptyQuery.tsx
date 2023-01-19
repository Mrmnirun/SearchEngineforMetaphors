import Box from "@mui/material/Box"
import SearchBox from "./SearchBox"

const EmptyQuery = () => {
    return (
        <Box
            sx={{
                
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            <SearchBox />
        </Box>
    )
}

export default EmptyQuery
