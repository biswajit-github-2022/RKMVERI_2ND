
#Importing the data
path="C:/Users/biswajit/Downloads/Lab_test_R/LabTestDataQ.csv"
Data=read.csv(path)

#Plotting data
ts_data=ts(Data[,2], frequency = 83)
plot.ts(ts_data,type='p',ylab="values")

# Splitting before the chunk and after the chunk
prev_data=slice(Data,1:31)
Post_data=slice(Data,44:83)


# Finding p and q for model selection
plot(prev_data[,2], ylab="Height", xlab="Year", main="post")
library(astsa)
acf2(prev_data[,2],max.lag=12)                      
library(itsmr)
huron.at = autofit(prev_data[,2], p = 0:5, q = 0:5)
# AR order selection
p=length(huron.at$phi)
if(p==1 && huron.at$phi[1]==0)
  p=0
# MA order selection
q=length(huron.at$theta)
if(q==1 && huron.at$theta[1]==0)
  q=0
# p= 2, q=0, using arma(2,0)
#print(p,q)

# forecasting na values from prev values
time_series <- ts(prev_data[,2], frequency = 1)
fit <- arima(time_series, order=c(2,0,0))
forecast_prev_values <-forecast::forecast(fit, h = 12)
print((forecast_prev_values$mean))
forecast_prev_values=forecast_prev_values$mean

# forecasting na values from after values
time_series <- ts(Post_data[,2], frequency = 1)
time_series <- rev(time_series)
fit <- arima(time_series, order=c(2,0,0))
forecast_post_values <- forecast::forecast(fit, h = 12)
print(rev(forecast_post_values$mean))
forecast_post_values=rev(forecast_post_values$mean)



str(forecast_post_values)
str(forecast_prev_values)


vector1 <- forecast_post_values
vector2 <- forecast_prev_values

pred <- (vector1 + vector2) / 2

print(pred)


# replacing preed in NA val.
large_vector <- Data[,2]


small_vector <- pred


replace_index <- 32  


large_vector[replace_index:(replace_index + length(small_vector) - 1)] <- small_vector

print(large_vector)


plot.ts(ts(large_vector))


#finding MSE

path="C:/Users/biswajit/Downloads/Lab_test_R/LabTestData.csv"
original_Data=read.csv(path)


# Example vectors
vector1 <- large_vector
vector2 <- original_Data[,2]

# Calculate MSE
mse <- mean((vector1 - vector2)^2)

# Print MSE
print(mse)
