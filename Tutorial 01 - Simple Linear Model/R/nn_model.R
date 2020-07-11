require(neuralnet)
dat <- read.csv("dat1.csv")
nn.mod <- neuralnet(var10~., 
                    hidden = 0,
                    data = dat) 
plot(nn.mod)
ls(nn.mod)

# add a hidden lay
nn.mod <- neuralnet(var10~., 
                    hidden = c(2,1),
                    rep = 150,
                    data = dat,
                    threshold = 0.01) 

?neuralnet
plot(nn.mod)
ls(nn.mod)
