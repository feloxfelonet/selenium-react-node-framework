const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

let users = [{ id: 1, username: 'admin', password: 'admin' }];
let items = [{ id: 1, name: 'First item' }];

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username && u.password === password);
  user ? res.status(200).json({ success: true }) : res.status(401).json({ success: false });
});

app.get('/items', (req, res) => res.json(items));

app.post('/items', (req, res) => {
  const newItem = { id: Date.now(), name: req.body.name };
  items.push(newItem);
  res.status(201).json(newItem);
});

app.put('/items/:id', (req, res) => {
  const item = items.find(i => i.id == req.params.id);
  if (item) {
    item.name = req.body.name;
    res.json(item);
  } else {
    res.status(404).send();
  }
});

app.delete('/items/:id', (req, res) => {
  items = items.filter(i => i.id != req.params.id);
  res.status(204).send();
});

app.listen(PORT, () => console.log(`Backend running on http://localhost:${PORT}`));