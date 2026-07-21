<template>
	<view class="wrapper">
		<view class="search-wrapper">
			<view class="search-wrapper-bar">
				<view class="search-bar" @click="go_search">
					<uni-icons type="search" size="30"></uni-icons>
				</view>
				<button class="fill" @click="go_fill">
					<uni-icons type="tune-filled" size="20"></uni-icons>
				</button>
			</view>
		</view>
		<WaterFallComponent :cards="cards"></WaterFallComponent>
	</view>
</template>

<script>
	import WaterFallComponent from "/component/WaterFall/WaterFall.vue"
	export default {
		components:{
			WaterFallComponent
		},
		data() {
			return {
				cards:[],
				page:1,
				limit:10
			}
		},
		onLoad() {
			this.get_cards({
				page:this.page,
				limit:this.limit
			})
		},
		methods: {
			go_search(){
				uni.navigateTo({
					url:"/pages/search/search"
				})
			},
			go_fill(){
				uni.navigateTo({
					url:"/pages/fill/fill"
				})
			},
			async get_cards(param){
				console.log(param);
				let {data:res}=await uni.$http.get('/api/playlets',param)
				console.log(res);
				this.cards.splice(this.page*this.limit,0,...res.data.hitDocs)
				console.log("okk");
				// console.log(this.cards);
			}
		},
		onReachBottom(){
			this.page++;
			this.get_cards({
				page:this.page,
				limit:this.limit
			})
			
		}
	}
</script>

<style lang="scss">
.wrapper{
	width: 720rpx;
	padding-top: 100rpx;
	.search-wrapper-bar{
		width: 720rpx;
		height: 110rpx;
		background-color: whitesmoke;
		display: flex;
		align-items: center;
		justify-content: space-around;
		position: fixed;
		top:43px;
		// #ifdef MP-WEIXIN
		top:-1px;
		// #endif
		z-index: 100;
		.search-bar{
			margin-left: 5px;
			width: 600rpx;
			height: 65rpx;
			background-color: white;
			display: flex;
			align-items: center;
			padding-left: 10rpx;
			border-radius: 20rpx;
		}
		.fill{
			width: 60rpx;
			height: 60rpx;
			background-color: white;
			display: flex;
			align-items: center;
			justify-content: center;
			border-radius: 20rpx;
		}
	}
}
</style>
