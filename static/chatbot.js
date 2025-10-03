// Chatbot JavaScript
class WomenSafetyChatbot {
    constructor() {
        this.isOpen = false;
        this.messages = [];
        this.init();
    }

    init() {
        this.createChatbotHTML();
        this.attachEventListeners();
        this.addWelcomeMessage();
    }

    createChatbotHTML() {
        const chatbotHTML = `
            <div class="chatbot-container">
                <button class="chatbot-toggle" id="chatbotToggle">
                    <i class="fas fa-comments"></i>
                </button>
                
                <div class="chatbot-widget" id="chatbotWidget">
                    <div class="chatbot-header">
                        <div class="chatbot-title">
                            <i class="fas fa-shield-alt"></i> Women Safety Assistant
                        </div>
                        <button class="chatbot-close" id="chatbotClose">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    
                    <div class="chatbot-messages" id="chatbotMessages">
                        <!-- Messages will be added here -->
                    </div>
                    
                    <div class="chatbot-input-area">
                        <div class="quick-actions" id="quickActions">
                            <button class="quick-action-btn" data-action="emergency">Emergency Help</button>
                            <button class="quick-action-btn" data-action="safety-tips">Safety Tips</button>
                            <button class="quick-action-btn" data-action="report">Report Issue</button>
                            <button class="quick-action-btn" data-action="volunteer">Volunteer Info</button>
                        </div>
                        <div class="chatbot-input-group">
                            <input type="text" class="chatbot-input" id="chatbotInput" placeholder="Type your message...">
                            <button class="chatbot-send" id="chatbotSend">
                                <i class="fas fa-paper-plane"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', chatbotHTML);
    }

    attachEventListeners() {
        const toggle = document.getElementById('chatbotToggle');
        const close = document.getElementById('chatbotClose');
        const send = document.getElementById('chatbotSend');
        const input = document.getElementById('chatbotInput');
        const quickActions = document.getElementById('quickActions');

        toggle.addEventListener('click', () => this.toggleChatbot());
        close.addEventListener('click', () => this.closeChatbot());
        send.addEventListener('click', () => this.sendMessage());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });

        quickActions.addEventListener('click', (e) => {
            if (e.target.classList.contains('quick-action-btn')) {
                this.handleQuickAction(e.target.dataset.action);
            }
        });
    }

    toggleChatbot() {
        const widget = document.getElementById('chatbotWidget');
        this.isOpen = !this.isOpen;
        
        if (this.isOpen) {
            widget.classList.add('active');
        } else {
            widget.classList.remove('active');
        }
    }

    closeChatbot() {
        const widget = document.getElementById('chatbotWidget');
        widget.classList.remove('active');
        this.isOpen = false;
    }

    addMessage(text, isBot = true) {
        const messagesContainer = document.getElementById('chatbotMessages');
        const messageHTML = `
            <div class="chatbot-message ${isBot ? 'bot' : 'user'}">
                <div class="message-bubble ${isBot ? 'bot' : 'user'}">
                    ${text}
                </div>
            </div>
        `;
        
        messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    sendMessage() {
        const input = document.getElementById('chatbotInput');
        const message = input.value.trim();
        
        if (message) {
            this.addMessage(message, false);
            input.value = '';
            
            // Simulate bot response
            setTimeout(() => {
                this.generateBotResponse(message);
            }, 1000);
        }
    }

    generateBotResponse(userMessage) {
        const message = userMessage.toLowerCase();
        let response = '';

        if (message.includes('emergency') || message.includes('help') || message.includes('urgent')) {
            response = `🚨 <strong>Emergency Numbers:</strong><br>
                       • Police: 100<br>
                       • Women's Helpline: 1091<br>
                       • Emergency: 112<br>
                       • Child Helpline: 1098<br>
                       • Cyber Crime: 1093<br><br>
                       <strong>For immediate assistance, please call these numbers!</strong>`;
        } else if (message.includes('safety') || message.includes('tips')) {
            response = `🛡️ <strong>Quick Safety Tips:</strong><br>
                       • Always inform someone about your whereabouts<br>
                       • Trust your instincts<br>
                       • Keep emergency contacts handy<br>
                       • Avoid isolated areas at night<br>
                       • Learn basic self-defense<br><br>
                       Visit our <a href="/safety-tips">Safety Tips</a> page for more!`;
        } else if (message.includes('volunteer') || message.includes('join')) {
            response = `🤝 <strong>Join Our Mission!</strong><br>
                       We welcome volunteers to help make AP safer for women.<br><br>
                       • Register at our <a href="/volunteer-registration">Volunteer Page</a><br>
                       • Participate in awareness programs<br>
                       • Help in community outreach<br><br>
                       Together we can make a difference!`;
        } else if (message.includes('report') || message.includes('complaint')) {
            response = `📋 <strong>Report an Issue:</strong><br>
                       • Call Women's Helpline: 1091<br>
                       • Visit nearest police station<br>
                       • Use our online portal<br>
                       • Contact <a href="/contact">our offices</a><br><br>
                       Your safety is our priority. Don't hesitate to reach out!`;
        } else if (message.includes('initiative') || message.includes('program')) {
            response = `🎯 <strong>Our Key Initiatives:</strong><br>
                       • SHE Teams for public safety<br>
                       • Bharosa Centers for support<br>
                       • Mahila Police Volunteers<br>
                       • Cyber Crime Prevention<br><br>
                       Learn more on our <a href="/initiatives">Initiatives page</a>!`;
        } else {
            response = `Hello! I'm here to help with women's safety information. You can ask me about:<br><br>
                       🚨 Emergency contacts<br>
                       🛡️ Safety tips<br>
                       🤝 Volunteer opportunities<br>
                       📋 Reporting issues<br>
                       🎯 Our initiatives<br><br>
                       How can I assist you today?`;
        }

        this.addMessage(response);
    }

    handleQuickAction(action) {
        switch (action) {
            case 'emergency':
                this.addMessage('I need emergency help', false);
                this.generateBotResponse('emergency help');
                break;
            case 'safety-tips':
                this.addMessage('Can you give me safety tips?', false);
                this.generateBotResponse('safety tips');
                break;
            case 'report':
                this.addMessage('How can I report an issue?', false);
                this.generateBotResponse('report complaint');
                break;
            case 'volunteer':
                this.addMessage('How can I volunteer?', false);
                this.generateBotResponse('volunteer join');
                break;
        }
    }

    addWelcomeMessage() {
        setTimeout(() => {
            this.addMessage(`👋 Welcome to AP Women Safety Wing!<br><br>
                           I'm your safety assistant. I can help you with:<br>
                           • Emergency contacts<br>
                           • Safety tips<br>
                           • Volunteer information<br>
                           • Reporting issues<br><br>
                           How can I help you today?`);
        }, 500);
    }
}

// Initialize chatbot when page loads
// document.addEventListener('DOMContentLoaded', () => {
//     // Check if we're not on admin login page
//     if (!window.location.pathname.includes('admin-login')) {
//         new WomenSafetyChatbot();
//     }
// });
