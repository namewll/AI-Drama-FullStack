<template>
	<view>
		<view class="head_wrapper">
			<view class="left">
				<image class="image" :src="image_load[0]" @click="previewImage(image_load)"></image>
				<uni-icons type="upload" size="20" style="position: relative;top: 60px;" @click="chooseImage()"></uni-icons>
			</view>
			<view class="right">
				<view class="my_name">{{my_info.name}}</view>
				<view class="info_wrapper">
					<view class="att">{{my_info.attention}}关注</view>
					<view class="fan">{{my_info.fans}}粉丝</view>
					<view class="like">{{my_info.getlike}}获赞</view>
				</view>
			</view>
		</view>
		
		<view class="tail">
			<view class="nav">
				<view class="history" @click="change_state(0)" :class="{'active':state==0}">历史</view>
				<view class="collect" @click="change_state(1)" :class="{'active':state==1}">收藏</view>
				<view class="like" @click="change_state(2)" :class="{'active':state==2}">点赞</view>
			</view>
		</view>
		
		<view class="last">
			<ThreeCard :cards="cards" :state="state" @refresh-data="handleRefreshData"></ThreeCard>
		</view>
	</view>
</template>

<script>
	import ThreeCard from '../../component/ThreeCard/ThreeCard.vue'
	// import {playletStore} from "/stores"
	// const store=playletStore()
	export default {
		components:{
			ThreeCard
		},
		data() {
			return {
				my_info:{},
				state:0,
				history:[],
				collect:[],
				like:[],
				cards:[],
				image_load:[]
			}
		},
		methods: {
			async chooseImage() {
			    uni.chooseImage({
			        count: 1,
			        success: (res) => {
			            let tempPath = res.tempFilePaths[0];
			            uni.uploadFile({
			                url: 'http://127.0.0.1:5001/api/upload',
			                filePath: tempPath,
			                name: 'image',
							success: async(uploadRes) => {
								await this.get_image_load()  
							}
			            })
			        }
			    })
			},
			async get_image_load(){
				let{data:res}=await uni.$http.get('/api/get/Image')
				this.image_load=res
				console.log("yuyu");
				console.log(this.image_load);
			},
			previewImage(current){
				uni.previewImage({
					urls:this.image_load,
					current
				})
			},
			async handleRefreshData(){
				await this.get_total_history()
				await this.get_total_collect()
				await this.get_total_like()
			},
			async get_my_info(){
				let {data:res}=await uni.$http.get("/api/user/user_info",{
					user_id:"u_001"
				})
				if(res.code===200){
					console.log(res.data);
					this.my_info=res.data
				}
			},
			async change_state(key){
				this.state=key
				await this.get_my_info()
				if(key===0){
					await this.get_total_history()
				}
				if(key===1){
					await this.get_total_collect()
				}
				if(key===2){
					await this.get_total_like()
				}
			},
			async get_total_history(){
				let{data:res}=await uni.$http.get('/select/total/history')
				console.log("history");
				this.cards=res.reverse()
				console.log(res);
			},
			async get_total_collect(){
				let{data:res}=await uni.$http.get('/select/total/collect')
				console.log("collect");
				this.cards=res.reverse()
				console.log(res);
			},
			async get_total_like(){
				let{data:res}=await uni.$http.get('/select/total/like')
				console.log("like");
				this.cards=res.reverse()
				console.log(res);
			},
		},
		async onShow(){
			await this.get_my_info()
			await this.get_total_history()
			await this.get_image_load()
		}
	}
</script>

<style lang="scss">
	.head_wrapper{
		width: 100%;
		display: flex;
		justify-content: center;
		margin-top: 30px;
		.left{
			width: 330rpx;
			display: flex;
			.image{
				width: 80px;
				height: 80px;
				border-radius: 50%;
				margin-left: 60px;
			}
		}
		.right{
			flex: 1;
			display: flex;
			flex-direction: column;
				.my_name{
					font-size: 20px;
					font-weight: 600;
				}
				.info_wrapper{
					display: flex;
					margin-top: 20px;
					.att,.fan,.like{
						width: 30%;
						text-align: center;
						color: #989898;
					}
				}
		}
	}
	.tail{
		margin-top: 30px;
		.nav{
			display: flex;
			justify-content: space-around;
			.history,.collect,.like{
				font-size: 16px;
				color: #989898;
				&.active{
					color: black;
					font-weight: 500;
				}
			}
		}
	}
	.last{
		margin-top: 20px;
	}
</style>