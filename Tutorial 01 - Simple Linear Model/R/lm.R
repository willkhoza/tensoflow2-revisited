dat <- read.csv("dat1.csv")
cor(dat)[11,]
summary(lm(var10~., data = dat))
summary(lm(var10~
             var0+
             var1+
             var2+
             var3+
             var4+
             var5+
             var6+
             var7+
             var8+
             var9, data = dat))

mod <- lm(var10~
            var0+
            var1+
            var2+
            var3+
            var4+
            var5+
            # var6+
            var7+
            var8+
            var9, data = dat)
summary(mod)

y.hat <- (predict(mod, dat))
y <- dat$var10
plot(y.hat~y)
error <- y-y.hat
plot(error)
var(error)
plot(dist(error))
hist(error)
