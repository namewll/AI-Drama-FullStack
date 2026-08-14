<template>
	<view class="wrapper">
		<view class="item" v-for="card,index in cards" @click="go_detail(card.clipId)" @longpress="testRightClick(index,card)">
			<image :src="card.img" class="image"></image>
			<view class="name">{{card.title}}</view>
			<view v-show="!(state<=2)" class="info">{{(card.type && card.type[0]) || '未分类'}}·全{{card.episode_cnt}}集</view>
			<view v-show="state==0" class="info">观看至{{Math.floor((card.progress)/card.episode_cnt*100)}}%</view>
			<view v-show="state==1 || state==2" class="info">看至{{card.progress}}集/全{{card.episode_cnt}}集</view>		
		</view>
	</view>
</template>

<script>
	export default {
		props:["cards","state"],
		data() {
			return {
				
			}
		},
		methods: {			
			go_detail(param){
				uni.navigateTo({
					url:"/pages/detail/detail?id="+param
				})	
			},
			testRightClick(index,card){
				uni.showModal({
					title: '确认删除',
					content: '确定要删除这条消息吗？',
					success: async (res) => {
						if (res.confirm) {
							let {data:resp}=await uni.$http.get("/delete/history",{
								card:card.clipId
							})
							uni.showToast({ title: '已删除' })
							this.$emit('refresh-data')
						}
					}
				})
			}
		},
		mounted(){
			console.log(this.cards);
		}
	}
</script>

<style lang="scss">
	.wrapper{
		display: flex;
		flex-wrap: wrap;
		margin-left: 5px;
		.item{
			width: 123px;
			height: 223px;
			border-radius: 15px;
			.image{
				width: 115px;
				height: 160px;
				border-radius: 15px;
			}
			.name{
				white-space: nowrap;
				overflow: hidden;
				text-overflow: ellipsis;
				text-align: center;
				font-size: 15px;
			}
			.info{
				font-size: 13px;
				text-align: center;
				color: #a5a5a5;
			}
		}
	}
</style>
