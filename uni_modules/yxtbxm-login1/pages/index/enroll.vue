<template>
	<view class="content">
		<view class="top">
			<!-- 主标题 -->
			<view class="title">
				<text>
					注册
				</text>
			</view>
			<!-- 副标题 -->
			<view class="sub">
				<text>已有账号了，<text class="text" @tap="pageTo('/pages/index/index')">马上登录</text></text>
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
				<view class="inputStyle justify-space">
					<input type="safe-password" v-model="formData.password" password maxlength="18"
						placeholder-class="placeholderClass" placeholder="输入验证码" />
					<view class="label-left" @tap="sendCode()">
						{{countDownText()}}
					</view>
				</view>
				<view class="button">
					<button type="primary" form-type="submit" class="primary">注册</button>
				</view>
				<view class="button-text" @tap="pageTo('/pages/index/index')">
					账号登录
				</view>
			</form>
		</view>
		<view class="bottom">
			<!-- <view class="item">
				<image src="/static/微信.png" mode=""></image>
			</view>
			<view class="item">
				<image src="/static/微博.png" mode=""></image>
			</view> -->
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
	//是否正在倒计时
	const isCountingDown = ref(false);
	//倒计时秒数
	const countDown = ref(60);

	//提交表单(注册)
	const submit = () => {
		uni.showToast({
			title: '注册！'
		})
	}

	//发送验证码
	const sendCode = () => {
		if (isCountingDown.value) {
			return;
		}
		// 这里可以添加发送验证码的API调用逻辑
		//...
		uni.showToast({
			title: '发送验证码！'
		})
		// 开始倒计时
		isCountingDown.value = true;
		countDownTimer();
	}

	// 显示在按钮上的文本
	const countDownText = () => {
		return isCountingDown.value ? `${countDown.value}秒后重试` : '发送验证码';
	}

	// 递归倒计时函数
	const countDownTimer = () => {
		if (countDown.value > 0) {
			countDown.value -= 1;
			setTimeout(countDownTimer, 1000);
		} else {
			// 倒计时结束，重置倒计时
			countDown.value = 60;
			isCountingDown.value = false;
		}
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

			.justify-space {
				justify-content: space-between;
				font-size: 14px;
				color: #333;
			}

			.inputStyle {
				display: flex;
				align-items: center;
				margin-bottom: 20px;
				background-color: #f3f5f5;
				padding: 10px 20px;
				border-radius: 40px;
				font-size: 14px;

				.label {
					padding-right: 10px;
					font-weight: 500;
				}

				.label-left {
					font-weight: 500;
					white-space: nowrap;
					color: #333;
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