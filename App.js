import React, { useState } from "react";
import "./App.css";

// ================= ADMIN COMPONENTS =================
import AdminLogin from "./components/admin/AdminLogin";
import AdminDashboard from "./components/admin/AdminDashBoard";

// ================= STUDENT COMPONENTS =================
import StudentLogin from "./components/Student_temp/StudentLogin";
import StudentDashboard from "./components/Student_temp/StudentDashboard";

function App() {
  const [adminLogged, setAdminLogged] = useState(false);
  const [studentId, setStudentId] = useState(null);

  // ================= LOGOUT HANDLERS =================
  const handleAdminLogout = () => {
    setAdminLogged(false);
  };

  const handleStudentLogout = () => {
    setStudentId(null);
  };

  return (
    <div className="App">
      {/* ================= ADMIN DASHBOARD ================= */}
      {adminLogged && (
        <AdminDashboard onLogout={handleAdminLogout} />
      )}

      {/* ================= LOGIN PAGE ================= */}
      {!adminLogged && !studentId && (
        <>
          <h1>Student Management System</h1>

          <div
            style={{
              display: "flex",
              justifyContent: "center",
              gap: "50px",
              marginTop: "30px",
            }}
          >
            <AdminLogin onLogin={() => setAdminLogged(true)} />
            <StudentLogin onLogin={(id) => setStudentId(id)} />
          </div>
        </>
      )}

      {/* ================= STUDENT DASHBOARD ================= */}
      {studentId && !adminLogged && (
        <StudentDashboard
          studentId={studentId}
          onLogout={handleStudentLogout}
        />
      )}
    </div>
  );
}

export default App;

