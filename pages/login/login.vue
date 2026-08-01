<template>
	<view class="total">
		<view class="title">
			<view class="hello">hello!</view>
			<view class="tv">欢迎使用雨白影视</view>
		</view>
		<view class="box">
			<view class="choice">
				<view class="login" @click="go_login" :class="{'active':state==0}">快速登录</view>
				<view class="register" @click="go_register" :class="{'active':state==1}">注册账号</view>
			</view>
			
			<view class="input" v-show="state==0">
				<input type="text" v-model="phone" class="phone" placeholder="请输入您的账号"/>
				<input type="password" v-model="password" class="passwd" placeholder="请输入您的密码"/>
				<button @click="start_login">登录</button>
			</view>
			<view class="input" v-show="state==1">
				<input type="text" v-model="re_phone" class="phone" placeholder="请输入您的账号"/>
				<input type="password" v-model="re_password" class="passwd" placeholder="请设置您的密码"/>
				<button @click="start_register">注册</button>
			</view>
			<view class="user">
				<view class="question">没有账号?</view>
				<view class="yes" @click="go_register">立即注册</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				phone:'',
				password:'',
				state:0,
				re_phone:'',
				re_password:''
			}
		},
		methods: {
			go_login(){
				this.state=0
			},
			go_register(){
				this.state=1
			},
			async start_login(){
				if(this.phone.trim().length==11 && this.password.trim().length==7){
					let {data:res}=await uni.$http.get('/api/login',
						{'phone':this.phone,'password':this.password},
					)
					if(res.code==200){
						uni.showToast({
							'title':'登录成功',
							'icon':''
						})
						uni.switchTab({
							url:'/pages/index/index'
						})
					}
					if(res.code==400){
						uni.showToast({
							'title':'账户不存在，登录失败',
							'icon':''
						})
					}
				}
			},
			async start_register(){
				if(this.re_phone.trim().length==11 && this.re_password.trim().length==7){
					let {data:res}=await uni.$http.get('/api/register',
						{'re_phone':this.re_phone,'re_password':this.re_password},
					)
					if(res.code==200){
						uni.showToast({
							'title':'注册成功',
							'icon':''
						})
					}
					if(res.code==400){
						uni.showToast({
							'title':'账户已存在，注册失败',
							'icon':''
						})
					}
				}
			}
		}
	}
</script>

<style lang="scss" scoped>
	page{
		background-image: url("../../static/log1.jpeg");
		background-repeat: no-repeat;
		background-size: cover;
		width: 750rpx;
		height: 100%;
		display: flex;
		flex-direction: column;
	}
	.total{
		width: 750rpx;
		height: 100%;
		.title{
			display: flex;
			flex-direction: column;
			width: 100%;
			height: 15%;
			align-items: center;
			justify-content: start;
			text-align: start;
			margin-top: 70px;
			margin-left: 20px;
			.hello,.tv{
				width: 100%;
				font-size: 30px;
				font-weight: 600;
				color: white;
			}
		}
		.box{
			width: 100%;
			height: 76%;
			background-color: white;
			margin: 0 auto;
			border-top-right-radius: 20px;
			border-top-left-radius: 20px;
			.choice{
				position: relative;
				top: 30px;
				margin:0 auto;
				width: 80%;
				height: 50px;
				display: flex;
				justify-content: space-around;
				.login,.register{
					width: 45%;
					height: 100%;
					font-size: 18px;
					line-height: 50px;
					text-align: center;
					border-radius: 25px;
					background-color: rgb(61,132,220,0.3);
					color: #3D84DC;
					&.active{
						background-color: #3D84DC;
						color: white;
					}
				}
				
			}
			.input{
				width: 80%;
				margin: 30px auto;
				position: relative;
				top: 30px;
				.phone,.passwd{
					width: 100%;
					height: 45px;
					background-color: rgb(212, 212, 212,0.4);
					border-radius: 15px;
					margin-bottom: 15px;
					text-indent: 20px;
				}
				button{
					border-radius: 23px;
					background-color: #4086DC;
					color: white;
				}
				
			}
			.user{
				width: 50%;
				margin: 0 auto;
				position: relative;
				top: 20px;
				display: flex;
				justify-content: center;
				.question{
					color: #c2c2c2;
				}
				.yes{
					margin-left: 10px;
					color: #1ea0e5;
				}
			}
		}
	}
	
</style>