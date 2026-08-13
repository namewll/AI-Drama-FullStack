<!-- 本示例未包含完整css，获取外链css请参考上文，在hello uni-app项目中查看 -->
<template>
	<view>
		<view class="uni-margin-wrap">
			<swiper class="swiper" circular :indicator-dots="indicatorDots" :autoplay="autoplay" :interval="interval"
				:duration="duration">
				<swiper-item v-for="card in cards">
					<view class="swiper-item" @click="go_detail(card['jumpId'])">
						<image :src="card['imageNew']" mode='aspectFill'></image>
						<view class="info">
							<view class="title">{{card['name']}}</view>
							<view class="type">{{card['subName']}}</view>
						</view>
					</view>
				</swiper-item>
			</swiper>
		</view>

	</view>
</template>
<script>
export default {
    data() {
        return {
            indicatorDots: true,
            autoplay: true,
            interval: 2000,
            duration: 500,
			cards:[]
        }
    },
    methods: {
		go_detail(param){
			uni.navigateTo({
				url:"/pages/detail/detail?id="+param
			})
		},
        changeIndicatorDots(e) {
            this.indicatorDots = !this.indicatorDots
        },
        changeAutoplay(e) {
            this.autoplay = !this.autoplay
        },
		async get_swiper_data(){
			let{data:res}=await uni.$http.get('/api/swiper')
			if(res.code===200){
				this.cards=res.data
			}
		}
    },
	async mounted(){
		await this.get_swiper_data()
	}
}
</script>
<style lang="scss">
	.uni-margin-wrap {
		width: 720rpx;
		margin-bottom: 5px;
	}
	.swiper {
		height: 500rpx;
	}
	.swiper-item {
		display: block;
		height: 500rpx;
		image{
			width: 100%;
			height: 450rpx;
			border-radius: 10px;
		}
		.info{
			width: 100%;
			height: 50px;
			position: relative;
			top: -65px;
			left: 20px;
			display: flex;
			justify-content: center;
			flex-direction: column;
			align-items: center;
			.title,.type{
				width: 100%;
				height: 100%;
				color: #FFFFFF;
				
			}
			.title{
				font-size: 25px;
				font-weight: 800;
				color: #FFFFFF;
				text-indent: 10px;
			}
			.type{
				font-size: 16px;
				font-weight: 500;
				margin-left: 10px;
				margin-top: 2px;
				color: #ffffff;
			}
		}
	}

</style>
