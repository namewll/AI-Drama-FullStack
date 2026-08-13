<template>
	<view v-show="role===0">
		<view class="head_wrapper">
			<view class="head">
				<uni-icons type="headphones" size="30" class="icon"></uni-icons>
				<view class="title">剧小迷</view>
			</view>
		</view>
		
		<view class="modd_wrapper">
			<view class="ai_wrapper">
				<image src="../../static/my_image/ai.jpeg" class="ai_image"></image>
				<view class="ai_chat">你好,我是剧小迷！</view>
			</view>
			
			<view class="couple" v-for="index in my_infos.length" :key="index"  @longpress="testRightClick(index)">
				<view class="user_wrapper" v-show="user_show">
					<view v-if="!my_infos[index-1].includes('http')" class="user_chat">{{my_infos[index-1]}}</view>
					<image v-else :src="my_infos[index-1]"></image>
					<image src="../../static/my_image/img1.jpeg" class="user_image"></image>
				</view>
				<view class="ai_wrapper" v-show="ai_show">
					<image src="../../static/my_image/ai.jpeg" class="ai_image"></image>
					<view class="ai_chat">{{ai_infos[index-1]}}</view>
				</view>
			</view>
		</view>
		
		<view class="tail_wrapper">
			<view class="tail">
				<button size="mini" class="add_button" @click="change_role">
					<uni-icons type="plus" size="28" class="add_icon" color="#6a6a6a"></uni-icons>
				</button>
				<textarea @blur="bindTextAreaBlur" auto-height class="input_chat" placeholder="请输入想咨询的问题" v-model="user_input"/>
				<button size="mini" class="add_button" @click="send_user_info">
					<uni-icons type="arrow-up" size="28" class="add_icon" color="#6a6a6a"></uni-icons>
				</button>
			</view>
		</view>
		
	</view>
	<view v-show="role===1">
		<view class="head_wrapper">
			<view class="head">
				<uni-icons type="headphones" size="30" class="icon"></uni-icons>
				<view class="title">计算机专家</view>
			</view>
		</view>
		
		<view class="modd_wrapper">
			<view class="ai_wrapper">
				<image src="../../static/my_image/ai.jpeg" class="ai_image"></image>
				<view class="ai_chat">你好,我是计算机专家老师！</view>
			</view>
			
			<view class="couple" v-for="index in student_infos.length" :key="index"  @longpress="te_testRightClick(index)">
				<view class="user_wrapper" v-show="student_show">
					<view v-if="!student_infos[index-1].includes('http')" class="user_chat">{{student_infos[index-1]}}</view>
					<image v-else :src="student_infos[index-1]"></image>
					<image src="../../static/my_image/img1.jpeg" class="user_image"></image>
				</view>
				<view class="ai_wrapper" v-show="teacher_show">
					<image src="../../static/my_image/ai.jpeg" class="ai_image"></image>
					<view class="ai_chat">{{teacher_infos[index-1]}}</view>
				</view>
			</view>
		</view>
		
		<view class="tail_wrapper">
			<view class="tail">
				<button size="mini" class="add_button" @click="change_role">
					<uni-icons type="plus" size="28" class="add_icon" color="#6a6a6a"></uni-icons>
				</button>
				<textarea @blur="bindTextAreaBlur" auto-height class="input_chat" placeholder="请输入想咨询的问题" v-model="user_input"/>
				<button size="mini" class="add_button" @click="send_student_info">
					<uni-icons type="arrow-up" size="28" class="add_icon" color="#6a6a6a"></uni-icons>
				</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				response:"",
				user_show:false,
				ai_show:false,
				user_input:'',
				my_infos:[],
				ai_infos:[],
				image_url:'',
				es:null,
				student_infos:[],
				teacher_infos:[],
				student_show:false,
				teacher_show:false,
				role:0
			}
		},
		methods: {
			async send_user_info(){
				if(this.user_input.trim().length>0){
					this.user_show=true
					this.my_infos.push(this.user_input)
					console.log(this.my_infos);
					await this.get_ai_response()
					this.user_input=""
					uni.pageScrollTo({
						scrollTop: 99999,
						duration: 0
					})
				}
			},
			async send_student_info(){
				if(this.user_input.trim().length>0){
					this.student_show=true
					this.student_infos.push(this.user_input)
					console.log(this.student_infos);
					await this.get_teacher_response()
					this.user_input=""
					uni.pageScrollTo({
						scrollTop: 99999,
						duration: 0
					})
				}
			},
			async get_ai_response(){
				if (this.es) {
					this.es.close();
					this.es = null;
				}
				const url = `http://127.0.0.1:5001/api/chat?content=${encodeURIComponent(this.user_input)}&&role=${this.role}`
				const es = new EventSource(url);
				this.es = es;
				const cur_len = this.ai_infos.length
				this.ai_infos.push("")
				es.onmessage = (res) => {
					if (res.data === '[DONE]') {
						es.close();
						this.es = null;
						return;
					}
					this.ai_infos[cur_len] += res.data;
					uni.pageScrollTo({
						scrollTop: 99999,
						duration: 0
					});
				}
				es.onerror = () => {
					es.close()
					this.es = null
				}
			},
			async get_teacher_response(){
				if (this.es) {
					this.es.close();
					this.es = null;
				}
				const url = `http://127.0.0.1:5001/api/chat?content=${encodeURIComponent(this.user_input)}&&role=${this.role}`
				const es = new EventSource(url);
				this.es = es;
				const cur_len = this.teacher_infos.length
				this.teacher_infos.push("")
				es.onmessage = (res) => {
					if (res.data === '[DONE]') {
						es.close();
						this.es = null;
						return;
					}
					this.teacher_infos[cur_len] += res.data;
					uni.pageScrollTo({
						scrollTop: 99999,
						duration: 0
					});
				}
				es.onerror = () => {
					es.close()
					this.es = null
				}
			},
			// async get_ai_response(){
			// 	const cur_len = this.ai_infos.length
			// 	const response=await fetch("http://127.0.0.1:5001/api/chat",{
			// 		method:"POST",
			// 		headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
			// 		body: `content=${encodeURIComponent(this.user_input)}`
			// 	});
			// 	const reader=response.body.getReader()
			// 	const decoder=new TextDecoder()
			// 	while(true){
			// 		const{done,value}=await reader.read()
			// 		console.log(done,value);
			// 		if(done) break
			// 		const text=decoder.decode(value)
			// 		const data=text.replace(/^data:/,"")
			// 		if(data=="[DONE]")continue
			// 		this.ai_infos[cur_len] += data;
			// 	}
				
			// },
			
			async show_teacher_history(){
				this.student_infos=[]
				this.teacher_infos=[]
				let {data:res}=await uni.$http.get("/teacher/info")
				console.log(res);
				for(let i=0;i<res.length;i++){
					this.student_infos.push(res[i]['user'])
					this.teacher_infos.push(res[i]['ai'])
				}
				this.student_show=true
				this.teacher_show=true
				setTimeout(() => {
					uni.pageScrollTo({
						scrollTop: 99999,
						duration: 0
					})
				}, 100) // 延迟100ms
			},
			async testRightClick(index) {
				 uni.showModal({
					title: '确认删除',
					content: '确定要删除这条消息吗？',
					success: async (res) => {
						if (res.confirm) {
							let {data:resp}=await uni.$http.get("/delete/info",{
								user_text:this.my_infos[index-1],
								ai_text:this.ai_infos[index-1],
								role:this.role
							})
							console.log(resp);
							uni.showToast({ title: '已删除' })
							await this.show_history()
						}
					}
				})
			},
			async te_testRightClick(index) {
				 uni.showModal({
					title: '确认删除',
					content: '确定要删除这条消息吗？',
					success: async (res) => {
						if (res.confirm) {
							let {data:resp}=await uni.$http.get("/delete/info",{
								user_text:this.student_infos[index-1],
								ai_text:this.teacher_infos[index-1],
								role:this.role
							})
							console.log(resp);
							uni.showToast({ title: '已删除' })
							await this.show_teacher_history()
						}
					}
				})
			},
			async show_history(){
				this.my_infos=[]
				this.ai_infos=[]
				let {data:res}=await uni.$http.get("/chat/info")
				console.log(res);
				for(let i=0;i<res.length;i++){
					this.my_infos.push(res[i]['user'])
					this.ai_infos.push(res[i]['ai'])
				}
				this.user_show=true
				this.ai_show=true
				setTimeout(() => {
					uni.pageScrollTo({
						scrollTop: 99999,
						duration: 0
					})
				}, 100) // 延迟100ms
			},
			async change_role(){
				const itemlist = ['剧小迷', '计算机专家老师']
				uni.showActionSheet({
					itemList:itemlist,
					success: async(res) => {
						this.role=res.tapIndex
						console.log(this.role);
						let{data:resp}=await uni.$http.get("/change_role",{role:itemlist[res.tapIndex]})
						console.log(resp);
						if (this.role === 0) {
							await this.show_history()
						} else {
							await this.show_teacher_history()
						}
					}
				})
			}
		},
		onShow(){
			this.role=0
			this.show_history()
		}
	}
