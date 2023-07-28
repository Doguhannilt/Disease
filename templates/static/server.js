const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/submit', (req, res) => {
  const selectedDiseases = req.body.disease;
  const selectedDiseasesText = selectedDiseases.join('\n');

  fs.writeFile('C:/Users/doguy/Desktop/Health/selected_diseases.txt', selectedDiseasesText, (err) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error saving selected diseases');
    } else {
      console.log('Selected diseases saved successfully');
      res.send('Selected diseases saved successfully');
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
