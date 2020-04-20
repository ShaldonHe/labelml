<template>
  <div class="indexPage">
    <div class="topBox">
      <div class="rightArea">
        <div class="resultArea">
          <div class="checkGroupBox">
            <el-checkbox-group v-model="checkboxGroup1" @change="handleCheckbox">
              <el-checkbox v-for="(item, index) in Legend" :label="item" :key="item">
                <div :style="{color: textColorBox[index]}" class="checkboxItem">{{item}}</div>
              </el-checkbox>
            </el-checkbox-group>
          </div>
          <div class="svgArea">
            <div
              id="svgArea"
              element-loading-spinner="el-icon-loading"
              element-loading-background="rgba(0, 0, 0, 0.4)"
              v-loading="currentFile.name && !(currentFile.points && currentFile.points.shapes)"
            >
              <svg></svg>
            </div>
            <div class="canvasBox" id="viewContainer">
              <canvas id="dcmCanvas"></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import * as d3 from "d3";
import axios from "axios";
import Url from "../../common/request/api";
let svg, canvas;
export default {
  name: "annotator",
  data() {
    return {
      currentFile: {
        uid: ""
      },
      resultWidth: 0,
      picBaseUrl: "http://localhost:2048",
      picArray: [],
      checkboxGroup1: [],
      Legend: [],
      LegendColor: [],
      textColorBox: [],
      reportvisiable:false,
      gradeName: [
        "0 - 单纯",
        "1 - 正常",
        "2 - 海绵",
        "3 - 苔癣",
        "4 - 银屑",
      ],
      gradeindex: 5,
      gradeDict: {
        0:"海绵",
        1:"正常",
        2:"单纯",
        3:"苔癣",
        4:"银屑",
        5:"未分析"},
      showPage: true,
      exportLoading: false
    };
  },
  mounted() {
    let svgArea = document.getElementById("svgArea");
    this.resultWidth = svgArea.clientWidth;
    this.svgCreate(this.resultWidth, svgArea.clientHeight);
  },
  methods: {
    svgCreate(width, height) {
      svg = d3
        .select("svg")
        .attr("height", height)
        .attr("width", width)
        .style("pointer-events", "all")
        .call(
          d3
            .zoom()
            .scaleExtent([1, 4])
            .on("zoom", this.zoomed)
        );
      canvas = document.getElementById("dcmCanvas");
      canvas.height = height;
      canvas.width = width;
    },
    zoomed() {
      var transform = d3.event.transform;
      svg.attr(
        "transform",
        `translate(${transform.x}, ${transform.y}) scale(${transform.k})`
      );
    },
    clearData() {
      svg.selectAll("image").remove();
      svg.selectAll("path").remove();
      this.Legend = [];
      this.LegendColor = [];
      this.textColorBox = [];
      this.reportFormData = {
        name: "",
        sex: "",
        age: "",
        date: "",
        filename: "",
        grade: "",
        reportFormData: "",
        weight: "",
        hypertension: false,
        highBloodSugar: false,
        diabetesYear: ""
      };
    },
    uploadBeforeMethods(file) {
      this.clearData();
      this.picArray.push(file);
      this.currentFile = file;
      this.dDrawPic();
    },
    dDrawPic() {
      svg
        .append("image")
        .attr("xlink:href", this.currentFile.imageLocalPath)
        .attr("width", this.resultWidth)
        .attr("x", 0)
        .attr("y", 0)
        .attr("id", "svgPic");
      this.getImageSize(this.currentFile.imageLocalPath, this.currentFile.uid);
    },
    dDrawPath(data) {
      this.clearData();
      this.dDrawPic();
      this.reportFormData = data.reportFormData
        ? data.reportFormData
        : this.reportFormData;
      if (data.headerInfo) {
        this.reportFormData.name = this.reportFormData.name
          ? this.reportFormData.name
          : data.headerInfo.PatientName || "";
        this.reportFormData.sex = this.reportFormData.sex
          ? this.reportFormData.sex
          : data.headerInfo.PatientSex || "";
        this.reportFormData.age = this.reportFormData.age
          ? this.reportFormData.age
          : data.headerInfo.age || "";
      }
      this.reportFormData.date = this.reportFormData.date
        ? this.reportFormData.date
        : new Date().getTime();
      this.reportFormData.filename = data.name;
      this.reportFormData.grade = data.grade;
      if (!data.points || !data.points.shapes) {
        return;
      }
      this.gradeindex = data.grade
      data.points.shapes.forEach(item => {
        let fillColor = `rgba(${item.fill_color[0]}, ${item.fill_color[1]}, ${
          item.fill_color[2]
        }, ${item.fill_color[3] / 255})`;
        let lineColor = `rgba(${item.line_color[0]}, ${item.line_color[1]}, ${
          item.line_color[2]
        }, ${item.line_color[3] / 255})`;
        let textColor = `rgb(${item.line_color[0]}, ${item.line_color[1]}, ${
          item.line_color[2]
        })`;
        if (this.Legend.indexOf(item.label) === -1) {
          this.Legend.push(item.label);
          this.LegendColor.push(lineColor);
          this.textColorBox.push(textColor);
        }
        let label = item.label;
        let that = this;
        let lineGenerator = d3
          .line()
          .x(function(value) {
            return (value[0] * that.resultWidth) / data.originalPic.width;
          })
          .y(function(value) {
            return (value[1] * that.resultWidth) / data.originalPic.width;
          });
        if (!data) {
          this.$message({
            message: "Drawing error",
            type: "warning"
          });
        }
        let dataFin = item.points;
        let labelFin = label;
        let fillColorFin = fillColor;
        let lineColorFin = lineColor;
        let pathString = lineGenerator(dataFin);
        svg
          .append("path")
          .attr("d", pathString)
          .attr("class", labelFin)
          .attr("stroke", lineColorFin)
          .attr("fill", fillColorFin);
      });
      this.checkboxGroup1 = this.Legend;
    },
    getImageSize(url, uid) {
      let that = this;
      return new Promise(resolve => {
        let image = new Image();
        image.src = url;
        image.onload = function() {
          that.addPicArrayInfo({
            uid: uid,
            originalPic: { width: image.width }
          });
          let height = (that.resultWidth / image.width) * image.height;
          svg.attr("height", height);
          document.getElementById("svgArea").style.height = height + "px";
          resolve();
        };
      });
    },
    handleSuccess(data) {
      this.getPredict(data);
      this.addPicArrayInfo(data);
    },
    addPicArrayInfo(info) {
      return new Promise((resolve, reject) => {
        let that = this;
        this.picArray.forEach((item, index) => {
          if (item.uid === info.uid) {
            this.showPage = false;
            that.picArray[index] = { ...item, ...info };
            this.showPage = true;
            if (item.uid === this.currentFile.uid) {
              this.currentFile = { ...item, ...info };
            }
          }
        });
        resolve("success");
      });
    },
    getPredict(data) {
      axios
        .get(Url.predict, {
          params: {
            processed: data.changedName
          }
        })
        .then(res => {
          this.gradeindex = res.data.grade
          this.addPicArrayInfo({ ...res.data, uid: data.uid }).then(
            this.getDrawPathData
          );
        })
        .catch(err => {
          console.log("err", err);
        });
    },
    getDrawPathData() {
      this.picArray.forEach(item => {
        if (
          item.uid === this.currentFile.uid &&
          item.points &&
          item.points.shapes
        ) {
          this.dDrawPath(item);
        }
      });
    },
    handleCheckbox(data) {
      this.Legend.forEach(item => {
        if (data.indexOf(item) !== -1) {
          d3.selectAll(`.${item}`).attr("display", "block");
        } else {
          d3.selectAll(`.${item}`).attr("display", "none");
        }
      });
    },
    handleImageClick(data) {
      let that = this;
      this.clearData();
      this.picArray.forEach((item, index) => {
        if (item.uid === data.uid) {
          this.currentFile = item;
          this.dDrawPic();
          if (!item.originalPic) {
            this.getImageSize(item.imageLocalPath, item.uid).then(() => {
              that.dDrawPath(item);
            });
          } else {
            that.dDrawPath(item);
          }
        }
      });
    },
    handleCancel(data) {
      this.picArray.forEach((item, index) => {
        if (item.uid === data.uid) {
          this.picArray.splice(index, 1);
        }
      });
      if (data.uid === this.currentFile.uid) {
        console.log(data, this.currentFile);
        let that = this;
        this.clearData();
        if (this.picArray.length > 0) {
          let item = this.picArray[this.picArray.length - 1];
          this.currentFile = item;
          this.dDrawPic();
          if (!item.originalPic) {
            this.getImageSize(item.imageLocalPath, item.uid).then(() => {
              that.dDrawPath(item);
            });
          } else {
            that.dDrawPath(item);
          }
        }
      }
    },
    exportPdf() {
      this.exportLoading = true;
      this.addPicArrayInfo({
        uid: this.currentFile.uid,
        reportFormData: this.reportFormData
      });
      axios
        .get(Url.report, {
          params: {
            infor: this.reportFormData,
            file: this.currentFile.changedName
          }
        })
        .then(res => {
          this.exportLoading = false;
          window.open(this.picBaseUrl + res.data.report_path, "_blank");
        })
        .catch(() => {
          this.exportLoading = false;
        });
    }
  },
  components: {
    Upload,
    Title
  }
};
</script>

