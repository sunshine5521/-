<template>
  <div class="login-container">
    <div class="login-form-wrapper">
      <div class="login-title">智能停车管理系统</div>
      <el-form :model="loginForm" label-width="0" class="login-form">
        <el-form-item prop="username">
          <div class="input-group">
            <i class="el-icon-user"></i>
            <el-input v-model="loginForm.username" placeholder="用户名" class="login-input"></el-input>
          </div>
        </el-form-item>
        <el-form-item prop="password">
          <div class="input-group">
            <i class="el-icon-lock"></i>
            <el-input type="password" v-model="loginForm.password" placeholder="密码" class="login-input"></el-input>
          </div>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="login" class="login-button">登录</el-button>
        </el-form-item>
        <el-form-item class="register-link">
          <span>还没有账号？</span>
          <el-button type="text" @click="$router.push('/register')">立即注册</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="login-animation">
      <div class="car-animation"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage'
}
</script>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

const loginForm = ref({
  username: '',
  password: ''
})
const router = useRouter()

const login = async () => {
  try {
    const trimmedForm = {
      username: loginForm.value.username.trim(),
      password: loginForm.value.password.trim()
    }
    const response = await fetch('http://127.0.0.1:5000/api/user/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(trimmedForm)
    })
    const data = await response.json()
    if (data.code === 200) {
        // 保存token、用户ID和角色到localStorage
        localStorage.setItem('token', data.data.token)
        localStorage.setItem('user_id', data.data.user_id)
        localStorage.setItem('role', data.data.role || 'user')
        ElMessage.success('登录成功')
        // 跳转到首页
        router.push('/')
      } else {
      ElMessage.error(data.message)
    }
  } catch (error) {
    ElMessage.error('网络错误，请重试')
  }
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

.login-container::before {
  content: '';
  position: absolute;
  width: 300px;
  height: 300px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  top: -100px;
  left: -100px;
  animation: float 8s ease-in-out infinite;
}

.login-container::after {
  content: '';
  position: absolute;
  width: 200px;
  height: 200px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 50%;
  bottom: -50px;
  right: -50px;
  animation: float 10s ease-in-out infinite reverse;
}

@keyframes float {
  0%, 100% {
    transform: translate(0, 0) scale(1);
  }
  50% {
    transform: translate(50px, 50px) scale(1.1);
  }
}

.login-form-wrapper {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  width: 100%;
  max-width: 420px;
  position: relative;
  z-index: 1;
  animation: slideUp 0.6s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.login-form {
  width: 100%;
}

.input-group {
  position: relative;
  margin-bottom: 20px;
}

.input-group i {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
  font-size: 18px;
}

.login-input {
  width: 100%;
  padding-left: 45px;
  height: 45px;
  border: 1px solid #ddd;
  border-radius: 25px;
  font-size: 14px;
  transition: all 0.3s ease;
}

.login-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
}

.login-button {
  width: 100%;
  height: 45px;
  border-radius: 25px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.login-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
}

.register-link {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #666;
}

.register-link span {
  margin-right: 5px;
}

.register-link .el-button {
  color: #667eea;
  padding: 0;
}

.register-link .el-button:hover {
  text-decoration: underline;
}

.login-animation {
  margin-left: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50%;
  height: 100vh;
  position: relative;
}

.car-animation {
  width: 200px;
  height: 120px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  position: relative;
  animation: carMove 3s ease-in-out infinite;
}

.car-animation::before {
  content: '';
  position: absolute;
  top: 10px;
  left: 10px;
  width: 60px;
  height: 40px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
}

.car-animation::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 20px;
  width: 40px;
  height: 30px;
  background: #333;
  border-radius: 5px;
  box-shadow: 100px 0 0 #333;
}

@keyframes carMove {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  25% {
    transform: translateY(-10px) rotate(2deg);
  }
  75% {
    transform: translateY(10px) rotate(-2deg);
  }
}
</style>