</script>

<style lang="scss" scoped>
	page{
		background-image: url("/static/ai_bg/img4.jpg");
		background-size: cover;
		background-repeat: repeat;
	}
	.head_wrapper{
		padding-top:50px ;
		.head{
			width: 100%;
			height: 50px;
			background-color: rgb(181, 198, 169,0.9);
			position: fixed;
			// #ifdef H5
			top: 43px;
			// #endif
			// #ifdef MP-WEIXIN
			top:0px;
			// #endif
			z-index: 100;
			display: flex;
			.icon{
				width: 50px;
				line-height: 50px;
				margin-left: -5px;
			}
			.title{
				width:100px ;
				height: 100%;
				line-height: 50px;
				text-align: start;
				font-size: 17px;
				font-weight: 350;
				margin-left: -5px;
			}
		}
	}
	.modd_wrapper{
		width: 100%;
		.user_wrapper{
			margin-top: 20px;
			width: 100%;
			display: flex;
			justify-content: flex-end;
			.user_image{
				width: 45px;
				height: 45px;
				border-radius: 50%;
			}
			.user_chat{
				background-color: whitesmoke;
				margin-left: 10px;
				margin-right: 10px;
				text-align: start;
				padding: 5px 8px;
				font-size: 18px;
				border-radius: 10px;
				max-width: 50%;
				overflow-wrap: break-word;
				padding:10px;
			}
		}
		.ai_wrapper{
			margin-top: 30px;
			display: flex;
			.ai_image{
				width: 45px;
				height: 45px;
				border-radius: 50%;
			}
			.ai_chat{
				background-color: whitesmoke;
				margin-left: 10px;
				margin-right: 10px;
				text-align: start;
				padding: 5px 8px;
				font-size: 18px;
				border-radius: 10px;
				max-width: 50%;
				overflow-wrap: break-word;
				padding:10px;
			}
		}
	}
	.tail_wrapper{
		padding-bottom: 60px;
		.tail{
			width: 100%;
			height: 55px;
			background-color: rgb(181, 198, 169,0.9);
			position: fixed;
			bottom: 50px;
			// #ifdef MP-WEIXIN
			bottom: 0px;
			// #endif
			display: flex;
			justify-content: space-around;
			align-items: center;
			.input_chat{
				width: 50%;
				height: 45px;
				background-color: white;
				display: flex;
				min-height:45px;
				align-items: center;
				line-height: 20px;
				padding:0 20px ;
				border-radius: 15px;
			}
			.add_button{
				width: 43px;
				height: 43px;
				display: flex;
				justify-content: center;
				align-items: center;
				border-radius: 10px;
			}
		}
	}
</style>