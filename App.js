import logo from './logo.svg';
import './App.css';

function App() {

  const employees = [
    { name: "Rohan", id: 101, salary: 25000 },
    { name: "Amit", id: 102, salary: 30000 },
    { name: "Sneha", id: 103, salary: 28000 }
  ];

  return (
    <div className="App">
      <h1>This is my first page</h1>

      <table border="1" cellPadding="10" style={{ margin: "auto" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>ID</th>
            <th>Salary</th>
          </tr>
        </thead>

        <tbody>
          {employees.map((emp, index) => (
            <tr key={index}>
              <td>{emp.name}</td>
              <td>{emp.id}</td>
              <td>{emp.salary}</td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
}

export default App;
