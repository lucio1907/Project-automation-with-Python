def get_server_file_structure():
    return """import express from "express";
import cors from "cors";
import "dotenv/config";

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

const PORT = 8080 || process.env.PORT
app.listen(PORT, () => console.log(`Server running in port ${PORT}`))
"""