<template>
    <div id="home">
        <div class="header">
            <h1 class="title">东九室内指纹定位可视化系统</h1>
        </div>

        <div class="topnav">
            <div v-for="item in menuList" :key="item.id" class="item">
                <div v-if="item.id == chosed">
                    <a
                        class="tab-item"
                        style="background-color: #333; color: #f1f1f1"
                        >{{ item.text }}</a
                    >
                </div>
                <div v-else @click="chooseMenu(item.id)">
                    <a class="tab-item">{{ item.text }}</a>
                </div>
            </div>
        </div>

        <div class="block">
            <router-view />
        </div>

        <div class="footer">
            <p>@电信1901 胡润龙 付丁捷</p>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            menuList: [],
            chosed: 1,
            chosed_MenuList: "室内地图区",
        };
    },
    mounted() {
        this.getMenuList();
    },
    methods: {
        getMenuList() {
            axios({
                url: "http://127.0.0.1:9000/get-menu-list/",
                type: "json",
                method: "get",
            }).then((res) => {
                this.menuList = res.data;
                console.log(this.menuList);
            });
        },
        chooseMenu(change) {
            this.chosed = change;
            console.log(change);
            for (let index = 0; index < this.menuList.length; index++) {
                const element = this.menuList[index];
                if (element.id == this.chosed)
                    this.chosed_MenuList = element.text;
            }
            // this.$router.push({path:'/',query:{menuId:change}})
            this.$router.push(this.chosed_MenuList);
        },
    },
};
</script>

<style>
body {
    width: 100%;
    height: 100%;
}

#home .header {
    background-color: #f1f1f1;
    padding: 20px;
    text-align: center;
}

#home .topnav {
    overflow: hidden;
    background: transparent;
    /* background-color: #333; */
}

#home .topnav a {
    float: left;
    display: block;
    /* color: #f2f2f2; */
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    width: 100/3%;
    background-color: rgba(128, 128, 128, 0.8);
}

/* #home .topnav a:hover{
    background-color: #ddd;
    color: black;
}  */

#home .footer {
    background-color: #333;
    padding: 10px;
    text-align: center;
    color: #ddd;
}
.tab-item {
    background-color: rgba(155, 155, 155, 0.637);
}
</style>
