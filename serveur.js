const express = require("express");
const app = express();
const PORT = 8080; // You can change this to any port you want
const sqlite3 = require("sqlite3").verbose();
const cors = require("cors");

const db = new sqlite3.Database("campus.sqlite");

app.use(cors());
app.use(
  cors({
    origin: "http://localhost:3000", // Replace with the URL of your NUXT.js application
  })
);

app.use(express.json());

// Route to get JSON data
app.get("/api/universities", (req, res) => {
  db.all("SELECT * FROM Universite", (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    // Return the JSON data
    res.json(rows);
  });
});

// Route to fetch implantations based on selected university (etablissement_siege)
app.get("/api/implantations", async (req, res) => {
  try {
    // Extract the etablissement_siege from the request query
    const { etablissement_siege } = req.query;

    // Check if the etablissement_siege parameter is provided
    if (!etablissement_siege) {
      return res
        .status(400)
        .json({ error: "Etablissement_siege parameter is missing" });
    }

    // Construct the SQL query to fetch the code_universite based on the provided etablissement_siege
    const queryGetCodeUniversite = `
        SELECT code_universite
        FROM Universite
        WHERE etablissement_siege = ${etablissement_siege}
      `;

    console.log(queryGetCodeUniversite);

    const universities = await new Promise((resolve, reject) => {
      db.all(queryGetCodeUniversite, (err, rows) => {
        if (err) {
          console.log("HERE THE ERROR : " + err.message);
          reject(err);
        } else {
          console.log(rows);
          resolve(rows);
        }
      });
    });

    const code_universite = universities[0]?.code_universite;
    console.log(code_universite);

    // If code_universite is not found, return an empty array (no matching implantations)
    if (!code_universite) {
      return res.json([]);
    }

    // Construct the SQL query to fetch implantations based on the code_universite
    const queryGetImplantations = `
        SELECT *
        FROM Implantations
        WHERE code_universite = \'${code_universite}\'
      `;

    console.log(queryGetImplantations);
    const implantations = await new Promise((resolve, reject) => {
      db.all(queryGetImplantations, (err, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve(rows);
        }
      });
    });

    res.json(implantations);
  } catch (error) {
    // Handle any errors
    console.error("Error fetching implantations:", error);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
