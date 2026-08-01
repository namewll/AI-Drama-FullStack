<template>
	<view class="content">
		<view class="top">
			<!-- 主标题 -->
			<view class="title">
				<text>
					欢迎登录
				</text>
			</view>
			<!-- 副标题 -->
			<view class="sub">
				<text>
					还没有账号，<text class="text" @tap="pageTo('/pages/index/enroll')">立即注册</text>
				</text>
			</view>
		</view>
		<view class="middle">
			<form ref="form" @submit="submit()">
				<view class="inputStyle">
					<view class="label">
						+86
					</view>
					<input type="number" v-model="formData.number" maxlength="11" placeholder-class="placeholderClass"
						placeholder="输入手机号" />
				</view>
				<view class="inputStyle">
					<input v-show="!isPassword" type="safe-password" v-model="formData.password" password maxlength="18"
						placeholder-class="placeholderClass" placeholder="输入密码" />
					<input v-show="isPassword" type="text" v-model="formData.password" maxlength="18"
						placeholder-class="placeholderClass" placeholder="输入密码" />
					<uni-icons v-if="formData.password" :type="`${isPassword?'eye-slash-filled':'eye-filled'}`"
						size="22" @tap="showPassword()"></uni-icons>
				</view>
				<view class="button">
					<button type="primary" form-type="submit" class="primary">登录</button>
				</view>
				<view class="button-text" @tap="pageTo('/pages/index/enroll')">
					短信验证
				</view>
			</form>
		</view>
		<view class="bottom">
			<view class="item" @tap="setwx">
				<image src="/static/微信.png"></image>
			</view>
			<view class="item" @tap="setwb">
				<image src="/static/微博.png"></image>
			</view>
		</view>
	</view>
</template>

<script setup>
	import {
		ref,
		reactive
	} from 'vue';
	import {
		pageTo
	} from '/utlis/index.js';
	// 表单
	const formData = reactive({
		number: '',
		password: ''
	});
	const isPassword = ref(false);

	//切换密码显示
	const showPassword = () => {
		isPassword.value = !isPassword.value;
	}

	//提交表单(登录)
	const submit = () => {
		uni.showToast({
			title: '登录！'
		})
	}

	//点击微信
	const setwx = () => {
		uni.showToast({
			title: '微信！'
		})
	}
	//点击微博
	const setwb = () => {
		uni.showToast({
			title: '微博！'
		})
	}
</script>

<style scoped lang="scss">
	* {
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	}

	.content {

		.top {
			padding-top: 60px;
			padding-left: 20px;
			padding-right: 20px;
			padding-bottom: 50px;

			.title {
				text {
					font-size: 24px;
					font-weight: bold;
				}
			}

			.sub {
				padding-top: 10px;

				text {
					font-size: 14px;
					color: #999;

					.text {
						color: #2e95ff;
					}
				}
			}
		}

		.middle {
			padding: 20px;
			padding-top: 0;


			.inputStyle {
				display: flex;
				align-items: center;
				margin-bottom: 20px;
				background-color: #f3f5f5;
				padding: 12px 20px;
				border-radius: 40px;
				font-size: 14px;

				.label {
					padding-right: 10px;
					font-weight: 500;
				}

				.placeholderClass {
					color: #bcbcbc;
					font-size: 12px;
				}

				input {
					width: 100%;
				}
			}

			.button {
				margin-top: 30px;
			}

			.primary {
				display: flex;
				justify-content: center;
				align-items: center;
				border-radius: 40px;
				height: 40px;
				font-size: 14px;
				box-shadow: 3px 5px 10px #eee, 4px 6px 30px #eee;
			}

			.button-text {
				display: flex;
				justify-content: center;
				align-items: center;
				font-size: 14px;
				color: #666;
				margin-top: 20px;
			}
		}

		.bottom {
			display: flex;
			justify-content: center;
			margin-top: 20px;

			.item {
				display: flex;
				justify-content: center;
				align-items: center;
				flex-shrink: 1;
				padding: 5px;
				margin: 20px;
				border-radius: 100px;
				background-color: #939393;

				image {
					width: 30px;
					height: 30px;
				}
			}
		}
	}
</style>