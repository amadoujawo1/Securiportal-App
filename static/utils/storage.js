// static/js/storage.js
class Storage {
    constructor() {
      this.ACTIVATED_TEAM_LEAD_KEY = 'activatedTeamLead';
    }
  
    hashPassword(password) {
      let hash = 0;
      for (let i = 0; i < password.length; i++) {
        let char = password.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
      }
      return hash.toString();
    }
  
    findUser(username, password) {
      const users = this.getUsers();
      const hashedPassword = this.hashPassword(password); // Hash the entered password
      return users.find(user => user.username === username && user.password === hashedPassword && user.active !== false);
    }
  
    findUserByUsername(username) {
      const users = this.getUsers();
      return users.find(user => user.username === username);
    }
  
    getUsers() {
      return JSON.parse(localStorage.getItem('users') || '[]');
    }
  
    saveUser(user) {
      const users = this.getUsers();
      user.password = this.hashPassword(user.password); // Hash the password before saving
      users.push(user);
      localStorage.setItem('users', JSON.stringify(users));
    }
  
    deleteUser(username) {
      let users = this.getUsers();
      users = users.filter(user => user.username !== username);
      localStorage.setItem('users', JSON.stringify(users));
    }
  
    activateUser(username) {
      const users = this.getUsers();
      const userIndex = users.findIndex(user => user.username === username);
      if (userIndex !== -1) {
        users[userIndex].active = true;
        localStorage.setItem('users', JSON.stringify(users));
      }
    }
  
    deactivateUser(username) {
      const users = this.getUsers();
      const userIndex = users.findIndex(user => user.username === username);
      if (userIndex !== -1) {
        users[userIndex].active = false;
        localStorage.setItem('users', JSON.stringify(users));
      }
    }
  
    updateUserPassword(username, newPassword) {
      const users = this.getUsers();
      const userIndex = users.findIndex(user => user.username === username);
      if (userIndex !== -1) {
        users[userIndex].password = this.hashPassword(newPassword);
        localStorage.setItem('users', JSON.stringify(users));
      }
    }
  
    getFlightsAndSupervisors() {
      return JSON.parse(localStorage.getItem('flightsAndSupervisors') || '{"flights": [], "supervisors": []}');
    }
  
    saveFlightsAndSupervisors(flights, supervisors) {
      const data = { flights, supervisors };
      localStorage.setItem('flightsAndSupervisors', JSON.stringify(data));
    }
  
    getReports() {
      return JSON.parse(localStorage.getItem('reports') || '[]');
    }
  
    getReportsByUser(username) {
      const reports = this.getReports();
      return reports.filter(report => report.submittedBy === username);
    }
  
    getReportById(id) {
      const reports = this.getReports();
      return reports.find(report => report.id === id);
    }
  
    saveReport(report) {
      const reports = this.getReports();
      reports.push(report);
      localStorage.setItem('reports', JSON.stringify(reports));
    }
  
    updateReport(id, updatedReport) {
      const reports = this.getReports();
      const reportIndex = reports.findIndex(report => report.id === id);
      if (reportIndex !== -1) {
        reports[reportIndex] = { ...reports[reportIndex], ...updatedReport };
        localStorage.setItem('reports', JSON.stringify(reports));
        return true;
      }
      return false;
    }
  
    verifyUpdate(id, status, verifiedBy) {
      const reports = this.getReports();
      const reportIndex = reports.findIndex(report => report.id === id);
      if (reportIndex !== -1) {
        reports[reportIndex].verified = status === 'approved';
        reports[reportIndex].verifiedBy = verifiedBy;
        localStorage.setItem('reports', JSON.stringify(reports));
      }
    }
  
    activateUpdateForTeamLead(username, date) {
      const activationData = { username: username, date: date };
      localStorage.setItem(this.ACTIVATED_TEAM_LEAD_KEY, JSON.stringify(activationData));
    }
  
    isUpdateActivated(username, date) {
      const activationData = JSON.parse(localStorage.getItem(this.ACTIVATED_TEAM_LEAD_KEY) || '{}');
      return activationData.username === username && activationData.date === date;
    }
  
    calculateTotal(formData) {
      const sum = [
        'paid', 'diplomats', 'infants', 'notPaid', 'paidCardQr',
        'deportees', 'transit', 'waivers', 'prepaidBank',
        'roundTrip', 'latePayment'
      ].reduce((sum, field) => sum + Number(formData[field] || 0), 0);
      return sum - Number(formData['refunds'] || 0);
    }
  }
  
  const storage = new Storage();