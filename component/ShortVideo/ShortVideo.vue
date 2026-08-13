<template>
	<view v-for="item in cards[0]['short_video']" class="total" @click="go_video(item)">
		<view class="left">
			<image class='image' :src="item['pic']" mode="widthFix"></image>
			<view class="during" v-if="cards[0]['name']===false">{{item['updateInfo']}}</view>
		</view>
		
		<view class="right">
			<view>
				<view class="title" v-if="cards[0]['name']" style="height: 90px;display: flex;align-items: center;margin-top: 15px;"><text>{{item['title']}}</text></view>
				<view class="title" v-else><text>{{item['subtitle']}}</text></view>
				<view class="info" v-if="cards[0]['name']===false">
					<view class="time">时间：{{item['pic'].split('/').slice(5, 6).join('')}}</view>
					<view class="type">类型：{{cards[0]['kind'].join('·')}}</view>
				</view>
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
			async go_video(item){
				window.open(item['url'],'_blank')
			}
		}
	}
</script>

<style lang="scss">
	.total{
		margin-top: 20px;
		display: flex;
		align-items: center;
		
		.left{
			width: 183px;
	        display: flex;
			align-items: center;
			justify-content: center;
			.image{
				width: 150px;
				border-radius: 10px;
			}
			.during{
				position: relative;
				top: 30px;
				left: -40px;
				font-size: 13px;
				color: #F8F7F7;
				
			}
		}
		.right{
			width: 180px;
			height: 86px;
			display: flex;
			align-items: center;
			.title{
				padding: 0;
				width: 180px;
				font-weight: 500;
				text-align: start;
				margin-bottom: 5px;
				margin-top: 0px !important;
			}
			.info{
				width: 180px;
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
				}
			}
		}
	}
</style>