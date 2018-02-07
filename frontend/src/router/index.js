import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import HelloAgain from '@/components/HelloAgain'
import LeafletExample from '@/components/LeafletExample'
import FactsheetPage from '@/components/FactsheetPage'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/helloagain/:text',
      name: 'HelloAgain',
      component: HelloAgain
    },
    {
      path: '/kaart',
      name: 'LeafletExample',
      component: LeafletExample
    },
    {
      path: '/factsheet',
      name: 'FactsheetComponent',
      component: FactsheetPage
    }
  ]
})
