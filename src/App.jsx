import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API = "http://127.0.0.1:5000";

function App() {
  const [properties, setProperties] = useState([]);
  const [user, setUser] = useState(localStorage.getItem("user"));
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [dividend, setDividend] = useState(0);
  const [selected, setSelected] = useState(null);

  // 🔥 FETCH DATA (WITH EXTRA PROPERTIES)
  const fetchData = async () => {
    try {
      const res = await axios.get(`${API}/properties/`);

      const extra = [
        {
          id: 2,
          name: "Beach House",
          location: "Goa",
          price: 8000000,
          available_shares: 70,
          rent: 60000
        },
        {
          id: 3,
          name: "Tech Park Office",
          location: "Bangalore",
          price: 12000000,
          available_shares: 40,
          rent: 120000
        }
      ];

      setProperties([...(res.data || []), ...extra]);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchDividend = async () => {
    try {
      const res = await axios.get(`${API}/dividend/`);
      setDividend(res.data.monthly_dividend || 0);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchData();
    fetchDividend();
  }, []);

  // 🔐 LOGIN
  const login = async () => {
    try {
      const res = await axios.post(`${API}/auth/login`, {
        username,
        password
      });

      if (res.data.msg === "Login success") {
        localStorage.setItem("user", username);
        setUser(username);
      } else {
        alert("Login Failed");
      }
    } catch {
      alert("Login Failed");
    }
  };

  const logout = () => {
    localStorage.removeItem("user");
    setUser(null);
  };

  // 💰 BUY
  const buyShare = async (id) => {
    await axios.post(`${API}/invest/buy`, {
      property_id: id,
      shares: 1
    });

    fetchData();
    fetchDividend();
  };

  // 🔐 LOGIN UI
  if (!user) {
    return (
      <div className="login">
        <div className="login-box">
          <h2>🔐 Login</h2>

          <input
            placeholder="Username"
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            onChange={(e) => setPassword(e.target.value)}
          />

          <button onClick={login}>Login</button>
        </div>
      </div>
    );
  }

  return (
    <div>

      {/* NAVBAR */}
      <div className="navbar">
        <h2>🏠 Real Estate App</h2>
        <div>
          👤 {user}
          <button onClick={logout}>Logout</button>
        </div>
      </div>

      {/* SUMMARY */}
      <div className="summary-grid">
        <div className="summary-card">💰 ₹500000<br />Investment</div>
        <div className="summary-card">📊 12 Shares</div>
        <div className="summary-card">💸 ₹{dividend}</div>
        <div className="summary-card">📈 12% ROI</div>
      </div>

      <h2 style={{ marginLeft: "20px" }}>Available Properties</h2>

      {/* PROPERTY GRID */}
      <div className="grid">
        {properties.map((p) => (
          <div className="card" key={p.id}>

            <img
              src={`https://source.unsplash.com/400x300/?house,${p.location}`}
              alt="property"
            />

            <div className="card-body">

              <div className="card-header">
                <h3>{p.name}</h3>
                <span className="tag">🔥 Premium</span>
              </div>

              <p className="location">📍 {p.location}</p>

              <div className="stats">
                <span>💰 ₹{p.price}</span>
                <span>🏠 ₹{p.rent}/mo</span>
                <span>📈 12%</span>
              </div>

              {/* Progress */}
              <div className="progress">
                <div style={{
                  width: `${((100 - p.available_shares) / 100) * 100}%`
                }}></div>
              </div>

              <div className="actions">
                <button onClick={() => buyShare(p.id)}>Buy</button>
                <button
                  className="outline"
                  onClick={() => setSelected(p)}
                >
                  Details
                </button>
              </div>

            </div>
          </div>
        ))}
      </div>

      {/* MODAL */}
      {selected && (
        <div className="modal">
          <div className="modal-box">
            <h2>{selected.name}</h2>
            <p>📍 {selected.location}</p>
            <p>💰 ₹{selected.price}</p>
            <p>🏠 Rent: ₹{selected.rent}</p>

            <button onClick={() => setSelected(null)}>Close</button>
          </div>
        </div>
      )}

    </div>
  );
}

export default App;