package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func root(c *gin.Context) {
	c.String(http.StatusOK, "DataCenter Interface!")
}

func image(c *gin.Context) {
	c.File("/home/sheldon/Document/code/beyes/labelml/server/project/skin-feature/skin.jpg")
}

func wsi(c *gin.Context) {
	c.File("/home/sheldon/Document/code/beyes/labelml/server/project/skin-feature/skin.jpg")
}

func thumbnail(c *gin.Context) {
	c.File("/home/sheldon/Document/code/beyes/labelml/server/project/skin-feature/skin.jpg")
}

func main() {
	router := gin.Default()
	router.GET("/", root)
	router.GET("/image", image)
	router.GET("/wsi", wsi)
	router.GET("/thumbnail", thumbnail)
	router.Run(":8000")
}
