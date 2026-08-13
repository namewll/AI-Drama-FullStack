<template>
	<view v-show="loadSuccess" class="detail_wrapper">
		<view class="detail_top_wrapper">
			<view class="left">
				<image class="img" :src="detail.img"></image>
			</view>
			
			<view class="right">
				<view class="name">
					<text class="text_name">{{detail.title}}</text>
				</view>
				<view class="episode_cnt">
					<text class="text_epcnt">全{{detail.episode_cnt}}集</text>
				</view>
				<view class="tv_type">
					<uni-tag v-for="tag in show_tags" :text="tag" class="tag"/>
				</view>
			</view>
		</view>
		<view class="horizontal_line"></view>
		
		<view class="brif_info_wrapper">
			<view class="brif_info" :class="{'active':state==false}">
				<text selectable='true'>{{detail.info}}</text>
			</view>
			<view class="info_state_total" v-if="detail.info.length>50" @click="change_state">
				<view class="info_state">{{state ? "展开":"收起"}}</view>
				<uni-icons :type="state ? 'down':'up'" size="20"></uni-icons>
			</view>
		</view>
		
		<view class="episode_wrapper">
			<view class="episode_head">
				<view class="title_head">剧情</view>
				<view class="content_head">已完结&nbsp;共{{detail.episode_cnt}}集
					<uni-icons type="right" size="15" color="#a8a8a8"></uni-icons>
				</view>
			</view>
			<view class="episode_midd">
				<scroll-view 
					class="scroll_top"
					scroll-x="true"
					scroll-left="0"
					show-scrollbar="false">
					<view 
						class="episode_cut" 
						v-for="epcut,index in episode_cut" 
						:key="index" 
						@click="cut_state=index"
						:class="{'active':cut_state==index}">
						{{epcut.start}}-{{epcut.end}}
					</view>
				</scroll-view>
				
				<scroll-view class="scroll_low hide_scrollbar" scroll-x="true" scroll-left="0" show-scrollbar="false">
					<view class="item" 
					v-for="item in show_episode[cut_state]"
					:key="item"
					@click="chang_epi(item,cut_state)"
					:class="{'active':item==detail.progress}">{{item}}</view>
				</scroll-view>
			</view>
		</view>
		
		<view class="coll_like_wrapper">
			<view class="collect_wrapper" @click="change_coll">
				<text>{{detail.collect?"已收藏":"收藏"}}</text>
				<uni-icons :type="detail.collect?'star-filled':'star'" size="20" :color="detail.collect?'#ffba15':''"></uni-icons>
			</view>
			<view class="like_wrapper" @click="change_like">
				<text>{{detail.like?"已点赞":"点赞"}}</text>
				<uni-icons :type="detail.like?'heart-filled':'heart'" size="20" :color="detail.like?'#fe3259':''"></uni-icons>
			</view>
		</view>
	</view>	
</template>

<script>
	// import {playletStore} from "/stores"
	// const store=playletStore()
	export default {
		data() {
			return {
				detail:{
					clipId:"",
					kind:[],
					info:"",
					episode_cnt:0,
					progress:0,
					collect:false,
					like:false,
					video_total:[]
				},
				state:true,
				cut_state:0,
				loadSuccess:false
			}
		},
		methods: {
			async get_detail_data(id){
				let {data:res}=await uni.$http.get('/api/playlet/detail',{id:id})
				if(res.code===200){
					this.detail=res.data;
					this.loadSuccess=true;
				}
				else{
					uni.showToast({
						title:"数据加载失败,请检查网络",
						icon:"none"
					})
				}
			},
			async get_history(id){
				let {data:res}=await uni.$http.get('/select/history')
				console.log("hij");
				console.log(res);
			},
			change_state(){
				this.state=!this.state
			},
			async change_coll(){
				this.detail.collect=!this.detail.collect
				if(this.detail.collect){
					let {data:res}=await uni.$http.get('/add/history',{
						"card":JSON.stringify(this.detail)
					})
				}
				else{
					let {data:res}=await uni.$http.get('/delete/history',{
						"card":JSON.stringify(this.detail.clipId)
					})
				}
			},
			async change_like(){
				this.detail.like=!this.detail.like
				if(this.detail.like){
					let {data:res}=await uni.$http.get('/add/history',{
						"card":JSON.stringify(this.detail)
					})
				}
				else{
					let {data:res}=await uni.$http.get('/delete/history',{
						"card":JSON.stringify(this.detail.clipId)
					})
				}
				
			},
			async chang_epi(index,cut_state){
				this.detail.progress=index
				const videoUrl=`https://www.mgtv.com/b/${this.detail.clipId}/${this.detail.video_total[index+index*cut_state]}.html?fpa=se&lastp=so_result`
				// #ifdef H5
				window.open(videoUrl, '_blank');
				// #endif
				let {data:res}=await uni.$http.get('/add/history',{
					"card":JSON.stringify(this.detail)
				})
			}
		},
		async onLoad(detail_id){
			this.loadSuccess=true
			let {data:res}=await uni.$http.get('/select/history',{id:detail_id.id})
			if(res){
				this.detail=res;
			}	
			else{
				await this.get_detail_data(detail_id.id)
			}
			console.log(this.detail);
		},
		computed:{
			show_tags(){
				let curLen=0
				return this.detail.kind.filter((tag,index)=>{
					curLen+=tag.length
					return curLen<=60 && index<10
				})
			},
			episode_cut(){
				let cut=[]
				let start_ep=1
				let cur_ep=this.detail.episode_cnt
				while(true){
					if(cur_ep<=30){
						cut.push({
							start:start_ep,
							end:this.detail.episode_cnt
						})
						break
					}
					else{
						cut.push({
							start:start_ep,
							end:start_ep+29
						})
					}
					start_ep+=30
					cur_ep-=30
				}
				return cut
			},
			show_episode(){
				return this.episode_cut.map((item,index)=>{
					let episode_list=[]
					for(let i=item.start;i<=item.end;i++){
						episode_list.push(i)
					}
					return episode_list
				})
			}
		}
	}
