require(neuralnet)
dat <- read.csv("dat1.csv")
nn.mod <- neuralnet(var10~., 
                    hidden = 0,
                    data = dat) 
plot(nn.mod)