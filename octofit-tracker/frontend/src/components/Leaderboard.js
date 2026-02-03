import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Fetched leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div className="card shadow mb-4">
      <div className="card-header bg-success text-white">
        <h2 className="h4 mb-0">Leaderboard</h2>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                {leaderboard[0] && Object.keys(leaderboard[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, idx) => (
                <tr key={entry.id || idx}>
                  {Object.values(entry).map((val, i) => (
                    <td key={i}>{val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {leaderboard.length === 0 && <div className="text-center text-muted">No leaderboard data found.</div>}
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
