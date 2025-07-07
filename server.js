const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Simple route
app.get('/', (req, res) => {
  res.send('Hello, Projects Dashboard API is running!');
});
// Sample in-memory projects data
const projects = [
  {
    id: 1,
    name: "Water Supply Project",
    description: "Provide clean water to villages",
    status: "Submitted",
    start_date: "2025-01-15",
    end_date: "2025-06-30",
    funding_amount: 100000,
    donor: "NoRAD"
  },
  {
    id: 2,
    name: "School Meals Program",
    description: "Nutrition support for school children",
    status: "Draft",
    start_date: "2025-03-01",
    end_date: "2025-12-31",
    funding_amount: 75000,
    donor: "WFP"
  }
];

// GET /projects - return the list of projects
app.get('/projects', (req, res) => {
  res.json(projects);
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
