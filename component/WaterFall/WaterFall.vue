<template>
	<view class="content">
		
		<view class="left">
			<view class="block" v-for="card in get_left_cards" :key="card.clipId" @click="go_detail(card.clipId)">
				<image :src="card.img" class="bg_img"></image>
				<view class="title">
					<text class="text_title">{{card.title}}</text>
				</view>
				<view class="tag">
					<text class="text_tag">{{(card.kind || []).join("·")}}</text>
				</view>
			</view>
		</view>
		
		<view class="right">
			<view class="block" v-for="card in get_right_cards" :key="card.clipId" @click="go_detail(card.clipId)">
				<image :src="card.img" class="bg_img"></image>
				<view class="title">
					<text class="text_title">{{card.title}}</text>
				</view>
				<view class="tag">
					<text class="text_tag">{{(card.kind || []).join("·")}}</text>
				</view>
			</view>
		</view>
		
	</view>
</template>

<script>
	export default {
		props:{
			cards:{
				typeof:Object,
				default:[]
			}
		},
		data() {
			return {
				
			}
		},
		methods: {
			async go_detail(param){
				uni.navigateTo({
					url:"/pages/detail/detail?id="+param
				})
			}
		},
		mounted() {
			console.log(this.cards);
		},
		computed:{
			get_left_cards(){
				return this.cards.filter((item,index)=>{
					return index%2==0
				})
			},
			get_right_cards(){
				return this.cards.filter((item,index)=>{
					return index%2==1
				})
			}
		}
	}
</script>

<style lang="scss">
	.content{
		width:100%;
		display:flex;
		justify-content: space-between;
		.left,.right{
			width: 350rpx;
			.block{
				width: 350rpx;
				border-radius: 30px;
				margin-bottom: 10px;
				.bg_img{
					width: 100%;
					height: 490rpx;
					border-radius: 15px;
				}
				.title{
					padding: 0 10px;
					.text_title{
						font-size: 15px;
						font-weight: 600;
					}
				}
				.tag{
					padding-left: 10px;
					padding-right: 30px;
					overflow: hidden;
					text-overflow: ellipsis;
					.text_tag{
						font-size: 13px;
						color: #999997;
						white-space: nowrap;
					}
				}
			}
		}
	}
</style>
