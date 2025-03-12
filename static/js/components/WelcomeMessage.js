class WelcomeMessage {
    constructor(container) {
      this.container = container;
    }
  
    render() {
      this.container.innerHTML = `
        <p>Welcome to the Daily Cash Collection Report!</p>
      `;
    }
  }