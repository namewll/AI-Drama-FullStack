<template>
	<view v-for="item in cards[0]['short_video']" class="total" @click="go_video(item['url'])">
		<view class="left">
			<image class='image' :src="item['pic']"></image>
			<view class="during" v-if="cards[0]['name']===false">{{item['updateInfo']}}</view>
		</view>
		
		<view class="right">
			<view class="title" v-if="cards[0]['name']" style="height: 90px;display: flex;align-items: center;margin-top: 15px;">{{item['title']}}</view>
			<view class="title" v-else>{{item['subtitle']}}</view>
			<view class="info" v-if="cards[0]['name']===false">
				<view class="time">时间：{{item['pic'].split('/').slice(5, 8).join('-')}}</view>
				<view class="type">类型：{{cards[0]['kind'].join('·')}}</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		props:["cards"],
		data() {
			return {
				
			}
		},
		methods: {
			go_video(url){
				window.open(url,'_blank')
			}
		}
	}
</script>

<style lang="scss">
	.total{
		margin-top: 20px;
		display: flex;
		align-items: center;
		justify-content: space-around;
		.left{
			.image{
				width: 150px;
				height: 90px;
				border-radius: 10px;
			}
			.during{
				position: relative;
				top: -26px;
				left:108px;
				font-size: 13px;
				color: #F8F7F7;
				
			}
		}
		.right{
			margin-top: -25px;
			width: 180px;
			height: 90px;
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: start;
			.title{
				width: 180px;
				height: 35px;
				font-weight: 500;
				text-align: start;
			}
			.info{
				margin-top: 5px;
				width: 180px;
				height: 40px;
				color: #c2c2c2;
				font-size: 12px;
				font-weight: 350;
		        display: flex;
				flex-direction: column;
				align-items: center;
				justify-content: start;
				.time,.type{
					width: 180px;
					text-align: start;
					margin-top: 5px;
				}
			}
		}
	}
</style>