<style lang='less'>
.indexPage {
  height: 100%;
  display: flex;
  flex-flow: row nowrap;
  margin: 60px 140px 200px;
  background: #000428; /* fallback for old browsers */
  background: -webkit-linear-gradient(
    45deg,
    #004e92,
    #000428
  ); /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(
    45deg,
    #004e92,
    #000428
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  position: relative;
  border-radius: 4px;
  box-sizing: border-box;
  box-shadow: 0 0 10px 0px #525151a3;
  .el-form-item {
    margin-bottom: 5px;
    width: 346px;
  }
  .el-date-editor {
    width: 100%;
  }
  .el-upload-list__item-name {
    color: #fff;
  }
  .el-select {
    width: 100%;
  }
  .topBox {
    position: absolute;
    width: 95%;
    min-height: 70%;
    margin: 100px 5% 0;
    display: flex;
    flex-flow: row nowrap;
    .leftArea {
      width: 20%;
      min-width: 240px;
      display: flex;
      flex-flow: column nowrap;
      .UploadArea {
        flex: 1;
        display: flex;
        flex-flow: column nowrap;
        padding: 20px;
        overflow: auto;
        .fileList {
          overflow: auto;
          height: 306px;
          .perFileList {
            display: flex;
            flex-flow: row nowrap;
            justify-content: space-between;
            cursor: pointer;
            color: #fff;
            font-size: 14px;
            line-height: 28px;
            &:hover {
              background: rgba(0, 0, 0, 0.4);
            }
            .name {
              flex: 1;
            }
            i {
              margin-right: 6px;
            }
            .el-icon-circle-check {
              color: #08b908;
            }
          }
        }
      }
    }
    .rightArea {
      border-radius: 10px;
      width: 75%;
      display: flex;
      flex-flow: row nowrap;
      background: #fff;
      box-shadow: 0 1px 10px 0 #333;
      .titleBox .mainTitle {
        color: #333;
      }
    }
  }
  .reportArea {
    padding: 20px;
    flex: 1;
    display: flex;
    flex-flow: column nowrap;
    .el-form-item__label {
      color: #333;
    }
    .reportForm {
      display: flex;
      flex-flow: row wrap;
      justify-content: space-between;
    }
  }
  .resultArea {
    width: 100%;
    padding: 20px;
    border-radius: 10px;
    display: flex;
    flex-flow: column nowrap;
    background: url("../../assets/images/skin_image.jpg");
    background-size: cover;
    background-position: bottom right;
    .checkGroupBox {
      height: 20px;
      padding-bottom: 6px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .svgArea {
      flex: 1;
      overflow: hidden;
      cursor: pointer;
      position: relative;
      .canvasBox {
        display: none;
      }
    }
  }
}
</style>
<style>
.el-checkbox-button__inner {
  background: #a3a7a5;
  border: 1px solid #b8babd;
}
</style>
