import './utils/api.js'
import {createPinia} from "pinia"
const pinia=createPinia()
import App from './App'
import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  app.use(pinia)
  return {
    app,
	pinia
  }
}