package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func root(c *gin.Context) {
	c.String(http.StatusOK, "Annotation Center Interface!")
}

func image(c *gin.Context) {
	// 图像接口
	c.File("/home/sheldon/Document/code/beyes/labelml/server/project/skin-feature/skin.jpg")
}

func wsi(c *gin.Context) {
	// WSI 影像接口
	//
	c.File("/home/sheldon/Document/code/beyes/labelml/server/project/skin-feature/skin.jpg")
}

func thumbnail(c *gin.Context) {
	// 缩略图接口
	c.File("/home/sheldon/Document/code/beyes/labelml/server/project/skin-feature/skin.jpg")
}

func upload(c *gin.Context) {
	// 文件上传接口
	c.File("/home/sheldon/Document/code/beyes/labelml/server/project/skin-feature/skin.jpg")
}

func main() {
	router := gin.Default()
	router.GET("/", root)
	router.GET("/data/image", image)
	router.GET("/data/wsi", wsi)
	router.GET("/data/thumbnail", thumbnail)
	router.GET("/data/upload", upload)
	router.Run(":8000")
}
