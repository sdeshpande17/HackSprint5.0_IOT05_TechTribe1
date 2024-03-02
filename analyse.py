library(dplyr)
library(caTools)
library(rpart)
library(rpart.plot)
library(caret)
library(data.tree)
 library(ggplot2)
library(reshape2)

#crop <- read.csv("Crop_recommendation.csv")
crop=Crop_recommendation
show(crop)
#selecting only meaningful columns for prediction
crop1=select(crop,temperature,humidity,ph,rainfall,label)
crop1=mutate(crop1,label=as.factor(label),temperature=as.numeric(temperature),humdity=as.numeric(humidity),ph=as.numeric(ph),rainfall=as.numeric(rainfall))
#splitting training and testing data
set.seed(123)
sample=sample.split(crop1$label,SplitRatio =.70)
train=subset(crop1,sample==TRUE)
test=subset(crop1,sample==FALSE)

tree=rpart(label~temperature+humidity+ph+rainfall,data=train,method='class')

tree.label.predicted=predict(tree,test,type = 'class')

confusionMatrix(tree.label.predicted,test$label)

prp(tree)
print(c(tree.label.predicted))
hum=as.numeric(readline(prompt="Enter the value of hum:"))
temp=as.numeric(readline(prompt="Enter the value of temp:"))
ph1=as.numeric(readline(prompt="Enter the value of ph:"))
rain=as.numeric(readline(prompt="Enter the value of rainfall:"))
a=data.frame(temperature=c(temp),humidity=c(hum),ph=c(ph1),rainfall=c(rain))
result=predict(tree,a)
print(result)
cat("\014")

# Read the dataset containing historical data of crop yield and weather variables
crop_data=yielddataset
head(crop_data)
crop_data1=select(crop_data,Area,Production,Rainfall,temperature,ph)
plot(crop_data1)
model=lm(Production~Area+Rainfall+temperature+ph,data=crop_data1)
summary(model)
area=as.numeric(readline(prompt="Enter the area:"))
rain=as.numeric(readline(prompt="Enter the value of rainfall:"))
temp=as.numeric(readline(prompt="Enter the value of temp:"))
ph1=as.numeric(readline(prompt="Enter the value of ph:"))
p=data.frame(Area=c(area),Rainfall=c(rain),temperature=c(temp),ph=c(ph1))
prediction=predict(model,p)
cat("Predicted production:",prediction)
cat("\014")

