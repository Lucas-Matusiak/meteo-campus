// plugins/sqlite.js

const sqlite3 = require('sqlite3').verbose();

// Chemin vers votre base de données SQLite. Remplacez 'chemin_vers_votre_bdd.sqlite' par le chemin de votre fichier SQLite.
const dbPath = 'chemin_vers_votre_bdd.sqlite';

// Créer une nouvelle instance de la base de données SQLite
const db = new sqlite3.Database(dbPath, (err) => {
  if (err) {
    console.error('Erreur lors de la connexion à la base de données SQLite :', err.message);
  } else {
    console.log('Connexion à la base de données SQLite réussie');
  }
});

// Exporter la connexion à la base de données pour l'utiliser dans votre application
export default ({ app }, inject) => {
  inject('sqlite', db);
}
