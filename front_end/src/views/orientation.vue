<template>
    <div class="orientation">
        <div class="RSS">
            <span>RSS指纹:</span>
            <input v-model="rss" type="text" placeholder="输入RSS" />
        </div>
        <div class="position" v-if="location != ''">
            Prediction :
            <td class="opttd">{{ location }}</td>
        </div>
        <div class="position" v-else>
            Prediction :
            <td class="deftd">预测坐标将显示在此处</td>
        </div>
        <div class="position" v-if="testLocation != ''">
            Real :
            <td class="opttd">{{ testLocation }}</td>
        </div>
        <div class="position" v-else>
            Real :
            <td class="deftd">真实坐标将显示在此处</td>
        </div>
        <div class="position" v-if="testDisplay == 1">
            Accuracy :
            <td class="opttd">
                NN: {{ accuracy[0] }}, KNN: {{ accuracy[1] }}, WK-NNC:
                {{ accuracy[2] }}
            </td>
        </div>
        <div class="position" v-else>
            Accuracy :
            <td class="deftd">NN准确度, KNN准确度, WKNNC准确度</td>
        </div>
        <button @click="submit">上传RSS</button>
        <button @click="test">算法测试</button>
        <div v-if="testDisplay == 1" class="view">
            <img src="../assets/NN_KNN_WKNNC.jpg" />
        </div>
        <div class="view" style="position: relative">
            <img src="../assets/img/DJ室内布局图.svg" />
            <a
                title="预测位置"
                v-bind:style="
                    'display:block;position:absolute; left:' +
                    parseInt(19.5 * location[1] + 453.7) +
                    'px;top:' +
                    parseInt(-20 * location[0] + 616.6) +
                    'px;width:7px;height:7px;border-radius:50%;background:#207f4c'
                "
            ></a>
            <a
                title="正确位置"
                v-bind:style="
                    'display:block;position:absolute; left:' +
                    parseInt(19.5 * testLocation[1] + 453.7) +
                    'px;top:' +
                    parseInt(-20 * testLocation[0] + 616.6) +
                    'px;width:7px;height:7px;border-radius:50%;background:#ec2b24'
                "
            ></a>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";

export default {
    name: "orientation",
    data() {
        return {
            rss: "",
            location: [],
            rssList: [],
            testLocation: [],
            testDisplay: 0,
            accuracy: "",
        };
    },
    mounted() {},
    methods: {
        submit() {
            console.log(this.rss);
            var rss = this.rss;
            if (rss.length > 0) {
                axios({
                    url: "http://127.0.0.1:9000/orientation/",
                    data: Qs.stringify({
                        rss,
                    }),
                    method: "post",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                }).then((res) => {
                    console.log(res);
                    this.location = res.data[0];
                    this.testLocation = res.data[1];
                });
            }
        },
        test() {
            if (this.testDisplay == 0) {
                this.testDisplay = 1;
            } else {
                this.testDisplay = 0;
                this.accuracy = "";
            }
            if (this.testDisplay == 1) {
                axios({
                    url: "http://127.0.0.1:9000/algorithmTest",
                    method: "get",
                    type: "json",
                }).then((res) => {
                    console.log(res.data[0]);
                    this.accuracy = res.data;
                });
            }
        },
    },
};
</script>

<style>
td {
    border: 1px solid rgba(0, 0, 0, 0.274);
    /* min-width: 80px; */
}
td:hover {
    background-color: rgba(128, 128, 128, 0.192);
}
input {
    background-color: rgba(197, 197, 197, 0.397);
    margin: 5px 10px;
    width: 80px;
    border-radius: 4px;
    height: 8px;
    padding: 10px;
}
button {
    border-radius: 8px;
    height: 30px;
    margin: 10px;
    width: 80px;
    outline: none;
}
button:hover {
    background-color: rgba(128, 128, 128, 0.4);
}
button:active {
    background-color: rgba(128, 128, 128, 0.9);
}
span {
    font-size: 15px;
    font-weight: bold;
}
.opttd {
    font-size: small;
    color: rgba(41, 37, 37, 0.9);
    margin: 5px 10px;
    border-radius: 4px;
    background-color: rgba(197, 197, 197, 0.397);
}
.deftd {
    font-style: italic;
    font-size: small;
    color: rgba(88, 83, 83, 0.4);
    margin: 5px 10px;
    border-radius: 4px;
    background-color: rgba(197, 197, 197, 0.397);
}
.position {
    font-size: 15px;
    font-weight: bold;
    border-radius: 8px;
    line-height: 30px;
    /* height: 30px;
    width: 30px; */
    outline: none;
}
.orientation .view img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>