</script>

<style lang="scss">
	.detail_wrapper{
		.detail_top_wrapper{
			width: 100%;
			display: flex;
			justify-content: space-around;
			margin: 10px auto;
			.left{
				.img{
					width: 250rpx;
					height: 360rpx;
					border-radius: 10px;
				}
			}
			.right{
				display: flex;
				flex-direction: column;
				width: 380rpx;
				padding-top: 10px;
				.name{
					.text_name{
						font-size: 20px;
						font-weight: 600;
					}
				}
				.episode_cnt{
					margin-top: 8px;
					.text_epcnt{
						color: #999999;
					}
				}
				.tv_type{
					display: flex;
					justify-content: start;
					margin-top: 8px;
					flex-wrap: wrap;
					.tag{
						font-size: 12px;
						height: 18px;
						line-height: 18px;
						margin: 3px;
					}
				}
			}
		}
		.horizontal_line{
			width: 100%;
			height: 1px;
			background-color: #999999;
			margin-top: 20px;
		}
		.brif_info_wrapper{
			margin-top: 20px;
			width: 100%;
			.brif_info{
				display: -webkit-box;
				-webkit-line-clamp: 2;
				-webkit-box-orient: vertical;
				overflow: hidden;
				&.active{
					-webkit-line-clamp:unset;
					display: block;
				}
			}
			.info_state_total{
				display: flex;
				align-items: center;
				float: right;
				.info_state{
					color: deepskyblue;
				}	
			}
		}
		.episode_wrapper{
			width: 100%;
			margin-top: 30px;
			.episode_head{
				display: flex;
				justify-content: space-between;
				align-items: center;
				.title_head{
					font-size: 18px;
					font-weight: 600;
					margin-left: 10px;
				}
				.content_head{
					font-size:15px;
					color: #a8a8a8;
				}
			}
			.episode_midd{
				width:100%;
				margin-top: 7px;
				.scroll_top{
					width: 100%;
					height: 50px;
					display: flex;
					white-space: nowrap;
					.episode_cut{
						display: inline-block;
						width: 60px;
						height: 30px;
						line-height: 30px;
						text-align: center;
						margin-right: 10px;
						color: #a8a8a8;
						&.active{
							color: #00aa9e;
							font-weight: 600;
						}
					}
				}
				.scroll_low{
					width: 100%;
					margin-top: -10px;
					display: flex;
					flex-direction: row;
					white-space: nowrap;
					margin-left: 10px;
					.item{
						display: inline-block;
						width: 45px;
						height: 45px;
						background-color: #f1f1f1;
						// background-color: #f8d629;
						line-height: 45px;
						text-align: center;
						border-radius: 8px;
						margin-right: 10px;
						font-weight: 500;
						&.active{
							// background-color: rgba(35, 221, 206, 0.6);
							background-color: #e4faf8;
							color: #00aa9e;
							font-weight: 600;
							font-size: 18px;
						}
					}
					.item:nth-last-child(1){
						margin-right:3px
					}
				}
			}
		}
		.coll_like_wrapper{
			width: 100%;
			position: fixed;
			bottom: 5rpx;
			display: flex;
			justify-content: space-around;
			.collect_wrapper,.like_wrapper{
				width: 100px;
				height: 50px;
				background-color: #f5f5f5;
				display: flex;
				justify-content: center;
				align-items: center;
				border-radius: 10px;
			}
		}
	}	
</style>