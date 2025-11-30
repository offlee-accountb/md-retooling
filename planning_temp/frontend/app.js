// ==================== Configuration ====================
const API_BASE_URL = 'http://localhost:8000';

// ==================== State Management ====================
const state = {
    currentPage: 'login',
    tokens: {
        access: localStorage.getItem('access_token'),
        refresh: localStorage.getItem('refresh_token')
    },
    user: null
};

// ==================== Page Navigation ====================
function showPage(pageName) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    
    const page = document.getElementById(`${pageName}-page`);
    if (page) {
        page.classList.add('active');
        state.currentPage = pageName;
    }
}

// ==================== API Calls ====================
async function apiCall(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const config = {
        headers: {
            'Content-Type': 'application/json',
            ...options.headers
        },
        ...options
    };
    
    // Add auth token if available
    if (state.tokens.access && !options.skipAuth) {
        config.headers['Authorization'] = `Bearer ${state.tokens.access}`;
    }
    
    try {
        const response = await fetch(url, config);
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.detail || 'Request failed');
        }
        
        return data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// ==================== Auth Functions ====================
async function login(email, password) {
    const data = await apiCall('/auth/login', {
        method: 'POST',
        skipAuth: true,
        body: JSON.stringify({ email, password })
    });
    
    // Store tokens
    state.tokens.access = data.access_token;
    state.tokens.refresh = data.refresh_token;
    localStorage.setItem('access_token', data.access_token);
    localStorage.setItem('refresh_token', data.refresh_token);
    
    return data;
}

async function register(name, email, password) {
    return await apiCall('/auth/register', {
        method: 'POST',
        skipAuth: true,
        body: JSON.stringify({ name, email, password })
    });
}

async function getCurrentUser() {
    return await apiCall('/auth/me');
}

function logout() {
    state.tokens.access = null;
    state.tokens.refresh = null;
    state.user = null;
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    showPage('login');
}

// ==================== UI Helpers ====================
function showError(elementId, message) {
    const el = document.getElementById(elementId);
    if (el) {
        el.textContent = message;
        el.classList.add('show');
        
        setTimeout(() => {
            el.classList.remove('show');
        }, 5000);
    }
}

function showSuccess(elementId, message) {
    const el = document.getElementById(elementId);
    if (el) {
        el.textContent = message;
        el.classList.add('show');
        
        setTimeout(() => {
            el.classList.remove('show');
        }, 5000);
    }
}

function setButtonLoading(button, loading) {
    if (loading) {
        button.classList.add('loading');
        button.disabled = true;
    } else {
        button.classList.remove('loading');
        button.disabled = false;
    }
}

function updatePasswordStrength(password) {
    const strengthBar = document.querySelector('.strength-bar');
    if (!strengthBar) return;
    
    let strength = 0;
    if (password.length >= 8) strength += 25;
    if (password.match(/[a-z]/)) strength += 25;
    if (password.match(/[A-Z]/)) strength += 25;
    if (password.match(/[0-9]/) || password.match(/[^a-zA-Z0-9]/)) strength += 25;
    
    strengthBar.style.width = `${strength}%`;
}

// ==================== Event Handlers ====================
// Login Form
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    setButtonLoading(submitBtn, true);
    
    try {
        await login(email, password);
        
        // Load user data
        state.user = await getCurrentUser();
        
        // Update dashboard
        updateDashboard();
        
        // Show dashboard
        showPage('dashboard');
    } catch (error) {
        showError('login-error', error.message || '로그인에 실패했습니다.');
    } finally {
        setButtonLoading(submitBtn, false);
    }
});

// Register Form
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('register-name').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
    const passwordConfirm = document.getElementById('register-password-confirm').value;
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    // Validate passwords match
    if (password !== passwordConfirm) {
        showError('register-error', '비밀번호가 일치하지 않습니다.');
        return;
    }
    
    setButtonLoading(submitBtn, true);
    
    try {
        await register(name, email, password);
        
        showSuccess('register-success', '✓ 회원가입 성공! 로그인해주세요.');
        
        // Clear form
        e.target.reset();
        
        // Switch to login after 2 seconds
        setTimeout(() => {
            showPage('login');
            document.getElementById('login-email').value = email;
        }, 2000);
    } catch (error) {
        showError('register-error', error.message || '회원가입에 실패했습니다.');
    } finally {
        setButtonLoading(submitBtn, false);
    }
});

// Password strength indicator
document.getElementById('register-password').addEventListener('input', (e) => {
    updatePasswordStrength(e.target.value);
});

// Page navigation buttons
document.getElementById('goto-register').addEventListener('click', () => {
    showPage('register');
});

document.getElementById('goto-login').addEventListener('click', () => {
    showPage('login');
});

// Logout button
document.getElementById('logout-btn').addEventListener('click', () => {
    if (confirm('로그아웃 하시겠습니까?')) {
        logout();
    }
});

// ==================== Dashboard Updates ====================
function updateDashboard() {
    if (!state.user) return;
    
    // Update user info
    document.getElementById('user-name').textContent = state.user.name;
    document.getElementById('user-email').textContent = state.user.email;
    
    // Update initials
    const initials = state.user.name
        .split(' ')
        .map(word => word[0])
        .join('')
        .toUpperCase()
        .slice(0, 2);
    document.getElementById('user-initials').textContent = initials;
}

// ==================== Auto-login Check ====================
async function checkAuth() {
    if (state.tokens.access) {
        try {
            state.user = await getCurrentUser();
            updateDashboard();
            showPage('dashboard');
        } catch (error) {
            console.error('Auto-login failed:', error);
            logout();
        }
    }
}

// ==================== Initialize ====================
document.addEventListener('DOMContentLoaded', () => {
    checkAuth();
    
    // Add smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
        });
    });
});

// ==================== Input Animations ====================
document.querySelectorAll('input').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    
    input.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
});

// ==================== Console Welcome Message ====================
console.log('%c🚀 MD Retooling', 'font-size: 24px; font-weight: bold; color: #6366F1;');
console.log('%cAuth Backend API: ' + API_BASE_URL, 'color: #8B5CF6;');
console.log('%cBuilt with ❤️ by Antigravity', 'color: #a1a1aa;');
