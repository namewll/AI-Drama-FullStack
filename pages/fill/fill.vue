<template>
	<view>
		<view class="fill_head">
			<view class="row" v-for="big_card,index1 in big_cards" :key="big_card.row_id">
				<view class="type">
					{{big_card.typeName}}
				</view>
				<scroll-view class="scroll_item hide_scrollbar" scroll-x="true" scroll-left="0" show-scrollbar="false">
					<view class="cell" 
					v-for="detail_block in big_card.items" 
					@click="change_type(index1,detail_block.params)"
					:class="{'active':selected_state[index1]==detail_block.params}">
						{{detail_block.tagName}}
					</view>
				</scroll-view>
			</view>		
		</view>
		
		<view class="cards_low">
			<ThreeCard :cards="cards"></ThreeCard>
		</view>
	</view>
</template>

<script>
	import ThreeCard from "/component/ThreeCard/ThreeCard"
	export default {
		components:{
			ThreeCard
		},
		data() {
			return {
				big_cards:[],
				selected_state:['','','','','',''],
				page:1,
				limit:10,
				cards:[]
			}
		},
		methods: {
			async get_fill_data(){
				let {data:res}=await uni.$http.get('/api/selector')
				if(res.code===200){
					this.big_cards=res.data.listItems
					console.log("uouo");
					console.log(this.big_cards);
				}
				else{
					uni.showToast({
						title:"网络异常,请检查网络"
					})
				}
			},
			change_type(index1,name){
				this.selected_state[index1]=name
				console.log(this.selected_state);
				this.get_card_data()
			},
			async get_card_data(){
				let {data:res}=await uni.$http.get("/api/playlet/screen",{
					background:this.selected_state[0],
					topic:this.selected_state[1],
					setting:this.selected_state[2],
					gender:this.selected_state[3],
					time:this.selected_state[4],
					sort_type:this.selected_state[5],
					limit:this.limit,
					page:this.page
				})
				if(res.code===200){
					console.log(res.data);
					this.cards=res.data
				}
				else{
					uni.showToast({
						title:"请检查网络,数据获取失败"
					})
				}
			},
			async next_card_data(){
				let {data:res}=await uni.$http.get("/api/playlet/screen",{
					background:this.selected_state[0],
					topic:this.selected_state[1],
					setting:this.selected_state[2],
					gender:this.selected_state[3],
					time:this.selected_state[4],
					sort_type:this.selected_state[5],
					limit:this.limit,
					page:this.page
				})
				if(res.code===200){
					console.log(res.data);
					this.cards.splice(this.page*this.limit,0,...res.data)
				}
				else{
					uni.showToast({
						title:"请检查网络,数据获取失败"
					})
				}
			}
		},
		onLoad(){
			this.get_fill_data()
		},
		onShow(){
			this.get_card_data()
		},
		onReachBottom(){
			this.page++
			this.next_card_data()
		}
	}
</script>

<style lang="scss">
	.fill_head{
		width: 100%;
		display: flex;
		flex-direction: column;
		.row{
			display: flex;
			margin-bottom: 3px;
			height: 40px;
			line-height: 40px;
			.type{
				background-color:  #E6FAF7;
				border-radius: 10px;
				font-size: 18px;
				font-weight: 500;
				width: 80px;
				text-align: center;
				height: 30px;
				line-height: 30px;
				padding: 5px;
				color: #71CBC2;
			}
			.scroll_item{
				flex:1;
				display: flex;
				white-space: nowrap;
				margin-left: 20px;
				height: 30px;
				line-height: 30px;
				margin-top: 4px;
				.cell{
					display: inline-block;
					margin-right: 30px;
					font-size: 17px;
					font-weight: 400;
					&.active{
						color: #39bab6;
						font-weight: 600;
					}
				}
			}
		}
	}
	.cards_low{
		margin-top: 20px;
	}
</style>