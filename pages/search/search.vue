<template>
	<view>
		<view class="search_head_wrapper">
			<view class="search_head">
				<uni-search-bar class="search_bar" v-model="search_value" cancelButton="none" clearButton="auto" 
				@confirm="confirm_search"
				@input="input_content"
				@clear="clear_content"
				selectabled="true">
				</uni-search-bar>
				<button class="but_search" size="mini" type="default" @click="click_search">搜索</button>
			</view>
		</view>
		
		<view v-show="!start_search" class="search_history">
			<view class="search_history_top">
				<view class="history_title">搜索历史</view>
				
				<view class="total_state">
					<view class="box_state" @click="change_state">
						<view class="info_">{{state ? "展开":"收起"}}</view>
						<uni-icons :type="state ? 'down':'up'" size="20"></uni-icons>
						<view>|</view>
					</view>
					<uni-icons type="trash-filled" size="25" color="#c2c2c2" @click="clear_block"></uni-icons>
				</view>
				
			</view>
			<view class="history_content">
				<view class="item" :class="{'active':state==true}" v-for="item,index in search_blocks" :key="index" @click="block_search(item)" @longpress="testRightClick(index,item)">{{item}}</view>
			</view>
		</view>
		
		<WaterFall :cards="cards"></WaterFall>
		
		<view class="info">
			&emsp;&emsp;{{cards[0]['story']}}
		</view>
		
		<ShortVideoVue :cards="cards"></ShortVideoVue>
	</view>
</template>

<script>
	import WaterFall from "/component/WaterFall/WaterFall"
	import ShortVideoVue from "../../component/ShortVideo/ShortVideo.vue"
	// import {playletStore} from "/stores"
	// const store=playletStore()
	export default {
		components:{
			WaterFall,
			ShortVideoVue
		},
		data() {
			return {
				search_value:'',
				start_search:false,
				search_blocks:[],
				page:1,
				limit:1,
				cards:[{"story":''}],
				state:true
			}
		},
		methods: {
			async change_state(){
				this.state=!this.state
				if(this.state==true){
					this.search_blocks=this.search_blocks.slice(0,6)
				}
				else{
					await this.show_search_info()
				}
			},
			async confirm_search(){
				if(this.search_value.trim().length>0){
					this.start_search=true
					this.start_search_()
				}
				await this.show_search_info()
				this.search_blocks=this.search_blocks.slice(0,6)
				uni.pageScrollTo({
					scrollTop: -99999,
					duration: 0
				})
				
			},
			async click_search(){
				if(this.search_value.trim().length>0){
					this.start_search=true
					this.start_search_()
				}
				await this.show_search_info()
				this.search_blocks=this.search_blocks.slice(0,6)
				uni.pageScrollTo({
					scrollTop: -99999,
					duration: 0
				})
				
			},
			input_content(){
				this.start_search=false
			},
			clear_content(){
				this.start_search=false
			},
			async clear_block(){
				let{data:res}=await uni.$http.get('/delete/block')
				await this.show_search_info()
			},
			async start_search_(){
				// console.log(this.search_value);
				// console.log(this.limit);
				// console.log(this.page);
				let {data:res}=await uni.$http.get("/api/playlet/search",{
					query:this.search_value,
					limit:this.limit,
					page:this.page
				})
				if(res.code===200){
					console.log(res.data);
					this.cards=res.data;
					if(this.cards.length==0){
						uni.showToast({
							title:"无搜索数据",
							icon:"none"
						})
						console.log("无搜索数据");
					}
				}
				else{
					uni.showToast({
						title:"数据加载失败,请检查网络",
						icon:"none"
					})
				}
			},
			block_search(param){
				this.search_value=param
				this.confirm_search()
			},
			async testRightClick(index,item) {
				 uni.showModal({
					title: '确认删除',
					content: '确定要删除这条消息吗？',
					success: async (res) => {
						if (res.confirm) {
							let {data:resp}=await uni.$http.get("/delete/search_info",{
								title:item
							})
							uni.showToast({ title: '已删除' })
							await this.show_search_info()
						}
					}
				})
			},
			async show_search_info(){
				let{data:res}=await uni.$http.get('/show/search_info')
				this.search_blocks=res.reverse()
			}
		},
		async onShow(){
			await this.show_search_info()
			this.search_blocks=this.search_blocks.slice(0,6)
		}
	}
</script>

<style lang="scss">
	.search_head_wrapper{
		padding-top: 100rpx;
		.search_head{
			width: 100%;
			background-color: white;
			display: flex;
			justify-content: space-around;
			align-items: center;
			position: fixed;
			z-index: 100;
			// #ifdef H5
			top: 43px;
			// #endif
			// #ifdef MP-WEIXIN
			top: -1px;
			// #endif
			.search_bar{
				width: 80%;
			}
			.but_search{
				width: 40px;
				height: 30px;
				line-height: 30px;
				text-align: center;
				padding: 0;
				margin-left: -3px;
			}
			.but_search::after{
				display: none;
			}
		}
	}
	.search_history{
		width:100%;
		margin-top: 10px;
		.search_history_top{
			width:90%;
			margin: 0 auto;
			display: flex;
			justify-content: space-between;
			.history_title{
				font-weight: bold;
				font-size: 16px;
			}
			.total_state{
				width: 130px;
				height: 30px;
				display: flex;
				justify-content: space-around;
				.box_state{
					width: 100px;
					height: 100%;
					display: flex;
					justify-content: space-around;
					.info_,uni-icons,view{
						text-align: center;
						width: 50px;
						height: 100%;
					}
					.info_{
						color: deepskyblue;
					}
					view{
						color: #e8e8e8;
					}
				}
			}
		}
		.history_content{
			width:90%;
			margin: 0 auto;
			.item{
				width: 80px;
				height: 30px;
				margin: 10px;
				display: inline-block;
				background-color: #e8e8e8;
				border-radius: 10px;
				line-height: 30px;
				text-align: center;
				overflow: hidden;
				white-space: nowrap;
				text-overflow: ellipsis;
				padding: 0 6px;
			}
		}
	}
	.update_time{
		color: #FF5F00;
		margin-right: 20px;
		font-size: 17px;
		font-weight: 600;
	}
	.info{
		margin-top: 15px;
		line-height: 30px;
		font-size: 17px;
		padding: 0 10px;
	}
</style>
