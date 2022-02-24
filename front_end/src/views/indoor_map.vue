<template>
    <div class="map">
        <img
            src="../assets/img/DJ室内布局图.svg"
            usemap="#image-map"
            class="img"
        />
        <map name="image-map">
            <area
                v-for="item in rssList"
                :key="item.id"
                target=""
                alt=""
                v-bind:title="'RSS：'+item.rss+'\n'+'xLabel:'+item.xlabel+'\n'+'yLabel:'+item.ylabel"
                href=""
                v-bind:coords="
                    parseInt(19.5 * item.ylabel + 107.7) +
                    ',' +
                    parseInt(-20 * item.xlabel + 616.6) +
                    ',' +
                    7
                "
                shape="circle"
            />
        </map>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "indoor-map",
    components: {
        // HelloWorld
    },
    data() {
        return {
            rssList: [],
        };
    },
    mounted() {
        this.getRssList();
    },
    methods: {
        getRssList() {
            axios({
                url: "http://127.0.0.1:9000/get-rss-list/",
                type: "json",
                method: "get",
            }).then((res) => {
                console.log(res);
                this.rssList = res.data;
            });
        },
    },
};
</script>

<style>
.map {
    text-align: center;
}
</style>
